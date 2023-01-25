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

folder = './data/'
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