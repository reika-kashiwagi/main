import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
	st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

st.header('1.Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jacl&surname=Beanstalk`
''')

st.header('2.Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())

st.header('3.Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hellow **{firstname} {surname}**,how are you?')