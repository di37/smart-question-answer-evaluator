import streamlit as st
import random

from utilities import evaluate_answer
from utilities import QA_PAIRS

def main():
    st.title("In-Depth Question Answering Evaluation App")

    # Initialize session state for tracking the current question
    if "current_qa" not in st.session_state:
        st.session_state.current_qa = random.choice(QA_PAIRS)

    # Display the current question
    st.subheader("Question:")
    st.write(st.session_state.current_qa["question"])

    # Input for the user's answer
    user_answer = st.text_area("Your answer:", height=200)

    if st.button("Submit and Evaluate"):
        if user_answer:
            st.subheader("Feedback:")
            feedback_placeholder = st.empty()
            feedback_text = ""

            for chunk in evaluate_answer(
                st.session_state.current_qa["question"],
                st.session_state.current_qa["answer"],
                user_answer,
            ):
                feedback_text += chunk.text
                feedback_placeholder.markdown(feedback_text)

            # Display the model answer after evaluation
            st.subheader("Model Answer for Reference:")
            st.write(st.session_state.current_qa["answer"])
        else:
            st.warning("Please provide an answer.")

    if st.button("Next Question"):
        st.session_state.current_qa = random.choice(QA_PAIRS)
        st.rerun()


if __name__ == "__main__":
    main()
