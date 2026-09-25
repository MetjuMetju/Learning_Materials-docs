### 1. SELF-SIGNED CERTIFICATE
   Type:
   - X.509 certificate
   - Self-signed
   - RSA 2048-bit private key
   - Valid for 365 days

   Generated with:
   - OpenSSL
   - alpine/openssl

   Files:
   certs/server.crt
   certs/server.key

   Used for:
   - Local development
   - Local production-style testing

   Important:
   Browsers and curl do not automatically trust a self-signed
   certificate because it is not issued by a trusted CA.

   That is why we use:
   curl -k https://localhost:8443


### 2. CERTIFICATE ISSUED BY A TRUSTED CA

   This is what you normally use for real public production.

   Examples of Certificate Authorities:
   - Let's Encrypt
   - DigiCert
   - GlobalSign
   - Sectigo

   The CA signs the certificate, so normal browsers and operating
   systems can trust it.

   Example:
   https://example.com
   would use a certificate issued for example.com by a trusted CA.


### 3. LET'S ENCRYPT

   A very common free alternative for production.

   Characteristics:
   - Trusted by browsers
   - Free
   - Automated certificate issuance
   - Automated renewal
   - Uses ACME

   Typical tools:
   - Certbot
   - ACME clients
   - cert-manager in Kubernetes


### 4. INTERNAL / PRIVATE CA

   Useful when the application is only inside an organization.

   Example:

   Internal CA
       |
       +-- certificate for nginx
       +-- certificate for internal API
       +-- certificate for internal services

   The organization's computers must trust the internal CA.

   Examples:
   - HashiCorp Vault PKI
   - Smallstep step-ca
   - Microsoft AD CS


### 5. KUBERNETES CERTIFICATE MANAGEMENT

   For our later Kubernetes phase, an important option is:

   cert-manager

   It can automatically:
   - request certificates
   - renew certificates
   - store certificates as Kubernetes Secrets
   - work with Let's Encrypt
   - work with private/internal CAs



### SELF-SIGNED
- good for local lab
- no trusted external CA
- browsers will warn

### TRUSTED CA
- normal production choice
- certificate is signed by a trusted CA
- browsers trust it

### INTERNAL CA
- private/company environments
- clients must trust the organization's CA