# VIP with VRRP and used for HAProxy notes

### Official Documentations

https://www.keepalived.org/documentation/keepalived-conf/
<br>
https://www.rfc-editor.org/rfc/rfc9568.html
<br>
https://www.haproxy.com/downloads
<br>
https://www.haproxy.com/documentation/haproxy-configuration-tutorials/proxying-essentials/configuration-basics/
<br>

### VRRP (Virtual Router Redundancy Protocol)
- provides a virtual/floating IP (VIP)
- VIP moves between MASTER and BACKUP
- used for high availability / failover


### Install keepalived and haproxy

    sudo apt update
    sudo apt install -y keepalived haproxy
    keepalived --version
    haproxy -v
    ls -l /etc/keepalived

### Create the dedicated user (on both servers):

```code
sudo useradd --system --no-create-home --shell /usr/sbin/nologin keepalived_script
getent passwd keepalived_script
```

### Check for any existing VRRP IDs:

    sudo tcpdump -ni eth0 'ip proto 112'


### On Backup server:
```code
    sudo systemctl stop haproxy     # on backup one
    sudo systemctl start haproxy    # after started on master
    ls -l /usr/bin/systemctl
    /usr/bin/systemctl is-active --quiet haproxy
    echo $?


### /etc/keepalived/keepalived.conf

global_defs {
    router_id STARTER_BACKUP
    enable_script_security
}
vrrp_script chk_haproxy {
    script "/usr/bin/systemctl is-active --quiet haproxy"
    interval 2
    weight -100
}
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    unicast_src_ip 37.27.32.56
    unicast_peer {
        204.168.132.77
    }
    authentication {
        auth_type PASS
        auth_pass test1234
    }
    virtual_ipaddress {
        10.250.0.224/32
    }
    track_script {
        chk_haproxy
    }
}

sudo keepalived -t -f /etc/keepalived/keepalived.conf
```

### On Master:
```code
sudo systemctl start haproxy
pgrep -x haproxy
command -v systemctl
ls -l /usr/bin/systemctl
/usr/bin/systemctl is-active --quiet haproxy
echo $?

### /etc/keepalived/keepalived.conf
global_defs {
    router_id KLAB_MASTER
    enable_script_security
}
vrrp_script chk_haproxy {
    script "/usr/bin/systemctl is-active --quiet haproxy"
    interval 2
    weight -100
}
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 150
    advert_int 1
    unicast_src_ip 204.168.132.77
    unicast_peer {
        37.27.32.56
    }
    authentication {
        auth_type PASS
        auth_pass test1234
    }
    virtual_ipaddress {
        10.250.0.224/32
    }
    track_script {
        chk_haproxy
    }
}

sudo keepalived -t -f /etc/keepalived/keepalived.conf
sudo systemctl enable --now keepalived
ip addr show eth0 | grep 10.250.0.224
sudo journalctl -u keepalived --no-pager
sudo journalctl -u keepalived --since "2 minutes ago" --no-pager
sudo systemctl stop haproxy
sudo systemctl start haproxy
sudo systemctl status haproxy
```

### Notes:
```code
- interval 2 = HAProxy check interval - check HAProxy every 2 seconds
- advert_int 1 = VRRP advertisement interval - MASTER sends VRRP "I'm alive" every 1 second

- vrrp_script chk_haproxy  -> defines the check
- track_script chk_haproxy -> attaches the check to VRRP

- The IPv4 multicast address as assigned by the IANA for VRRP is: 224.0.0.18
- This is a link-local scope multicast address.
- Routers MUST NOT forward a datagram with this destination address, regardless of its TTL.
https://www.rfc-editor.org/rfc/rfc9568.html
VRRP = IP protocol number 112 (Layer 3 - Network in ISO)
```

### Useful commands:
```code
sudo systemctl stop haproxy
sudo systemctl stop keepalived
ip neigh show
- the Linux ARP/neighbor table. It shows which IP addresses the machine has recently resolved to MAC addresses on directly reachable networks.
ip route get 172.31.1.1
ping -c 3 37.27.32.56
ping -c 3 204.168.132.77

ip addr show eth0

### on server 1:
sudo tcpdump -ni eth0 'host 37.27.32.56 and ip proto 112'
### on server 2:
sudo tcpdump -ni eth0 'host 204.168.132.77 and ip proto 112'

ip addr
ip -br addr
ip addr show eth0
ip route
sudo tcpdump -ni eth0 'ip proto 112'
sudo systemctl cat keepalived
sudo cat /etc/keepalived/keepalived.conf 2>/dev/null
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo ss -lntp | grep haproxy

# Check keepalived
systemctl status keepalived --no-pager
journalctl -u keepalived --no-pager

# Check HAProxy
systemctl status haproxy --no-pager
journalctl -u haproxy --no-pager

# Check VIP
ip addr show

# Check keepalived config
cat /etc/keepalived/keepalived.conf

# Check HAProxy config
cat /etc/haproxy/haproxy.cfg

# Check VRRP traffic
tcpdump -ni any 'ip proto 112'

# Test HAProxy failover
systemctl stop haproxy

# Start HAProxy again
systemctl start haproxy

# Test keepalived failover
systemctl stop keepalived
```