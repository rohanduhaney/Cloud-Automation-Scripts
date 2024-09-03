#!/bin/bash

# Variables
PROJECT_ID="my-gcp-project" # Replace with your GCP project ID
ZONE="us-central1-a"
INSTANCE_NAME="my-instance"
MACHINE_TYPE="n1-standard-1"
IMAGE_FAMILY="debian-9"
IMAGE_PROJECT="debian-cloud"

# Create Compute Engine Instance
gcloud compute instances create $INSTANCE_NAME \
    --project=$PROJECT_ID \
    --zone=$ZONE \
    --machine-type=$MACHINE_TYPE \
    --image-family=$IMAGE_FAMILY \
    --image-project=$IMAGE_PROJECT

echo "Google Cloud Compute Engine instance $INSTANCE_NAME has been created."
