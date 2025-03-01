import streamlit as st

about = st.Page(
    page="views/aboutme.py",
    title="About",
    icon=":material/account_circle:",
    default=True,
)

qualification = st.Page(
    page="views/qualification.py",
    title=" Qualification",
    icon=":material/school:",
)

experience = st.Page(
    page="views/experience.py",
    title=" Experience",
    icon=":material/work:",
)

skills = st.Page(
    page="views/skills.py",
    title=" Skills",
    icon=":material/monitoring:",
)

p1=st.Page(
    page="views/project_1.py",
    title="Project 1",
    icon=":material/rocket_launch:",
)

p2=st.Page(
    page="views/project_2.py",
    title="Project 2",
    icon=":material/rocket_launch:",
)

p3=st.Page(
    page="views/project_3.py",
    title="Project 3",
    icon=":material/rocket_launch:",
)

pg=st.navigation(
    {
        "Info :" : [about,qualification,experience,skills],
        "Projects :" : [p1,p2,p3]
    }
)

st.logo("./assets/my_logo.png")
st.sidebar.text("Made with ❤️ by Gugan")

pg.run()

st.markdown(
    """
    <style>
        /* Hide the Streamlit top header bar */
        header[data-testid="stHeader"] {
            visibility: hidden;
            height: 0px;
        }

        /* Hide the specific icons (Share, Edit, GitHub) */
        .st-emotion-cache-zq5wmm {
            display: none !important;
        }
        
        /* Ensure sidebar headers remain visible */
        div[data-testid="stSidebarNav"] h2 {
            visibility: visible !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


