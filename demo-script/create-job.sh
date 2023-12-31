#!/bin/bash

# usage ./create-job.sh 17461204521323,20202020220021,3809491708961,52,25366202179

PROJECT_ID=${PROJECT_ID:=gateway-multicluster-01}
REGION=${REGION:=us-central1}
IMAGE=${IMAGE:=us-central1-docker.pkg.dev/cicd-system-demo-01/dispatch-demo/worker@sha256:2236164556d08addc59674b4f06b85c65add35a192ea228375bd5063a266e73f}
JOB_NAME=primefinder-$(date +%s)

# prime candidates
CANDIDATES=${1:-679,23222321,324324232432231,110101010101001010101010101} # default to this if nothing else provided; it'll end quickly
NUM_TASKS=$(echo $CANDIDATES | tr ',' ' ' | wc -w)

echo "Creating ${JOB_NAME} in project ${PROJECT_ID} using $IMAGE, with prime candidates $CANDIDATES, in ${NUM_TASKS} tasks"
gcloud beta run jobs create ${JOB_NAME} --execute-now \
    --project $PROJECT_ID \
    --region $REGION \
    --image $IMAGE \
    --command python \
    --set-env-vars=^:^CANDIDATES=${CANDIDATES} \
    --args worker.py \
    --tasks $NUM_TASKS \
    --task-timeout 24h # 24 hour duration, if needed