def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "bye": "Goodbye! Have a nice day!",
        "how are you": "I'm just a bunch of code, but I'm doing well!",
        "Good Morning": "Good Morning!!!"
    }
    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    return "Sorry, I don't understand that."


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Chatbot:", chatbot_response(user_input))
