import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 인덱스 번호를 활용해서 두 요소를 연결해서 사용하고 있어요 
book_select = ['신곡', '데일카네기 인간관계론', '미움받을 용기']
book_select_option = st.sidebar.selectbox('좋아하는 책을 선택하세요', book_select, index=2)

# 본문
folder = './data/'
st.header(':blue[2. BOOK]')
st.header(book_select_option)
book_image_files = ['book/신곡.jpg', 'book/데일카네기_인간관계론.jpg', 'book/미움받을용기.jpg']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
st.write('선택한 책:', book_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
book_select_index = book_select.index(book_select_option)

st.write(book_select_index)
st.image(folder + book_image_files[book_select_index])

html = """
<style>
h2 {
color : blue;
}
<style>
"""
st.markdown(html, unsafe_allow_html=True)