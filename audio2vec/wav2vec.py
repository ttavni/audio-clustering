import numpy as np
import pandas as pd
from pyAudioAnalysis import audioBasicIO #A
from pyAudioAnalysis import audioFeatureExtraction #B
import os #C

def getNoteFrequency(chromagram):
	numberOfWindows = chromagram.shape[1]  # A

	freqVal = chromagram.argmax(axis=0)  # B

	histogram, bin = np.histogram(freqVal, bins=12)  # C

	normalized_hist = histogram.reshape(1, 12).astype(float) / numberOfWindows  # D

	return normalized_hist

def getDataset(filenames):

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
