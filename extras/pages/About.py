import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    # password="kill7",
    # port=8080
)
c = mydb.cursor()

st.title("Hey")
st.header("This is my project for DBMS")
st.write("I am Haneyah and the python libraries i used are myql, streamlit etc")