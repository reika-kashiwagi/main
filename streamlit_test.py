import streamlit as st

st.title('タイトル行 (st.title)')
st.header('ヘッダー行 (st.header)')
st.subheader('サブヘッダー行 (st.subheader)')

st.button('ボタン (st.button)')
st.write('テキスト (st.write)')

selectbox = st.selectbox(
		'セレクトボックス (st.selectbox)',
		('選択肢1','選択肢2','選択肢3')）

checkbox1 = st.checkbox('選択肢1')
checkbox2 = st.checkbox('選択肢2')
checkbox3 = st.checkbox('選択肢3')

