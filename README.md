# Bank Management System with Streamlit UI

This is a Database Management System (DBMS) project for managing a bank. It includes functionalities for managing accounts, branches, employees, customers, and loans, along with a Streamlit Python user interface.

## Features

### Account
- Unique account_id for each account.
- Tracks balance and transaction history.

### Branch
- Contains employees, accounts, and an IFSC code.

### Employee
- Performs various operations to assist customers.
- Helps customers avail loans.

### Customer
- Profile with name, personal information, and credit score.
- May or may not have an account and loan.

### Loan
- Unique identifier loan_id.
- Includes time period, amount, and loan type (e.g., personal, home, education).

## User Roles and Functionality

### Customer
- Log in with their ID.
- View personal details.
- Access their own loan details.
- Access the assisted employee's contact number (helpline).

### Employee
- Log in with their ID.
- Make credit/debit transactions for customer accounts.
- Apply for a loan on behalf of a customer.
- Register a new account or a customer.
- View a list of customers they helped avail loans.

### Admin
- Hire an employee.
- Fire an employee.
- Delete a customer.
- Delete an account.
- Perform custom administrative commands.

## ER Diagram

![ER Diagram](pages/ERD.jpg)

The ER diagram illustrates the relationships between different entities in the database.

## Relational Diagram

![Relational Diagram](pages/RD.jpg)

The relational diagram displays how the entities are organized into tables within the database, showcasing their attributes and relationships.

