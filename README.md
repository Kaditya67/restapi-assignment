## Bank API Service
This project is a Django-based REST API server that provides endpoints to fetch information about banks and their branches. It is designed as part of an assignment to demonstrate clean code practices, test cases, and optional deployment on services like Heroku.

#### Features
- Fetch a list of all banks with their details.
- Retrieve branch details for a specific IFSC code.
- Each bank includes a URL field that links to the bank's detail endpoint.
- Clean and maintainable code using Django REST Framework (DRF).
- Supports easy deployment to Heroku.


#### Problem Statement
The task was to create an API service using a Python web framework (Django in this case) with the following requirements:

- Provide REST API endpoints to:
- Fetch a list of banks.
- Fetch branch details for a specific branch using IFSC.

#### Solution
##### Data Modeling
Two models were created to represent the database structure:

##### Bank:

- id: Primary key.
- name: Unique name of the bank.

##### Branch:

- bank: Foreign key linking to the Bank model.
- ifsc: Unique identifier for each branch.
- branch_name: Name of the branch.
- address: Full address of the branch.
- city: City where the branch is located.
- district: District where the branch is located.
- state: State where the branch is located.

##### API Endpoints
###### Banks List: /api/banks/

- Method: GET
- Returns a list of all banks with their id, name, and url fields.

###### Bank Detail: /api/banks/<id>/

- Method: GET
- Returns details of a specific bank.

###### Branch Detail: /api/branches/<ifsc>/

- Method: GET
- Returns details of a specific branch based on its IFSC code.

#### Implementation Details
###### Serializers:

- Used ModelSerializer for both Bank and Branch. 

###### Views:

- Used ListAPIView for listing all banks.
- Used RetrieveAPIView for retrieving specific bank or branch details.

##### Time Taken
Approximate Time:
Development: 2-3 hours
Documentation and Deployment: 1-2 hours