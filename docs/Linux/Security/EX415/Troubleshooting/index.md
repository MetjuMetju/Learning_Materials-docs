# Troubleshooting

??? note "Troubleshooting"


    **Official Documentation**

    **Red Hat Documentation**

    [https://docs.redhat.com/](https://docs.redhat.com/)



??? note "1. SELinux"

    **Investigate AVC Denials**


    ```code
    ausearch -m AVC
    sealert -a /var/log/audit/audit.log
    restorecon -Rv /var/www
    ```


??? note "2. Firewalld"

    **Verify Firewall**


    ```code
    firewall-cmd --state
    firewall-cmd --list-all
    firewall-cmd --list-all-zones
    ```


??? note "3. Authentication"

    **Verify Authentication**


    ```code
    systemctl status sssd
    id username
    getent passwd username
    ```


??? note "4. Authorization"

    **Verify sudo**


    ```code
    sudo -l
    visudo -c
    ```


??? note "5. Auditd"

    **Search Audit Events**


    ```code
    auditctl -l
    ausearch -m AVC
    aureport --summary
    ```


??? note "6. OpenSCAP"

    **Verify Compliance**


    ```code
    oscap --version
    oscap info /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    ```


??? note "7. AIDE"

    **Verify Integrity**


    ```code
    aide --check
    ```


??? note "8. EX415 Practice"

    **Common Exam Tasks**

    - Diagnose SELinux issues.
    - Diagnose firewall problems.
    - Troubleshoot authentication.
    - Troubleshoot sudo.
    - Investigate audit logs.
    - Verify OpenSCAP scans.
    - Verify file integrity.