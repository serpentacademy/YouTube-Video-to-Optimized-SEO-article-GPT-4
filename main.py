import os
import openai
with open('key.txt', 'r') as file:
  first_line = file.readline()
openai.api_key = first_line

audio_file = open("audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)
with open('transcript.txt', 'w') as f:
    f.write(transcript.text)
