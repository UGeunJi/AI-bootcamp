import streamlit as st

manhwa_select = ['짱구는 못말려', '몬스터', '중쇄를 찍자']
manhwa_select_option = st.sidebar.selectbox('좋아하는 만화를 선택하세요', manhwa_select, index=1)

folder = '../data/'

# 사이드바에 아까 선택하지 않은 것(애니메이션, 영화, 책 등등) 이미지파일3개 가져오셔서
manhwa_image_files = ['manhwa/jjanggu.png',  'manhwa/monster.png', 'manhwa/jung.jpeg']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
st.header(manhwa_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
manhwa_select_index = manhwa_select.index(manhwa_select_option)

st.write(manhwa_select_index)
st.image(folder + manhwa_image_files[manhwa_select_index])
