import streamlit as st


with st.sidebar:
    st.image("https://github.com/Justinfungi/Justinfungi/blob/c6614b817be1b28467cd83f065661723a986bea7/METAVERSE.jpg")
    st.title("AutoStreamML")
    choice = st.radio("Nav",["upload","Profiling","ML","Download"])

st.write("Im Javis")
