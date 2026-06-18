from openai import OpenAI
client=OpenAI(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def start_chatbot():
    messages = [{"role":"system","content":"you are a helper and assistant"}]
    print("Buddy Chatbot, Type 'quit' to exit")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit"]:
            break
        messages.append({"role":"user","content":user_input})
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = messages,
            temperature=0.7
        )
        assistant_reply=response.choices[0].message.content
        print(f"Buddy: {assistant_reply}")
        message.append({"role":"assistant","content":assistant_reply})

if __name__== "__main__":
    start_chatbot()
