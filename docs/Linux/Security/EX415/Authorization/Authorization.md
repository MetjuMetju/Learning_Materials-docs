# Authorization

??? note "Authorization"


    **Official Documentation**

    **Red Hat Security Hardening Guide**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/)



??? note "1. sudo"

    **Configuration**


    ```code
    # Edit sudoers safely
    sudo visudo
    
    # Validate configuration
    visudo -c
    
    # View current privileges
    sudo -l
    ```


    **sudoers.d**


    ```code
    # List additional rules
    ls -l /etc/sudoers.d/
    
    # View rule file
    sudo cat /etc/sudoers.d/*
    ```



??? note "2. Password Policies"

    **Password Aging**


    ```code
    # View password aging
    chage -l username
    
    # Maximum password age
    sudo chage -M 90 username
    
    # Minimum password age
    sudo chage -m 7 username
    
    # Warning days
    sudo chage -W 14 username
    ```


    **System Defaults**


    ```code
    # View login defaults
    cat /etc/login.defs
    
    # View password quality
    cat /etc/security/pwquality.conf
    ```



??? note "3. Account Lockout"

    **Failed Login Tracking**


    ```code
    # Display failed logins
    sudo faillock
    
    # Reset failures
    sudo faillock --user username --reset
    ```



??? note "4. Troubleshooting"

    **Verify Permissions**


    ```code
    # Verify sudo access
    sudo -l
    
    # Check login definitions
    cat /etc/login.defs
    
    # Check password policy
    cat /etc/security/pwquality.conf
    ```



??? note "5. EX415 Practice"

    **Common Exam Tasks**

    - Configure sudo privileges.
    - Validate sudoers configuration.
    - Configure password aging.
    - Configure password quality policies.
    - Reset failed login counters.
    - Troubleshoot authorization problems.