import streamlit as st
import requests
import pandas as pd

generate_ad_url= 'http://127.0.0.1:8000/create_ad'

st.title("광고 문구 생성기")
product_name = st.text_input("제품 이름")
details = st.text_input("주요 내용")
options = st.multiselect("광고 문구의 느낌",options = ['기본','재미있게','차분하게','과장스럽게','참신하게','고급스럽게','센스있게','아름답게'])

if st.button("문구 생성") :
    try:
        response = requests.post(generate_ad_url,
            json = {
            "product_name":product_name,
            "details":details,
            "tone_and_manner":",".join(options)
            }
        )
        ad = response.json()['ad']
        st.success(ad)

        ad_list = response.json()['ad_list']
        df = pd.read_json('ad_list')
        st.dataframe(df)

    except:
        st.error("연결실패")