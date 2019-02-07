import numpy as np
import pandas as pd
from pyAudioAnalysis import audioBasicIO #A
from pyAudioAnalysis import audioFeatureExtraction #B
import os #C


def preProcess(fileName):
	[Fs, x] = audioBasicIO.readAudioFile(fileName)  # A

	# B
	if (len(x.shape) > 1 and x.shape[1] == 2):
		x = np.mean(x, axis=1, keepdims=True)
	else:
		x = x.reshape(x.shape[0], 1)
	# C
	F, f_names = audioFeatureExtraction.stFeatureExtraction(
		x[:, 0],
		Fs, 0.050 * Fs,
			0.025 * Fs
	)

	return (f_names, F)


def getChromagram(audioData):
	# A
	temp_data = audioData[21].reshape(
		1,
		audioData[21].shape[0]
	)
	chronograph = temp_data

	# B
	for i in range(22, 33):
		temp_data = audioData[i].reshape(
			1,
			audioData[i].shape[0]
		)
		chronograph = np.vstack([chronograph, temp_data])

	return chronograph

def getNoteFrequency(chromagram):
	numberOfWindows = chromagram.shape[1]  # A

	freqVal = chromagram.argmax(axis=0)  # B

	histogram, bin = np.histogram(freqVal, bins=12)  # C

	normalized_hist = histogram.reshape(1, 12).astype(float) / numberOfWindows  # D

	return normalized_hist

def getNoteFreqs(filenames):

	fileList = []
	X = pd.DataFrame()

	columns = ["G#", "G", "F#", "F", "E", "D#", "D", "C#", "C", "B", "A#", "A"]

	for file in filenames:
		fileList.append(file)
		feature_name, features = preProcess(file)
		chromagram = getChromagram(features)
		noteFrequency = getNoteFrequency(chromagram)
		x_new = pd.Series(noteFrequency[0, :])
		X = pd.concat([X, x_new], axis=1)

	data = X.T.copy()
	data.columns = columns
	data.index = [i for i in range(0, data.shape[0])]

	return data
