import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 사이드바 만드는 방법 1: st.sidebar.요소명 
# Using object notation
# 사이드바에 셀렉트박스(혹은 라디오버튼 등등 뭐라도 좋습니다)로 
# 각 드라마 혹은 애니메이션의 제목 세개를 
# 선택할 수 있도록 해주세요
AI_select = ['AI1', 'AI2', 'AI3']
AI_select_option = st.sidebar.selectbox('좋아하는 로봇 선택하세요', AI_select, index=2)

# 인덱스 번호를 활용해서 두 요소를 연결해서 사용하고 있어요 
book_select = ['신곡', '데일카네기 인간관계론', '미움받을 용기']
book_select_option = st.sidebar.selectbox('좋아하는 책을 선택하세요', book_select, index=2)

# 본문
folder = './data/'

[col1, col2] = st.columns([1, 1]) 

# 사이드바 만드는 방법 2: with st.sidebar:
#                           변수명 = st.요소명 
with col1:
    st.header(':blue[1. AI]')
    st.header(AI_select_option)
    image_files = ['AI/0214_AI-이미지-분석_02-720x4801.jpg', 'AI/143532_148677_45.jpg', 'AI/2020112521134800164607.jpg']
    st.write('선택한 AI:', AI_select_option)

    AI_select_index = AI_select.index(AI_select_option)

    st.write(AI_select_index)
    st.image(folder + image_files[AI_select_index])
    
    html = """
    <style>
    h2 {
        color : blue;
    }
    <style>
    """
    st.markdown(html, unsafe_allow_html=True)



with col2:
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
    

# st.columns()를 통해 다단을 구현합니다. 
# [col1, col2, col3] = st.columns(3) 
# 각 컬럼의 비율을 다르게 하고 싶다면

import streamlit as st
import cv2
import numpy as np
img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))
    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)

    # 보통 사이드바 / 메뉴는 주제별로 서비스를 분류할 때 쓰입니다
    # 1) AI 목록
    # 2) 책 좋아하는 목록
    # 3) 사진찍기

# 1. 하나의 파일에 3개를 다 넣고 클릭할 때마다 해당 div만 보이게 만들
# 2. 각 기능별로 별도 파일 혹은 폴더로 만들어 놓고 클릭할 때마다 해당 파일에 들어가도록 만들기
# 보통은 2번의 구조를 많이 사용함 ->1_AI_app.py, 2_book_app.py, 3_picture_app.py 3개로 파일 분리하기
# streamlit run 1_AI_app.py
# streamlit run 2_book_app.py
# streamlit run 3_picture_app.py