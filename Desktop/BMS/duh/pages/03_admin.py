import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root"
)
c = mydb.cursor()
Role = "User"
ID = None
placeholder=st.empty()
def Login():
    global Role,ID
    st.header("Login")
    TID = st.text_input("ID")
    if st.button("Submit"):
        ID = TID
        main()
def main():
 if(ID==None):
    Login()
 else:
    st.write(ID)


main()
