### Ansible using for KeyDB notes

### OFFICIAL DOCUMENTATIONS
Ansible:
<br>
https://docs.ansible.com
<br>
https://docs.ansible.com/projects/ansible/latest/collections/ansible/posix/index.html
<br>

Ansible Roles:
<br>
https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html
<br>

KeyDB:
<br>
https://docs.keydb.dev
<br>
https://docs.keydb.dev/docs/ppa-deb/
<br>
https://docs.keydb.dev/docs/rpm/
<br>
https://docs.keydb.dev/docs/config-file
<br>

KeyDB GitHub:
<br>
https://github.com/Snapchat/KeyDB
<br>

### TASK
    
#### Create an Ansible role that installs and configures KeyDB.

1. INSTALL KEYDB
    - Add KeyDB repository
    - Install keydb-server
    - Make sure required Ubuntu packages are installed

2. KEYDB CONFIG
    - Deploy KeyDB configuration using Ansible template
    - Config values come from inventory variables

3. RESTART
    - If config changes -> restart KeyDB
    - Use Ansible handler

4. SYSCTL

    - Set:
        - net.core.somaxconn = 65535
        - net.ipv4.tcp_max_syn_backlog = 511
    - Use Ansible sysctl module.


5. INVENTORY VARIABLES
    - Parameterize:
        - maxclients
        - maxmemory
        - maxmemory-policy

    - replicaof
        - must support multiple entries -> LIST

    - active-replica
    - multi-master

6. IDEMPOTENCE
    - Running the role twice should produce the same result.
    - Example:
        - 1st run -> changes system
        - 2nd run -> ideally "changed=0"


### SIMPLE ROLE STRUCTURE

    roles/keydb/
    tasks/main.yml
    handlers/main.yml
    templates/keydb.conf.j2
    defaults/main.yml
    vars/main.yml

### MAIN FLOW

    tasks:
    install repository
    install packages
    configure sysctl
    deploy keydb.conf
    notify restart

    handler:
    restart keydb


### IMPORTANT
- Use defaults/main.yml for variables that the user should override from inventory.
```code
    Example:
    keydb_maxclients: 10000
    keydb_maxmemory: 2gb
    keydb_maxmemory_policy: allkeys-lru
    keydb_replicaof: []
    keydb_active_replica: false
    keydb_multi_master: false
```
- Inventory can override these values per server.


### FILES STRUCTURE:
defaults/main.yml
<br>

```code
mkdir -p roles/keydb/{tasks,handlers,templates,defaults,vars}

Galaxy command:
ansible-galaxy role init roles/keydb

Created automatically by the command:
roles/keydb/defaults/main.yml
roles/keydb/handlers/main.yml
roles/keydb/tasks/main.yml
roles/keydb/templates/
roles/keydb/files/

roles/keydb/meta/main.yml
roles/keydb/tests/
roles/keydb/vars/main.yml
roles/keydb/README.md

### Created manually:
inventory.yml
keydb.yml     (could be also: site.yml)
roles/keydb/templates/keydb.conf.j2

### ansible-galaxy role init roles/keydb
roles/keydb/defaults/main.yml
roles/keydb/files/
roles/keydb/handlers/main.yml
roles/keydb/meta/main.yml
roles/keydb/README.md
roles/keydb/tasks/main.yml
roles/keydb/templates/
roles/keydb/tests/inventory
roles/keydb/tests/test.yml
roles/keydb/vars/main.yml
```
<br>

### TEST ROLE:

```code
cd roles/keydb
ansible-playbook -i tests/inventory tests/test.yml

- But your real project deployment stays outside the role:
~/Ansible/
├── inventory.yml
├── keydb.yml
└── roles/keydb/
```

### repository part task + configuration part task:
```code
inventory.yml
keydb.yml
roles/keydb/defaults/main.yml
roles/keydb/tasks/main.yml
```

### Commands part:

```code
ansible-playbook -i inventory.yml keydb.yml
ansible-playbook -i inventory.yml keydb.yml -k -K
-k = ask SSH password
-K = ask sudo password

ansible all -i inventory.yml -m ping -k
ansible keydb -i inventory.yml -m setup -a 'filter=ansible_os_family' -k -K

1. Test SSH:
ssh mates@192.168.0.215

2. Test Ansible connectivity:
ansible all -i inventory.yml -m ping -k

3. Check OS:
cat /etc/os-release

4. Check KeyDB package:
rpm -q keydb-server

5. Check KeyDB service:
systemctl status keydb --no-pager
systemctl list-units --type=service | grep -i keydb
systemctl cat keydb.service

6. Check KeyDB version:
keydb-server --version

7. Check KeyDB is listening:
ss -lntp | grep 6379

8. Test KeyDB locally:
keydb-cli ping
ps aux | grep '[k]eydb'
sudo cat /etc/keydb/keydb.conf

9. Check sysctl
sysctl net.core.somaxconn
sysctl net.ipv4.tcp_max_syn_backlog

10. Check the persistent configuration:
sudo grep -R "net.core.somaxconn\|net.ipv4.tcp_max_syn_backlog" /etc/sysctl.conf /etc/sysctl.d/ 2>/dev/null

11. running kernel values:
sysctl -n net.core.somaxconn
sysctl -n net.ipv4.tcp_max_syn_backlog

12. check ansible modules
ansible --version
ansible-galaxy collection list ansible.posix
ansible-galaxy collection list
```

### FILES CONTENTS
```code
vi inventory.yml
all:
  children:
    keydb:
      hosts:
        keydb01:
          ansible_user: mates
          ansible_host: 192.168.0.215

vi keydb.yml
---
- name: Install KeyDB
  hosts: keydb
  become: true
  roles:
    - keydb


vi roles/keydb/defaults/main.yml
---
keydb_repo: "deb https://download.keydb.dev/open-source-dist {{ ansible_distribution_release }} main"
keydb_package: keydb-server

keydb_rpm_key: "https://download.keydb.dev/pkg/open_source/rpm/RPM-GPG-KEY-keydb"
keydb_rpm_url: "https://download.keydb.dev/pkg/open_source/rpm/centos8/x86_64/keydb-latest-1.el8.x86_64.rpm"

keydb_service: keydb
keydb_config: /etc/keydb/keydb.conf

keydb_sysctl:
  net.core.somaxconn: 65535
  net.ipv4.tcp_max_syn_backlog: 511



vi roles/keydb/tasks/main.yml
---
- name: Include Debian tasks
  ansible.builtin.include_tasks: Debian.yml
  when: ansible_os_family == "Debian"
- name: Include RedHat tasks
  ansible.builtin.include_tasks: RedHat.yml
  when: ansible_os_family == "RedHat"
- name: Deploy KeyDB configuration
  ansible.builtin.template:
    src: keydb.conf.j2
    dest: "{{ keydb_config }}"
    owner: keydb
    group: keydb
    mode: "0644"
  notify: Restart KeyDB
- name: Enable and start KeyDB
  ansible.builtin.systemd:
    name: "{{ keydb_service }}"
    enabled: true
    state: started
- name: Configure KeyDB sysctl parameters
  ansible.posix.sysctl:
    name: "{{ item.key }}"
    value: "{{ item.value }}"
    state: present
    sysctl_set: true
    reload: true
  loop: "{{ keydb_sysctl | dict2items }}"

vi roles/keydb/tasks/Debian.yml
---
- name: Install required packages
  ansible.builtin.apt:
    name:
      - ca-certificates
      - curl
      - gnupg
    state: present
    update_cache: true
- name: Add KeyDB repository
  ansible.builtin.apt_repository:
    repo: "{{ keydb_repo }}"
    state: present
    filename: keydb
- name: Install KeyDB
  ansible.builtin.apt:
    name: "{{ keydb_package }}"
    state: present
    update_cache: true


vi roles/keydb/tasks/RedHat.yml
---
- name: Install required packages
  ansible.builtin.dnf:
    name:
      - ca-certificates
      - curl
    state: present
- name: Import KeyDB RPM signing key
  ansible.builtin.rpm_key:
    key: "{{ keydb_rpm_key }}"
    state: present
- name: Install KeyDB
  ansible.builtin.dnf:
    name: "{{ keydb_rpm_url }}"
    state: present
    disable_gpg_check: false

vi roles/keydb/handlers/main.yml
---
- name: Restart KeyDB
  ansible.builtin.systemd:
    name: "{{ keydb_service }}"
    state: restarted

vi roles/keydb/templates/keydb.conf.j2
bind 0.0.0.0
port 6379
daemonize no        # don't background yourself
supervised systemd  # let systemd manage - supervise you


### NOTES:
    - for ansible.posix.sysctl, state: present
        - tells Ansible to ensure the setting is present in the persistent sysctl configuration file
    - sysctl_set: true
        - set the value in the running kernel
    - reload: true
        - applies the configuration after changing it


### If ONLY FOR UBUNTU:
vi roles/keydb/tasks/main.yml
---
- name: Install required packages
  ansible.builtin.apt:
    name:
      - ca-certificates
      - curl
      - gnupg
    state: present
    update_cache: true

- name: Add KeyDB repository
  ansible.builtin.apt_repository:
    repo: "{{ keydb_repo }}"
    state: present
    filename: keydb

- name: Install KeyDB
  ansible.builtin.apt:
    name: "{{ keydb_package }}"
    state: present
    update_cache: true
```