Python version: 3.6.4
导入包 : flask, kubernetes, io, pycurl, logging

环境配置：pip3 install requirements.txt
运行： python3 myproj.py启动成功后，访问 http://127.0.0.1:5000 即可。


各文件功能：

    1. route.py: 路由文件
    2. forms.py: 网页表单
    3. myproj.py: app运行文件
    4. __init__.py: 初始化app
    5. base.html: 初始目录页面
    6. index.html: 查看当前运行的pod
    7. log.html: 查看每个pod的日志
    8. create_deployment.html: 创建deployment，同时创建服务
    9: configmap.html: 展示已有的configmap，也可创建新的configmap
    10: list_cm.html: 展示已有的configmap（configmap.html中已含此部分代码）
    11: list_edit_cm.html: 展示指定configmap的具体内容
    12: delete_cm.html: 删除configmap

函数功能：

    1. index():
        获取k8s上pod信息，显示pod名称、namespace和podIP。

    2. log():
        获取指定pod的日志信息。

    3. create_deployment():
        调用loading_image()获取服务器镜像信息。再通过调用deploy_with_cm() 或 deploy_no_cm()创建deployment。

    4. deploy_with_cm(form,image,radio):
        创建挂载 configmap 的 deployment，form为表单，image为镜像名称，radio 为 configmap 名。

    5. deploy_no_cm(form,image):
        创建不挂载 configmap 的 deployment。form为表单，image为镜像名称。

    6. configmap():
        接收前端表单，创建configmap。

    7. list_cm():
        获取已创建好的 configmap 名字信息。

    8. list_edit_cm():
        获取已创建好的 configmap 的具体内容。

    9: delete_cm():
        删除已有的 configmap

    10: loading_images():
        访问公司docker镜像库，获取镜像名和标签。

    11: create_svc(port,targetport):
        根据创建的 deployment，同时创建clusterIP服务，port为service暴露在cluster ip上的端口，targetport为pod端口。

    12: deploy_part():
        创建 deployment 的公共组件，包含selector, metadata, body，并完成deployment创建。



