import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

api_key = "AIzaSyAJ0zuUGLSTMn7i3Uc-9vaMy_ks8IZ53vU"
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
# print(
#     llm.invoke(
#         "What are some of the pros and cons of Python as a programming language?"
#     )
# )


st.title("🤔 What's TheWord For")
desc = st.text_area("Describe/define the word you are looking for: ")

if st.button("FIND THE WORD"):

    words = llm.invoke("You are a master linguist well-versed in all the dictionaries in existence. I have forgotten a word and can't quite recall it - but I can give you a broad description for it. I want you to return me all the words that you can find that relate to this description. I want you to sort them by relevance nd separte them by a comma and there should ne no white spaces in the response. here is the description for that word:"+desc+ " Just output the words in lowercase strings. No description or images. If there are no relevant words, return exactly the following words: 'Cannot find relevant words. Please specify your description.'")
    word_list = words.split(",")
    for word in word_list:
    # Trim any extra spaces from the word
        word = word.strip()
        if word!="Cannot find relevant words. Please specify your description.":  # Check if the word is not an empty string
            # Format the URL with the word
            dictionary_url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}?q={word}"
            # Create a Markdown link with the word as the hyperlink text
            st.markdown(f"[{word}]({dictionary_url})")

        else:
            st.write(word)
        