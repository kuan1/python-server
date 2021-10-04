FROM python:3.9-slim

WORKDIR /app

# RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list \
#   && apt-get update && apt-get install -y python3 python3-pip \
#   && apt-get -y install python3.7-dev

# RUN pip3 install virtualenv && virtualenv venv
# RUN [ "/bin/bash", "-c", "source venv/bin/activate" ]

COPY ./python-api/requirement.txt .
RUN pip3 install -r requirement.txt 
COPY ./python-api/ .

CMD gunicorn -b 0.0.0.0:5001 -w 2 app:app

EXPOSE 5001
