from pydub import AudioSegment
# from pydub.playback import play

f = open("Voice.mp3")
f.close()
sound = AudioSegment.from_mp3("Voice.mp3")
# play(sound)