import streamlit as st
import pandas as pd

# chart 1
data1 = [ -2,   5,  -3,  -3,   9,  -4,  -7,  -9,   2,   3]
data2 = [  3,   4,  -4,  -2,  -3,  -2,   0,   7,  -6,   6]
data3 = [-10,   2,   8,   6,  -7,  -1,  -4,  -1,   4,   5]
dict_data = {"data1":data1, "data2":data2, "data3":data3}

# 데이터프레임으로 만들고 화면에 출력


df = pd.DataFrame(dict_data)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)