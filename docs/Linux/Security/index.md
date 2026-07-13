# Linux Security

Linux security is the practice of protecting Linux systems using access control, hardening, auditing, compliance checks, and vulnerability management.

## Official Documentation

Red Hat Enterprise Linux Security Documentation

https://docs.redhat.com/en/documentation/red_hat_enterprise_linux

NIST SCAP

https://csrc.nist.gov/projects/security-content-automation-protocol

OpenSCAP

https://www.open-scap.org/

CIS Benchmarks

https://www.cisecurity.org/cis-benchmarks

DISA STIG

https://public.cyber.mil/stigs/


---

# Security Fundamentals

## Authentication

Authentication answers:

"Who are you?"

Common methods:

- Passwords
- SSH keys
- Certificates
- Multi-factor authentication


### Basic commands

```bash
id
who
last
```

???+ info "Click to expand: Authentication details"

    Authentication verifies the identity of a user or system.

    Examples:

    - Logging into Linux with a password
    - Connecting using an SSH key
    - Using LDAP or Active Directory authentication

    Linux authentication is commonly managed through PAM.
    Authorization

    Authorization answers:

    "What are you allowed to do?"

    Linux controls access using:

    File permissions
    Users and groups
    sudo
    ACLs
    Basic commands
    ls -l

    groups

    sudo -l

???+ note "Click to expand: Authorization example"

    Example:

    A user may successfully authenticate:

    ```text
    User: john
    Password: correct
    ```

    But authorization decides:

    ```text
    Can john run this command?
    Can john read this file?
    Can john become root?
    ```
    Encryption

    Encryption protects information from unauthorized access.

    Two main types:

    Data at rest

    Examples:

    LUKS disk encryption
    Encrypted backups
    Data in transit

    Examples:

    SSH
    TLS
    HTTPS

???+ tip "Click to expand: Encryption commands"

    Check certificates:

    ```bash
    openssl x509 -text -in certificate.crt
    ```

    Test TLS:

    ```bash
    openssl s_client -connect example.com:443
    ```
    Remember

    Authentication

    Who are you?

    Authorization

    What can you do?

    Encryption

    Can someone read your data?
