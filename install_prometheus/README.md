To download the chart to make changes manually and deploy:
- kubectl create namespace {namespace}
- helm repo add prometheus-community
- helm pull prometheus-community/kube-prometheus-stack
- tar -xzvf kube-prometheus-stack-19.2.2.tgz {dir_name}
- helm install {dir_name} -n {namespace}
