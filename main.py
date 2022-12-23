import wave
obj = wave.open("Audios\Voice.wav","rb") #read binary
print("Number of channels: ", obj.getnchannels())
print("Sample Width ", obj.getsampwidth())
print("frame rate ", obj.getframerate())
print("Number of frames ", obj.getnframes())
print("Parameters ", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate() # in seconds

print(t_audio)
