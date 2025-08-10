def chatbot():
    print("Hello! I'm your friendly chatbot.")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input.lower():
            print("Chatbot: Hi there!")
        elif 'how are you' in user_input.lower():
            print("Chatbot: I'm just a program, but I'm functioning well!")
        elif 'name' in user_input.lower():
            print("Chatbot: I'm ChatBot 1.0")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()
