import os
import base64
import streamlit as st
import openai
from brain import notes_generator

# Constants
DEFAULT_LINK = "https://www.youtube.com/watch?v=ukzFI9rgwfU"
OPENAI_API_KEY = os.getenv("OPENAI_API")

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to set page background image
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_page_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;
        }}
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# STREAMLIT APP
st.set_page_config(
    page_title="insAIghts INTELLIGENCE",
    page_icon="assets/logo2.png",
    layout="wide"
)

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set page background
set_page_background("assets/background.webp")

# Sidebar
with st.sidebar:
    st.image("assets/logo2.png")
    st.caption("Get detailed notes from a YouTube video")
    st.info("""
        Please ensure that the chosen video includes English subtitles and has a duration of less than 20 minutes.
    """)
    default_bool = st.checkbox('Use Example Link', value=False)
    link = st.text_input('Paste the youTube link here', value=DEFAULT_LINK if default_bool else "", placeholder=DEFAULT_LINK)

# Main content
create_notes = st.sidebar.button("Create Notes")
home_page = st.empty()
expander_1 = st.empty()
expander_2 = st.empty()
expander_3 = st.empty()

home_page.write("""
    <h1>Welcome to ins<span style='color:#8C52FF';>AI</span>ghts INTELLIGENCE</h1>

    A powerful tool that allows you to extract detailed notes from YouTube videos effortlessly. Whether you're a student looking to summarize educational content or a professional seeking to capture key insights from a conference, this app has you covered. Below, you'll find essential information about how to use this tool effectively and learn more about its features.
""", unsafe_allow_html=True)

# Expanders
with expander_1.expander("Getting Started", expanded=False):
    st.write("""
        ### Input YouTube Video Link
        To begin, simply provide the link to the YouTube video for which you want to generate detailed notes. The video should ideally have English subtitles available. You can either enter the YouTube link directly or use the "Use Example Link" option to get started with a sample video.

        ### Generating Notes
        Once you've entered the YouTube link, click the "Create Notes" button. The app will then start the process of extracting notes from the video. This might take a moment, so please be patient. You'll be notified once the notes are ready for review.
    """)

with expander_2.expander("Features", expanded=False):
    st.write("""
        ### Fast and Efficient
        The insAIghts INTELLIGENCE uses advanced natural language processing to quickly and efficiently extract relevant information from the video's subtitles. It saves you valuable time that you would otherwise spend manually transcribing and summarizing the content.

        ### Versatile Use Cases
        This tool can be used for a wide range of purposes, including:

        - Taking notes during educational lectures or tutorials.
        - Summarizing key points from online seminars and webinars.
        - Capturing insights from conference presentations.
        - Creating study materials for exams or assignments.
        - Preparing briefings or reports based on video content.

        ### User-Friendly Interface
        The Streamlit-based interface is designed to be user-friendly and intuitive. You can easily navigate through the app, making it accessible for users with various levels of technical expertise.
    """)

with expander_3.expander("About Us", expanded=False):
    st.write("""
        ## About Us
        This app was developed by [Arpit Sengar](https://github.com/arpy8), who is passionate about simplifying the process of extracting valuable information from online videos. If you have any questions, feedback, or feature requests, please don't hesitate to reach out.

        We hope you find insAIghts INTELLIGENCE a valuable addition to your toolkit for efficient knowledge extraction from YouTube videos.

        Thank you for using our app!
    """)

if create_notes and link:
    home_page.empty()

    expander_1.empty()
    expander_2.empty()
    expander_3.empty()

    response = notes_generator(link)

    st.balloons()
    st.write(response)
    st.toast("Notes generated successfully!")
