import streamlit as st

st.title("💙 datto-san's Practice Playground 👾")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). If not, then [watch this video](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for more information."
)

if "show_dialog" not in st.session_state:
    st.session_state.show_dialog = False
    
@st.dialog("Test Pop-Up Message")
def show_popup():
    st.write("Hello from the popup frame!")
    
    if st.button("Close"):
        st.session_state.show_dialog = False
        st.rerun()

    st.button("AMORGOS 📮, GREECE 🇬🇷")

if st.button("Say hi to the datCoolPro"):
    st.session_state.show_dialog = True

if st.session_state.show_dialog:
    show_popup()

st.write(
    "[Support Me](https://ko-fi.com/datcoolpro101)"
)
