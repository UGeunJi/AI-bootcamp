import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
 
def get_stock_info(maket_type=None):
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    if maket_type == 'kospi':         
        marketType = "stockMkt"      
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt"    
    elif maket_type == None:         
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)     
    df = pd.read_html(url, header=0)[0]
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
    df = df[['회사명','종목코드']]
    return df

def get_ticker_symbol(company_name, maket_type):     
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values    
    code = code[0]
    if maket_type == 'kospi':   
        ticker_symbol = code +".KS"     
    elif maket_type == 'kosdaq':      
        ticker_symbol = code +".KQ" 
    return ticker_symbol
st.title(":red[주식 정보를 가져오는 웹 앱]") 
st.markdown(
    """     <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}     </style>
    """, unsafe_allow_html=True )

st.sidebar.header("회사 이름과 기간 입력")
stock_name = st.sidebar.text_input('회사 이름', value="NAVER") 
date_range = st.sidebar.date_input("시작일과 종료일",
                 [datetime.date(2019, 1, 1), datetime.date(2021, 12, 31)]) 
clicked = st.sidebar.button("주가 데이터 가져오기")

if(clicked == True):
    ticker_symbol = get_ticker_symbol(stock_name, "kospi")     
    ticker_data = yf.Ticker(ticker_symbol)
    start_p = date_range[0]               
    end_p = date_range[1] + datetime.timedelta(days=1) 
    df = ticker_data.history(start=start_p, end=end_p)
    df.index = df.index.date
    st.subheader(f":blue[[{stock_name}] 주가 데이터]")
    st.dataframe(df.head())  
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'   
    matplotlib.rcParams['axes.unicode_minus'] = False
    ax = df['Close'].plot(grid=True, figsize=(15, 5)) 
    ax.set_title("Stock Price Graph", fontsize=25)     
    ax.set_xlabel("Period", fontsize=15)
    ax.set_ylabel("Price", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)     
    fig = ax.get_figure()  
    st.pyplot(fig)
    st.line_chart(df, y='Close')
    st.bar_chart(df, y='Close')
    st.markdown("**주가 데이터 파일 다운로드**")     
    csv_data = df.to_csv()  
    excel_data = BytesIO()      
    df.to_excel(excel_data)     
    columns = st.columns(2) 
    with columns[0]:
        st.download_button("CSV 파일 다운로드", csv_data, file_name='stock_data.csv')   
    with columns[1]:
        st.download_button("엑셀 파일 다운로드", 
        excel_data, file_name='stock_data.xlsx')