import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 사이드바 만드는 방법 1: st.sidebar.요소명 
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# 사이드바 만드는 방법 2: with st.sidebar:
#                           변수명 = st.요소명 
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.sidebar.write('사이드바입니다')

st.sidebar.image('./jjanggu.jpeg')

image_path = os.path.dirname(os.path.abspath(__file__)) + "/jjanggu.jpeg"
image = Image.open(image_path) # 경로와 확장자 주의!

# 메소드를 실행하는 순서대로 화면에 그려집니다!
st.image(image)

st.write(
    """
    # 필수항목만 넣은 페이지
    ## 관련 문서
    * [Streamlit 문서 보러가기](https://docs.streamlit.io/library/api-reference)
    * [Markdown 사용법 보러가기](https://goddaehee.tistory.com/307)
    """
)

# 이미지를 링크로 불러오려면...
# 무료 이미지 호스팅 : https://imgur.com/
st.image("https://imgur.com/a/vW5V5OV")

st.write(
    """
    ## 사용법
    * 제공한 다른 예시들을 편집하고 각자 github에 올려보면서 익혀보세요
    * 추가적으로 넣고 싶은 라이브러리는 `requirements.txt`에 넣어줘야 작동합니다
    * 실행 결과 : <https://yeonjikim0316-streamlit-example-00-startapp-zq0xtv.streamlit.app/>
    """
)


# st.columns()를 통해 다단을 구현합니다. 
# [col1, col2, col3] = st.columns(3) 
# 각 컬럼의 비율을 다르게 하고 싶다면
[col1, col2, col3] = st.columns([1,  0.5, 2]) 

with col1:
    st.header('1. IMAGE')
    st.image("https://i.imgur.com/10J2i4y.jpg")
with col2:
    st.header('2. AUDIO')
    # 저작권 무료 음악: https://studio.youtube.com/channel/UCjMXxVpbAqejiHiMh9nlPIg/music
    st.audio('.\Emotional Mess - Amy Lynn & the Honey Men.mp3')

with col3:
    st.header('3. HTML')

    # html 코드 첨부 참조: https://yeomss.tistory.com/300
    html = """
    <div style='
        background-color:red;
        color:white;
    '>
        HTML 코드로 작성했습니다 근데 아래의 style태그 때문에  가장 위의 # 필수항목만 넣은 페이지 까지 빨갛게 변한 것 확인되시나요
        그래서 Streamlit은 기본적으로는 자체 메소드들로만 화면을 구성할 것을 권장합니다.
    </div>

    <style>
    h1 {
        color : red;
    }
    <style>
    """

    st.markdown(html, unsafe_allow_html=True)
# 00_start 폴더 안의 app.py에 이어서 이미지 1개, 오디오링크 1개, html 코드를 st.write(명령어 안에 넣어서 화면에 출력을 해 보세요 )