# primarily used for debugging python on a version of python3
ARG PYTHON_VERSION=3.8
FROM python:$PYTHON_VERSION
WORKDIR /home


# Upgrade installed packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean


# Copy package contents into image
COPY reticulok/ reticulok/
COPY requirements.txt requirements.txt


# Ensure dependencies are installed
RUN pip3 install -r requirements.txt
