#!/bin/bash

packages=(
  nginx
  php5-cgi
  php5-cli
  php5-common
  php5-fpm
)

main() {
  install_packages
}

install_packages() {
  apt-get update
  apt-get install -y ${packages[@]}
}

main
