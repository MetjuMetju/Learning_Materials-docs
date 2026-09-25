### Ansible Config File - CONFIGURATION

### FILE:
Ansible/ansible.cfg

### OBJECT:

        [defaults]

- Defines common Ansible behavior for this project.

### USED SETTINGS:

Where project roles are located:

        roles_path

Avoids SSH host key confirmation during the lab:

        host_key_checking = False

Avoids creating retry files:

        retry_files_enabled = False


Automatically selects Python on managed hosts:

        interpreter_python = auto_silent


Part [privilege_escalation]

        [privilege_escalation]

        become = True
        become_method = sudo

- If true

        become_ask_pass = True

- Ansible asks:
        
        BECOME password:

- Command-line alternative
- Instead of changing the config:

        ansible-playbook playbooks/deploy.yml --ask-become-pass

- Short version:

        ansible-playbook playbooks/deploy.yml -K


Alternative methods

- Ansible supports other privilege escalation methods, for example:

        sudo
        su
        doas
        pfexec
        dzdo
        ksu
        machinectl

        become_ask_pass


ansible-playbook \
  -i inventories/prod/hosts.yml \
  playbooks/deploy.yml \
  --ask-vault-pass

ansible-vault create inventories/prod/group_vars/all/vault.yml
ansible-vault rekey inventories/prod/group_vars/all/vault.yml

head -n 1 inventories/dev/group_vars/all/vault.yml

ansible-playbook \
  -i inventories/prod/hosts.yml \
  playbooks/deploy.yml \
  --ask-pass \
  --ask-become-pass \
  --ask-vault-pass

ansible-playbook -i inventories/dev/hosts.yml playbooks/install-docker.yml --ask-pass --ask-become-pass