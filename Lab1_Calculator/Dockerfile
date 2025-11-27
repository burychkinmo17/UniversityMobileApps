FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 python3-pip python3-dev python3-venv \
    git zip unzip openjdk-17-jdk build-essential \
    autoconf automake libtool \
    libffi-dev libssl-dev zlib1g-dev libsqlite3-dev \
    libjpeg-dev libfreetype6-dev \
    && apt clean

RUN pip3 install --upgrade pip
RUN pip3 install buildozer cython virtualenv

# ПАТЧ ROOT-CHECK — удаляем input() в реальном пути pip
RUN sed -i "/Are you sure you want to continue/d" /root/.local/lib/python3.10/site-packages/buildozer/__init__.py || true
RUN sed -i "/Buildozer is running as root/d" /root/.local/lib/python3.10/site-packages/buildozer/__init__.py || true

ENV BUILDOZER_ALLOW_ROOT=1

WORKDIR /home/buildozer
