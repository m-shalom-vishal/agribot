import streamlit as st
import requests

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

st.title("Agriculture Chatbot")
st.write("Ask me anything about farming, crops, or agriculture!")

user_input = st.text_input("Enter your question:")

if user_input:
    st.subheader("Google Search Results:")
    st.markdown(google_search(user_input))
