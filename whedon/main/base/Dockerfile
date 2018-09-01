FROM continuumio/miniconda3

#########################################
# The Robot Namer
# 
# docker build -t vanessa/whedon-namer .
# docker run vanessa/whedon-namer
#########################################

LABEL maintainer vsochat@stanford.edu
ADD generate.py /
ENV PATH /usr/local/bin:$PATH
ENTRYPOINT ["python", "/generate.py"]
