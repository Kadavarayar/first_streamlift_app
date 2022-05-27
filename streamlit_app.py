import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favorites')


import pandas

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
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
