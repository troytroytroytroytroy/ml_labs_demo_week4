import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("Week 4: The Airbnb dataset of Amsterdam")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)

st.text("This widget can be used by hosts to check their expected tips per listing.")

# review_scores_rating: 0 to 5
review_scores_rating = st.slider('What rating is this listing?', 0.00, 5.00, 4.50)
# room_type: ['Shared room', 'Private room', 'Hotel room', 'Entire home/apt']
room_type = st.radio(
    "What room type do you have?",
    ('Shared room', 'Private room', 'Hotel room', 'Entire home/apt'))
# service_cost: ['$0.99', '$4.99', '$2.99', '$10.99']
service_cost = st.radio(
    "What room type do you have?",
    ('$0.99', '$4.99', '$2.99', '$10.99'))
# instant_bookable: 0, 1
instant_bookable = st.radio(
    "Is the listing instantly bookable?",
    ("True", "False"))
instant_bookable = 1 if instant_bookable == "True" else 0

example = pd.DataFrame({
    "review_scores_rating": [review_scores_rating],
    "room_type": [room_type],
    "service_cost": [service_cost],
    "instant_bookable": [instant_bookable]
    })

if st.button('Predict?'):
    st.write("The model predicts that the tipping category for this listing is:", model.predict(example)[0])
