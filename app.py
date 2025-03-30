# AI Recipe Generator using Gemini
from dotenv import load_dotenv
load_dotenv()  # Load all environment variables from .env

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to get Gemini's response for recipe generation
def get_gemini_response(ingredients):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are an expert chef who loves creating delicious and creative recipes. 
    Suggest a unique recipe based on the following ingredients:
    {ingredients}

    Please provide:
    1. Recipe Name
    2. Ingredients Required
    3. Step-by-Step Cooking Instructions
    4. Estimated Cooking Time
    """
    response = model.generate_content(prompt)
    return response.text

# Initialize Streamlit App
st.set_page_config(page_title="AI Recipe Generator")
st.header("🍲 AI Recipe Generator")
st.write("Enter ingredients you have, and I'll suggest a delicious recipe!")

# Input for ingredients
ingredients = st.text_area("Enter Ingredients (comma-separated):", key="ingredients")

# Submit button to generate a recipe
submit = st.button("Generate Recipe")

# If submit button is clicked
if submit:
    if ingredients:
        response = get_gemini_response(ingredients)
        st.subheader("Here's Your Recipe! 🍴")
        st.write(response)
    else:
        st.warning("⚠️ Please enter some ingredients to generate a recipe.")
