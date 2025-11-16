#Simple rule based chatbot 
#Developed by:HARSHITA BANSAL

#function to get reply based on user input
def chatbot_reply(user_input):
    user_input =user_input.lower() #convert to loqer case for easy matching
    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm fine,thanks for asking!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry,I don't understand that."
    
    #main chatbot function
    def main():
     print ("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input=input("You:") #user_input
        response = chatbot_reply(user_input) #get chatbot reply
        print ("Chatbot:",response)
        if "bye" in user_input.lower():
         break   
    if __name__ == "__main__":
          main()
             