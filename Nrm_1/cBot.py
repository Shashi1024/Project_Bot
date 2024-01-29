import random 
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow
from tensorflow import keras
from keras.models import load_model
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


lematizer  = WordNetLemmatizer()
lp = []
ln =[]
nn_l = []
bm_l = []

intents = json.loads(open("Nrm_1/Intents.json").read())
dep_model=pickle.load(open('Nrm_1/The_Palmist_new3.pkl','rb'))
words = pickle.load(open('Nrm_1/Words.pkl','rb'))
classes = pickle.load(open('Nrm_1/Classes.pkl','rb'))
model = load_model('Nrm_1/chatBot_model.h5')


a = "Itching,Skin Rash,Nodal Skin Eruptions,Continuous Sneezing,Shivering,Chills,Joint Pain,Stomach Pain,Acidity,Ulcers On Tongue,Muscle Wasting,Vomiting,Burning Urination,Spotting Urination,Fatigue,Weight Gain,Anxiety,Cold Hands And Feets,Mood Swings,Weight Loss,Restlessness,Lethargy,Pain In Throat,Irregular Sugar Level,Cough,High Fever,Sunken Eyes,Breathlessness,Sweating,Dehydration,Indigestion,Headache,Yellowish Skin,Dark Urine,Nausea,Loss of Appetite,Pain behind the Eyes,Back Pain,Constipation,Abdominal Pain,Diarrhoea,Mild Fever,Yellow Urine,Yellowing of Eyes,Liver Failure,Fluid Overload,Swelling Of Stomach,Swelled Lymph Nodes,Malaise,Blurred and Distorted Vision,Phlegm,Throat Irritation,Redness of Eyes,Sinus Pressure,Runny Nose,Congestion,Chest Pain,Weakness in Limbs,Fast Heart Rate,Pain During Bowel Movements,Pain in Anal Region,Bloody Stool,Irritation in Anus,Neck Pain,Dizziness,Cramps,Bruising,Obesity,Swollen Legs,Swollen Blood Vessels,Puffy Face,Enlarged Thyroid,Brittle Nails,Swollen Extremeties,Excessive Hunger,Extra-Marital Contacts,Dying Lipds,Slurred Speech,Knee Pain,Hip-Joint Pain,Muscle Weakness,Stiff Neck,Swelling Joints,Movement  Stiffness,Spinning movements,Loss Of Balance,Unsteadiness,Body Weakness,Loss of Smell,Bladder Discomfort,Foul Smell of Urine,Continuous Feel of Urine,Passage Of Gases,Internal itching,Toxic Look,Depression,Irritability,Muscle Pain,Altered Sensorium,Red Spots Over Body,Belly Pain,Abnormal Menstruation,Dischromic Patches,Watering from Eyes,Increased Appetite,Polyuria,Family History,Mucoid Sputum,Rusty Sputum,Lack of Concentration,Visual Disturbances,Receiving Blood Transfusion,Reciving unsterile innjections,Coma,Stomach Bleeding,Distention Of Abdomen,Alcohol addiction,Fuild Overload,Blood in Sputum,Prominent Veins on Calf,Palpitations,Painful Walking,Pimples,Blackheads,Scurring,Skin Peeling,Silver like Dusting,Small Dents in Nails,Inflammatory Nails,Blister,Red Sore around Nose,Yellow Crust Ooze"
a = a.lower()
symptom_list = a.split(",")


def clean_sen(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    l = ["itching", "skin rash", "nodal skin eruptions", "continuous sneezing", "shivering", "chills", "joint pain", "stomach pain", "acidity", "ulcers on tongue", "muscle wasting", "vomiting", "burning urination", "spotting urination", "fatigue", "weight gain", "anxiety", "cold hands and feets", "mood swings", "weight loss", "restlessness", "lethargy", "pain in throat", "irregular sugar level", "cough", "high fever", "sunken eyes", "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish skin", "dark urine", "nausea", "loss of appetite", "pain behind the eyes", "back pain", "constipation", "abdominal pain", "diarrhoea", "mild fever", "yellow urine", "yellowing of eyes", "liver failure", "fluid overload", "swelling of stomach", "swelled lymph nodes", "malaise", "blurred and distorted vision", "phlegm", "throat irritation", "redness of eyes", "sinus pressure", "runny nose", "congestion", "chest pain", "weakness in limbs", "fast heart rate", "pain during bowel movements", "pain in anal region", "bloody stool", "irritation in anus", "neck pain", "dizziness", "cramps", "bruising", "obesity", "swollen legs", "swollen blood vessels", "puffy face", "enlarged thyroid", "brittle nails", "swollen extremeties", "excessive hunger", "extra-marital contacts", "dying lipds", "slurred speech", "knee pain", "hip-joint pain", "muscle weakness", "stiff neck", "swelling joints", "movement stiffness", "spinning movements", "loss of balance", "unsteadiness", "body weakness", "loss of smell", "bladder discomfort", "foul smell of urine", "continuous feel of urine", "passage of gases", "internal itching", "toxic look", "depression", "irritability", "muscle pain", "altered sensorium", "red spots over body", "belly pain", "abnormal menstruation", "dischromic patches", "watering from eyes", "increased appetite", "polyuria", "family history", "mucoid sputum", "rusty sputum", "lack of concentration", "visual disturbances", "receiving blood transfusion", "reciving unsterile innjections", "coma", "stomach bleeding", "distention of abdomen", "alcohol addiction", "fuild overload", "blood in sputum", "prominent veins on calf", "palpitations", "painful walking", "pimples", "blackheads", "scurring", "skin peeling", "silver like dusting", "small dents in nails", "inflammatory nails", "blister", "red sore around nose", "yellow crust ooze"]
    
    sentence_words = [lematizer.lemmatize(word) for word in sentence_words]
    for i in l:
        if i in sentence:
            lp.append(i)
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_sen(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)



def pre_cls(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r> ERROR_THRESHOLD]
    results.sort(key = lambda x:x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1]) })
    return return_list



def pre_dep(n12):
    a = pd.read_csv("Nrm_1/test.csv")
    b = pd.read_csv("Nrm_1/updated test.emt_1 copy.csv")
    x=[]
    for i in n12:
        #
        x.append(b[i][1])
    for i in x:
        a[i][0]=1
    prediction=dep_model.predict(a)[0]
    snakes = pd.read_csv("Nrm_1/Snakes_fin.csv")
    output = snakes.iloc[prediction][1]
    print("++++++"+"it seems you have to consult a",output)

def get_res(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def nn_extrct(text):
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(tagged_tokens)

    for i in named_entities:
        if i[1] == 'NN':
            nn_l.append(i[0])



def bm_fuz():
    for i in nn_l:
        best_match, score = process.extractOne(i.lower(), symptom_list, scorer=fuzz.ratio)
        bm_l.append(best_match)
        if score >= 60: 
            bm_l.append(best_match)
    # print("BM")
    # print(bm_l)
    


print("Bot is Running")


while True:
    message = input('You: ')
    ints = pre_cls(message)
    if ints[0]['intent'] == 'symptoms':
        nn_extrct(message)

    res = get_res(ints, intents)

    # print(lp)
    # print(nn_l)

    print(f'Bot: {res}')

    if ints[0]['intent'] == 'exit':
        bm_fuz()
        lp_bm = lp+bm_l
        lp_bm = set(lp_bm)
        lp_bm = list(lp_bm)
        # print(lp_bm)
        pre_dep(lp_bm)
        break

