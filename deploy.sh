#!/bin/bash
pip install -r requirements.txt -t hello_world/build/;
cp hello_world/*.py hello_world/build/;

sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket cf-templates-kl6v54konfxv-us-east-1;

sam deploy \
    --template-file packaged.yaml \
    --stack-name dynamodb-labo \
    --capabilities CAPABILITY_IAM;
