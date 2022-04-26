FROM python:3.8-slim-buster

ENV INSTALL_PATH /app
ENV PYTHONPATH "${INSTALL_PATH}:${PYTHONPATH}"

WORKDIR ${INSTALL_PATH}

RUN apt-get update && apt-get install -y curl libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY build build
COPY server server
COPY logging.conf logging.conf

ENTRYPOINT ["python", "server"]
