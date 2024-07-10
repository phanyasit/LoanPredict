#pip install streamlit pandas scikit-learn

import tensorflow as tf
from ctypes import alignment
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from PIL import Image
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

img = Image.open('01blank.jpg')
img2 = Image.open('icon-bot.png')

#Load Model
pickle_in = open('test_code.pkl', 'rb')
classifier = pickle.load(pickle_in)

# สร้าง sidebar
option = st.sidebar.selectbox(
    'เลือกข้อมูล',
     ('เอกสารที่ 1', 'เอกสารที่ 2', 'เอกสารที่ 3'))

# แสดงข้อมูลตามที่เลือกจาก sidebar
if option == 'เอกสารที่ 1':
    st.title('เอกสารที่ 1')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(img)
    # เพิ่มเนื้อหาของเอกสารที่ 2ได้ที่นี่
    #code upload
    doc1 = st.file_uploader("เลือกรูปภาพ", type=["png", "jpg", "jpeg"])

    if doc1 is not None:
        image = Image.open(doc1)
        st.image(image, caption='รูปภาพที่อัปโหลด')

    
elif option == 'เอกสารที่ 2':
    st.title('เอกสารที่ 2')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(img2)
    # เพิ่มเนื้อหาของเอกสารที่ 2ได้ที่นี่
    #code upload
    doc2 = st.file_uploader("เลือกรูปภาพ", type=["png", "jpg", "jpeg"])

    if doc2 is not None:
        image = Image.open(doc2)
        st.image(image, caption='รูปภาพที่อัปโหลด')

else:
    st.title('เอกสารที่ 3')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(img)
    # เพิ่มเนื้อหาของหน้าเอกสารที่ 3ได้ที่นี่
    #code upload
    doc3 = st.file_uploader("เลือกรูปภาพ", type=["png", "jpg", "jpeg"])

    if doc3 is not None:
        image = Image.open(doc3)
        st.image(image, caption='รูปภาพที่อัปโหลด')

# สร้างปุ่มสำหรับคำนวณ
if st.button("ทำนาย"):
    # ดำเนินการคำนวณหรือแสดงผลลัพธ์ตามที่ต้องการ
    #prediction = model.predict(np.array([img_normalized]))
    #pred = model.predict([image])[0]
    prediction = classifier.predict([doc1])
    #prediction = classifier.predict(np.array([doc1]))
    if classifier == 'doc1':
            st.balloons()
            st.write("")
            st.success('ระบบประเมินเบื้องต้นว่าสามารถอนุมัติได้')
    else:
            st.error('ระบบประเมินเบื้องต้นว่าไม่สามารถอนุมัติได้')