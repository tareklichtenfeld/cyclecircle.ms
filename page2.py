import streamlit as st
from datetime import time
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("find your groupride")
st.write("'find your groupride' ist eine interaktive Möglichkeit, deinen perfekten groupride in Münster und im Münsterland zu finden. Beantworte einfach ein paar Fragen zu dir und wie du am liebsten Fahrrad fährst, und wir finden gemeinsam die perfekte Gruppe für dich.")

st.markdown("")
st.markdown("")

st.header("Infos über dich")


eingabe1, eingabe2 = st.columns([6,4])
with eingabe1:
    #-----Helm-----------------------
    on = st.toggle("Ich fahre mit Helm")

    if on:
        st.write("perfekt, los gehts!")

    st.markdown("##")

    #-----speed--------------------------------------------------
    st.title("`Geschwindigkeit`")
    pace = st.slider("", 20, 40, (25, 32), label_visibility="hidden")
    lower_pace, higher_pace = pace
    st.write(f"Ich fahre in der Gruppe am liebsten eine Geschwindigkeit zwischen {lower_pace} und {higher_pace} km/h.")


    st.markdown("##")

    #-----Uhrzeit--------------------------
    st.title("`Uhrzeit`")
    time = st.slider(
        "", label_visibility="hidden", value=(time(11, 30), time(12, 45))
    )
    start_time, end_time=time
    st.write(f"Ich habe normalerweise an Wochentagen zwischen {start_time} und {end_time} Uhr Zeit für ne Ausfahrt.")

    st.markdown("##")

    #-----radius--------------------------------------------------
    st.title("`Startpunkt`")
    location_geopy= st.text_input("","Münster")

    geolocator = Nominatim(user_agent="cyclecircle_ms")
    location = geolocator.geocode(f"{location_geopy}")
    st.write(f"Ich starte meinen Weg zum Groupride in der Regel von {location.address}.")

    lat = location.latitude
    lon = location.longitude
    
    start_coords = (lat,lon)

    st.markdown("##")

    #-----Anfahrt---------------------------------------------------
    st.title("`Anfahrt`")
    radius = st.slider(
        "anfahrt", 0, 20, 3, label_visibility="hidden")
    st.write(f"Für ne richtig coole Runde wäre ich bereit maximal {radius} km anzureisen.")
    
    
    
    
    with st.expander("Welche Grouprides passen zu mir?"):
        st.write("Hier werden in Kürze die Ergebnisse der Auswahl einzusehen sein!")
    
    #distance = geopy.distance.geodesic().km)