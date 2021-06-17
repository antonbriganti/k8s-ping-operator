#/bin/sh

echo "deploying operator 🔧"
./bin/deploy-operator.sh
echo

echo "deploying ping test examples 🧪"
kubectl apply -f ./example-pingtests/
echo

echo "waiting for operator to start and ping test to complete ✨"
count=0
while [ $count -lt 20 ] 
do
    printf "#"
    sleep 1
    count=$[$count+1]
done
echo "\n"

echo "now our operator should be working work 🤞"
echo "note, there's a chance that the operator might not have been up by now."
echo "if you see nothing from the following commands, just check that the operator is up and then check again"
echo "****** ping test which is successful ******"
kubectl get pingtest ping-test-good -o yaml

echo "****** ping test which is missing fields ******"
kubectl get pingtest ping-test-bad-host -o yaml
 
echo "****** ping test which is missing fields ******"
kubectl get pingtest ping-test-missing-fields -o yaml