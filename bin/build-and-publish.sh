#/bin/sh

COMMIT_SHA=$(git rev-parse HEAD)

docker build -t antonbriganti/pingtest-operator:$COMMIT_SHA --target app .
docker tag antonbriganti/pingtest-operator:$COMMIT_SHA antonbriganti/pingtest-operator:latest
# docker push antonbriganti/pingtest-operator:$COMMIT_SHA
# docker push antonbriganti/pingtest-operator:latest