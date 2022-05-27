import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favarites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard boiled Free-range Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put multiselection option for customer to choose the fruits they want to include
# streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index))
# streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_selected = streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

# streamlit.dataframe(my_fruit_list)
# streamlit.dataframe(fruits_to_show)
