#/bin/sh

kubectl apply -f ./operator-config/operator-namespace.yml
kubectl apply -f ./operator-config/pingtest-crd.yml
kubectl apply -f ./operator-config/operator-rbac.yml
kubectl apply -f ./operator-config/operator-deployment.yml