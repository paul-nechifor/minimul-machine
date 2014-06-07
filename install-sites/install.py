#!/usr/bin/env python2

import os

def install_nginx_config(id):
    file = """
    server {{
        server_name {id}.minimul.ro;
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

    vals = {
        'id': id
    }

    file = file.format(**vals)

    f = open('/etc/nginx/sites-available/{id}.minimul.ro'.format(**vals), 'w')
    f.write(file)
    f.close()

    os.system("""
        cd /etc/nginx/sites-enabled
        rm {id}.minimul.ro 2>/dev/null
        ln -s ../sites-available/{id}.minimul.ro {id}.minimul.ro
    """.format(**vals))

def copy_site(id):
    os.system("""
        rm -fr /opt/minimul-sites/{id} 2>/dev/null
        mkdir -p /opt/minimul-sites 2>/dev/null
        cp -r /vagrant/sites/{id} /opt/minimul-sites/{id}
    """.format(id=id))

def main():
    sites = [
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
