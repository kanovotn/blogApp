#!/usr/bin/env bash

# Created on Fri Feb 19 10:33:54 2021
# @author: kanovotn


set -o errexit

imageId=blogapp
container_source_path=/opt/blogApp

# Create a container
container=$(buildah from ubi8/python-38)

# Build the image for local usage
DEVEL_USE=0

if [ "$1" == "--devel-use" ]; then

    DEVEL_USE=1

fi

# Get the source
source="https://github.com/kanovotn/blogApp.git"

buildah config --label maintainer="Katerina Odabasi <lyrisha@gmail.com>" $container

buildah run $container pip3 install --upgrade pip

buildah config --workingdir $container_source_path $container

if [ $DEVEL_USE -eq 1 ]; then
    buildah copy $container . $container_source_path
else
    git clone $source /tmp/blogApp
    buildah copy $container /tmp/blogApp $container_source_path
fi

buildah run $container pip3 install -r requirements.txt

buildah config --cmd 'bash -x container/configure-container.sh' $container
buildah commit $container $imageId



