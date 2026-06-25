import streamlit as st
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

def generate_test_cases(requirement):
    prompt = f"""
    You are a Senior QA Engineer.
    Generate test cases in Markdown table format with columns:
    | Test Case ID | Test Type | Test Scenario | Steps | Expected Result | Severity | Priority |
    Requirement: {requirement}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

st.title("AI Test Case Generator")
req = st.text_area("Enter Requirement:", "Login must validate username and password.")
if st.button("Generate"):
    st.markdown(generate_test_cases(req))
