# Auditd

??? note "Auditd"


    **Official Documentation**

    **Linux Audit Project**

    [https://github.com/linux-audit/audit-documentation](https://github.com/linux-audit/audit-documentation)


    **audit-userspace**

    [https://github.com/linux-audit/audit-userspace](https://github.com/linux-audit/audit-userspace)


??? note "1. Installation and Verification"

    **Install and Verify Auditd**


    ```code
    # Install Auditd
    sudo dnf install -y audit
    
    # Enable service
    sudo systemctl enable --now auditd
    
    # Verify service
    systemctl status auditd
    
    # Verify version
    auditctl -v
    ```



??? note "2. Audit Rules"

    **View Rules**


    ```code
    # List active rules
    sudo auditctl -l
    
    # View persistent rules
    sudo cat /etc/audit/rules.d/audit.rules
    ```


    **Create Rules**


    ```code
    # Watch passwd file
    sudo auditctl -w /etc/passwd -p wa -k passwd_changes
    
    # Watch shadow file
    sudo auditctl -w /etc/shadow -p wa -k shadow_changes
    
    # Watch sudoers
    sudo auditctl -w /etc/sudoers -p wa -k sudo_changes
    ```


    **Persistent Rules**


    ```code
    # Create custom rules file
    sudo vi /etc/audit/rules.d/custom.rules
    
    # Reload Auditd
    sudo augenrules --load
    ```



??? note "3. Searching Audit Logs"

    **Search Events**


    ```code
    # Search by key
    sudo ausearch -k passwd_changes
    
    # Search AVC denials
    sudo ausearch -m AVC
    
    # Search failed logins
    sudo ausearch -m USER_LOGIN
    ```


    **Search by Time**


    ```code
    # Today's events
    sudo ausearch -ts today
    
    # Recent events
    sudo ausearch -ts recent
    ```



??? note "4. Reports"

    **Generate Reports**


    ```code
    # Authentication report
    sudo aureport --auth
    
    # Login report
    sudo aureport --login
    
    # File report
    sudo aureport --file
    
    # Summary report
    sudo aureport --summary
    ```



??? note "5. Log Files"

    **Audit Logs**


    ```code
    # View audit log
    sudo less /var/log/audit/audit.log
    
    # Follow log
    sudo tail -f /var/log/audit/audit.log
    ```



??? note "6. Troubleshooting"

    **Verify Audit Configuration**


    ```code
    # Verify service
    systemctl status auditd
    
    # View loaded rules
    sudo auditctl -l
    
    # Reload rules
    sudo augenrules --load
    
    # Restart Auditd
    sudo systemctl restart auditd
    ```



??? note "7. EX415 Practice"

    **Common Exam Tasks**

    - Install and enable Auditd.
    - Create audit watch rules.
    - Configure persistent audit rules.
    - Search audit events.
    - Generate audit reports.
    - Investigate authentication events.
    - Investigate SELinux AVC denials.
    - Verify Auditd configuration.