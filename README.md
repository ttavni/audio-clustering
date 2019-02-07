# Audio Clustering 

###### Made by Timothy Avni (tavni96)

Very simply cluster audio and reduce to 2-dimensions

```python

from audio2vec.wav2vec import preProcess,getChromagram, getDataset
from audio2vec.reduce import Mapper
import glob

audio_files = glob.glob("{}/*.{}".format(directory,file_type))
music_notes = getDataset(audio_files)
df = Mapper(music_notes.values,audio_files)
	
```