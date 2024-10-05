import streamlit as st
import random

from utilities import evaluate_answer, load_qa_pairs


def main():
    st.title("In-Depth Question Answering Evaluation App")

    # Display prettier ratings information in sidebar
    st.sidebar.markdown("### Ratings Information")
    st.sidebar.markdown(
        """
        <style>
            .rating-box {
                border: 1px solid #4CAF50;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 10px;
            }
            .rating-item {
                margin: 5px 0;
                padding: 5px;
                border-radius: 3px;
            }
            .excellent {background-color: #4CAF50; color: white;}
            .very-good {background-color: #8BC34A; color: white;}
            .good {background-color: #CDDC39; color: black;}
            .needs-improvement {background-color: #FFEB3B; color: black;}
            .poor {background-color: #FF9800; color: white;}
        </style>
        <div class="rating-box">
            <div class="rating-item excellent">5 - Excellent</div>
            <div class="rating-item very-good">4 - Very Good</div>
            <div class="rating-item good">3 - Good</div>
            <div class="rating-item needs-improvement">2 - Needs Improvement</div>
            <div class="rating-item poor">1 - Poor</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for file upload
    st.sidebar.title("Upload QA Pairs")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        qa_pairs = load_qa_pairs(uploaded_file)
        st.sidebar.success("File uploaded successfully!")

        # Initialize session state for tracking the current question
        if "current_qa" not in st.session_state or st.session_state.get(
            "file_changed", False
        ):
            st.session_state.current_qa = random.choice(qa_pairs)
            st.session_state.file_changed = False

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
            st.session_state.current_qa = random.choice(qa_pairs)
            st.rerun()
    else:
        st.info(
            "Please upload a CSV file containing questions and answers using the sidebar on the right."
        )


if __name__ == "__main__":
    main()
