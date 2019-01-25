from app import app
from flask import render_template,request
from kubernetes import client, config
from app.forms import LoginForm,replicationcontrollerForm,configmapForm,configmap_edit_Form
from io import BytesIO
import pycurl
import json


config.load_kube_config()

def deploy_with_cm(form,image,radio):
    app = form.app.data
    env = form.env.data
    command = form.command.data
    container_name = app
    targetport = form.targetport.data

    port = form.port.data

    volumes = client.V1Volume(
        name=app,
        config_map=client.V1ConfigMapVolumeSource(
            name=radio
        )
    )
    if command=='':
        container = client.V1Container(

            name=container_name,
            image=image,
            volume_mounts=[client.V1VolumeMount(
                mount_path='/etc/config',
                name=app
            )],
            ports=[client.V1ContainerPort(container_port=int(port))]
        )
    else:
        container = client.V1Container(
            command=["/bin/sh"],
            args=["-c", command],
            env=[env],
            name=container_name,
            image=image,
            volume_mounts=[client.V1VolumeMount(
                mount_path='/etc/config',
                name=app
            )],
            ports=[client.V1ContainerPort(container_port=int(port))]
        )

    mdata = client.V1ObjectMeta(
        name=app
    )

    selector = client.V1LabelSelector(
        match_labels={"app": app}
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": app}),
        spec=client.V1PodSpec(
            containers=[container],
            volumes=[volumes]
        )
    )

    spec = client.V1DeploymentSpec(
        selector=selector,
        template=template
    )

    body = client.V1Deployment(
        api_version='apps/v1',
        kind='Deployment',
        metadata=mdata,
        spec=spec,

    )
    svc = client.AppsV1Api()
    api_response_1 = svc.create_namespaced_deployment(namespace='default', body=body)
    print(api_response_1)

    spec = client.V1ServiceSpec(
        ports=[client.V1ServicePort(
            port=int(port),
            target_port=int(targetport)
        )],
        selector={"app": app}
    )

    v1_objectmetadata = client.V1ObjectMeta(
        name=app,
        labels={"app": app}
    )

    body = client.V1Service(
        api_version='v1',
        kind='Service',
        metadata=v1_objectmetadata,
        spec=spec
    )
    svc = client.CoreV1Api()
    api_response = svc.create_namespaced_service(namespace='default', body=body)

    print("Deployment created. status='%s'" % str(api_response.status))

    return str(api_response.status)

def deploy_no_cm(form,image):
    app = form.app.data
    env = form.env.data
    command = form.command.data
    container_name = app
    targetport = form.targetport.data
    port = form.port.data
    if command!='':
        container = client.V1Container(
            name=container_name,
            image=image,
            env=[env],      #环境变量未进行过实际测试
            command=["/bin/sh"],
            args=["-c",command],
            ports=[client.V1ContainerPort(container_port=int(port))]
        )
    else:
        container = client.V1Container(
            name=container_name,
            image=image,
            ports=[client.V1ContainerPort(container_port=int(port))]
        )
    mdata = client.V1ObjectMeta(
        name=app
    )
    selector = client.V1LabelSelector(
        match_labels={"app": app}
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": app}),
        spec=client.V1PodSpec(
            containers=[container],
        )
    )
    spec = client.V1DeploymentSpec(
        selector=selector,
        template=template
    )

    body = client.V1Deployment(
        api_version='apps/v1',
        kind='Deployment',
        metadata=mdata,
        spec=spec,

    )
    svc = client.AppsV1Api()
    api_response_1 = svc.create_namespaced_deployment(namespace='default', body=body)
    print(api_response_1)
    spec = client.V1ServiceSpec(
        ports=[client.V1ServicePort(
            port=int(port),
            target_port=int(targetport)
        )],
        selector={"app": app}
    )
    v1_objectmetadata = client.V1ObjectMeta(
        name=app,
        labels={"app": app}
    )
    body = client.V1Service(
        api_version='v1',
        kind='Service',
        metadata=v1_objectmetadata,
        spec=spec
    )
    svc = client.CoreV1Api()
    api_response = svc.create_namespaced_service(namespace='default', body=body)

    print("Deployment created. status='%s'" % str(api_response.status))

    return str(api_response.status)



@app.route('/')
@app.route('/catalog')
def catalog():
    return render_template('base.html')

@app.route('/index')
def index():

    user = {'username':'yinzi'}
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_namespaced_pod(namespace='default',watch=False)


    return render_template('index.html',title='wode',user=user,posts=ret.items)


@app.route('/log/<pod>',methods=['GET'])
def log(pod):
    v1 = client.CoreV1Api()
    ret = v1.read_namespaced_pod_log(namespace='default',name=pod,pretty=True)
    print(ret)

    return render_template('log.html',title=pod,posts=ret)

@app.route('/create_deployment',methods=['GET','POST'])
def create_deployment():
    form = LoginForm()

    if form.validate_on_submit():
        radio = request.values.get("cm")
        image_tag = request.values.get("image")
        version = request.values.get("version")
        print(image_tag,version)
        image = image_tag+':'+version

        print(image)
        print(radio)

        if  radio=='no':
            messege=deploy_no_cm(form,image)
            return '%s' % messege
        else:
            messege=deploy_with_cm(form,image,radio)
            return '%s' % messege


    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://nexus.ahi.internal:5000/v2/_catalog')
    c.setopt(pycurl.WRITEDATA, b)
    c.perform()
    string_body = b.getvalue().decode('utf-8')
    sb = eval(string_body)
    c.close()
    b.close()
    image_list = []
    for i in sb["repositories"]:
        url = 'http://nexus.ahi.internal:5000/v2/' + i + '/tags/list'
        b = BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.WRITEDATA, b)

        m = pycurl.CurlMulti()
        m.add_handle(c)
        while 1:
            ret, num_handles = m.perform()
            if ret != pycurl.E_CALL_MULTI_PERFORM: break
        while num_handles:
            if ret == -1:  continue
            while 1:
                ret, num_handles = m.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM: break
        string_body = b.getvalue().decode('utf-8')
        sc = eval(string_body)
        c.close()
        b.close()
        image_list.append(sc)
        # for j in sc["tags"]:
        #     image = sc["name"] + ':' + j
        #     image_list.append(image)
    for i in image_list:
        print(i)
    user = {'username': 'yinzi'}
    # config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.list_namespaced_config_map(namespace='default', watch=False)
    return render_template('create_deployment.html',user=user,form=form,posts =ret.items,ima=image_list)

@app.route('/configmap',methods=['POST'])
def configmap():
    form = configmapForm()
    if form.validate_on_submit():
        dict={}
        name = form.name.data
        confignames = request.values.getlist("configname")
        configtxts = request.values.getlist("configtxt")
        for i in range(len(configtxts)):
            if confignames[i]!='':
                dict[confignames[i]]=configtxts[i]

        mdata = client.V1ObjectMeta(
            name=name
        )

        body = client.V1ConfigMap(
            data = dict,
            metadata = mdata
            )
        svc = client.CoreV1Api()
        api_response = svc.create_namespaced_config_map(namespace='default', body=body)
        return '%s' % str(api_response)

    return render_template('configmap.html',form = form)


@app.route('/configmap',methods=['GET'])
def list_cm():
    form=configmapForm()
    user = {'username':'yinzi'}
    v1 = client.CoreV1Api()
    print("Listing cm with their:")
    ret1 = v1.list_namespaced_config_map(namespace='default',watch=False)
    for i in ret1.items:
        ret2 = v1.read_namespaced_config_map(namespace='default',name=i.metadata.name,pretty=True)
        # print(ret2)

    return render_template('configmap.html',title='configmap info',user=user,posts=ret1.items,form=form)

@app.route('/list_cm/<cm>',methods=['GET','POST'])
def list_edit_cm(cm):
    form = configmap_edit_Form()

    if form.validate_on_submit():
        dict={}
        configtxts = request.values.getlist("cm_inf")
        name = request.values.get("cm")
        confignames = request.values.getlist("cm_name")
        print(name)
        print(configtxts,confignames)
        for i in range(len(configtxts)):
            if confignames[i]!='':
                dict[confignames[i]]=configtxts[i]

        mdata = client.V1ObjectMeta(
            name=name
        )

        body = client.V1ConfigMap(
            data = dict,
            metadata = mdata
            )
        svc = client.CoreV1Api()
        api_response = svc.replace_namespaced_config_map(name=name,namespace='default', body=body)
        return '%s' % str(api_response)


    v1 = client.CoreV1Api()
    ret = v1.read_namespaced_config_map(namespace='default',name=cm,pretty=True)
    print(ret)
    return render_template('list_edit_cm.html',title=cm,posts=ret,form=form)





@app.route('/delete_cm',methods=['GET','POST'])
def delete_cm():
    cm_name = request.values.get("delete_cm")
    print(cm_name)
    v1=client.CoreV1Api()
    ret1 = v1.delete_namespaced_config_map(name=cm_name,namespace='default',body=client.V1DeleteOptions())
    print(ret1)


    return list_cm()
