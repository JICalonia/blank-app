import streamlit as st

st.title("💙 datto-san's Practice Playground 👾")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). If not, then [watch this video](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for more information."
)

@st.dialog("Welcome")
def show_popup():
    st.write("Hello from the popup frame!")
    st.button("Close")

if st.button("Say hi to the datCoolPro"):
    show_popup()

st.write(
    "[Support Me](https://ko-fi.com/datcoolpro101)"
)
