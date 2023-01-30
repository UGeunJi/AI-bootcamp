import streamlit as st

# 드라마 앱 
drama_select = ['내 이름은 김삼순', '눈이 부시게', '언젠가 이 사랑을 떠올리면 울어버릴 것 같아']
# 인덱스 번호를 활용해서 두 요소를 연결해서 사용하고 있어요 
drama_select_option = st.sidebar.selectbox('좋아하는 드라마를 선택하세요', drama_select, index=0)


# 본문
folder = '../data/'  # .. : 지금 내 폴더 기준으로 하나 위의 디렉토리

drama_image_files = ['samsun.jpg', 'noon.jpg', 'unjenga.png']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
html = """
<style>
h2 {
    color : blue;
}
<style>
"""

st.markdown(html, unsafe_allow_html=True)
st.header(drama_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
drama_select_index = drama_select.index(drama_select_option)

st.write(drama_select_index)
st.image(folder + drama_image_files[drama_select_index])
