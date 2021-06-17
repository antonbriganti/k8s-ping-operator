# k8s-ping-operator
a simple operator for k8s that pings a given host. 
written in python using the kopf framework. ([check it out here]("https://github.com/nolar/kopf"))

> **NOTE**: sorry about the lack of commit history, I'm dumping this into git after writing it. 

## installing the operator 🚀
I used kind to test this operator locally. You can check out [kind and its docs here.](https://kind.sigs.k8s.io)

### deploying to cluster
> the image that's used by the operator exists in a public docker repo, so it'll be pulled by the cluster.

here's a script to quickly deploy everything needed:
```sh
./bin/deploy-operator.sh # deploys CRD, RBAC rules and operator
```

## using the operator ⚙️

an example CRD looks something like this:
```yaml
apiVersion: app.seek.com/v1
kind: PingTest
metadata:
  name: ping-test-good
spec:
  host: google.com
  count: 5
```

I've provided some example pingtests to show both the positive path as well as a couple of bad paths. they can be deployed as follows:

```sh
kubectl apply -f ./operator-config/
```

## running tests 🧪
use the script:
```
./bin/run-tests.sh
```

## thoughts and reflections 💭
it's over in [this file here](dev-reflections.md)