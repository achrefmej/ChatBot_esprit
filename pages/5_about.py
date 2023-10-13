# 5_about.py (modified)
import streamlit as st
import pymongo

def get_created_chatbots():
    client = pymongo.MongoClient("mongodb+srv://mejriachref:OaD8s53tTudShBBq@cluster0.g5ttgqk.mongodb.net/?retryWrites=true&w=majority")
    db = client["chatbotesprit"]
    chatbots_collection = db["chatbots"]
    created_chatbots = chatbots_collection.find({}, {"_id": 0, "bot_name": 1})
    chatbot_names = [chatbot["bot_name"] for chatbot in created_chatbots]
    client.close()  # Close the connection after fetching data
    return chatbot_names

def about_page():
    st.title("About")
    st.write("This is the about page.")

    st.header("List of Created Chatbots")
    created_chatbots = get_created_chatbots()
    if created_chatbots:
        for i, bot_name in enumerate(created_chatbots):
            st.write(f"{i+1}. {bot_name}")
    else:
        st.write("No chatbots created yet.")

if __name__ == '__main__':
    about_page()
