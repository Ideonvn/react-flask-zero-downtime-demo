FROM python:3.8-slim-buster

ENV INSTALL_PATH /zenysis
ENV PYTHONPATH "${ZENYSIS_SRC_ROOT}:${PYTHONPATH}"

WORKDIR ${INSTALL_PATH}

RUN apt-get update && apt-get install -y curl

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY build build
COPY server server

ENTRYPOINT ["python", "server"]
