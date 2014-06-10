#!/usr/bin/env python2

import os

def install_nginx_config(id):
    vals = {
        'id': id,
        'site': 'minimul.ro' if id == 'default' else id + '.minimul.ro',
        'path_name': 'default' if id == 'default' else id + '.minimul.ro',
    }

    file = """
    server {{
        server_name {site};
        root /opt/minimul-sites/{id};
        index index.html index.php;

        location / {{
        }}
        location ~ \.php$ {{
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            include fastcgi_params;
        }}
    }}
    """

    file = file.format(**vals)

    f = open('/etc/nginx/sites-available/{path_name}'.format(**vals), 'w')
    f.write(file)
    f.close()

    os.system("""
        cd /etc/nginx/sites-enabled
        rm {path_name} 2>/dev/null
        ln -s ../sites-available/{path_name} {path_name}
    """.format(**vals))

def copy_site(id):
    os.system("""
        rm -fr /opt/minimul-sites/{id} 2>/dev/null
        mkdir -p /opt/minimul-sites 2>/dev/null
        cp -r /vagrant/sites/{id} /opt/minimul-sites/{id}
    """.format(id=id))

def main():
    sites = [
        'default',
        'paulscripts',
        'collegesite',
        'collegesite2',
        'italiafascista',
        'rstsd',
        'meetfirefox',
        'timr',
    ]

    for site in sites:
        install_nginx_config(site)
        copy_site(site)

    os.system('service nginx restart')

if __name__ == '__main__':
    main()
