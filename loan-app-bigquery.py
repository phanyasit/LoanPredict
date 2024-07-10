#pip install streamlit pandas scikit-learn
import json

from ctypes import alignment
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import pickle
# from sklearn.preprocessing import LabelEncoder
from PIL import Image

from google.cloud import bigquery
from google.oauth2 import service_account

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

image = Image.open('logo-kmitl.png')

# st.set_option('browser.gatherUsageStats', False)

#Load Model
# pickle_in = open('RandomForest.pkl', 'rb')
# classifier = pickle.load(pickle_in)

# st.title('🎈 App Name')

# st.write('Hello world!')

# # รับข้อมูลชื่อ-นามสกุล
# name = st.text_input("กรุณากรอก ชื่อ - นามสกุล")

#Logo
st.image(image, use_column_width=True,)
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image(image)

st.markdown("<h1 style='text-align: center;'>การพัฒนารูปแบบการประเมินความเสี่ยงด้านสินเชื่อ</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>The Development of Credit Risk Assessment Model</h2>", unsafe_allow_html=True)

# รับค่าเพศ
sex = {0:"หญิง", 1:"ชาย"}

def format_func5(option):
    return sex[option]

Gender = st.radio('กรุณาระบุเพศของคุณ',options=list(sex.keys()), format_func=format_func5)
# st.write(f"Value = {sex} label = {format_func5(sex)}")


# แสดงผลลัพธ์
# st.write("เพศของคุณเป็น", Gender)

# รับข้อมูลอายุ
# x_age = st.slider('ช่วยอายุระหว่าง 20-70', min_value=20, max_value=70, value=41, step=1)
# age = st.write("กรุณาระบุอายุ", x_age)

age = st.slider('ช่วยอายุระหว่าง 20-70?', 20, 75, 41)
st.write("อายุของคุณ ", age, " ปี")


# รับข้อมูลราคาประเมินรถ
# car_value = st.number_input("กรุณาระบุราคาประเมินรถ", min_value=0)
Evaluation_Amount_str = st.number_input("กรุณาระบุราคาประเมินรถ", value=120642.87)

try:
    Evaluation_Amount = float(Evaluation_Amount_str)
except ValueError:
    st.write("กรุณาระบุเฉพาะตัวเลข")

# รับข้อมูลวงเงินที่อนุมัติ
# loan_amount = st.number_input("กรุณาระบุวงเงินที่อนุมัติ", min_value=0)
Principal_Approve_Amount_str = st.number_input("กรุณาระบุวงเงินที่อนุมัติ", value=75629.66)

try:
    Principal_Approve_Amount = float(Principal_Approve_Amount_str)
except ValueError:
    st.write("กรุณาระบุเฉพาะตัวเลข")

# รับข้อมูลจำนวนงวดที่ผ่อน
Repayment_Tenor_Month_Number = st.selectbox("กรุณาระบุจำนวนงวดที่ผ่อน", ["6", "12", "18", "24", "30", "36", "42", "48", "54", "60", "66", "72"])

# รับข้อมูลอาชีพ
Occupation_Description = {0:'STREET VENDOR',1:'ข้าราชการ',2:'บุคลากรทางการแพทย์',
3:'พนักงานบริษัท',4:'พนักงานรัฐวิสาหกิจ',5:'อาจารย์',7:'เกษตรกร', 8:'เลี้ยงสัตว์', 6:'อื่นๆ'}

def format_func4(option):
    return Occupation_Description[option]

Occupation = st.selectbox('กรุณาเลือกอาชีพ', options=list(Occupation_Description.keys()), format_func=format_func4)
# st.write(f"Value = {Occupation} label = {format_func4(Occupation)}")

# รับข้อมูลรายได้ต่อเดือน
monthly_income = st.number_input("กรุณาระบุรายได้ต่อเดือน", value=19168.37)

# # รับข้อมูลประเภทรถ
# car_type = st.selectbox("กรุณาระบุประเภทรถ", ["รถกระบะ", "รถเก๋ง", "รถมอเตอร์ไซค์", "รถตู้", "รถบรรทุก"])

# # รับข้อมูลยี่ห้อ
# brand = st.text_input("กรุณาระบุยี่ห้อ")

# # รับข้อมูลยี่ห้อ
# brand = st.selectbox("กรุณาระบุยี่ห้อ", list(models_dict.keys()))

# # รับข้อมูลรุ่นรถ
# models = models_dict.get(brand, [])

# if models:
#     model = st.selectbox("กรุณาระบุรุ่นรถ", models)
# else:
#     st.warning("ไม่พบข้อมูลรุ่นรถสำหรับยี่ห้อที่เลือก")

# สร้าง dict เพื่อเก็บรายการยี่ห้อรถและรุ่นรถของแต่ละประเภท
car_dict = {
"CAR": {"Audi": [{"name": "A3", "key": "audi_a3"}, {"name": "A4", "key": "audi_a4"}, {"name": "A6", "key": "audi_a6"}],
"Mercedes": [{"name": "C-Class", "key": "mercedes_cclass"}, {"name": "E-Class", "key": "mercedes_eclass"}, {"name": "S-Class", "key": "mercedes_sclass"}]},
"TRUCK": {"KOBOTA": [{"name": "Nong Few", "key": "FEW"}, {"name": "P'TONGGY", "key": "TONGGY"}]}
}


car_brands = {
   (0,"CAR"): {
        (1,"CHEVROLET"): [(6,"AVEO"), (10,"CAPTIVA"), (46,"CRUZE"), (131,"OPTRA"), (164,"SONIC")],
        (2,"FORD"): [(59,"ECOSPORT"),(62,"ESCAPE"),(63,"EVEREST"),(67,"FIESTA"),(75,"FOCUS")],
        (5,"HONDA"): [(2,"ACCORD"), (12,"BRIO"), (18,"BRV"), (28,"CITY"), (29,"CIVIC"), (46,"CR-V"), (93,"JAZZ")],
        (6,"KIA"): [(138,"PICANTO")],
        (7,"MG"): [(108,"MG3")],
        (8,"MITSUBISHI"): [(17,"ATTRAGE"), (96,"LANCER"), (97,"LANCER EX"), (113,"MIRAGE"), (131,"PAJERO SPORT")],
        (9,"NISSAN"): [(16,"CEFIRO"), (21,"ALMERA"), (105,"LIVINA"), (107,"MARCH"), (127,"NOTE"), (174,"SUNNY"), (179,"SYLPHY"), (180,"TEANA"), (182,"TIIDA"), (201,"XTRAIL")],
        (10,"PROTON"): [(136,"PERSONA"),(151,"SAVVY")],
        (18,"MAZDA"): [(0,"2"),(1,"3"),(47,"CX3")],
        (19,"SUZUKI"): [(23,"CELERIO"), (27,"CIAZ"), (177,"SWIFT"), (178,"SX4")],
        (22,"TOYOTA"): [(9,"CAMRY"), (11,"AVANZA"), (38,"COROLLA"), (39,"COROLLA ALTIS"), (40,"CORONA"), (92,"INNOVA"), (140,"PRIUS"), (162,"SOLUNA"), (188,"VIOS"), (197,"WISH"), (202,"YARIS"), (203,"YARISATIV")]
    },
    (1,"MC"): {
        (0,"BENELLI"): [(183,"TNT 25")],
        (3,"GPX"): [(41,"COUNTRY 125"), (42,"CR5 200"), (49,"DEMON 125"), (50,"DEMON 150"), (57,"DRONE 150"), (99,"LEGEND 150"), (100,"LEGEND 200"), (145,"RAPTOR 180"), (148,"ROCK ELEGNACE")],
        (5,"HONDA"): [(5,"AIR-BLADE"), (15,"CBR 650"), (19,"CB 150"), (20,"CBR 150"), (22,"CBR 300"), (31,"CLICK 110"), (32,"CLICK 110I"), (33,"CLICK 125I"), (34,"CLICK 150I"), (35,"CLICK 160"), (43,"CRF 250"), (48,"CZI 110"), (54,"DREAM 110"), (55,"DREAM 110I"), (56,"DREAM 125"), (76,"FORZA 300"), (91,"ICON"), (98,"LEAD 125"), (114,"MONKEY 125"), (115,"MOOVE 110I"), (117,"MSX 125"), (132,"PCX 125I"), (133,"PCX 150"), (134,"PCX 150I"), (135,"PCX 160"), (137,"PHANTOM 200"), (146,"REBEL 300"), (147,"REBEL 500"), (152,"SCOOPY"), (153,"SCOOPY CLUB 12"), (154,"SCOOPY I"), (155,"SCOOPY PRESTIGE"), (175,"SUPER CUB 110"), (176,"SUPER CUB 110I"), (189,"WAVE 100"), (190,"WAVE 110 I"), (191,"WAVE 110I"), (192,"WAVE 125"), (193,"WAVE 125 I"), (194,"WAVE 125 X"), (195,"WAVE 125C"), (196,"WAVE X"), (208,"ZOOMER X 110I")],
        (11,"KAWASAKI"): [(60,"ER6N 650"), (95,"KSR 110"), (121,"NEW KSR 110"), (122,"NEW KSR 110 PRO"), (124,"NINJA 650"), (206,"Z 125"), (207,"Z 300")],
        (12,"LAMBRETTA"): [(187,"V 200")],
        (13,"RYUKA"): [(30,"CLASSIC"), (44,"CRUISER"), (150,"SAVE-II S")],
        (14,"STALLION"): [(24,"CENTAUR 150"), (25,"CENTAUR 250"), (26,"CENTAUR 400")],
        (15,"VESPA"): [(84,"GTS 150"), (106,"LX 125"), (139,"PRIMAVERA 150"), (149,"S 125"), (170,"SPRINT 125"), (171,"SPRINT 150")],
        (16,"YAMAHA"): [(4,"AEROX 155"),(63,"EXCITER 150"),(68,"FILANO"),(69,"FINN 115I"),(70,"FINO (4DO)"),(71,"FINO (MLEKE)"),
                    (72,"FINO 115"),(73,"FINO 125"),(81,"GRAND FILANO 125"),(83,"GT 125"),(94,"JUPITER RC 115"),(103,"LEXI 125"),
                    (104,"LEXI 125 S"),(109,"MIO 115"),(110,"MIO 115 I"),(111,"MIO 125"),(112,"MIO 125I"),(116,"M-SLAZ 150"),(118,"MT 15"),
                    (126,"N-MAX 155"),(128,"NOUVO 135"),(141,"QBIX 125"),(142,"QBIX 125 ABS"),(143,"QBIX 125 S"),(164,"SPARK 115 I"),
                    (165,"SPARK 135"),(166,"SPARK LX 115"),(167,"SPARK NANO"),(181,"TIARA"),(185,"TTX 115"),(199,"X-MAX 300"),(200,"XSR 155"),
                    (204,"YZF R15"), (205, "YZF R3")],
        (19,"SUZUKI"): [(80,"GD 110"),(82,"GSX-R 150"),(101,"LET'S"),(102,"LETS 110 (CAST)"),(123,"NEX"),(156,"SHOGUN 125"),(157,"SHOOTER"),(158,"SKYDRIVE 125"),
                    (159,"SMASH"),(160,"SMASH 110"),(161,"SMASH 115"),(172,"STEP 125")]
    },
    (2,"PU"): {
        (1,"CHEVROLET"): [(36,"COLORADO")],
        (2,"FORD"): [(144,"RANGER")],
        (8,"MITSUBISHI"): [(173,"STRADA"),(184,"TRITON")],
        (9,"NISSAN"): [(77,"FRONTIER"),  (78,"FRONTIER NAVARA"), (120,"NAVARA"), (129,"NP300")],
        (17,"ISUZU"): [(3,"ADVENTURE"),  (51,"D-MAX"),  (52,"DRAGON EYE"),  (53,"DRAGON POWER"),  (59,"ELF"),  (64,"FASTER Z"),  (119,"MU-7")],
        (18,"MAZDA"): [(7,"BT-50"), (8,"BT-50PRO"), (67,"FIGHTER")],
        (19,"SUZUKI"): [(13,"CARIBIAN"),(14,"CARRY")],
        (20,"TATA"): [(198,"XENON")],
        (22,"TOYOTA"): [(75,"FORTUNER"), (87,"HILUX MIGHTY X"), (88,"HILUX REVO"), (89,"HILUX TIGER"), (90,"HILUX VIGO"), (168,"SPORT CRUISER"), (169,"SPORT RIDER")]
    },
    (3,"TRUCK"): {
        (4,"HINO"): [(186,"FF177")],
        (17,"ISUZU"): [(85,"FVZ12MY"),(37,"NKR71L")]
    },
    (4,"VAN"): {
        (9,"NISSAN"): [(186,"URVAN")],
        (21,"HYUNDAI"): [(85,"H1")],
        (22,"TOYOTA"): [(37,"COMMUTER"),(86,"HIACE")]
    }
}


# รับประเภทรถที่เลือก
car_type = st.selectbox("เลือกประเภทรถ", list(car_brands.keys()))

# แสดงรายการยี่ห้อรถที่เกี่ยวข้องกับประเภทรถที่เลือก
car_brand = st.selectbox("เลือกยี่ห้อรถ", list(car_brands[car_type].keys()))

# แสดงรายการรุ่นรถที่เกี่ยวข้องกับยี่ห้อรถที่เลือก
car_model = st.selectbox("เลือกรุ่นรถ", car_brands[car_type][car_brand])

# # รับข้อมูลรุ่นรถ
# model = st.text_input("กรุณาระบุรุ่นรถ")

# รับข้อมูลปีรถ
# y = st.slider('ช่วงของปีรถ', min_value=1993, max_value=2023, value=2012, step=1)
# car_year = st.write("กรุณาระบุปีรถ", y)

car_year = st.slider('ปีรถ?', 1993, 2023, 2013)
st.write("ปีรถของคุณ ", car_year, " ปี")

# รับข้อมูลอายุรถ
# z = st.slider('อายุรถ', min_value=0, max_value=30, value=10, step=1)
# car_age = st.write("กรุณาระบุอายุรถ", z)

car_age = pd.to_datetime('today').year - car_year

# cc = st.slider('อายุรถ?', 0, 30, 0)
st.write("อายุรถของคุณ ", car_age, " ปี")

loan_ratio = Principal_Approve_Amount / Evaluation_Amount * 100

    

if st.button("Predict"):
    # read model
    # make prediction

    # st.write("% LTV :", loan_ratio)

    keyfile_bigquery = "final-load-from-gcs-to-bigquery-410501-f7609d0f3f4a.json"
    service_account_info_bigquery = json.load(open(keyfile_bigquery))
    credentials_bigquery = service_account.Credentials.from_service_account_info(
        service_account_info_bigquery
    )
    project_id = "orbital-eon-410501"
    bigquery_client = bigquery.Client(
        project=project_id,
        credentials=credentials_bigquery,
        location="us-central1",
    )
    query = f"""
        select
            *
            from
              ml.predict(MODEL `pim_chaiyo.xgboost_predictor_1`,(
                select
                            {Principal_Approve_Amount_str} as Principal_Approve_Amount,
                            {Repayment_Tenor_Month_Number} as Repayment_Tenor_Month_Number,
                            {Gender} as Gender,
                            {Occupation} as Occupation_Description,
                            {monthly_income} as Total_Income_Amount__Month_,
                            {car_type[0]} as Collateral_Type_Code,
                            {car_brand[0]} as Vehicle_Brand,
                            {car_model[0]} as Vehicle_Model,
                            {car_year} as Vehicle_Release_Year,
                            {int(Evaluation_Amount_str)} as Evaluation_Amount,
                            {age} as age,
                            {car_age} as Vehicle_Age,
                            DPD as label
                        from `pim_chaiyo.chaiyo`))
    """
    df = bigquery_client.query(query).to_dataframe()
    print(df.head())

    threshold = 0.9825
    prob = df['predicted_label_probs'][0][0]['prob']
    if prob >= threshold:
        st.balloons()
        result = "ระบบประเมินเบื้องต้นว่าสามารถอนุมัติได้"
    else:
        result = "ระบบประเมินเบื้องต้นว่าไม่สามารถอนุมัติได้ ☠️"

    st.write(result)
    