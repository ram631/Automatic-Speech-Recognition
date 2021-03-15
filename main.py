#!/usr/bin/env python3

import speech_recognition as sr
import os
from datetime import datetime
import time


PROCESSING_FOLDER = 'for_processing/'
PROCESSED_FOLDER = 'processed/'
RESULTS_FOLDER = 'results/'


def process_audio(filename):
    AUDIO_FILE = (filename)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


while(True):
    for filename in os.listdir(PROCESSING_FOLDER):
        print("processing " + filename)
        if filename.endswith(".wav") or filename.endswith(".wavs"):
            # used to get current timestamp
            now = datetime.now()
            # converts current timestamp to specified format
            dt_string = now.strftime("-%d%m%Y%H%M%S")
            # remove the .wav extension in the file name and store to variable
            fnamenoext = filename.split('.')[0]
            # process the actual file
            result = process_audio(PROCESSING_FOLDER+filename)
            # this function moves the processed file and rename it to have a timestamp
            os.rename(PROCESSING_FOLDER+filename,                              
                      PROCESSED_FOLDER+fnamenoext+dt_string+'.wav')            
            
            with open(RESULTS_FOLDER+fnamenoext+dt_string+".txt", "w") \
                    as text_file:
                text_file.write(result)

            continue
        else:
            continue
    print("waiting for new file")
    time.sleep(20)