import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favarites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard boiled Free-range Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put multiselection option for customer to choose the fruits they want to include
# streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index))
# streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error ("Please select a fruit to get a information.")
else: 
# import requests
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
except URLerror as e:
  streamlit error():

# dont run anything past here
streamlit.stop()

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("My Fruit Load List Contains: ")
streamlit.dataframe(my_data_row)

add_new_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write ('Thanks for adding ',add_new_fruit)

my_cur.execute("insert into fruit_load_list values ('from Streamlit')")

