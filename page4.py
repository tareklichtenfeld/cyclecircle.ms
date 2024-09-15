import streamlit as st

st.title("Questions & Answers")
st.markdown("##")

with st.expander("Ist cyclecircle.ms kostenlos?"):
    st.write("Ja, klar :D. Ich bin selbst Anfang 2024 zum ersten Mal in einer Gruppe gefahren und weiß, dass es am Anfang schwierig sein kann, die richtige Gruppe zu finden. Zum einen gibt es nirgends eine richtige Übersicht, weder auf Strava noch auch grouprides.cc, und zum anderen findet man dann auch selten gute Angaben zur gefahrenen Geschwindigkeit, was einschüchternd sein kann."
    )

with st.expander("Werden meine Daten gespeichert oder kann jemand sie einsehen?"):
    st.write("Nein, alles, was du auf dieser Seite eingibst, bleibt in deinem Browser. Diese App bietet dir lediglich die Möglichkeit, deinen Groupride zu finden, indem die hinterlegte Bibliothek mit Grouprides nach deinen Wünschen gefiltert wird. Eine Funktion zum Speichern der Daten ist nicht eingebaut."
    )

with st.expander("Die Seite funktioniert nicht. Was kann ich machen?"):
    st.write("Schreib mir gerne über 'Kontakt' eine Nachricht mit dem Problem. Ich versuche dann, das zu klären :)"
    )