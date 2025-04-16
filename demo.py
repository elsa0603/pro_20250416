import numpy as np
import pandas as pd
import streamlit as st

# 文字輸出
st.title("Demo123")
st.header("123")
st.text("Text")
st.write("Write")
st.write("## Write")

a = np.array([10,20,30,40,50])
st.write(a)

b = pd.DataFrame({'name':["Joe","May","Joe"]})
st.write(b)
st.table(b)

# 核取方塊
st.write("核取方塊")
ck = st.checkbox("是否加糖?")
if ck:
    st.write("要加糖")
else:
    st.write("不加糖")

ck2 = st.checkbox("是否加冰?")
if ck2:
    st.write("要加冰")
else:
    st.write("不加冰")

# 選項按鈕
st.write("選項按鈕")
rb = st.radio("性別:",["F", "M", "no"])
st.info(rb)
rb2 = st.radio("性別:",["F", "M", "no"], key="rb2")
st.info(rb2)

# 下拉選單
st.write("下拉選單")
sb = st.selectbox("請選擇:",["奶茶","咖啡","不用"])
st.info(sb)

# 按鈕
st.write("按鈕")
def show():
    st.text("121311323231")
btn = st.button("按下")
if btn:
    show()

# 滑桿
st.write("滑桿")
num = st.slider("請設定K=?", 1, 11, step=1)
st.info(num)

# 側邊欄
st.sidebar.write("## 側邊欄")
sb3 = st.sidebar.selectbox("請選擇:",["奶茶","咖啡","不用"], key="sb3")
st.sidebar.info(sb3)

# 分欄
cols = st.columns(4)
with cols[0]:
    n1 = st.number_input("數字1", key="n1")
with cols[1]:
    n2 = st.number_input("數字2", key="n2")
with cols[2]:
    n3 = st.number_input("數字3", key="n3")
with cols[3]:
    n4 = st.number_input("數字4", key="n4")

st.info(n1+n2+n3+n4)

# 上傳檔案
st.write("上傳檔案(csv)")
file = st.file_uploader("請選擇CSV檔")
if file is not None:
    df = pd.read_csv(file)
    st.write(df.head(10))

