import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 사이드바 만드는 방법 1: st.sidebar.요소명 
# Using object notation
# 사이드바에 셀렉트박스(혹은 라디오버튼 등등 뭐라도 좋습니다)로 
# 각 드라마 혹은 애니메이션의 제목 세개를 
# 선택할 수 있도록 해주세요
book_select = ['신곡', '데일카네기 인간관계론', '미움받을 용기']

# 인덱스 번호를 활용해서 두 요소를 연결해서 사용하고 있어요 
book_select_option = st.sidebar.selectbox('좋아하는 책을 선택하세요', book_select, index=2)

# 사이드바 만드는 방법 2: with st.sidebar:
#                           변수명 = st.요소명 

# 본문
folder = './00_start/'
image_files = ['신곡.jpg', '데일카네기_인간관계론.jpg', '미움받을용기.jpg']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
st.write('선택한 책:', book_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
book_select_index = book_select.index(book_select_option)

st.write(book_select_index)
st.image(folder + image_files[book_select_index])