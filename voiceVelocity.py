import samplerate
import IPython.display as ipd
import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

FIG_SIZE = (14, 5) #그래프 사이즈
data, sr = librosa.load('/content/drive/MyDrive/colabbox/helloEN.mp3', sr=None)
out_data1 = samplerate.resample(data, 0.5, 'sinc_best')
out_data2 = samplerate.resample(data, 1.5, 'sinc_best')

print('Higher pitch:')
ipd.display(ipd.Audio(out_data1, rate=sr))
print('Lower pitch:')
ipd.display(ipd.Audio(out_data2, rate=sr))

plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(out_data1, sr=sr)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.xticks([0, 1, 2, 4, 5])
plt.title("Waveform")
plt.show()

plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(out_data2, sr=sr)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.xticks([0, 1, 2, 4, 5])
plt.title("Waveform")
plt.show()
