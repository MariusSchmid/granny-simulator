FROM ubuntu:22.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive
ENV DISPLAY :1

# Update Ubuntu Software repository
RUN apt update
RUN apt upgrade -y
RUN apt install weston -y
RUN apt install wget ca-certificates -y
RUN apt install xorg openbox -y
RUN apt-get update
RUN apt install python3-pip -y


RUN apt-get update \
    && apt-get -y install xserver-xorg-video-dummy x11-apps

COPY ./xorg.conf /etc/X11/xorg.conf
COPY . /data
VOLUME /tmp/.X11-unix

COPY entrypoint.sh /opt
ENTRYPOINT ["/opt/entrypoint.sh"]

WORKDIR data

CMD ["/bin/bash", "-c", "pip3 install -r requirements.txt;python3 -m pytest"]