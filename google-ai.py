import google.generativeai as genai
import os

genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat = model.start_chat(history=[])

print("Buddy Chatbot (Type 'exit' to quit) \n")
print("Welcome, how can I help you buddy? \n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"Buddy Chatbot: {response.text}")
