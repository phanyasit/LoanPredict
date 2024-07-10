import streamlit as st
import pickle
import numpy as np
from PIL import Image

# โหลดโมเดลที่สร้างจากการ train แล้วจากไฟล์ pickle
model = pickle.load(open('test_code.pkl', 'rb'))

# สร้างฟังก์ชันเพื่อทำนายภาพ
def predict(image):
    # แปลงภาพเป็นขนาด 28x28 pixels และเปลี่ยนเป็น grayscale
    image = image.convert('L')
    image = image.resize((28,28))
    image = np.array(image)
    
    # แปลงภาพให้มีขนาดเดียวกับภาพในชุดข้อมูล train
    image = image.reshape(1,28,28,1)
    image = image/255.0
    
    # ทำนายหมายเลขด้วยโมเดล
    pred = model.predict([image])[0]
    
    return np.argmax(pred)

# ตั้งค่าหน้าต่าง web app
st.set_page_config(page_title="MNIST Digit Recognizer", page_icon=":pencil2:", layout="wide")

# เริ่มต้นเขียนเว็บแอปด้วยการสร้าง sidebar
st.sidebar.title("MNIST Digit Recognizer")

# สร้างปุ่ม upload รูปภาพ
upload_image = st.sidebar.file_uploader("Upload an image", type=["jpg","jpeg","png"])

# สร้างปุ่ม predict
if st.sidebar.button('Predict'):
    if upload_image is not None:
        # แสดงภาพที่อัปโหลด
        image = Image.open(upload_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # ทำนายหมายเลขและแสดงผลลัพธ์
        st.write("")
        st.write("Classifying...")
        label = predict(image)
        st.write(f"Predicted Label: {label}")
    else:
        st.write("Please upload an image to predict.")
