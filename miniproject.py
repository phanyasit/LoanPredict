#pip install streamlit pandas scikit-learn
import keras
import tensorflow as tf
from ctypes import alignment
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from keras import optimizers
from sklearn.preprocessing import LabelEncoder
from PIL import Image
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

img = Image.open('01blank.jpg')
img2 = Image.open('icon-bot.png')

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
    # แปลงภาพเป็นขนาด 28x28 pixels และเปลี่ยนเป็น grayscale
    if option == 'เอกสารที่ 1':
        #Load Model เอกสารที่ 1
        pickle_in = open('test_code.pkl', 'rb')
        classifier = pickle.load(pickle_in)
        image = Image.open(doc1)
        image = image.resize((248,351))
        image = np.array(image)
        x = np.expand_dims(image, axis=0) #เพิ่ม array จาก 2 มิติ เป็น 3 มิติ
        image = np.vstack([x])
        prediction = classifier.predict(image)
        print(prediction)
        if prediction[0] < 0.5:
                st.balloons()
                st.write("")
                st.success('ระบบประเมินเบื้องต้นว่าสามารถอนุมัติได้')
        else:
                st.error('ระบบประเมินเบื้องต้นว่าไม่สามารถอนุมัติได้')
    elif option == 'เอกสารที่ 2':
        #Load Model เอกสารที่ 2
        pickle_in = open('...', 'rb')
        classifier = pickle.load(pickle_in)
        image = Image.open(doc1)
        image = image.resize((248,351)) # resize ตาม model ที่ train
        image = np.array(image)
        x = np.expand_dims(image, axis=0) #เพิ่ม array จาก 2 มิติ เป็น 3 มิติ
        image = np.vstack([x])
        prediction = classifier.predict(image)
        print(prediction)
        if prediction[0] < 0.5:
                st.balloons()
                st.write("")
                st.success('ระบบประเมินเบื้องต้นว่าสามารถอนุมัติได้')
        else:
                st.error('ระบบประเมินเบื้องต้นว่าไม่สามารถอนุมัติได้')
    elif option == 'เอกสารที่ 3':
        #Load Model เอกสารที่ 3
        pickle_in = open('...', 'rb')
        classifier = pickle.load(pickle_in)
        image = Image.open(doc1)
        image = image.resize((248,351)) # resize ตาม model ที่ train
        image = np.array(image)
        x = np.expand_dims(image, axis=0) #เพิ่ม array จาก 2 มิติ เป็น 3 มิติ
        image = np.vstack([x])
        prediction = classifier.predict(image)
        print(prediction)
        if prediction[0] < 0.5:
                st.balloons()
                st.write("")
                st.success('ระบบประเมินเบื้องต้นว่าสามารถอนุมัติได้')
        else:
                st.error('ระบบประเมินเบื้องต้นว่าไม่สามารถอนุมัติได้')
    else :
          st.error('ระบบไม่รองรับรูปแบบเอกสาร')