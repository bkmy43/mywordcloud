#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import sys
import time

import speech_recognition as sr


# this is called from the background thread
def callback(recognizer, audio):
    sys.stdout.write("\nTRY...")
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        sys.stdout.write("SUCCESS: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        sys.stdout.write("FAIL")
    except sr.RequestError as e:
        sys.stdout.write("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print('Adjusted microphone, ready to go...')

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# wait and listen
while True:
    time.sleep(1)
