import streamlit as st
import numpy as np
import joblib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import webbrowser

# Load the trained model
model = joblib.load('placement_model.pkl')

# Streamlit UI
st.title('Student Placement Prediction')

st.header('Enter Student Details')

# Add a box with a button to take an IQ test on an external website
st.markdown("""
    **Take an IQ Test**  
    You can take an IQ test on our external platform, and your IQ score will automatically fill in the IQ field.
""")
if st.button('Take IQ Test'):
    webbrowser.open_new_tab('https://www.123test.com/iq-test/')  # Redirect to IQ test site

# Input field for IQ test ID
test_id = st.text_input('Enter IQ Test ID', '')

# Initialize iq_score in session state if it doesn't exist
if 'iq_score' not in st.session_state:
    st.session_state.iq_score = 0

from selenium.webdriver.chrome.options import Options

def fetch_iq_score(test_id):
    url = f"https://www.123test.com/iq-test/id={test_id}&version="
    driver = None  # Initialize driver variable

    try:
        # Set up headless Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless
        chrome_options.add_argument("--no-sandbox")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        # Initialize WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)

        # Wait for page to load and locate the article with class "lopende-tekst"
        article = driver.find_element(By.CLASS_NAME, 'lopende-tekst')

        # Find the <p> tag containing the target text
        paragraphs = article.find_elements(By.TAG_NAME, 'p')

        # Loop through the paragraphs and search for the score
        iq_text = None  # Initialize iq_text
        for p in paragraphs:
            if "IQ score" in p.text:
                iq_text = p.text
                break

        # Check if iq_text was found before trying to extract the score
        if iq_text:
            iq_score = re.search(r'IQ score.*?(\d{1,3})', iq_text).group(1)
            iq_score = int(iq_score)
        else:
            raise ValueError("IQ score not found in the text.")

        return iq_score

    except Exception as e:
        st.error(f"Error fetching IQ score: {e}")
        return None

    finally:
        if driver:
            driver.quit()  # Ensure driver is quit if it was initialized

# Add an "Apply" button next to the Test ID input
if st.button('Apply'):
    if test_id:
        iq_score = fetch_iq_score(test_id)
        if iq_score:
            st.session_state.iq_score = iq_score  # Save the score in session state
            st.write(f"Your IQ score is: {iq_score}")
        else:
            st.write("Could not find IQ score, please check the test ID or the page structure.")
    else:
        st.warning("Please enter a valid Test ID.")

# Input fields for CGPA and IQ
cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input('IQ', min_value=0, max_value=300, step=1, value=st.session_state.iq_score)

# Predict placement when the button is clicked
if st.button('Predict Placement'):
    example = np.array([[cgpa, iq]])
    prediction = model.predict(example)
    result = 'Placed' if prediction[0] == 1 else 'Not Placed'
    st.write(f'The student is: **{result}**')
