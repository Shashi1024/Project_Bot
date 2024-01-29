import json

a = "Itching,Skin Rash,Nodal Skin Eruptions,Continuous Sneezing,Shivering,Chills,Joint Pain,Stomach Pain,Acidity,Ulcers On Tongue,Muscle Wasting,Vomiting,Burning Urination,Spotting Urination,Fatigue,Weight Gain,Anxiety,Cold Hands And Feets,Mood Swings,Weight Loss,Restlessness,Lethargy,Pain In Throat,Irregular Sugar Level,Cough,High Fever,Sunken Eyes,Breathlessness,Sweating,Dehydration,Indigestion,Headache,Yellowish Skin,Dark Urine,Nausea,Loss of Appetite,Pain behind the Eyes,Back Pain,Constipation,Abdominal Pain,Diarrhoea,Mild Fever,Yellow Urine,Yellowing of Eyes,Liver Failure,Fluid Overload,Swelling Of Stomach,Swelled Lymph Nodes,Malaise,Blurred and Distorted Vision,Phlegm,Throat Irritation,Redness of Eyes,Sinus Pressure,Runny Nose,Congestion,Chest Pain,Weakness in Limbs,Fast Heart Rate,Pain During Bowel Movements,Pain in Anal Region,Bloody Stool,Irritation in Anus,Neck Pain,Dizziness,Cramps,Bruising,Obesity,Swollen Legs,Swollen Blood Vessels,Puffy Face,Enlarged Thyroid,Brittle Nails,Swollen Extremeties,Excessive Hunger,Extra-Marital Contacts,Dying Lipds,Slurred Speech,Knee Pain,Hip-Joint Pain,Muscle Weakness,Stiff Neck,Swelling Joints,Movement  Stiffness,Spinning movements,Loss Of Balance,Unsteadiness,Body Weakness,Loss of Smell,Bladder Discomfort,Foul Smell of Urine,Continuous Feel of Urine,Passage Of Gases,Internal itching,Toxic Look,Depression,Irritability,Muscle Pain,Altered Sensorium,Red Spots Over Body,Belly Pain,Abnormal Menstruation,Dischromic Patches,Watering from Eyes,Increased Appetite,Polyuria,Family History,Mucoid Sputum,Rusty Sputum,Lack of Concentration,Visual Disturbances,Receiving Blood Transfusion,Reciving unsterile innjections,Coma,Stomach Bleeding,Distention Of Abdomen,Alcohol addiction,Fuild Overload,Blood in Sputum,Prominent Veins on Calf,Palpitations,Painful Walking,Pimples,Blackheads,Scurring,Skin Peeling,Silver like Dusting,Small Dents in Nails,Inflammatory Nails,Blister,Red Sore around Nose,Yellow Crust Ooze"
x = "itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_ urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look_(typhos),depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic _patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooz"
a = a.lower()
b = a.split(",")
y = x.split(",")

n = []

# for i in range(len(y)):
#     n.append({"tag": y[i] , "patterns": [y[i]], "responses": [""]})

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

user_input = "I have a stomachache."
symptom_list = b




# while True:
#     user_input = input("You: ")
#     symptom_list = b
#     # for symptom in symptom_list:
#     #     ratio = fuzz.ratio(user_input.lower(), symptom.lower())
#     #     if ratio >= 20:  # Adjust threshold as needed
#     #         print(f"Possible symptom match: {symptom} (Ratio: {ratio})")
#     best_match, score = process.extractOne(user_input.lower(), symptom_list, scorer=fuzz.ratio)
#     if score >= 60:  # Adjust threshold as needed
#         print(f"Best symptom match: {best_match} (Ratio: {score})")
#     else:
#         print("No close enough symptom matches found.")




import nltk

# while True:
#     text = input("You: ")
#     tokens = nltk.word_tokenize(text)
#     tagged_tokens = nltk.pos_tag(tokens)
#     named_entities = nltk.ne_chunk(tagged_tokens)

#     for i in named_entities:
#         if i[1] == 'NN':
#             print(i[0])

# for entity in named_entities.subtrees(filter=lambda t: t.label() == 'NE'):
#     print(entity)
#     print(f"Entity: {''.join([c[0] for c in entity.leaves()])}")

    


import spacy

nlp = spacy.blank("en")

doc = nlp("Hello world!")

for token in doc:
    print(token.text)


nlp = spacy.load("en_core_web_sm")  # Load model with medical NER capabilities


symptoms = []
user_input = "he is having head ache"
#content = "Trinamool Congress leader Mahua Moitra has moved the Supreme Court against her expulsion from the Lok Sabha over the cash-for-query allegations against her. Moitra was ousted from the Parliament last week after the Ethics Committee of the Lok Sabha found her guilty of jeopardising national security by sharing her parliamentary portal's login credentials with businessman Darshan Hiranandani."
content = "he has fever"
doc1 = nlp(content)
for ent in doc1.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print("@@@@@@@@@@@@@")
for token in doc1:
    print(token.text, "-", token.pos_, '-', token.dep_,'_', spacy.explain(token.dep_))

from spacy import displacy
displacy.render(doc1, style="ent")



text = "he is having head ache"
tokens = nltk.word_tokenize(text)
tagged_tokens = nltk.pos_tag(tokens)
named_entities = nltk.ne_chunk(tagged_tokens)

# for token in named_entities:
#     print(token.text, "-", token.pos_, '-', token.dep_)
    


# from spacy.lang.en.examples import sentences 

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(sentences[0])
# print(sentences)
# print(doc.text)
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

# print("===========================================================")
# import medspacy
# from medspacy.ner import TargetRule

# nlp1 = medspacy.load()
# print(nlp1.pipe_names)

# nlp1.get_pipe('medspacy_target_matcher').add([TargetRule('stroke pain', 'CONDITION'), TargetRule('diabetes', 'CONDITION'), TargetRule('pna', 'CONDITION')])
# doc2 = nlp1('he is having fever')

# for ent in doc2.ents:
#     print(ent, ent._.is_negated, ent._.is_family, ent._.is_historical)


