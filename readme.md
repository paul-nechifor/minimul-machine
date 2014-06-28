# Minimul

A Vagrant configuration for storing all my old websites. It's not complete.

## Running it

Bring up the machine.

    vagrant up

Copy the projects into `sites/`. This step will need to be fixed since projects
are hardcoded to `/home/p/pro`.

    scripts/copy-sites.sh

Go in the machine:

    vagrant ssh

From inside the machine:

    sudo /vagrant/scripts/install-sites.py

The default site is at [10.10.10.10](http://10.10.10.10). The rest need the
appropriate hosts file rules.

## Deploying

The DigitalOcean keys must be on a line in `private/api_key` and
`private/client_id`. After that:

    vagrant plugin install vagrant-digitalocean
    vagrant up --provider=digital_ocean

## License

MIT
