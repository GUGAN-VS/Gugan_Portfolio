import streamlit as st
from forms.contact import contact_form

@st.dialog("Contect Me")
def show_contact_form():
    contact_form()

col1,col2=st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("assets/my_profil.png",width=230)
with col2:
    st.title("GUGAN VS",anchor=False)
    st.markdown("#### :material/database: Data Engineer")
    if st.button(":material/contact_page: Contact Me"):
        show_contact_form()

st.write("\n")
st.write(
    """
    :material/star: I’m an **adaptive and passionate Data Engineer & Web Developer** from Coimbatore, India.  
    :material/star: I have expertise in **Django, Flask, Python, Azure Data Factory,and PySpark, Power BI**.  
    :material/star: I focus on building **scalable data solutions** and **intelligent applications** to solve real-world problems.  
    """
)

st.write("\n")
st.subheader("🚀 What I Do")  
st.markdown(
    """
    - 🏗 **Data Engineering** – Building efficient ETL pipelines with **Azure Data Factory & PySpark**  
    - 🌐 **Web Development** – Developing **secure & scalable** applications with **Django & Flask**  
    - 📊 **Business Intelligence** – Creating insights with **Power BI & Machine Learning**  
    - 🤖 **AI Integration** – Implementing AI models in **chatbots & data analytics**  
    """
)

