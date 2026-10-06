import streamlit as st

st.title("💙 datto-san's Practice Playground 👾")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). If not, then [watch this video](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for more information."
)

if "show_frame" not in st.session_state:
    st.session_state.show_frame = False

if st.button("Say hi to the datCoolPro"):
    st.session_state.show_frame = not st.session_state.show_frame

if st.session_state.show_frame:
    with st.container(border=True):
        st.subheader("Frame Layer")
        st.write("This frame is now open!")

st.write(
    "[Support Me](https://ko-fi.com/datcoolpro101)"
)
