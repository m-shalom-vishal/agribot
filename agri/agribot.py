import streamlit as st
import requests
import nltk
from textblob import TextBlob

nltk.download("punkt")

# Google Custom Search API credentials
GOOGLE_API_KEY = "AIzaSyBGKiSPD8Aj1TWm1OqE9Cpn0laxzE1n0O0"
SEARCH_ENGINE_ID = "57e4625115f494176"

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    data = response.json()
    
    if "items" in data:
        results = []
        for item in data["items"][:3]:  # Top 3 results
            results.append(f"[{item['title']}]({item['link']})")
        return "\n".join(results)
    return "No relevant information found."

def simple_nlp_response(user_input):
    user_input = user_input.lower()
    
    # Basic intent detection
    if "crop" in user_input or "best crop" in user_input:
        return "Choosing the best crop depends on soil type, climate, and water availability. Check the search results for more details."
    elif "fertilizer" in user_input:
        return "Fertilizer recommendations depend on the soil's nutrient content. It's best to get a soil test before applying fertilizers."
    elif "pest control" in user_input or "how to control pests" in user_input:
        return "Common pest control methods include biological control, organic pesticides, and crop rotation."
    else:
        return "I'm not sure, but check the search results for the most relevant information."

st.title("Agriculture Chatbot")
st.write("Ask me anything about farming, crops, or agriculture!")

user_input = st.text_input("Enter your question:")

if user_input:
    st.subheader("NLP-Based Answer:")
    st.write(simple_nlp_response(user_input))

    st.subheader("Google Search Results:")
    st.markdown(google_search(user_input))
