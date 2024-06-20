import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

def ex_rate():
    def get_exchange_data(code="USD", max_page=10):
        
        # url에 들어갈 변수 2개
        currency_code = code
        last_page_num = max_page

        # 데이터프레임 준비
        df = pd.DataFrame()

        # 데이터 가져오기
        for page_no in range(1, last_page_num+1):
            url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{currency_code}KRW&page={page_no}"
            dfs = pd.read_html(url, header=1, encoding="cp949")
            
            if (dfs[0].empty):
                if page_no == 1:
                    print(f"Wrong currency code : {currency_code}")
                    break;
                else:
                    print("The end of the data")
                    break;
            
            # print(dfs[0])
            df = pd.concat([df, dfs[0]], ignore_index=True)
            
        return df


    # temp = get_exchange_data("EUR", 10)
    # print(temp)

    # 통화 dictionary
    currency_name_dict = {"미국 달러": "USD", "유럽연합 유로": "EUR", "일본 옌": "JPY", "중국 위안": "CNY", "영국 파운드": "GBP", "캐나다 달러": "CAD", "스위스 프랑": "CHF"}

    # 스트림릿에 올리기
    # currency_selected = st.sidebar.selectbox("통화 선택", currency_name_dict.keys())
    # clicked = st.sidebar.button("환율 데이터 가져오기")
    currency_selected = st.selectbox("통화 선택", currency_name_dict.keys())
    clicked = st.button("환율 데이터 가져오기")

    # 버튼 클릭되면
    if clicked:
        currency_code = currency_name_dict[currency_selected]
        df = get_exchange_data(currency_code)
        
        # 헤더
        st.header(f"Exchange Rate For {currency_code}")
        
        rate = df.drop("전일대비", axis=1)
        
        # 날짜열의 데이터 변경 후 인덱스 처리
        rate.날짜 = pd.to_datetime(rate.날짜).dt.date
        rate2 = rate.set_index("날짜")

        # 환율 데이터 표시
        st.dataframe(rate2)
        
        # 차트 (선 그래프) 그리기
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'
        ax = rate2.매매기준율.plot(figsize=(20, 10))
        ax.set_xlabel("기간", fontsize=20)
        ax.set_ylabel(f"원화/{currency_code}", fontsize=20)
        ax.set_title("환율(매매기준율) 그래프", fontsize=25)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        fig = ax.get_figure()
        st.pyplot(fig)
        
        # 파일 다운로드
        st.text("** 환율 데이터 파일 다운로드 **", )
        
        # dataframe 데이터를 csv 데이터로 변환
        csv_data = rate.to_csv()
        
        # dataframe 데이터를 excel 데이터로 변환
            # 바이너리 파일로 메모리에 넣은 후 엑셀로 convert!
        excel_data = BytesIO()       # 메모리 버퍼(임시장소)에 바이너리 객체 생성
        rate.to_excel(excel_data)    # 엑셀 형식으로 버퍼에 쓰기
        
        col = st.columns(2)
        with col[0]:
            st.download_button("csv file download", csv_data, file_name=f"exchange_rate_data_{currency_code}.csv")
            
        with col[1]:
            st.download_button("excel file download", excel_data, file_name=f"exchange_rate_data_{currency_code}.xlsx")