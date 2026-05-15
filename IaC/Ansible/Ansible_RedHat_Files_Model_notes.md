## RHEL (RED HAT) BASE SYSTEM INSTALLATION VIA ANSIBLE

### PROJECT STRUCTURE
```code
rhel-ansible/
├── inventory.ini
├── site.yml
└── roles/
    ├── common/
    │   └── tasks/main.yml
    ├── security/
    │   └── tasks/main.yml
    ├── packages/
    │   └── tasks/main.yml
    └── services/
        └── tasks/main.yml
```

```bash
### 1. INVENTORY
# rhel-ansible/inventory.ini
[redhat]
rhel-node1 ansible_host=192.168.1.10 ansible_user=root


### 2. MAIN PLAYBOOK
# rhel-ansible/site.yml
---
- name: RHEL Base System Setup
  hosts: redhat
  become: true
  roles:
    - common
    - security
    - packages
    - services


### 3. COMMON ROLE (SYSTEM BASICS)
# rhel-ansible/roles/common/tasks/main.yml
---
- name: Set hostname
  hostname:
    name: rhel-node1

- name: Update all packages
  dnf:
    name: "*"
    state: latest

- name: Install base tools
  dnf:
    name:
      - vim
      - curl
      - wget
      - net-tools
      - bash-completion
      - lsof
    state: present


### 4. SECURITY ROLE
# rhel-ansible/roles/security/tasks/main.yml
---
- name: Disable SELinux (temporary)
  selinux:
    state: permissive

- name: Configure firewalld (enable)
  systemd:
    name: firewalld
    enabled: true
    state: started

- name: Open SSH port
  firewalld:
    service: ssh
    permanent: true
    state: enabled
    immediate: true


### 5. PACKAGES ROLE
# rhel-ansible/roles/packages/tasks/main.yml
---
- name: Install system utilities
  dnf:
    name:
      - git
      - htop
      - tar
      - unzip
      - rsync
      - chrony
    state: present

- name: Enable time sync
  systemd:
    name: chronyd
    enabled: true
    state: started


### 6. SERVICES ROLE
# rhel-ansible/roles/services/tasks/main.yml
---
- name: Ensure SSH is enabled
  systemd:
    name: sshd
    enabled: true
    state: started

- name: Ensure firewalld is running
  systemd:
    name: firewalld
    enabled: true
    state: started


### 7. DELETE OLD STATE (OPTIONAL CLEAN START)
systemctl stop firewalld
dnf remove -y <unwanted-packages>
hostnamectl set-hostname localhost


### 8. RUN DEPLOYMENT
ansible-playbook -i inventory.ini site.yml


### 0. VERIFY SYSTEM
hostnamectl
dnf list installed | head
systemctl status sshd
systemctl status firewalld
ip a
firewall-cmd --list-all
