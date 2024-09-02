# Student Placement Prediction

This project is a web application that predicts whether a student will get placement based on their CGPA and IQ using a machine learning model. The application is built using Streamlit, a Python library for creating interactive web apps, and is deployed on Streamlit Cloud.

## Features

- User-friendly interface for inputting student details.
- Real-time prediction of placement based on trained logistic regression model.
- Simple deployment and easy to use.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python and pip installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/placement-prediction.git
    cd placement-prediction
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app locally:

    ```bash
    streamlit run app.py
    ```

### Deployment

This app can be deployed directly on Streamlit Cloud. Follow the steps below to deploy:

1. Push your code to a GitHub repository.

2. Ensure you have the following files in your repository:
    - `app.py`
    - `placement_model.pkl`
    - `requirements.txt`

3. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in with your GitHub account.

4. Click on "New app" and connect your GitHub repository.

5. Select the repository and branch containing your `app.py` file and click "Deploy".

## Usage

1. Open the app in your browser.

2. Enter the CGPA and IQ of the student.

3. Click the "Predict Placement" button.

4. The app will display whether the student is likely to be placed or not.

## Files

- `app.py`: The main script containing the Streamlit application code.
- `placement_model.pkl`: The pre-trained logistic regression model.
- `requirements.txt`: A file listing the dependencies needed to run the app.

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
