from flask import Flask, render_template, Response, request, redirect, url_for
import numpy as np
import sounddevice
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__)

@app.route("/")
def index():
    x=3
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Record Audio
    fps=44100
    duration= 10 
    recording= sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
    sounddevice.wait()
    #save the audio
    write("static/audio/output.wav", fps, recording)

   

    return render_template('result.html')

