import streamlit as st


st.set_page_config(page_title="cyclecircle.ms", layout="wide",
                   page_icon=":material/directions_bike:")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.header('cyclecircle.ms')
st.logo("cyclecircle_logo_big.png")

#-----SIDEBAAARRR----------------------------------------------------------
st.sidebar.header('cyclecircle.ms')

page1 = st.Page("page1.py", title="Übersicht", icon=":material/overview_key:")
page2 = st.Page("page2.py", title="find your groupride", icon=":material/directions_bike:")
page3 = st.Page("page3.py", title="Über cyclecircle.ms", icon=":material/info:")
page4 = st.Page("page4.py", title="Q&A", icon=":material/contact_support:")
page5 = st.Page("page5.py", title="Kontakt", icon=":material/alternate_email:")

pages = {
        "For you :D": [page1, page2],
        "Infos": [page3, page4, page5],
        }
pg = st.navigation(pages)
pg.run()