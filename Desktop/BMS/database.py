import streamlit as st
import pandas as pd
import mysql.connector
# from create import *
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="Bank"
)
c = mydb.cursor()

def getcustomer(ID):
    c.execute('SELECT * FROM customer WHERE customer_id=' + str(ID))
    data=c.fetchone()
    return data
def getaccount(ID):
    c.execute('SELECT * FROM account WHERE customer_id=' + str(ID))
    data=c.fetchone()
    # print(data)
    return data
def getloan(ID):
    c.execute('SELECT * FROM loan WHERE customer_id=' + str(ID))
    data=c.fetchone()
    return data
def getemployee(ID):
    c.execute('SELECT * FROM employee WHERE employee_id=' + str(ID))
    data=c.fetchone()
    return data
def gettransactions(ID):
    c.execute('SELECT * FROM transaction WHERE account_id=' + str(ID))
    data=c.fetchall()
    return data
def update(ID,value):
    # print("UPDATE")
    c.execute('UPDATE account SET balance='+str(value)+' WHERE account_id='+str(ID))
def branchname(ID):
    c.execute('SELECT name FROM branch WHERE IFSC=' + str(ID))
    data=c.fetchone()
    return data

# def transaction(values):
#     c.execute('INSERT INTO transaction values '+values)
def insert(table, values):
 try:
    c.execute('INSERT INTO '+table+' VALUES '+str(values))
    # q = 'INSERT INTO {} VALUES {}'.format(table,values)
    # print(q)
    # c.execute(q)
    mydb.commit()
    st.success("value added successfully")
 except Exception as e:
    st.write(e)

def removeemployee(i):
    q = 'DELETE FROM employee WHERE employee_id = '+str(i)
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')
def removecustomer(i):
    q = 'DELETE FROM customer WHERE customer_id ='+str(i)
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')
def removeaccount(i):
    q = 'DELETE FROM account WHERE account_id ='+str(i)
    c.execute(q)
    mydb.commit()



def runquery(a):
    c.execute(a)