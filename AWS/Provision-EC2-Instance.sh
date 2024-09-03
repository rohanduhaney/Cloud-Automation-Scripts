#!/bin/bash

# Variables
AMI_ID="ami-0abcdef1234567890" # Replace with your desired AMI ID
INSTANCE_TYPE="t2.micro"
KEY_NAME="my-key-pair" # Replace with your key pair name
SECURITY_GROUP="sg-0123456789abcdef0" # Replace with your security group ID

# Create EC2 Instance
aws ec2 run-instances --image-id $AMI_ID --instance-type $INSTANCE_TYPE --key-name $KEY_NAME --security-group-ids $SECURITY_GROUP --count 1

echo "EC2 Instance has been created."
