import streamlit
import requests
streamlit.title('My healthy new diner!')
streamlit.header('Fruity Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
