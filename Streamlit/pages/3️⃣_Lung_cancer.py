import streamlit as st
import joblib
import pandas as pd



st.markdown('## Liver Cancer Prediction')
st.markdown('### Predicting the likelihood of a patient developing lung cancer')
st.markdown('Choose below options according to the report to know the patient status')
st.write('-----')

Age = st.text_input(label='Enter your age', value='20')

Gender = st.radio(label = 'Select your gender',options=['Male', 'Female'])
if Gender == 'Male':
    Gender = 1
elif Gender == 'Female':
    Gender = 2

st.write('-----')
st.write('Please select the option from slider')
st.info('1 means very low and 9 means very high')

Pollution = st.slider(label='The level of air pollution exposure of the patient', min_value=1, max_value=9, key=0)
Alcohol_use = st.slider(label='The level of alcohol use of the patient', min_value=1, max_value=9, key=1)
Dust_allergy = st.slider(label='The level of dust allergy of the patient', min_value=1, max_value=9, key=2)
chronic_lung_Disease = st.slider(label='The level of chronic lung disease of the patient. ', min_value=1, max_value=9, key=3)
Occupational_hazards= st.slider(label='The level of occupational hazards of the patient.', min_value=1, max_value=9, key=4)
Genetic_risk = st.slider(label='The level of genetic risk of the patient.', min_value=1, max_value=9, key=5)
Balanced_diet = st.slider(label='The level of balanced diet of the patient.', min_value=1, max_value=9, key=6)
Obesity = st.slider(label='The level of obesity of the patient.', min_value=1, max_value=9, key=7)
Smoking = st.slider(label='The level of smoking of the patient.', min_value=1, max_value=9, key=8)
Passive_Smoker = st.slider(label='The level of passive smoker of the patient.', min_value=1, max_value=9, key=9)
Chest_Pain = st.slider(label='The level of chest pain of the patient.', min_value=1, max_value=9, key=10)
Coughing_of_Blood = st.slider(label='The level of coughing of blood of the patient. ', min_value=1, max_value=9, key=22)
Fatigue = st.slider(label='The level of fatigue of the patient.', min_value=1, max_value=9, key=11)
Weight_loss = st.slider(label='The level of weight loss of the patient.', min_value=1, max_value=9, key=12)
Shortness_of_Breath = st.slider(label='The level of shortness of breath of the patient. ', min_value=1, max_value=9, key=13)
Wheezing = st.slider(label='The level of wheezing of the patient.', min_value=1, max_value=9, key=15)
Swallowing_Difficulty = st.slider(label='The level of swallowing difficulty of the patient.', min_value=1, max_value=9, key=16)
Clubbing_of_Finger_Nails = st.slider(label='The level of clubbing of finger nails of the patient. ', min_value=1, max_value=9, key=17)
Frequent_Cold = st.slider(label='The level of frequent cold of the patient. ', min_value=1, max_value=9, key=18)
Dry_Cough = st.slider(label='The level of dry cough of the patient. ', min_value=1, max_value=9, key=19)
Snoring = st.slider(label='The level of snoring of the patient. ', min_value=1, max_value=9, key=20)


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



model = joblib.load('C:/Users/6/healthify/Streamlit/pages/lung_cancer.joblib')



predict = st.button("Predict")
st.write('-----')
if predict:

    df = pd.DataFrame(data=[
        [Age, Gender, Pollution, Alcohol_use, Dust_allergy, Occupational_hazards, Genetic_risk, chronic_lung_Disease,
         Balanced_diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood, Fatigue, Weight_loss,
         Shortness_of_Breath, Wheezing,
         Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring]],
                      columns=['Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy',
                               'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease',
                               'Balanced Diet', 'Obesity', 'Smoking', 'Passive Smoker', 'Chest Pain',
                               'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath',
                               'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails',
                               'Frequent Cold', 'Dry Cough', 'Snoring'])


    st.markdown('##### This is the data you have submitted:')
    st.markdown('**Age** : '+ Age)
    st.markdown('**Gender** : '+ str(Gender))
    st.markdown('**Air Pollution**  : '+ str(Pollution))
    st.markdown('**Alcohol Use**  : ' + str(Alcohol_use))
    st.markdown('**Dust Allergy**  : ' + str(Dust_allergy))
    st.markdown('**Occupational Hazards**  : ' + str(Occupational_hazards))
    st.markdown('**Genetic Risk**  : ' + str(Genetic_risk))
    st.markdown('**Chronic Lung Disease**  : ' + str(chronic_lung_Disease))
    st.markdown('**Balanced Diet**  : ' + str(Balanced_diet))
    st.markdown('**Obesity**  : ' + str(Obesity))
    st.markdown('**Smoking**  : ' + str(Smoking))
    st.markdown('**Passive Smoker**  : ' + str(Passive_Smoker))
    st.markdown('**Chest Pain**  : ' + str(Chest_Pain))
    st.markdown('**Coughing of Blood**  : ' + str(Coughing_of_Blood))
    st.markdown('**Fatigue**  : ' + str(Fatigue))
    st.markdown('**Weight Loss**  : ' + str(Weight_loss))
    st.markdown('**Shortness of Breath**  : ' + str(Shortness_of_Breath))
    st.markdown('**Wheezing**  : ' + str(Wheezing))



    pred = model.predict(df)
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
            infec = doctor_search("Oncologist")
            st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
            st.markdown(f"- [Oncologist]({infec}) 👨‍⚕")
            st.markdown("---")
    if pred == 0:
        st.subheader(
            "The patient doesn't have any chances of having a liver disease 😄"
        )

        st.balloons()
    if pred == 2:
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
            infec = doctor_search("Oncologist")
            st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
            st.markdown(f"- [Oncologist]({infec}) 👨‍⚕")
            st.markdown("---")