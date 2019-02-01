#Using lightweight alpine image
FROM python:3.6-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f -s http://localhost:5000/ || exit 1
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]