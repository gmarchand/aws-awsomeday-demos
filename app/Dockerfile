#Using lightweight alpine image
FROM python:3.6-alpine

MAINTAINER Guillaume Marchand "gmarchan@amazon.fr"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

ENV AWS_ACCESS_KEY_ID ""
ENV AWS_SECRET_ACCESS_KEY ""
ENV AWS_DEFAULT_REGION "us-west-1"