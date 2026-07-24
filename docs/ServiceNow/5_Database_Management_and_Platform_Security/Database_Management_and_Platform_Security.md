# Database Management and Platform Security

#### Data Schema
The structure that defines how information is stored and related in ServiceNow.

Includes:
- Tables
- Fields
- Relationships
- Records

#### Table
A collection of records with the same structure.

Example:
The Incident table stores incident records.

#### Record
A single entry stored inside a table.

Example:
One incident is one record.

#### Field
A column in a table that stores a specific piece of information.

Examples:
- Name
- Status
- Assigned user

#### Table Extension
A child table that inherits fields and functionality from a parent table.

Example:
Task table → Incident table

#### Dictionary
Defines the properties and behavior of fields in ServiceNow tables.

Examples:
- Field type
- Length
- Default value
- Mandatory setting

#### Access Control List (ACL)
A security rule that controls who can access records and fields.

Controls:
- Create
- Read
- Write
- Delete

#### CMDB
Configuration Management Database stores Configuration Items (CIs) and their relationships.

Examples:
- Servers
- Applications
- Networks

#### CSDM
Common Service Data Model provides a standardized way to organize ServiceNow data.

#### Security
ServiceNow security protects:
- Data
- Applications
- Users
- Access permissions
