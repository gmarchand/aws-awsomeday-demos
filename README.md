# AWSomeDay Demos

## Objective

## Prerequis

- If you use AWS Cloud 9, you can upgrade system and applicationpackages with this shell script `cloud9/bootstrap.sh`

- [Task](https://taskfile.org/) is a task runner, an alternative of Makefile. You need to [install it](https://taskfile.org/#/installation?id=install-script) :

```bash
curl -s https://taskfile.org/install.sh | sh
mv ./bin/task /usr/local/bin/
```

- Update the [Task variables](https://taskfile.org/#/usage?id=variables) `Taskvars.yml`.

- Install [HTTPie](https://httpie.org/doc#linux), a command line HTTP client with an intuitive UI and JSON support.

## Demo : Static Website on S3

**Objective :** You don't need to deploy a static html/js webapp on compute, you just need to deploy your archive to an Amazon S3 bucket.

1. Create a public S3 Website `task static-cfn-deploy`

1. Describe the cloudformation template `cfn-template-static.yml`

1. Describe the bucket in the AWS Console. The output of cloudformation lists the website URL

1. Deploy the static website `task static-deploy`

## Demo : Static Website on EC2

**Objective :**

## Demo : Static Website with Auto Scaling Group

**Objective :**

## Demo : Python API on Beanstalk

**Objective :**

## Demo : Python API on ECS Fargate

**Objective :** Deploy a CRUD API on ECS Fargate

1. Deploy the API on local inside a container `task api-docker-local`

1. Test it with HTTPie

## Demo : Python API on Lambda

1. Deploy the sam API on local with SAM `task api-docker-local`

1. Test it with HTTPie

**Objective :** 

## Bibliography

<https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5>

<https://github.com/shekhargulati/python-flask-docker-hello-world>

<https://auth0.com/blog/developing-restful-apis-with-python-and-flask/>
