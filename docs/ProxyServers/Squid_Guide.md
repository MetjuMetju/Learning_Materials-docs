### SQUID

- Client → Squid → Internet

Official site

    https://www.squid-cache.org


Configuration

    /etc/squid/squid.conf

Port

    3128

Basic configuration

    http_port 3128
    acl localnet src 192.168.1.0/24
    http_access allow localnet
    http_access deny all

Start

    systemctl enable --now squid

Check configuration

    squid -k parse

Reload

    systemctl reload squid

Log

    /var/log/squid/access.log