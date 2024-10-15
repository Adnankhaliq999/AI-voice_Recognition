# Assistant working with text input (no microphone or PyAudio)
#import speech_recognition as sr
#import pyttsx3
#import pywhatkit
#import datetime

def take_command():
    # Instead of listening via microphone, get input from user
    command = input("You: ")
    return command.lower()


# Function to print text response
def respond(text):
    print(f"Assistant: {text}")


# Main function where the assistant operates
def main():
    respond("Hello! I am your text-based assistant. How can I help you today?")
    while True:
        command = take_command()

        if 'stop' in command:
            respond("Goodbye! Have a great day!")
            break

        elif 'hello' in command:
            respond("Hello! How can I assist you today?")

        elif 'time' in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            respond(f"The current time is {current_time}.")

        elif 'date' in command:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            respond(f"Today's date is {current_date}.")

        elif 'your name' in command:
            respond("I am your virtual assistant. You can call me Assistant.")

        elif 'weather' in command:
            respond(
                "I can't check the weather right now, but you can check it on your phone or computer!"
            )

        elif 'joke' in command:
            respond(
                "Why don't scientists trust atoms? Because they make up everything!"
            )

        elif 'help' in command:
            respond(
                "You can ask me about the time, date, my name, or tell me to tell a joke. I can also answer questions about programming languages, fun facts, and more!"
            )

        elif 'programming language' in command:
            respond(
                "There are many programming languages! Some popular ones include Python, JavaScript, Java, and C++."
            )

        elif 'python' in command:
            respond(
                "Python is a versatile and popular programming language known for its simplicity and readability."
            )

        elif 'java' in command:
            respond(
                "Java is a robust, object-oriented programming language widely used for building applications and software."
            )

        elif 'fun fact' in command:
            respond(
                "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"
            )

        elif 'capital of france' in command:
            respond("The capital of France is Paris.")

        elif 'math' in command:
            respond(
                "I can help you with math! Try asking me to solve simple calculations or math problems."
            )

        elif 'square root of 16' in command:
            respond("The square root of 16 is 4.")

        elif 'largest planet' in command:
            respond("The largest planet in our solar system is Jupiter.")

        elif 'smallest planet' in command:
            respond("The smallest planet in our solar system is Mercury.")

        elif 'sun' in command:
            respond(
                "The Sun is the star at the center of our solar system. It's about 4.6 billion years old."
            )

        else:
            respond(
                "I'm sorry, I didn't understand that. You can ask about the time, date, or even request a fun fact!"
            )


if __name__ == "__main__":
    main()
