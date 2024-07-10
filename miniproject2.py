import streamlit as st
import pickle
import numpy as np
from PIL import Image

# โหลดโมเดลที่สร้างจากการ train แล้วจากไฟล์ pickle
model = pickle.load(open("test_code.pkl", "rb"))

# สร้างฟังก์ชันเพื่อทำนายภาพ
def predict(image):
    # แปลงภาพเป็นขนาด 28x28 pixels และเปลี่ยนเป็น grayscale
    image = image.resize((248,351))
    image = np.array(image)
    # ทำนายหมายเลขด้วยโมเดล
    x = np.expand_dims(image, axis=0) #เพิ่ม array จาก 2 มิติ เป็น 3 มิติ
    image = np.vstack([x])
    pred = model.predict(image)
    return pred[0]

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
        if label[0] > 0.5:
            st.write(f"Incomplete")
        else:
            st.write(f"Complete")
    else:
        st.write("Please upload an image to predict.")
