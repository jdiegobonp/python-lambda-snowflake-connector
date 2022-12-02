# Lambda Snowflake Connector using layer
A common problem when we are developing with AWS Lambdas specifically using the Python language is the use of layers. A layer is a group of external libraries that you can add for a Lambda if you need to. This repository contains an example and steps to create a Snowflake layer that uses a Lambda function to connect to a Snowflake database.

## Pre-requisites
- Docker
- Python
- AWS CLI
- AWS Credentials
## Steps

1. Open a terminal and run the following commands to create a layer into a ZIP file.

```sh
# Create a layer name
LAYER="snowlib"
# Create the layer structure
mkdir -p $LAYER/python/lib/python3.8/site-packages
# Create the layer through docker job
docker run -v "$PWD":/var/task "public.ecr.aws/sam/build-python3.8" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.8/site-packages/; exit"
# Create a ZIP file
zip -r $LAYER.zip python > /dev/null
```

**Aditional Steps**

These steps permit to upload of the ZIP file and create a new version of the layer.

```sh
# Copy the ZIP file to an S3 bucket
aws s3 cp layer_$LAYER.zip s3://<BucketName>
# Create a new version of the lambda layer
aws lambda publish-layer-version --layer-name Snowflake-Python --description "My python snowflake libs" --zip-file fileb://layer.zip --compatible-runtimes "python3.8"
```

## Reference
- https://aws.amazon.com/premiumsupport/knowledge-center/lambda-layer-simulated-docker/