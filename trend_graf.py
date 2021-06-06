import pandas as pd
import datetime
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st

st.title('  グラフ作成アプリ')
def read_data(file):
    df = pd.read_csv(file,encoding='cp932')
    df = df[df['店舗']!='合計']
    df['期間'] = pd.to_datetime(df['期間'])
    
    return df

def creat_graf(hinshu):
    fig = plt.figure(figsize=(7,3))
    plt.xlabel('期間')
    plt.ylabel('売上金額')
    graf = plt.plot(df[df['品種名称']==hinshu]['期間'],df[df['品種名称']==hinshu]['売上金額'])
    
    return graf


file = st.file_uploader('ファイル選択(csv)',type='csv')
if file is not None:
    df = read_data(file)

    select = df['品種名称'].unique()
    select = select.tolist()
    select  = st.multiselect('品種選択(上限：６）',select)

    fig = plt.figure(figsize=(20,12))
    plt.subplots_adjust(wspace=0.2,hspace=0.5)
    for i,kind in enumerate(select):
        plt.subplot(3,2,i+1)
        plt.title(kind)
        plt.plot(df[df['品種名称']==kind]['期間'],df[df['品種名称']==kind]['売上金額'])

    st.pyplot(fig)