FROM python:3.11

COPY . ${HOME}
WORKDIR ${HOME}
RUN pip install -r requirements.txt
