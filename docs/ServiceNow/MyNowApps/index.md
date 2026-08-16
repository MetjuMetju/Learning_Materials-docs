# APPLICATIONS, TABLES AND USERS

<br>

##### BUILD ORDER

 1. Create Onboarding Management application.
 2. Create Leave Management application.
 3. Create Employees table.
 4. Create Onboarding Requests table.
 5. Create Leave Requests table.
 6. Create Approval Rules table.
 7. Define users and roles.
 8. Create Employee Services catalog.
 9. Create Request Onboarding Record Producer.
10. Create Request Leave Record Producer.
11. Define questions and map them to table fields.
12. Define catalog visibility.
13. Define Pending Approval state.
14. Define Manager approval and rejection.
15. Test with user impersonation.

<br>

# APPLICATIONS

### 1. Onboarding Management
- Purpose: create and onboard new employees.

### 2. Leave Management
- Purpose: manage leave requests for existing employees.

<br>

# CUSTOM TABLES

### 1. Employees
- Stores all employees.

### 2. Onboarding Requests
- Stores onboarding requests.

### 3. Leave Requests
- Stores leave requests.

### 4. Approval Rules
- Defines who can Create, Approve and Reject.

<br>

# USER TYPES

- Employee - Submits requests.
- Manager - Approves or rejects requests.
- HR Administrator - Manages HR data.
- System Administrator - Configures the system.

<br>

### EMPLOYEES TABLE

### TABLE: Employees

- PURPOSE
    - Stores all employees who can use Leave Management and other services.


### FIELDS:

    Number
    Type: Auto Number
    Required: Yes

    Name
    Type: String
    Required: Yes

    Email
    Type: Email
    Required: Yes

    User
    Type: Reference -> User
    Required: Yes

    Department
    Type: Reference -> Department
    Required: Yes

    Manager
    Type: Reference -> User
    Required: Yes

    Start date
    Type: Date
    Required: Yes

    Active
    Type: True/False
    Default: true
    Required: Yes

<br>

### ONBOARDING REQUESTS TABLE

### TABLE: Onboarding Requests

- PURPOSE
    - Stores requests for creating and onboarding new employees.


### FIELDS

    Number
    Type: Auto Number

    Employee name
    Type: String
    Required: Yes

    Email
    Type: Email
    Required: Yes

    Department
    Type: Reference -> Department
    Required: Yes

    Manager
    Type: Reference -> User
    Required: Yes

    Start date
    Type: Date
    Required: Yes

    Requested by
    Type: Reference -> User
    Required: Yes

    Approver
    Type: Reference -> User
    Required: No

    State
    Type: Choice

    Values:
    Draft
    Pending Approval
    Approved
    Rejected

<br>

### LEAVE REQUESTS TABLE

### TABLE: Leave Requests

- PURPOSE:
    - Stores leave requests for employees who already exist in Employees.

### FIELDS

    Number
    Type: Auto Number

    Employee
    Type: Reference -> Employees
    Required: Yes

    Start date
    Type: Date
    Required: Yes

    End date
    Type: Date
    Required: Yes

    Reason
    Type: String
    Required: No

    Requested by
    Type: Reference -> User
    Required: Yes

    Approver
    Type: Reference -> User
    Required: No

    State
    Type: Choice

    Values:
    Draft
    Pending Approval
    Approved
    Rejected

<br>

### APPROVAL RULES TABLE

### TABLE: Approval Rules

- PURPOSE
    - Stores configurable authorization rules for both applications.


### FIELDS

    Application
    Type: Choice

    Values:
    Onboarding
    Leave

    Action
    Type: Choice

    Values:
    Create
    Approve
    Reject

    Role
    Type: Choice

    Values:
    Employee
    Manager
    HR Administrator
    System Administrator

    Allowed
    Type: True/False
    Default: true

    Active
    Type: True/False
    Default: true


    EXAMPLE RULES

    Onboarding / Create / Employee / Allowed
    Onboarding / Approve / Manager / Allowed
    Onboarding / Reject / Manager / Allowed

    Leave / Create / Employee / Allowed
    Leave / Approve / Manager / Allowed
    Leave / Reject / Manager / Allowed

<br>

### EMPLOYEE SERVICES CATALOG

### CATALOG: Employee Services

- PURPOSE
    - Provides one place where employees find available services.


### CATALOG ITEM: Request Onboarding

- Application
    - Onboarding Management

- Creates
    - Onboarding Request

### CATALOG ITEM: Request Leave

- Application
    - Leave Management

- Creates
    -Leave Request


##### Catalog
    - Place where services are offered.

##### Catalog Item
    - Service available to the user.

##### Record Producer
    - Form that creates a record.

<br>

### RECORD PRODUCERS

### RECORD PRODUCER: Request Onboarding

- Target table:
    - Onboarding Requests


### QUESTIONS

    Employee name
    Type: String

    Email
    Type: Email

    Department
    Type: Reference -> Department

    Manager
    Type: Reference -> User

    Start date
    Type: Date


### RECORD PRODUCER: Request Leave
- Target table:
    - Leave Requests


### QUESTIONS

    Employee
    Type: Reference -> Employees

    Start date
    Type: Date

    End date
    Type: Date

    Reason
    Type: String



- Questions belong to the Record Producer.
- Answers are mapped into fields of the target table.

<br>

### CATALOG VISIBILITY

### CATALOG: Employee Services


### REQUEST ONBOARDING

- Visible to: Employee
- Purpose: Start onboarding for a new employee.


### REQUEST LEAVE

- Visible to: Employee
- Condition: User must have an active Employee record.


- MANAGER
    - Does not need to submit requests in order to approve them.
    - Manager sees requests assigned for approval.


- ADMINISTRATOR
    - Can configure the catalog, Record Producers and rules.

- Catalog visibility controls who can see and use a service.
- Approval Rules control who can approve or reject a request.

<br>

### APPROVAL PROCESS

### ONBOARDING

- Employee submits Request Onboarding.
- Record Producer creates an Onboarding Request.
    - State becomes: Pending Approval

- Assigned Manager reviews the request.
    - Manager chooses:
    - Approve - Final state: Approved
    - Reject: Final state: Rejected


### LEAVE

- Existing Employee submits Request Leave.
- Record Producer creates a Leave Request.
    - State becomes: Pending Approval.

- Employee's Manager reviews the request.
- Manager chooses:
    - Approve - Final state: Approved
    - Reject - Final state: Rejected

### APPROVER
- Manager is the normal approver.
- Approval Rules determines whether the Manager can Approve or Reject.

<br>

### TESTING

### TEST 1: ONBOARDING

1. Impersonate Employee.
2. Open Employee Services.
3. Select Request Onboarding.
4. Fill in the questions.
5. Submit.
6. Verify State = Pending Approval.


### TEST 2: MANAGER APPROVAL

1. Impersonate Manager.
2. Open Approvals.
3. Find the onboarding request.
4. Select Approve.
5. Verify State = Approved.
6. Verify Employee record exists.


### TEST 3: MANAGER REJECTION

1. Create another onboarding request.
2. Impersonate Manager.
3. Open Approvals.
4. Select Reject.
5. Verify State = Rejected.


### TEST 4: LEAVE

1. Impersonate existing Employee.
2. Open Employee Services.
3. Select Request Leave.
4. Enter Start date.
5. Enter End date.
6. Submit.
7. Verify State = Pending Approval.


### TEST 5: LEAVE APPROVAL

1. Impersonate Employee's Manager.
2. Open Approvals.
3. Approve or Reject.
4. Verify the final state.


### TEST 6: SECURITY

1. Impersonate Employee.
2. Verify Employee cannot approve another user's request.
3. Impersonate Manager.
4. Verify Manager can Approve and Reject according to Approval Rules.
