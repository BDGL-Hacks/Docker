FROM ubuntu:14.04

# Let's start with some basic stuff.
RUN apt-get update -q && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    lxc \
    iptables \
    python-pip\
    python-dev
    && pip install --upgrade pip \
    && pip install --upgrade virtualenv

# Install Docker from Docker Inc. repositories.
RUN echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 \
  && apt-get update -qq \
  && apt-get install -qqy lxc-docker

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
ADD ../DockerFiles /DockerFiles
ADD ../../docker   /maroon
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]

