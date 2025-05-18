import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
	'What are your favolite colors',
	['Green','Yellow','Red','Blue','White'],
	['Yellow','Red'])

st.write('You selected:',options)