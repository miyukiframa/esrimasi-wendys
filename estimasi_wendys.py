import pickle
import streamlit as st

model = pickle.load(open('estimasi_wendys.sav', 'rb'))

st.title('Estimasi Jumlah Kolesterol Pada Menu Wendys')

Fat = st.number_input('Input Total Lemak (g)')
Sodium = st.number_input('Input Jumlah Sodium (mg)')
Total_Carb = st.number_input('Input Total Karbohidrat (g)')
Sugars = st.number_input('Input Jumlah Gula (g)')
Protein = st.number_input('Input Jumlah Protein (g)')
Calories = st.number_input('Input Kalori')

predict = ''

if st.button('Estimasi Kolesterol'):
    predict = model.predict(
        [[Fat, Sodium, Total_Carb, Sugars, Protein, Calories]]
    )
    st.write ('Estimasi Jumlah Kolesterol : ', predict)