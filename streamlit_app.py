import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favarites')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put multiselection option for customer to choose the fruits they want to include
# streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index))

streamlit.multiselect("Please select your fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
