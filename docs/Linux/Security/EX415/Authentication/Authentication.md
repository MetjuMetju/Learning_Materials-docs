# Authentication

??? note "Authentication"


    **Official Documentation**

    **Red Hat Security Hardening Guide**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/)


    **Linux-PAM**

    [https://www.linux-pam.org/](https://www.linux-pam.org/)


    **SSSD Project**

    [https://sssd.io/](https://sssd.io/)



??? note "1. PAM"

    **Configuration**


    ```code
    # View PAM configuration
    ls /etc/pam.d/
    
    # View system-auth
    cat /etc/pam.d/system-auth
    
    # View password-auth
    cat /etc/pam.d/password-auth
    ```



??? note "2. SSSD"

    **Installation**


    ```code
    # Install SSSD
    sudo dnf install -y sssd
    
    # Enable service
    sudo systemctl enable --now sssd
    
    # Verify service
    systemctl status sssd
    ```


    **Configuration**


    ```code
    # View configuration
    sudo cat /etc/sssd/sssd.conf
    
    # Validate configuration
    sudo sssctl config-check
    
    # Restart service
    sudo systemctl restart sssd
    ```



??? note "3. Identity Verification"

    **User Lookup**


    ```code
    # Query local and remote users
    id username
    
    getent passwd username
    
    getent group
    
    cat /etc/nsswitch.conf
    ```



??? note "4. Troubleshooting"

    **Authentication Logs**


    ```code
    journalctl -xe
    
    journalctl -u sssd
    
    sudo sss_cache -E
    ```



??? note "5. EX415 Practice"

    **Common Exam Tasks**

    - Configure PAM.
    - Install and configure SSSD.
    - Verify user authentication.
    - Troubleshoot authentication failures.