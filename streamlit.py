import streamlit
import requests
streamlit.title('My healthy new diner!')
streamlit.header('Fruity Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.jason())
