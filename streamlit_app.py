import streamlit

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

# import csv
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_first_list)
