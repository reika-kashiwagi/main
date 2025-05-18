import streamlit as st
st.header('st.selectbox')

option = st.selectbox(
	'What is your favorite color?',
	('Blue','Red','Green','White'))

st.write('Your favolite color is ',option)