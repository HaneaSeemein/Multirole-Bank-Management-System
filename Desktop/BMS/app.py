import mysql.connector
import streamlit as st
import random
import datetime
# import database as db
from database import *
import pandas as pd
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="Bankdb"
)
c = mydb.cursor()
c.execute("use Bank;")
role = "Employee"
ID = 0
# placeholder=st.empty()
# with placeholder.container():
#         st.header("Login")
#         trole = st.radio("Role",('Customer', 'Employee', 'Admin'))
#         TID = st.number_input("ID",max_value=99999)
#         if st.button("Submit",key="login"):
#             ID = TID
#             role = trole
#             placeholder.empty()


if(role=="Customer"):
    customerprofile=getcustomer(ID)
    # CID = customerprofile[0]
    # cIFSC = customerprofile[3]
    customeraccount = getaccount(ID)
    try:
     branch = branchname(customerprofile[3])
    except:
     branch = "master"
    st.header("Hi "+customerprofile[1])
    profile, account, loan, history = st.tabs(["Profile", "Accounts", "Loan", "History"])
    with profile:
        # st.header("//customer data//")
        st.write("ID          : "+str(ID))
        st.write("Phone       : "+customerprofile[2])
        st.write("Address     : "+customerprofile[4])
        st.write("Email       : "+customerprofile[3])
        st.write("Credit score: "+str(customerprofile[5]))
    try:
     customeraccount = getaccount(ID)
     with account:
        st.write("Account ID: "+str(customeraccount[0]))
        st.write("IFSC code : "+str(customeraccount[3]))
        st.write("Balance   : "+str(customeraccount[1]))
        st.write("Type      : "+customeraccount[2])
        st.write("Branch    :"+branch)
    except:
     with account:
        st.write("No Account associated with your ID yet")
    try:
     customerloan = getloan(ID)
     helperemployee = getemployee(customerloan[5])
     with loan:
        st.write("Loan ID                : "+customerloan[0])
        st.write("Amount                 : "+str(customerloan[1]))
        st.write("Time                   : "+customerloan[2])
        st.write("Type                   : "+customerloan[3])
        st.write("Assisted employee name : "+helperemployee[1])
        st.write("Helpline               : "+helperemployee[4])
    except:
     with loan:
        st.write("No loans Yay!")
    try:
     customerhistory = gettransactions(ID)
    #  customeraccount = getaccount(ID)
     with history:
        for transaction in customerhistory:
            st.header(transaction[0])
            st.write("Amount : "+str(transaction[2]))
            st.write("Date   : "+str(transaction[1])) 
    except:
     with history:
        st.write("No transactions yet!")


elif(role == "Employee"):
    st.header("Employee")
    transaction, loan, account = st.tabs(["Transaction","Loan","Account"])
    with transaction:
     with st.form(key="transaction"):
        TID = random.randint(10000,99999)
        y=''
        x = str(datetime.datetime.now())
        for i in x:
            if (i!='-'): y = y+i
        tdate = y[0:8]
        toID= st.number_input("Customer's account ID",key="toID",value=10000,max_value=99999)
        # fromID= st.number_input("Customer's ID",key="fromID",value=10000,max_value=99999)
        tAmount= st.number_input("Amount",value=1000,step=200,min_value=200,key="tamount")
        transact = st.form_submit_button("Transact")
        if transact:
          print('ok')
          tvalues = (TID,int(tdate),tAmount,toID)
          insert('transaction',tvalues)

    with loan:
        with st.form(key="loan"):
            lid= st.number_input("Loan ID",max_value=99999)
            lamount=st.number_input("Amount",value=200000,step=20000)
            ltime=st.number_input("time(in years)",value=2,step=1,min_value=1,max_value=30)
            ltype=st.selectbox("Type",("Home","Personal","Education","Fund"))
            lcid = st.number_input("customer's ID",max_value=99999)
            leid = st.number_input("served employee's ID",max_value=99999)
            lifsc = st.number_input("branch's IFSC code",min_value=1000,max_value=9999)
            apply = st.form_submit_button("Apply")
    with account:
        with st.form(key="account"):
            aid= st.number_input("Account ID",max_value=99999)
            abalance=st.number_input("Amount",value=200000,step=20000)
            atype=st.selectbox("Type",("Savings","Current","Fixed deposit"))
            aifsc = st.number_input("branch's IFSC code",min_value=1000,max_value=9999)
            acid = st.number_input("customer's ID",max_value=99999)
            create = st.form_submit_button("Create")
            # values = (aid,abalance,atype,aifsc,acid)
            # insert('account',values)


elif (role=="Admin"):
    st.title("Administrator")
    hireemployee, fireemployee, deletecustomer = st.tabs(["Hire", "Fire", "Delete customer"])
    with deletecustomer:
        st.header("Delete customer")
        tdcid = st.number_input("enter the customer's ID",key="1",max_value=99999)
        if st.button("Delete",key="11"):
         DID=tdcid
         removecustomer(DID)
    with fireemployee:
        st.header("Fire employee")
        tdeid = st.number_input("enter the employee's ID",key="2",max_value=99999)
        if st.button("Fire", key="21"):
         fID=tdeid
         removeemployee(fID)
    with hireemployee:
        with st.form(key='hire'):
                hname = st.text_input("Name",key="333")
                heid = st.number_input("ID",key="31",max_value=99999)
                hrole=st.selectbox('Role', ['Branch Head','Manager','Officer', 'Advisor'], key="546")
                hpoints = st.number_input(" Points",key="37")
                hsalary = st.number_input("Salary",key="33",step=2000,value=10000)
                hphone = st.number_input("Phone",key="34",max_value=9999999999)
                hemail = st.text_input("Email",key="35")
                haddress = st.text_input("Address",key="36")
                hifsc = st.number_input("IFSC code",key="38",min_value=1000,max_value=9999)
                submithere = st.form_submit_button('Submit')
                if submithere:
                    st.write("//hey//")