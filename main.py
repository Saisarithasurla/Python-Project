from speech_module import listen_command
from tts_module import speak
from wikipedia_module import search_wikipedia
from weather_module import get_weather
from music_module import play_youtube
from jokes_module import tell_joke
from datetime_module import get_time, get_date
from calculator_module import calculate
from fun_module import guess_number, rock_paper_scissors, roll_dice, coin_toss
from quotes_module import get_quote



def main():
    speak("Hello I am your assistant. How can I help you today?")

    while True:
        command = listen_command()
        command=command.lower()

        if "wikipedia" in command:
            # Remove the trigger word 'wikipedia' and normalize the query
            query = command.lower().replace("wikipedia", "").strip()

            if query == "":
                speak("Please tell me what you want me to search on Wikipedia.")
            else:
                # Capitalize each word to improve Wikipedia matching
                query = " ".join(word.capitalize() for word in query.split())

                # Fetch summary from Wikipedia
                result = search_wikipedia(query)
                speak(result)


        elif "weather" in command:
            city = command.replace("weather in", "").replace("weather", "").strip()
            result = get_weather(city)
            speak(result)
        elif "joke" in command:
            speak(tell_joke())
        elif "time" in command:
            speak(get_time())

        elif "date" in command:
            speak(get_date())
        elif "quote" in command or "motivation" in command or "inspire" in command:
            quote = get_quote()
            speak("Here’s a quote for you.")
            speak(quote)
        elif "calculate" in command:
            expression = command.replace("calculate", "").strip()
            expression = expression.replace("plus", "+").replace("minus", "-")
            expression = expression.replace("times", "*").replace("multiplied by", "*")
            expression = expression.replace("divided by", "/")

            if expression == "":
                speak("Please tell me what to calculate.")
            else:
                result = calculate(expression)
                speak(f"The result is {result}")
        elif "play game" in command:
            speak(
                "Which game would you like to play? Guess the Number, Rock Paper Scissors, Dice Roll or Coin Toss?")
            game_choice = listen_command().lower()

            if "guess" in game_choice:
                messages = guess_number()
            elif "rock" in game_choice or "scissors" in game_choice:
                messages = rock_paper_scissors()
            elif "dice" in game_choice:
                messages = roll_dice()
            elif "coin" in game_choice:
                messages = coin_toss()
            else:
                messages = ["Sorry, I didn't understand that game choice."]

            for msg in messages:
                speak(msg)
        elif "play" in command:
            video = command.replace("play", "").strip()
            play_youtube(video)
            speak(f"Playing {video} on YouTube")

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye Saritha! Have a great day.")
            break

        elif command == "":
            speak("I didn’t hear anything. Please say again.")

        else:
            speak("Sorry, I didn’t understand that.")
