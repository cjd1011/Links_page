import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Camilo Diaz C, 25 Years Old')

st.info('Professional in Business Administration, currently working in Business Intelligence and creating educational content. You can reach out to me at camilodiaz961011@gmail.com ')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/channel/UCAdEr61O-jMY0SyzApo91iA', 'Inteligencia de Negocios Para Todos', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/camilodiazc/', 'Follow me on LinkedIn', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/camilodiaz', 'Buy me a Coffee', icon_size)
st_button('cup', 'https://cjd1011.github.io/Camilo-Diaz-Portfolio/', 'Portfolio', icon_size)
