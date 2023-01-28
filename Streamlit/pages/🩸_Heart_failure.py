import streamlit as st
import joblib
import pandas as pd


st.markdown('## Heart Failure Prediction')
st.markdown("### Predicting the likelihood of a patient's heart failure")
st.write('Choose below options according to the report to know the patient status')
st.markdown('----')


Age = int(st.text_input(label='Enter your age', value='20'))

Gender = st.radio(label = 'Select your gender',options=['Male', 'Female'])
if Gender == 'Male':
    Gender = 0
elif Gender == 'Female':
    Gender = 1

chest_pain_type = st.selectbox(label='Select the chest pain type',
                               options=['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])

if chest_pain_type == 'Atypical Angina':
    chest_pain_type = 1
elif chest_pain_type == 'Typical Angina':
    chest_pain_type = 0
elif chest_pain_type == 'Non-Anginal Pain':
    chest_pain_type = 2
elif chest_pain_type == 'Asymptomatic':
    chest_pain_type = 3

resting_BP = int(st.text_input(label='Enter your resting blood pressure [mm Hg]', key=2, value=0))
chol = int(st.text_input(label='Enter your serum cholesterol [mm/dl]', key=1, value=0))

fasting = st.selectbox(label='Enter your fasting blood sugar', options=[0,1], help='Select 1: if FastingBS > 120 mg/dl, 0: otherwise')
max_hr = int(st.text_input(label='Enter your maximum heart rate achieved', key=3, value=0))
exe_ang = st.selectbox(label='Enter your fasting blood sugar', options=['Yes', 'No'])
if exe_ang == 'No':
    exe_ang = 0
elif exe_ang == 'Yes':
    exe_ang = 1

old = float(st.text_input(label='Enter your  oldpeak', key=5, value=0, help='oldpeak = ST [Numeric value measured in depression'))
st_slope = st.selectbox(label='Enter your the slope of the peak exercise ST segment', options=['Up', 'Flat', 'Downslopping'])
if st_slope == 'Up':
    st_slope = 1
elif st_slope == 'Flat':
    st_slope = 0
elif st_slope == 'Downslopping':
    st_slope = 2

resting_ECG = st.selectbox(label='Enter your resting ECG', options=['Normal', 'ST', 'LVH'])
if resting_ECG == 'Normal':
    resting_ECG = 0
elif resting_ECG == 'ST':
    resting_ECG = 1
elif resting_ECG == 'LVH':
    resting_ECG = 2

with st.expander("See explanation"):
    st.markdown("Normal: Normal")
    st.markdown("ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)")
    st.markdown(" LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria")

def doctor_search(doctor_type):
    """
    Searches the specialist near you
    """
    base_url = "https://www.google.com/search?q="
    query = doctor_type.split(" ")
    query = "+".join(query)
    query = f"{query}+near+me"
    final_url = base_url + query

    return final_url



model = joblib.load('C:/Users/6/healthify/ML models and notebooks/trained models/heart_failure')



predict = st.button("Predict")
st.write('-----')
if predict:

    df = pd.DataFrame(data=[
        [Age, Gender, chest_pain_type, resting_BP, chol, fasting, resting_ECG, max_hr, exe_ang, old, st_slope ]],
                      columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])


    st.markdown('##### This is the data you have submitted:')
    st.markdown('**Age** : '+ str(Age))
    st.markdown('**Gender** : '+ str(Gender))
    st.markdown('**Chest Pain Type** : ' + str(chest_pain_type))
    st.markdown('**Resting BP** : ' + str(resting_BP))
    st.markdown('**Cholesterol** : ' + str(chol))
    st.markdown('**Fasting** : ' + str(fasting))
    st.markdown('**Resting ECG** : ' + str(resting_ECG))
    st.markdown('**Max HR** : ' + str(max_hr))
    st.markdown('**Exercise Angina** : ' + str(exe_ang))
    st.markdown('**Old Peak** : ' + str(old))
    st.markdown('**ST Slope** : ' + str(st_slope))



    pred = model.predict(df)

    if pred == 0:
        st.subheader(
            "The patient doesn't have any chances of having a liver disease 😄"
        )

        st.balloons()
    if pred == 1:
            st.subheader("The patient have chances of having a liver disease 😔")
            st.markdown("---")
            st.error(
                "If you are a patient, consult with one of the following doctors immediately"
            )
            st.subheader("Specialists 👨‍⚕")
            st.write(
                "Click on the specialists to get the specialists nearest to your location 📍"
            )
            pcp = doctor_search("Primary Care Provider")
            infec = doctor_search("cardiologists")
            st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
            st.markdown(f"- [cardiologists]({infec}) 👨‍⚕")
            st.markdown("---")