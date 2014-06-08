# Minimul

A Vagrant configuration for storing all my old websites. It's not complete.

## Running it

Bring up the machine.

    vagrant up

Copy the projects into `sites/`. This step will need to be fixed since projects
are hardcoded to `/home/p/pro`.

    sites/copy.sh

From inside the machine:

    sudo /vagrant/install-sites/install.py

The default site is at [10.10.10.10](http://10.10.10.10). The rest need the
appropriate hosts file rules.

## Deploying

    vagrant plugin install vagrant-digitalocean
    vagrant up --provider=digital_ocean

## License

MIT
