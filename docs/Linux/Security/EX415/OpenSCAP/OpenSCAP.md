# OpenSCAP

??? note "OpenSCAP"


    **Official Documentation**

    **OpenSCAP Project**

    [https://www.open-scap.org/](https://www.open-scap.org/)


    **Red Hat Security Hardening Guide**

    [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/)


    **SCAP Security Guide (SSG)**

    [https://www.open-scap.org/security-policies/scap-security-guide/](https://www.open-scap.org/security-policies/scap-security-guide/)



??? note "1. Installation and Verification"

    **Install OpenSCAP Tools**


    ```code
    # Install OpenSCAP scanner and security content
    sudo dnf install -y openscap-scanner scap-security-guide
    
    # Verify installation
    oscap --version
    ```



??? note "2. Security Content"

    **Locate SCAP Content**


    ```code
    # List installed SCAP content
    ls -l /usr/share/xml/scap/ssg/content/
    
    # Display information about the RHEL data stream
    oscap info /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    ```


    **List Available Profiles**


    ```code
    # Display available compliance profiles
    oscap info /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml | less
    ```



??? note "3. Compliance Scanning"

    **Run Security Scan**


    ```code
    # Evaluate system compliance
    sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cis \
    --results results.xml \
    --report report.html \
    /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    
    # Open HTML report
    firefox report.html
    ```



??? note "4. Remediation"

    **Generate Remediation Script**


    ```code
    # Generate Bash remediation script
    sudo oscap xccdf generate fix \
    --profile xccdf_org.ssgproject.content_profile_cis \
    --fix-type bash \
    --output remediation.sh \
    /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    
    # Apply remediation
    sudo bash remediation.sh
    ```



??? note "5. Verification"

    **Verify Compliance Again**


    ```code
    # Run compliance scan after remediation
    sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cis \
    --results after-remediation.xml \
    --report after-remediation.html \
    /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    ```



??? note "6. Troubleshooting"

    **Review Logs**


    ```code
    # View system log
    journalctl -xe
    
    # Search SELinux AVC denials
    ausearch -m AVC
    
    # Analyze SELinux alerts
    sealert -a /var/log/audit/audit.log
    ```



??? note "7. EX415 Practice"

    **Common Exam Tasks**

    - Install OpenSCAP and SCAP Security Guide.
    - Locate installed SCAP content.
    - Identify available compliance profiles.
    - Run XCCDF compliance scans.
    - Generate HTML compliance reports.
    - Generate Bash remediation scripts.
    - Apply automated remediations.
    - Verify system compliance after remediation.
    - Troubleshoot scan failures and SELinux denials.