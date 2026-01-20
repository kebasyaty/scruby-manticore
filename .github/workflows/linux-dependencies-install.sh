#!/bin/bash

set -e

apt update

# Install OS dependencies
apt install -y wget gnupg2 git

TEMP_DEB="$(mktemp)" &&
wget -O "$TEMP_DEB" 'https://repo.manticoresearch.com/manticore-repo.noarch.deb' &&
dpkg -i "$TEMP_DEB"
rm -f "$TEMP_DEB"

apt install -y manticore manticore-extra
service manticore start
