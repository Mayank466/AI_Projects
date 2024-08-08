import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hello! What can I do for you?"],
            "product_info": ["We have a variety of products including electronics, clothing, and books. What are you interested in?",
                              "Our product range includes electronics, clothing, and books. Do you have any specific product in mind?",
                                "We offer electronics, clothing, and books. Can I help you with any specific category?"],
            "hours": ["Our store is open from 9 AM to 9 PM from Monday to Saturday.", 
                      "We are open from 9 AM to 9 PM, Monday through Saturday.", 
                      "Our working hours are 9 AM to 9 PM, Monday to Saturday."],
            "bye": ["Goodbye! Have a great day!", "Bye! Take care!", "Goodbye! Feel free to reach out if you need anything else!"],
            "default": ["I'm sorry, I don't understand. Can you please rephrase?", 
                        "I didn't catch that. Can you please clarify?", "I'm not sure I understand. Could you elaborate?"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.responses["greeting"])
        elif "product" in user_input or "products" in user_input:
            return random.choice(self.responses["product_info"])
        elif "hours" in user_input or "time" in user_input:
            return random.choice(self.responses["hours"])
        elif "bye" in user_input or "goodbye" in user_input:
            return random.choice(self.responses["bye"])
        else:
            return random.choice(self.responses["default"])

def main():
    bot = Chatbot()
    print("Customer Service Chatbot\nType 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Bot:", bot.get_response(user_input))
            break
        else:
            print("Bot:", bot.get_response(user_input))

if __name__ == "__main__":
    main()
