from audio2vec.wav2vec import preProcess,getChromagram, getDataset
from audio2vec.reduce import Mapper
import glob

directory = 'corpus'
file_type = 'wav'

if __name__ == "__main__":
	audio_files = glob.glob("{}/*.{}".format(directory,file_type))
	music_notes = getDataset(audio_files)
	df = Mapper(music_notes.values,audio_files)
	df['value'] = 0.15
	df.to_csv('data.csv')