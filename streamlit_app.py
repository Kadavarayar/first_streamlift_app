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

# create repeatable code block (called Function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error ("Please select a fruit to get a information.")
  else: 
# import requests
       back_from_funtion = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_funtion)
except URLerror as e:
  streamlit.error()



# import snowflake.connector

streamlit.header('Fruity Load List Contains: ')
# snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")
         return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button("Get fruit load list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


# Allow end user to add fruit name to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return "Thanks for adding " + new_fruit

add_new_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a new fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_funtion = insert_row_snowflake(add_new_fruit)
    streamlit.text(back_from_funtion)

# dont run anything past here
streamlit.stop()

my_cur.execute("insert into fruit_load_list values ('from Streamlit')")

