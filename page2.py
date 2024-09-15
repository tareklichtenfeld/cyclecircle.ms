import streamlit as st
from datetime import time

st.title("find your groupride")
st.write("'find your groupride' ist eine interaktive Möglichkeit, deinen perfekten groupride in Münster und im Münsterland zu finden. Beantworte einfach ein paar Fragen zu dir und wie du am liebsten Fahrrad fährst, und wir finden gemeinsam die perfekte Gruppe für dich.")

st.markdown("")
st.markdown("")

st.header("Infos über dich")

pace = st.slider("Geschwindigkeit", 20, 40, (25, 32))
lower_pace, higher_pace = pace
st.write(f"Ich fahre in der Gruppe gerne eine Geschwindigkeit zwischen {lower_pace} und {higher_pace} km/h.")

st.markdown("")
st.markdown("")
st.markdown("")


time = st.slider(
    "Uhrzeit", value=(time(11, 30), time(12, 45))
)

start_time, end_time=time

st.write(f"Ich habe normalerweise an Wochentagen zwischen {start_time} und {end_time} Uhr Zeit für ne Ausfahrt.")

