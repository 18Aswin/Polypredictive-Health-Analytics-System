import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import streamlit as st
from streamlit_option_menu import option_menu


#Loading models
diabetes     =  pickle.load(open('Saved_Models/diabetes_predictor.sav', 'rb'))
heartdisease =  pickle.load(open('Saved_Models/heartdisease_predictor.sav', 'rb'))
hepititisC   =  pickle.load(open('Saved_Models/hepititisC_predictor.sav', 'rb'))
hiv          =  pickle.load(open('Saved_Models/hiv_predictor.sav', 'rb'))
hypertension =  pickle.load(open('Saved_Models/hypertension_predictor.sav', 'rb'))
liverdisease =  pickle.load(open('Saved_Models/liver_disease_predictor.sav', 'rb'))
lungcancer   =  pickle.load(open('Saved_Models/lung_cancer_predictor.sav', 'rb'))
osteoporosis =  pickle.load(open('Saved_Models/osteoporosis_predictor.sav', 'rb'))
parkinsons   =  pickle.load(open('Saved_Models/parkinsons_predictor.sav', 'rb'))
stroke       =  pickle.load(open('Saved_Models/stroke_predictor.sav', 'rb'))


#Sidebar

with st.sidebar:
    heading = option_menu("Polypredictive Health Analytics System",
                          
                          ['Diabetes Prediction','Heart Disease Prediction','Hepititis C Prediction','HIV Prediction','Hypertension Prediction','Liver Disease Prediction','Lung Cancer Prediction','Osteoporosis Prediction','Parkinsons Disease Prediction','Stroke Prediction'],
                          
                          icons=['capsule','heart','virus2','virus','hospital','capsule-pill','lungs','file-medical','clipboard2-pulse-fill','heart-pulse'],

                          default_index = 0)
    


#Diabetes Page
if (heading == 'Diabetes Prediction'):

    #Page Title
    st.title('Diabetes Prediction')
    col1, col2 = st.columns(2)


    with col1:
        Pregnancies = st.text_input('No of Pregnancies')
    with col2:
        Glucose = st.text_input('Blood Glucose Level')
    with col1:
        BloodPressure = st.text_input('Blood Pressure')
    with col2:
        SkinThickness = st.text_input('Skin fold thickness')
    with col1:
        Insulin = st.text_input('Insulin level')
    with col2:
        BMI = st.text_input('Body Mass Index value')
    with col1:
        DiabetesPedigreeFunction = st.text_input(' Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age')


    #Prediction
    d1 = ''

    #Button for prediction
    if st.button('Diabetes Test Result'):
       input1 = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

       input1 = [float(x) for x in input1]

       diabetes_prediction = diabetes.predict(input1)

       if(diabetes_prediction[0]==0):
          d1 = 'Person is NOT Diabetic'
       else:
          d1 = 'Person is Diabetic'
           
    st.success(d1)


#########################################################################################################################################################################


#Heart Disease Page
if (heading == 'Heart Disease Prediction'):

    #Page Title
    st.title('Heart Disease Prediction')
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age in Years')
    with col2:
        sex = st.text_input('Gender (1-male, 0-female)')
    with col1:
        cp = st.text_input('Chest pain type')
    with col2:
        trestbps = st.text_input('Resting blood pressure')
    with col1:
        chol = st.text_input('Serum cholestoral')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col1:
        exang = st.text_input('Exercise induced angina (1 = yes; 0 = no)')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col1:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col2:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('1 = normal; 2 = fixed defect; 3 = reversable defect')

    #Prediction
    d2 = ''

    #Button for prediction
    if st.button('Heart Test Result'):
       input2 = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

       input2 = [float(x) for x in input2]

       heart_prediction = heartdisease.predict([input2])

       if heart_prediction[0] == 1:
          d2 = 'The person is having heart disease'
       else:
           d2 = 'The person does not have any heart disease'
           
    st.success(d2)


#########################################################################################################################################################################


#Hepititis C Page
if (heading == 'Hepititis C Prediction'):

    #Page Title
    st.title('Hepititis C Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input('Age in Years')
    with col2:
        Sex = st.text_input('Gender (1-male, 0-female)')
    with col1:
        ALB = st.text_input('Albumin Blood Test')
    with col2:
        ALP = st.text_input('Alkaline phosphatase')
    with col1:
        ALT = st.text_input('Alanine Transaminase')
    with col2:
        AST = st.text_input('Aspartate Transaminase')
    with col1:
        BIL = st.text_input('Bilirubin')
    with col2:
        CHE = st.text_input('Acetylcholinesterase')
    with col1:
        CHOL = st.text_input('Cholesterol')
    with col2:
        CREA = st.text_input('Creatinine')
    with col1:
        GGT = st.text_input('Gamma-Glutamyl Transferase')
    with col2:
        PROT = st.text_input('Proteins')

    #Prediction
    d3 = ''

    #Button for prediction
    if st.button('Hepatitis C Test Result'):
       input3 = [Age,Sex,ALB,ALP,ALT,AST,BIL,CHE,CHOL,CREA,GGT,PROT]

       input3 = [float(x) for x in input3]

       hepatitisC_prediction = hepititisC.predict([input3])

       if (hepatitisC_prediction[0]== 0):
           d3 = 'The Person can be a Blood Donor'
       elif (hepatitisC_prediction[0]== 1):
           d3 = 'The Person can be a Suspected Blood Donor'
       elif (hepatitisC_prediction[0]== 2):
           d3 = 'The Person has Hepatitis '
       elif (hepatitisC_prediction[0]== 3):
           d3 = 'The Person has Fibrosis '
       else:
           d3 = 'The Person has Cirrhosis '
           
    st.success(d3)


#########################################################################################################################################################################


#HIV Page
if (heading == 'HIV Prediction'):

    #Page Title
    st.title('HIV Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input('Age in years')
    with col2:
        Marital_Status = st.text_input('Marital Status (0 - Cohabiting, 1 - Divorced, 2 - Married, 3 - Unmarried, 4 - Widowed )')
    with col1:
        STD = st.text_input('Any STD (0 - No, 1 - Yes)')
    with col2:
        Educational_Background = st.text_input('Educational Background (0 - College Degree, 1 - Illiteracy, 2 - Junior High School, 3 - Primary School, 4 - Senior High School)')
    with col1:
        HIV_TEST_IN_PAST_YEAR = st.text_input('HIV Test Done in Past Year (0 - No, 1 - Yes)')
    with col2:
        AIDS_education = st.text_input('Education about AIDS (0 - No, 1 - Yes)')
    with col1:
        Places_of_seeking_sex_partners = st.text_input('Places of seeking sex partners (0 - Bar, 1 - Internet, 2 - Others, 3 - Park, 4 - Public Bath, 5 - None)')
    with col2:
        SEXUAL_ORIENTATION = st.text_input('Sexual Orientation (0 - Bisexual, 1 - Heterosexual, 2 - Homosexual)')
    with col1:
        Drug_taking = st.text_input('Taking Drugs (0 - No, 1 - Yes)')

    #Prediction
    d4 = ''

    #Button for prediction
    if st.button('HIV Test Result'):
       input4 = [Age,Marital_Status,STD,Educational_Background,HIV_TEST_IN_PAST_YEAR,AIDS_education,Places_of_seeking_sex_partners,SEXUAL_ORIENTATION,Drug_taking]
       
       input4 = [float(x) for x in input4]

       hiv_prediction = hiv.predict([input4])

       if (hiv_prediction[0]== 0):
           d4 = 'The Person would most likely NOT have HIV'
       else:
           d4 = 'The Person would most likely have HIV'
           
    st.success(d4)


#########################################################################################################################################################################


#Hypertension Page
if (heading == 'Hypertension Prediction'):

    #Page Title
    st.title('Hypertension Prediction')
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age in Years')
    with col2:
        sex = st.text_input('Gender (1-male, 0-female)')
    with col1:
        cp = st.text_input('Chest pain type')
    with col2:
        trestbps = st.text_input('Resting blood pressure')
    with col1:
        chol = st.text_input('Serum cholestoral')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col1:
        exang = st.text_input('Exercise induced angina (1 = yes; 0 = no)')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col1:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col2:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('1 = normal; 2 = fixed defect; 3 = reversable defect')

    #Prediction
    d5 = ''

    #Button for prediction
    if st.button('Hypertension Test Result'):
       input5 = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

       input5 = [float(x) for x in input5]

       hypertension_prediction = hypertension.predict([input5])

       if hypertension_prediction[0] == 1:
          d5 = 'The person is suffering with Hypertension'
       else:
           d5 = 'The person is NOT suffering from hypertension'
           
    st.success(d5)


#########################################################################################################################################################################


#Liver Disease Page
if (heading == 'Liver Disease Prediction'):

    #Page Title
    st.title('Liver Disease Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input('Age of the patient')
    with col2:
        Gender = st.text_input('Gender of the patient')
    with col1:
        tb = st.text_input('Total Bilirubin')
    with col2:
        db = st.text_input('Direct Bilirubin')
    with col1:
        aap = st.text_input('Alkphos Alkaline Phosphotase')
    with col2:
        sgpt = st.text_input('Sgpt Alamine Aminotransferase')
    with col1:
        sgot = st.text_input('Sgot Aspartate Aminotransferase')
    with col2:
        tp = st.text_input('Total Protiens')
    with col1:
        alb = st.text_input('Albumin')
    with col2:
        ratio = st.text_input('A/G Ratio Albumin and Globulin Ratio')

    #Prediction
    d6 = ''

    #Button for prediction
    if st.button('Liver Test Result'):
       input6 = [Age,Gender,tb,db,aap,sgpt,sgot,tp,alb,ratio]

       input6 = [float(x) for x in input6]

       liver_prediction = liverdisease.predict([input6])

       if (liver_prediction[0]== 0):
           d6 = 'The Person is NOT a Liver Patient'
       else:
           d6 = 'The Person is a Liver Patient'
           
    st.success(d6)


#########################################################################################################################################################################


#Lung Cancer Page
if (heading == 'Lung Cancer Prediction'):

    #Page Title
    st.title('Lung Cancer Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input('Age (0-f, 1-m)')
    with col2:
        SMOKING	 = st.text_input('Do you Smoke (0-no, 1-yes)')
    with col1:
        YELLOW_FINGERS = st.text_input('Do you have yellow fingers (0-no, 1-yes)')
    with col2:
        ANXIETY = st.text_input('Do you have anxiety (0-no, 1-yes)')
    with col1:
        PEER_PRESSURE = st.text_input('Peer Pressure (0-no, 1-yes)')
    with col2:
        CHRONIC_DISEASE = st.text_input('Do you have any Chronic Disease (0-no, 1-yes)')
    with col1:
        FATIGUE = st.text_input('DO you feel Fatigue (0-no, 1-yes)')
    with col2:
        ALLERGY = st.text_input('Do you have allergy (0-no, 1-yes)')
    with col1:
        ALCOHOL_CONSUMPTION = st.text_input('Do you consume alcohol (0-no, 1-yes)')
    with col2:
        COUGHING = st.text_input('Do you have coughing (0-no, 1-yes)')
    with col1:
        SHORTNESS_BREATH = st.text_input('Do you feel shortness in breathing (0-no, 1-yes)')
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input('Do you have difficulty in Swallowing (0-no, 1-yes)')
    with col1:
        CHEST_PAIN  = st.text_input('Do you have Chest Pain (0-no, 1-yes)')

    #Prediction
    d7 = ''

    #Button for prediction
    if st.button('Lung Cancer Test Result'):
       input7 = [Age,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,ALCOHOL_CONSUMPTION,COUGHING,SHORTNESS_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]

       input7 = [float(x) for x in input7]

       lungcancer_prediction = lungcancer.predict([input7])

       if (lungcancer_prediction[0]== 0):
           d7 = 'The Person does NOT have Lung Cancer'
       else:
           d7 = 'The Person likely have Lung Cancer'
           
    st.success(d7)


#########################################################################################################################################################################


#Osteoporosis Page
if (heading == 'Osteoporosis Prediction'):

    #Page Title
    st.title('Osteoporosis Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input('Age')
    with col2:
        gender = st.text_input('Gender (0 - Female, 1 - Male)')
    with col1:
        Hormonal_Changes = st.text_input('Hormonal Changes (0 - Normal, 1 - Postmenopausal)')
    with col2:
        Family_History = st.text_input('Family History (0 - No, 1 - Yes)')
    with col1:
        Race = st.text_input('Race/Ethnicity (0 - African American, 1 - Asian, 2 - Caucasian)')
    with col2:
        Body_Weight = st.text_input('Body Weight (0 - Normal, 1 - Underweight)')
    with col1:
        Calcium_Intake = st.text_input('Calcium Intake (0 - Low, 1 - Adequate)')
    with col2:
        Vitamin_D_Intake = st.text_input('Vitamin D Intake (0 - Insufficient, 1 - Sufficient)')
    with col1:
        Physical_Activity = st.text_input('Physical Activity (0 - Active, 1 - Sedentary)')
    with col2:
        Smoking = st.text_input('Smoking (0 - No, 1 - Yes)')
    with col1:
        Alcohol_Consumption = st.text_input('Alcohol Consumption (0 - Moderate, 1 - None)')
    with col2:
        Medical_Condition = st.text_input('Medical Condition (0 - Hyperthyroidism, 1 - Rheumatoid Arthritis, 2 - None)')
    with col1:
        Medications = st.text_input('Medications (0 - Corticosteroids,1 - None)')
    with col2:
        Prior_Fractures = st.text_input('Prior Fractures (0 - No, 1 - Yes)')

    #Prediction
    d8 = ''

    #Button for prediction
    if st.button('Osteoporosis Test Result'):
       input8 = [Age,gender,Hormonal_Changes,Family_History,Race,Body_Weight,Calcium_Intake,Vitamin_D_Intake,Physical_Activity,Smoking,Alcohol_Consumption,Medical_Condition,Medications,Prior_Fractures]

       input8 = [float(x) for x in input8]

       osteoporosis_prediction = osteoporosis.predict([input8])

       if (osteoporosis_prediction[0]== 0):
           d8 = 'The Person would most likely NOT develop Osteoporosis'
       else:
           d8 = 'The Person would most likely develop Osteoporosis'
           
    st.success(d8)


#########################################################################################################################################################################


#Parkinsons Page
if (heading == 'Parkinsons Disease Prediction'):

    #Page Title
    st.title('Parkinsons Prediction')
    col1, col2 = st.columns(2)

    with col1:
        Fo = st.text_input('Average vocal fundamental frequency')
    with col2:
        Fhi = st.text_input('Maximum vocal fundamental frequency')
    with col1:
        Flo = st.text_input('Minimum vocal fundamental frequency')
    with col2:
        Jitter = st.text_input('Percentage of cycle-to-cycle variability of the period duration')
    with col1:
        Jitter_Abs = st.text_input('Absolute value of cycle-to-cycle variability of the period duration')
    with col2:
        RAP = st.text_input('Relative measure of the pitch disturbance')
    with col1:
        PPQ = st.text_input('Pitch perturbation quotient')
    with col2:
        DDP = st.text_input('Average absolute difference of differences between jitter cycles')
    with col1:
        Shimmer = st.text_input('Variations in the voice amplitdue')
    with col2:
        Shimmer_dB  = st.text_input('Variations in the voice amplitdue in dB')
    with col1:
        APQ3 = st.text_input('Three point amplitude perturbation quotient measured against the average of the three amplitude')
    with col2:
        APQ5 = st.text_input('Five point amplitude perturbation quotient measured against the average of the three amplitude')
    with col1:
        APQ = st.text_input('Amplitude perturbation quotient from MDVP')
    with col2:
        DDA = st.text_input('Average absolute difference between the amplitudes of consecutive periods.')
    with col1:
        NHR  = st.text_input('Noise-to-harmonics Ratio')
    with col2:
        HNR  = st.text_input('Harmonics-to-noise Ratio')
    with col1:
        RPDE = st.text_input('Recurrence period density entropy')
    with col2:
        DFA  = st.text_input('Signal fractal scaling exponent')
    with col1:
        spread1 = st.text_input('Discrete probability distribution of occurrence of relative semitone variations')
    with col2:
        spread2 = st.text_input('Three nonlinear measures of fundamental frequency variation')
    with col1:
        D2 = st.text_input('Correlation dimension')
    with col2:
        PPE = st.text_input('Entropy of the discrete probability distribution of occurrence of relative semitone variations')

    #Prediction
    d9 = ''

    #Button for prediction
    if st.button('Parkinsons Test Result'):
       input9 = [Fo,Fhi,Flo,Jitter,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

       input9 = [float(x) for x in input9]

       parkinsons_prediction = parkinsons.predict([input9])

       if (parkinsons_prediction[0]== 0):
           d9 = 'The Person does NOT have Parkinsons Disease'
       else:
           d9 = 'The Person does have Parkinsons Disease'
           
    st.success(d9)


#########################################################################################################################################################################


#Stroke Page
if (heading == 'Stroke Prediction'):

    #Page Title
    st.title('Stroke Prediction')
    col1, col2 = st.columns(2)

    with col1:
        gender = st.text_input('Gender (Female -> 0, Male -> 1, Other -> 2)')
    with col2:
        age = st.text_input('Age')
    with col1:
        hypertension = st.text_input('Suffering from Hypertension')
    with col2:
        heart_disease = st.text_input('Have any heart disease')
    with col1:
        ever_married = st.text_input('Ever Married (No -> 0, Yes -> 1)')
    with col2:
        work_type = st.text_input('Work Type (Govt_job -> 0, Never_worked -> 1, Private -> 2, Self-employed -> 3, children -> 4)')
    with col1:
        Residence_type = st.text_input('Residence Type (Rural -> 0, Urban -> 1)')
    with col2:
        avg_glucose_level = st.text_input('Average Glucose Level')
    with col1:
        bmi = st.text_input('BMI')
    with col2:
        smoking_status = st.text_input('Smoking Status (Unknown -> 0, formerly smoked -> 1, never smoked -> 2, smokes -> 3)')

    #Prediction
    d10 = ''

    #Button for prediction
    if st.button('Stroke Test Result'):
       input10 = [gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]

       input10 = [float(x) for x in input10]

       stroke_prediction = stroke.predict([input10])

       if (stroke_prediction[0]== 0):
           d10 = 'The Person did NOT had Stroke'
       else:
           d10 = 'The Person had or most likely will have Stroke'
           
    st.success(d10)
