import streamlit as st
from src.review_page1 import sa_questions
from src.transcript_page2 import generate_transcript_questions
from src.review_page1 import sa_questions
from src.reading_page3 import generate_reading_questions
from src.islr_long_form_questions_page5 import generate_open_questions
from src. image_questions_page4 import generate_image_questions

def intro():
    import streamlit as st

    st.write("# Welcome to the MGT 6203 Midterm Prep App! 👋")
    st.sidebar.success("Choose a practice category to begin.")

    st.markdown("""
Streamlit powers this interactive test aid designed to support Georgia Tech’s MGT 6203 students in their midterm exam preparation. Dive into a variety of question types encompassing weeks 1-8 of your course content, including:

1. **Review Questions**: Revisit self-assessment, homework, and knowledge check questions.
2. **Additional MPC Questions**: Tackle multiple-choice questions crafted by GPT-4, based on lecture transcripts.
3. **Reading MPC Questions**: Engage with multiple-choice questions generated from ISLR (chapters 2, 3, 4) and additional readings.
4. **Open-ended Questions**: Explore deeper thought questions inspired by ISLR and lectures.
5. **Chart & Statistical Analysis**: Test your skills in interpreting charts, graphs, and statistical summaries.

Get started by selecting a demo from the dropdown on the left and elevate your exam preparation to the next level.
    """)


def review_questions():
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write('self assessment and knowledge check questions')
    sa_questions()


def reading_questions():
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write('multiple choice questions based on the readings')
    generate_reading_questions()

def transcript_questions():
    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write('multiple choice questions based on lecture transcripts')
    generate_transcript_questions()


def open_ended_questions():
    import streamlit as st
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    st.write('Open ended Questions')
    generate_open_questions()

def chart_questions():
    import streamlit as st
    st.markdown(f"# {list(page_names_to_funcs.keys())[5]}")
    st.write('Chart & Graph Intepretation')
    generate_image_questions()

def reset_or_initialize_state():
    if 'token' in st.session_state:
        del st.session_state['token']

page_names_to_funcs = {
    "—": intro,
    "SA & KC": review_questions,
    "Course Readings": reading_questions,
    "Lecture Videos": transcript_questions,
    "Open Ended": generate_open_questions,
    "Charts & Code": generate_image_questions
}

if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

# Sidebar selection box
demo_name = st.sidebar.selectbox("Choose Practice Type", list(page_names_to_funcs.keys()))

# Check if the demo has changed
if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name  # Update the current demo
    reset_or_initialize_state()  # Reset or initialize state based on new demo

# Dynamically call the selected demo function
if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()
