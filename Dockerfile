FROM alpine:3.6
FROM ubuntu:latest
MAINTAINER Kalab Oster
RUN apt-get update -y
RUN apt-get install python3-pip -y
COPY . /wordsum2vec
WORKDIR /wordsum2vec
ENV PYTHONHASHSEED 0
RUN pip3 install -r requirements.txt
RUN pip3 install --ignore-installed six
ENTRYPOINT ["python3"]
CMD ["wordsum2vec_app.py"]