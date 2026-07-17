# Ansible_Security

??? note "Ansible Security"


    **Official Documentation**

    **Ansible Documentation**

    [https://docs.ansible.com/ansible/latest/](https://docs.ansible.com/ansible/latest/)


    **RHEL System Roles**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/automating_system_administration_by_using_rhel_system_roles/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/automating_system_administration_by_using_rhel_system_roles/)



??? note "1. Installation"

    **Install Ansible**


    ```code
    sudo dnf install -y ansible-core
    ansible --version
    ```


??? note "2. Inventory"

    **Verify Inventory**


    ```code
    cat inventory
    ansible all -m ping
    ```


??? note "3. SELinux Automation"

    **Apply SELinux Configuration**


    ```code
    ansible-playbook selinux.yml
    ```


??? note "4. Firewalld Automation"

    **Configure Firewall**


    ```code
    ansible-playbook firewalld.yml
    ```


??? note "5. OpenSCAP Automation"

    **Apply Remediation**


    ```code
    ansible-playbook openscap-remediation.yml
    ```


??? note "6. Verification"

    **Check Results**


    ```code
    ansible all -m setup
    ```


??? note "7. EX415 Practice"

    **Common Exam Tasks**

    - Configure inventory.
    - Execute playbooks.
    - Configure SELinux.
    - Configure Firewalld.
    - Apply OpenSCAP remediation.
    - Verify configuration.