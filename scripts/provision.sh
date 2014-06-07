#!/bin/bash

packages=(
  php5-common
  php5-cli
  php5-fpm
  nginx
)

main() {
  install_packages
}

install_packages() {
  apt-get update
  apt-get install -y ${packages[@]}
}

main
