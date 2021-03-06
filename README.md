# AWSomeDay Demos

## Objective

## Prerequis

- If you use AWS Cloud 9, you can upgrade system and application packages with this shell script `cloud9/bootstrap.sh`. Else if you need to install Docker and [AWS SAM CLI](https://aws.amazon.com/serverless/sam/)

- Install [Task](https://taskfile.org/) is a task runner, an alternative of Makefile.

```bash
curl -s https://taskfile.org/install.sh | sh
mv ./bin/task /usr/local/bin/
```

- Update the [Task variables](https://taskfile.org/#/usage?id=variables) `Taskvars.yml`.

- Install [HTTPie](https://httpie.org/doc#linux), a command line HTTP client with an intuitive UI and JSON support.

- Install [MU](https://github.com/stelligent/mu/wiki/Installation)

## Demo : Static Website on S3

**Objective :** You don't need to deploy a static html/js webapp on compute, you just need to deploy your archive to an Amazon S3 bucket.

1. Create a public S3 Website `task static-cfn-deploy`

1. Describe the cloudformation template `cfn-template-static.yml`

1. Describe the bucket in the AWS Console. The output of cloudformation lists the website URL

1. Deploy the static website `task static-deploy`

1. Show the source code in AWS S3 Console

1. Show the website

## Demo : Static Website on EC2

**Objective :**

## Demo : Static Website with Auto Scaling Group

**Objective :**

## Demo : Python API on Beanstalk

**Objective :**

## Demo : Python API on ECS Fargate

**Objective :** Deploy a CRUD API on ECS Fargate

1. Test the API on local inside a container `task api-docker-local`

1. Test the API with HTTPie `http POST http://127.0.0.1:5000/squirrel` and `http GET http://127.0.0.1:5000/squirrel`

1. Create the ECS Fargate Cluster with MU `task api-mu-env-deploy`

1. Deploy the API service on ECS Fargate with MU `task api-mu-service-deploy`

1. Test the API with HTTPie `http POST <FARGATE_ELB>/squirrel` and `http GET <FARGATE_ELB>/squirrel`

1. **TODO:** Load Test


## Demo : Python API on Lambda

**Objective :** Deploy the same CRUD API on API Gateway and Lambda

1. Test the local Lambda function with SAM `task api-sam-local-invoke`

1. Test the local API with SAM `ask api-sam-local`

1. Test the API with HTTPie `http POST http://127.0.0.1:3000/squirrel` and `http GET http://127.0.0.1:3000/squirrel`

1. Deploy the API service on Lambda and API Gateway `task api-sam-deploy`

1. **TODO:** Load test 


## TODO
[API TEST with Newman](https://github.com/stelligent/mu/blob/develop/examples/pipeline-newman/buildspec-test.yml)

[Add DynamoDB to MU](https://github.com/stelligent/mu-ref-dynamodb)

[Load Test with Artillery Pro](https://artillery.io/pro/)