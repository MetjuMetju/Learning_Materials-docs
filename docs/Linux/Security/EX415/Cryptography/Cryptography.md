# Cryptography

??? note "Cryptography"


    **Official Documentation**

    **OpenSSL**

    [https://docs.openssl.org/](https://docs.openssl.org/)


    **GnuPG**

    [https://gnupg.org/documentation/](https://gnupg.org/documentation/)



??? note "1. OpenSSL"

    **Version and Random Data**


    ```code
    openssl version
    openssl rand -hex 32
    ```


    **Hash Files**


    ```code
    sha256sum file.txt
    openssl dgst -sha256 file.txt
    ```


??? note "2. TLS Certificates"

    **Generate Private Key**


    ```code
    openssl genrsa -out server.key 4096
    ```


    **Generate Certificate Request**


    ```code
    openssl req -new -key server.key -out server.csr
    ```


    **Generate Self-Signed Certificate**


    ```code
    openssl req -x509 -nodes -days 365 \
    -key server.key \
    -out server.crt
    ```


    **Inspect Certificate**


    ```code
    openssl x509 -in server.crt -text -noout
    ```


??? note "3. GPG"

    **Generate Key**


    ```code
    gpg --full-generate-key
    ```


    **List Keys**


    ```code
    gpg --list-keys
    gpg --list-secret-keys
    ```


    **Encrypt and Decrypt**


    ```code
    gpg -e -r username file.txt
    gpg -d file.txt.gpg
    ```


    **Sign and Verify**


    ```code
    gpg --sign file.txt
    gpg --verify file.txt.gpg
    ```


??? note "4. EX415 Practice"

    **Common Exam Tasks**

    - Generate hashes.
    - Create TLS certificates.
    - Inspect certificates.
    - Generate GPG keys.
    - Encrypt and decrypt files.
    - Sign and verify files.