
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values('from streamlit')")
my_cur.execute("insert into fruit_load_list values('jackfruit')")
my_cur.execute("insert into fruit_load_list values('papaya')")
my_cur.execute("insert into fruit_load_list values('kiwi')")
my_cur.execute("insert into fruit_load_list values('guava')")



