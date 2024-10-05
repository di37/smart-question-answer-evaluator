# In-Depth Question Answering Evaluation App

This Streamlit application allows users to evaluate their answers to a series of pre-defined questions using natural language processing (NLP) techniques. The app provides immediate feedback on the correctness and quality of the answers, helping users improve their understanding and accuracy.

## Features

1. **Randomized Questions**: Each session starts with a randomly selected question from a predefined list.
2. **User Input**: Users can input their answers using a text area.
3. **Real-time Feedback**: As the user types, the app provides real-time feedback on the answer, highlighting strengths and areas for improvement.
4. **Model Answer Reference**: After submitting an answer, the app displays the correct model answer for reference.
5. **Next Question Button**: Users can move to the next question at any time.

## Installation

To run this application locally, you need to have Python installed on your machine. Follow these steps:

1. Clone the repository or download the code.
2. Create a conda environment and activate it:
   ```bash
   conda create -n ques_ans_eval python=3.12
   conda activate ques_ans_eval 
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application using the following command:
   ```bash
   streamlit run app.py
   ```
2. Open the provided URL in your web browser to access the app.

## Code Explanation

### Imports

```python
import streamlit as st
import random

from utilities import evaluate_answer
from utilities import QA_PAIRS
```

- **Streamlit**: A library used to create interactive web applications.
- **random**: Used to select a random question from the predefined list.
- **evaluate_answer** and **QA_PAIRS**: Functions and data from the `utilities` module, which handle the evaluation of answers and provide the list of question-answer pairs, respectively.

### Main Function

```python
def main():
    st.title("In-Depth Question Answering Evaluation App")
```

- Sets the title of the application.

#### Session State Initialization

```python
if "current_qa" not in st.session_state:
    st.session_state.current_qa = random.choice(QA_PAIRS)
```

- Initializes the session state to store the current question.

#### Display Current Question

```python
st.subheader("Question:")
st.write(st.session_state.current_qa["question"])
```

- Displays the current question.

#### User Input

```python
user_answer = st.text_area("Your answer:", height=200)
```

- Provides a text area for the user to input their answer.

#### Submit and Evaluate Button

```python
if st.button("Submit and Evaluate"):
    if user_answer:
        st.subheader("Feedback:")
        feedback_placeholder = st.empty()
        feedback_text = ""
```

- Handles the submission of the answer and provides real-time feedback.

#### Feedback Generation

```python
for chunk in evaluate_answer(
    st.session_state.current_qa["question"],
    st.session_state.current_qa["answer"],
    user_answer,
):
    feedback_text += chunk.text
    feedback_placeholder.markdown(feedback_text)
```

- Generates and updates the feedback in real-time.

#### Model Answer Reference

```python
st.subheader("Model Answer for Reference:")
st.write(st.session_state.current_qa["answer"])
```

- Displays the correct model answer for reference.

#### Next Question Button

```python
if st.button("Next Question"):
    st.session_state.current_qa = random.choice(QA_PAIRS)
    st.rerun()
```

- Allows the user to move to the next question and re-runs the app.

## Conclusion

The In-Depth Question Answering Evaluation App is a powerful tool for improving users' understanding and accuracy in answering questions. It combines real-time feedback with a randomized question set to provide a comprehensive learning experience. Whether you're a student, teacher, or anyone looking to enhance their NLP skills, this app is a valuable resource.