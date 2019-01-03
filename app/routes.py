from app import app
from flask import render_template,request
from kubernetes import client, config
from app.forms import LoginForm,replicationcontrollerForm,configmapForm
import os
# DEPLOYMENT_NAME = "kubectl-client-test"


@app.route('/')
@app.route('/catalog')
def catalog():
    return render_template('base.html')



@app.route('/index')
def index():

    user = {'username':'yinzi'}
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_namespaced_pod(namespace='default',watch=False)


    return render_template('index.html',title='wode',user=user,posts=ret.items)


@app.route('/log/<pod>',methods=['GET'])
def log(pod):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.read_namespaced_pod_log(namespace='default',name=pod,pretty=True)
    print(ret)

    return render_template('log.html',title=pod,posts=ret)

@app.route('/create_deployment',methods=['GET','POST'])
def create_deployment():
    form = LoginForm()

    if form.validate_on_submit():
        radio = request.values.get("cm")
        print(radio)

        if  radio=='no':
            app = form.app.data
            image = form.image.data
            env = form.env.data
            command = form.command.data
            container_name = app
            targetport = form.targetport.data
            port = form.port.data

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

            config.load_kube_config()
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
            config.load_kube_config()
            svc = client.CoreV1Api()
            api_response = svc.create_namespaced_service(namespace='default',body=body)

            print("Deployment created. status='%s'" % str(api_response.status))

            return '%s ' % str(api_response.status)
        else:
            app = form.app.data
            image = form.image.data
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

            container = client.V1Container(
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

            config.load_kube_config()
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
            config.load_kube_config()
            svc = client.CoreV1Api()
            api_response = svc.create_namespaced_service(namespace='default', body=body)

            print("Deployment created. status='%s'" % str(api_response.status))

            return '%s ' % str(api_response.status)


    user = {'username': 'yinzi'}
    config.load_kube_config()
    v1 = client.CoreV1Api()
    ret = v1.list_namespaced_config_map(namespace='default', watch=False)

    return render_template('create_deployment.html',user=user,form=form,posts =ret.items)

@app.route('/configmap',methods=['GET','POST'])
def configmap():
    form = configmapForm()
    if form.validate_on_submit():
        dict={}
        print(form.configname)
        name = form.name.data
        print(name)
        confignames = request.values.getlist("configname")
        print(confignames)
        configtxts = request.values.getlist("configtxt")
        print(configtxts)
        for i in range(len(configtxts)):
            dict[confignames[i]]=configtxts[i]


        mdata = client.V1ObjectMeta(
            name=name
        )

        body = client.V1ConfigMap(
            data = dict,
            metadata = mdata
            )
        config.load_kube_config()
        svc = client.CoreV1Api()
        api_response = svc.create_namespaced_config_map(namespace='default', body=body)
        return '%s' % str(api_response)

    return render_template('configmap.html',form = form)


