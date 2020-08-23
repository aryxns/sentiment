from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd

analyser = SentimentIntensityAnalyzer()

st.header("superr sentiment analysis")

def query():
	if not stop:
		text = ui
		score = analyser.polarity_scores(text)
		df = pd.DataFrame([score])
		df = df.drop("compound", axis=1)
		st.bar_chart(df)
	else:
		exit()

ui = st.text_input("Enter a sentence to analyze: ") 
start = st.button('Analyze')
stop = st.button('Reset')
if start:
	query()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)