# Firewalld

??? note "Firewalld"


    **Official Documentation**

    **Red Hat Security Hardening Guide**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/)


    **Firewalld Project**

    [https://firewalld.org/](https://firewalld.org/)



??? note "1. Installation and Verification"

    **Install and Check Service**


    ```code
    # Install Firewalld
    sudo dnf install -y firewalld
    
    # Enable service
    sudo systemctl enable --now firewalld
    
    # Verify service
    systemctl status firewalld
    
    # Verify firewall state
    firewall-cmd --state
    ```



??? note "2. Zones"

    **View Zones**


    ```code
    firewall-cmd --get-default-zone
    firewall-cmd --get-active-zones
    firewall-cmd --get-zones
    firewall-cmd --list-all
    ```


    **Change Default Zone**


    ```code
    sudo firewall-cmd --set-default-zone=public
    ```



??? note "3. Services"

    **View Services**


    ```code
    firewall-cmd --list-services
    firewall-cmd --get-services
    ```


    **Allow Services**


    ```code
    sudo firewall-cmd --add-service=http
    sudo firewall-cmd --permanent --add-service=https
    sudo firewall-cmd --reload
    ```


    **Remove Services**


    ```code
    sudo firewall-cmd --permanent --remove-service=http
    sudo firewall-cmd --reload
    ```



??? note "4. Ports"

    **Open Ports**


    ```code
    sudo firewall-cmd --add-port=8080/tcp
    sudo firewall-cmd --permanent --add-port=8443/tcp
    sudo firewall-cmd --reload
    ```


    **Close Ports**


    ```code
    sudo firewall-cmd --permanent --remove-port=8080/tcp
    sudo firewall-cmd --reload
    ```


    **View Ports**


    ```code
    firewall-cmd --list-ports
    ```



??? note "5. Rich Rules"

    **Create Rich Rule**


    ```code
    sudo firewall-cmd \
    --permanent \
    --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="ssh" accept"
    
    sudo firewall-cmd --reload
    ```


    **List Rich Rules**


    ```code
    firewall-cmd --list-rich-rules
    ```



??? note "6. Runtime vs Permanent"

    **Runtime Configuration**


    ```code
    sudo firewall-cmd --add-service=http
    firewall-cmd --list-services
    ```


    **Permanent Configuration**


    ```code
    sudo firewall-cmd --permanent --add-service=http
    sudo firewall-cmd --reload
    firewall-cmd --list-services
    ```



??? note "7. Troubleshooting"

    **Verify Configuration**


    ```code
    firewall-cmd --check-config
    firewall-cmd --list-all
    firewall-cmd --list-all-zones
    ```


    **Service Status**


    ```code
    systemctl status firewalld
    journalctl -u firewalld
    ```



??? note "8. EX415 Practice"

    **Common Exam Tasks**

    - Configure default zone.
    - Enable and disable services.
    - Open and close ports.
    - Configure rich rules.
    - Distinguish runtime and permanent configuration.
    - Reload firewall configuration.
    - Verify firewall rules.