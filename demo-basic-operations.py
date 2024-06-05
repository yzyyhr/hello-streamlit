
import streamlit as st
st.title('Hello World!')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.markdown('this is an image: ![Alt Text](https://tse1-mm.cn.bing.net/th/id/OIP-C.Rmu2HNfPTot9nN9kWt0dbgHaNK?w=106&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7)')


if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status=st.radio("select gender:",
                ("Male",
                 "Female"))
if status == "Male":
    st.success("Male")
else:
    st.success("Female")

hobbies=st.multiselect("Hobbies:",
               ['Reading','Writing','Coding','Traveling'])
st.write("You selected:",hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")
     
name = st.text_input("Enter Your Name:")
if st.button("Submit"):
    st.write("Hello,",name)
level = st.slider("select your lecel",1,5)
st.write("your selected:",level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",tupe=['jpg','png'])
if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256),
            caption="Uploaded Image")


























