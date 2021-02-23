#!/usr/bin/env bash

# Created on Fri Feb 19 10:33:54 2021
# @author: kanovotn


set -o errexit

imageId=blogapp
# Create a container
container=$(buildah from ubi8/python-38)

# Get the source
source="https://github.com/kanovotn/blogApp.git"

buildah config --label maintainer="Katerina Odabasi <lyrisha@gmail.com>" $container

buildah run $container pip3 install --upgrade pip

buildah config --workingdir /opt/blogApp $container

git clone $source /tmp/blogApp
buildah copy $container /tmp/blogApp /opt/blogApp

buildah run $container pip3 install -r requirements.txt

buildah config --cmd 'bash -x container/configure-container.sh' $container
buildah commit $container $imageId



