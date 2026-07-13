# OpenSCAP

OpenSCAP is an open source security compliance scanner for Linux systems.

It is used to check systems against security standards:

- CIS Benchmarks
- DISA STIG
- PCI DSS
- NIST security profiles


## Official Documentation

**OpenSCAP**

https://www.open-scap.org/


**Red Hat Security Documentation**

https://docs.redhat.com/en/documentation/red_hat_enterprise_linux


**ComplianceAsCode**

https://github.com/ComplianceAsCode/content


**NIST SCAP**

https://csrc.nist.gov/projects/security-content-automation-protocol


---

## Installation


???+ info "Install OpenSCAP on RHEL"

    ```bash
    sudo dnf install openscap-scanner scap-security-guide
    ```


???+ info "Verify installation"

    ```bash
    oscap --version
    ```


---

## Security Content


OpenSCAP uses security content provided by SCAP Security Guide.

The package contains profiles for:

- CIS
- STIG
- PCI DSS
- Standard security baseline


???+ info "Find available security content"

    ```bash
    ls /usr/share/xml/scap/ssg/content/
    ```


???+ info "Show available profiles"

    ```bash
    oscap info /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    ```


---

## Basic Scan


???+ info "Run compliance scan"

    ```bash
    sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_standard \
    --report report.html \
    /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
    ```


The result is an HTML report:

```text
report.html
```

## Remediation

OpenSCAP can create remediation instructions.
Ansible is commonly used to apply the fixes.

???+ info "Generate Ansible remediation"

    ```bash
    oscap xccdf generate fix \
    --fix-type ansible \
    results.xml > remediation.yml
    ```

???+ info "Run remediation"

    ```bash
    ansible-playbook remediation.yml
    ```

## Common Commands

???+ info "Show version"

    ```bash
    oscap --version
    ```

???+ info "Show profile information"

    ```bash
    oscap info file.xml
    ```

???+ info "Run evaluation"

    ```bash
    oscap xccdf eval
    ```
