# Data Migration and Integration

#### Import Sets
A mechanism used to import external data into temporary import tables before processing.

Examples:
- CSV files
- Excel files
- External databases

#### Transform Maps
Rules that define how imported data is converted into ServiceNow records.

#### Data Sources
Define where imported data comes from.

Examples:
- File uploads
- Database connections
- External systems

#### Business Rules
Server-side scripts that execute when records are created, updated, deleted, or displayed.

Common timings:
- Before
- After
- Async

#### UI Policies
Client-side rules that control form behavior without scripting.

Examples:
- Make a field mandatory
- Hide a field
- Make a field read-only

#### Client Scripts
JavaScript code executed in the user's browser.

Types:
- OnLoad
- OnChange
- OnSubmit

#### Update Sets
Containers used to move configuration changes between ServiceNow instances.

Example:
Development → Test → Production

#### Integration
Connecting ServiceNow with external systems to exchange data.

Common methods:
- REST API
- SOAP API
- IntegrationHub
