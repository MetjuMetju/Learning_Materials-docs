# SELinux

??? note "SELinux"


    **Official Documentation**

    **Red Hat Security Hardening Guide**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/)


    **SELinux Project Wiki**

    [https://github.com/SELinuxProject/selinux/wiki](https://github.com/SELinuxProject/selinux/wiki)



??? note "1. Installation and Verification"

    **Check SELinux Status**


    ```code
    # Check current mode
    getenforce
    # Display detailed status
    sestatus
    
    # Display configuration
    cat /etc/selinux/config
    ```


??? note "2. SELinux Modes"

    **Temporary Mode Changes**


    ```code
    # Switch to Permissive mode
    sudo setenforce 0
    # Switch to Enforcing mode
    sudo setenforce 1
    ```



    **Permanent Mode Changes**


    ```code
    # Edit configuration
    sudo vi /etc/selinux/config
    ```


??? note "3. Security Contexts"

    **File Contexts**


    ```code
    # View file contexts
    ls -Z
    ls -lZ /var/www
    ```

    **Process Contexts**


    ```code
    # View process contexts
    ps -eZ
    ps -eZ | grep httpd
    ```


??? note "4. File Labeling"

    **Restore Default Labels**


    ```code
    sudo restorecon -Rv /var/www
    ```


    **Temporary Labels**


    ```code
    sudo chcon -t httpd_sys_content_t index.html
    ```


    **Persistent Labels**


    ```code
    sudo semanage fcontext \
    -a \
    -t httpd_sys_content_t \
    "/web(/.*)?"
    sudo restorecon -Rv /web
    sudo semanage fcontext -l
    ```


??? note "5. SELinux Booleans"

    **View Booleans**


    ```code
    getsebool -a
    getsebool -a | grep http
    ```


    **Modify Booleans**


    ```code
    sudo setsebool -P httpd_can_network_connect on
    getsebool httpd_can_network_connect
    ```


??? note "6. SELinux Ports"

    **View Ports**


    ```code
    sudo semanage port -l
    ```


    **Add Port**


    ```code
    sudo semanage port \
    -a \
    -t http_port_t \
    -p tcp 8080
    ```


    **Remove Port**


    ```code
    sudo semanage port \
    -d \
    -t http_port_t \
    -p tcp 8080
    ```



??? note "7. Troubleshooting"

    **Audit Logs**


    ```code
    sudo ausearch -m AVC
    sudo sealert -a /var/log/audit/audit.log
    sudo less /var/log/audit/audit.log
    ```


    **Common Recovery**


    ```code
    sudo restorecon -Rv /var/www
    ls -lZ /var/www
    getsebool -a
    ```


??? note "8. EX415 Practice"

    **Common Exam Tasks**

    - Switch between Enforcing and Permissive mode.
    - Restore incorrect file labels.
    - Configure persistent file contexts.
    - Enable SELinux booleans.
    - Configure SELinux port mappings.
    - Investigate AVC denials.
    - Fix applications without disabling SELinux.