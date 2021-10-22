To download the chart to make changes manually and deploy:
- kubectl create namespace {namespace}
- helm repo add jaegertracing https://jaegertracing.github.io/helm-charts 
- helm pull jaegertracing/jaeger
- tar -xzvf jaegertracing/jaeger {dir_name}
- helm install {dir_name} -n {namespace}

Following the instructions from Udacity:
# Create a namespace
kubectl create namespace observability
# jaegertracing.io_jaegers_crd.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/crds/jaegertracing.io_jaegers_crd.yaml
# service_account.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/service_account.yaml
# role.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role.yaml
# role_binding.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role_binding.yaml
# operator.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/operator.yaml
## Expanding Roles
# cluster_role.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/cluster_role.yaml
# cluster_role_binding.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/cluster_role_binding.yaml
## Verify install
kubectl get deployments jaeger-operator -n observability
kubectl get pods,svc -n observability
# OPTIONAL - Deploy a sample application
# Note that the command below is an updated one.
kubectl apply -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/examples/business-application-injected-sidecar.yaml
