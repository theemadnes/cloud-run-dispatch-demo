# cloud-run-dispatch-demo
playing around with creating a dispatcher service that creates Cloud Run jobs

### build your images

docker build . -t us-central1-docker.pkg.dev/cicd-system-demo-01/dispatch-demo/worker
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/dispatch-demo/worker

docker build . -t us-central1-docker.pkg.dev/cicd-system-demo-01/dispatch-demo/dispatcher
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/dispatch-demo/dispatcher
