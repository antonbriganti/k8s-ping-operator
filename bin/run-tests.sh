#/bin/sh

echo "I'm only doing this because my docker-compose wasn't working 😭"
docker build -t anton-pingtest-unit-tests . -f Dockerfile.test
docker run anton-pingtest-unit-tests