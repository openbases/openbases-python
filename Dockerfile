FROM continuumio/miniconda3

# docker build -t openbases/openbases .
# docker run -v $PWD:/data openbases/openbases

RUN apt-get update && apt-get install -y git wget
RUN mkdir -p /data /code
ADD . /code
WORKDIR /code
RUN python setup.py install && \
    pip install --upgrade pip && \
    pip install .[validate] && \
    chmod u+x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
