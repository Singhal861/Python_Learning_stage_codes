import requests
import json
import pyttsx3

# engine = pyttsx3.init()
#
# en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
# engine.setProperty('voice', en_voice_id)


def speak(str):
    from win32com.client import Dispatch
    spek = Dispatch("SAPI.SpVoice")
    spek.Speak(str)


if __name__ == '__main__':
    speak("Today's News")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=7a0c809e57884bfa895bc61a6420b347"
    r = requests.get(url).text
    r_dict = json.loads(r)
    rr = r_dict['articles']
    for count, txt in enumerate(rr):
        print(f"News {count} is {txt['title']}")
        speak(f"News {count} is {txt['title']}")

    print("Today's headlines are complete")
    speak("Today's headlines are complete")
