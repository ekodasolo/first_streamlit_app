import streamlit
import pandas as pd

# import csv
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Title
streamlit.title('My Parents new healthy diner')

# Body
streamlit.header('Breakfast Favorites')

# Menu
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Pocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruites:", list(my_fruit_list.index))

# Data Table
streamlit.dataframe(my_fruit_list)
