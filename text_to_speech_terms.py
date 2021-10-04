# # # # Python program to convert
# # # # text to speech
# # #
# # # # import the required module from text to speech conversion
# # # import win32com.client
# # #
# # # # Calling the Disptach method of the module which
# # # # interact with Microsoft Speech SDK to speak
# # # # the given input from the keyboard
# # #
# # # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # #
# # # while 1:
# # # 	print("Enter the word you want to speak it out by computer")
# # # 	s = input()
# # # 	speaker.Speak(s)
# # #
# # # # To stop the program press
# # # # CTRL + Z
# #
# # # import win32com.client
# # # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # # speaker.Speak("Hello, it works!")
# #
# #
# # # Python program to show
# # # how to convert text to speech
# # import pyttsx3
# #
# # # Initialize the converter
# # converter = pyttsx3.init()
# #
# # # Set properties before adding
# # # Things to say
# #
# # # Sets speed percent
# # # Can be more than 100
# # converter.setProperty('rate', 150)
# # # Set volume 0-1
# # converter.setProperty('volume', 0.7)
# #
# # # Queue the entered text
# # # There will be a pause between
# # # each one like a pause in
# # # a sentence
# # converter.say("Hello GeeksforGeeks")
# # converter.say("I'm also a geek")
# #
# # # Empties the say() queue
# # # Program will not continue
# # # until all speech is done talking
# # converter.runAndWait()
# # import converter
# # voices = converter.conversion("voice")
# #
# #
# # for voice in voices:
# # 	# to get the info. about various voices in our PC
# # 	print("Voice:")
# # 	print("ID: %s" %voice.id)
# # 	print("Name: %s" %voice.name)
# # 	print("Age: %s" %voice.age)
# # 	print("Gender: %s" %voice.gender)
# # 	print("Languages Known: %s" %voice.languages)
#
# #pip3 install pyttsx3
# #apt-get install alsa-utils
# import pyttsx3, time
# engine = pyttsx3.init()
# engine.say("Hi, I am text to speach")
# engine.runAndWait()

#
# import pyttsx3
#
# test = "Once upon a time, a person was trying to convert text to speech using python"
# engine = pyttsx3.init()
#
# voices = engine.getProperty('voices')
# for voice in voices:
#  print("Voice:")
#  print(" - ID: %s" % voice.id)
#  print(" - Name: %s" % voice.name)
#  print(" - Languages: %s" % voice.languages)
#  print(" - Gender: %s" % voice.gender)
#  print(" - Age: %s" % voice.age)
#
#  en_voice_id = "voice.id"
#  engine.setProperty('voice', en_voice_id)
#
#  engine.say(test)
#  engine.runAndWait()
#
import pyttsx3
engine = pyttsx3.init("dummy")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#
def speak(text):
    print('Rex:' + text)
    engine.say(text)
    engine.runAndWait()

print("On")
speak("This program is running perfectly")
print("End")