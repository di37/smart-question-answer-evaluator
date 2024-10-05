import google.generativeai as genai
from utilities.constants import GEMINI_API_KEY, MODEL_NAME

# Configure the Gemini API (you'll need to replace this with your actual API key)
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model
model = genai.GenerativeModel(MODEL_NAME)


def evaluate_answer(question, correct_answer, user_answer):
    evaluate_answer_prompt = f"""
    Question: {question}
    Model Answer: {correct_answer}
    User's Answer: {user_answer}

    Please evaluate the user's answer compared to the model answer. Keep in mind that the user's answer doesn't need to match the model answer word-for-word, but should demonstrate understanding of the key concepts. Provide feedback and a rating based on the following scale:
    - Excellent (Demonstrates thorough understanding and covers all key points)
    - Very Good (Shows good understanding and covers most key points)
    - Good (Demonstrates basic understanding but may miss some important aspects)
    - Needs Improvement (Shows some understanding but misses several key points or contains inaccuracies)
    - Poor (Demonstrates little understanding of the topic or contains major inaccuracies)

    Give a brief explanation for your rating, highlighting what was correct and what could be improved. Be encouraging and constructive in your feedback.
    """

    return model.generate_content(evaluate_answer_prompt, stream=True)
