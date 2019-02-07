import glob
from pydub import AudioSegment
import os

audio_directory = 'corpus'
file_type = 'wav'
length = 2000
new_directory = 'shorten'

def GenerateSamples(audio_directory,file_type,length,new_directory):

	audio_files = glob.glob("{}/*.{}".format(audio_directory,file_type))

	if not os.path.exists(new_directory):
		os.makedirs(new_directory)

	for file in audio_files:
		newAudio = AudioSegment.from_wav(file)
		newAudio = newAudio[0:length]
		newAudio.export(file.replace('{}/'.format(audio_directory),'{}/'.format(new_directory)), format=file_type)
		print('{} changed to WAV'.format(file))

def main():
	GenerateSamples(audio_directory,file_type,length,new_directory)

if __name__== "__main__":
	main()