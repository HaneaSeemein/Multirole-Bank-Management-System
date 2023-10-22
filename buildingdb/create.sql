CREATE TABLE branch
(
  name VARCHAR(255) NOT NULL,
  IFSC INT(4) NOT NULL,
  location VARCHAR(255) NOT NULL,
  PRIMARY KEY (IFSC)
);

CREATE TABLE employee
(
  employee_id INT(7) NOT NULL,
  name VARCHAR(255) NOT NULL,
  role VARCHAR(10) NOT NULL,
  salary INT NOT NULL,
  phone VARCHAR(10) NOT NULL,
  email VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  credits INT(1) NOT NULL,
  IFSC INT(4) NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (IFSC) REFERENCES branch(IFSC)
);

CREATE TABLE customer
(
  customer_id INT(7) NOT NULL,
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(10) NOT NULL,
  email VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  credit_score INT(1) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE loan
(
  loan_id INT(10) NOT NULL,
  amount INT NOT NULL,
  time INT NOT NULL,
  type VARCHAR(10) NOT NULL,
  customer_id INT(7) NOT NULL,
  employee_id INT(7) NOT NULL,
  IFSC INT(4) NOT NULL,
  PRIMARY KEY (loan_id),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
  FOREIGN KEY (IFSC) REFERENCES branch(IFSC)
);

CREATE TABLE account
(
  account_id INT(10) NOT NULL,
  balance INT NOT NULL,
  type VARCHAR(10) NOT NULL,
  IFSC INT(4) NOT NULL,
  customer_id INT(7) NOT NULL,
  PRIMARY KEY (account_id),
  FOREIGN KEY (IFSC) REFERENCES branch(IFSC),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE Transaction
(
  TID INT(10) NOT NULL,
  date INT(8) NOT NULL,
  amount INT NOT NULL,
  account_id INT(10) NOT NULL,
  customer_id INT(7) NOT NULL,
  PRIMARY KEY (TID),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (account_id) REFERENCES account(account_id)
);

DELIMITER $$
CREATE TRIGGER update_bal
  AFTER INSERT
  ON Transaction for each row
  BEGIN
  update account set balance=balance+new.amount where account.account_id=new.account_id;
END $$

DELIMITER $$
CREATE FUNCTION totalamount(amount INT, type VARCHAR(10))
RETURNS INT
BEGIN   
    DECLARE interestpercent INT;
    IF  type = 'Home' THEN
       SET interestpercent = 5;
    ELSEIF type = 'Personal' THEN
       SET interestpercent = 10;
    ELSEIF  type = 'Education' THEN
       SET interestpercent = 2;
    ELSEIF  type = 'Fund' THEN
       SET interestpercent = 0;
    END IF;
    RETURN amount * interestpercent + amount;
END $$
DELIMITER;