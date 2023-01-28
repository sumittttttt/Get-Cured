import streamlit as st
import joblib
import pandas as pd


st.markdown('## Diabetes Prediction')
st.markdown('### Predicting the likelihood of a patient developing diabetes')
st.write('Choose below options according to the report to know the patient status')
st.markdown('----')

Age = st.Age = st.text_input(label='Enter your age', value='20')
Gender = st.radio(label = 'Select your gender',options=['Male', 'Female'])
st.markdown('----')

BMI = st.text_input(label='Enter your BMI', value='0', key=1, help='Body mass index (weight in kg/(height in m)^2)')
DPF = st.text_input(label='Enter your Diabetes Pedigree Function', key=2, value=0)
Insulin = st.text_input(label='Enter your Insulin (mu U/ml)', value=0, key=3, help='2-Hour serum insulin (mu U/ml)')
SkinThickness = st.text_input(label='Enter your Skin Thickness (mm)',help='Triceps skin fold thickness (mm)', value=0, key=4)
BloodPressure = st.text_input(label='Enter your Diastolic blood pressure (mm Hg)', value=0, key=5, autocomplete='')
Glucose = st.text_input(label='Enter your Glucose', value=0, key=6, help='Plasma glucose concentration a 2 hours in an oral glucose tolerance test')
st.markdown('----')
preg =st.slider(label='Enter Number of times pregnant', min_value=0, max_value=10)

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


model = joblib.load('C:/Users/6/healthify/ML models and notebooks/trained models/diabetes')
predict = st.button("Predict")


st.write('-----')
if predict:
    df = pd.DataFrame(data=[[preg, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]],
                      columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                               'BMI', 'DiabetesPedigreeFunction', 'Age'])
    df = df.astype('float64')

    st.markdown('##### This is the data you have submitted:')
    st.markdown('**Age** : '+ Age)
    st.markdown('**Gender** : '+ Gender)
    st.markdown('**BMI** : '+ BMI)
    st.markdown('**Diabetes Pedigree Function** : '+ DPF)
    st.markdown('**Insulin** : '+ Insulin)
    st.markdown('**Skin Thickness** : '+ SkinThickness)
    st.markdown('**Blood Pressure** : '+ BloodPressure)
    st.markdown('**Glucose** : '+ Glucose)
    st.markdown('**Number of Times Pregnant** : '+ str(preg))
    st.markdown('----')
    pred = model.predict(df)
    if pred == 1:
            st.subheader("The patient have chances of having a Diabetes 😔")
            st.markdown("---")
            st.error(
                "If you are a patient, consult with one of the following doctors immediately"
            )
            st.subheader("Specialists 👨‍⚕")
            st.write(
                "Click on the specialists to get the specialists nearest to your location 📍"
            )
            pcp = doctor_search("Primary Care Provider")
            infec = doctor_search("Diabetologist")
            st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
            st.markdown(f"- [Diabetologist]({infec}) 👨‍⚕")
            st.markdown("---")
    if pred == 0:
        st.subheader(
            "The patient doesn't have any chances of having a Diabetes 😄"
        )

        st.balloons()