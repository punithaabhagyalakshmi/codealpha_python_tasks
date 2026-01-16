#Basic_Chatbot
def chatbot(user):

    if user=="hello" or user=="hi":
        print("Hi! How can I help you?")
    elif user=="how are you":
        print("I'm doing great!")
    elif user=="bye":
        print("Goodbye! Have a great day")
        return False
    return True
start=True
while start:
    user=input("Ask chatbot: ").lower()
    start=chatbot(user)