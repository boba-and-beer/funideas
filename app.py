import streamlit as st

st.title('J & A Random Idea Generator')

DATES = """Play your favorite board games
Play strip Twister (or Monopoly) or any game you like
Build a blanket fort
At home stargazing
Paint together
Put together a craft
Have a DIY spa and pamper yourselves
Write down your bucket list
Ask each other deep questions
Learn a new skill from YouTube"""

DATES = DATES.split('\n')
DATES += [
	"Bali trip",
	"Japan trip",
	"Perth trip",
	"melbourne trip",

]

import random

if st.button("press here for random date idea"):
	RANDOM_DATE = random.choice(DATES)
	st.title(RANDOM_DATE)

