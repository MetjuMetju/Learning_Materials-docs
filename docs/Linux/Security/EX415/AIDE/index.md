# AIDE

??? note "AIDE"


    **Official Documentation**

    **AIDE Project**

    [https://github.com/aide/aide](https://github.com/aide/aide)



??? note "1. Installation and Verification"

    **Install AIDE**


    ```code
    sudo dnf install -y aide
    aide --version
    ```


??? note "2. Initialize Database"

    **Create Baseline**


    ```code
    sudo aide --init
    sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
    ```


??? note "3. Integrity Checking"

    **Run Scan**


    ```code
    sudo aide --check
    ```


??? note "4. Update Baseline"

    **Create New Database**


    ```code
    sudo aide --update
    sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
    ```


??? note "5. Troubleshooting"

    **Verify Configuration**


    ```code
    cat /etc/aide.conf
    ls -l /var/lib/aide/
    ```


??? note "6. EX415 Practice"

    **Common Exam Tasks**

    - Install AIDE.
    - Initialize database.
    - Detect file changes.
    - Update baseline.
    - Verify configuration.