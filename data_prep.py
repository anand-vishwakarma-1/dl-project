import json
import pandas as pd
import numpy as np
import os
import glob
from num2words import num2words
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip,ffmpeg_extract_audio
from pydub import AudioSegment

def time_convert(ms):
	return '{}:{}:{:.3f}'.format(0,int((ms/1000)/60),(ms/1000)%60)

# with open('edit.json', encoding="utf8") as f:
#   edit = json.load(f)
edit = {
	"normalize": {
		"'90s": "Nineties",
		"'80s": "Eighties",
		"'70s": "Seventies",
	},
	"remove": {
		"“": "",
		",": "",
		"”": "",
		"\n": " ",
		"!": "",
	},
	"number": {
		"%": "percent",
		"$": "dollar",
	}
}

def num_conv(word,edit_dict):
	if any(char.isalpha() for char in word):
		x = [] 
		for a in word:
			if a.isdigit():
				x.append(num2words(int(a)))
			elif a.isalpha():
				x.append(a)
		return " ".join(x)
	else:
		word_new = num2words(int("".join([a for a in word if a.isdigit()]))).replace("-"," ")
		for key in edit_dict:
			if key in word:
				temp = edit_dict[key]
				word_new = " ".join([word_new.replace(key,''),temp])
		return word_new

i = 1
duration_thres = 10
name = []
transcript = []
Ntranscript = []
out_path = 'JS/'
character = 'JS'
if not os.path.exists(out_path):
    os.mkdir(out_path)
if not os.path.exists(f'{out_path}wavs'):
    os.mkdir(f'{out_path}wavs')
for json_file in glob.glob('{}_*.json'.format(character)):
    print(json_file)
    with open(json_file, encoding="utf8") as f:
        data = json.load(f)
    duration = 0
    audio_files = []
    temp = 0
    trans = ''
    prev_time = 0
    for f in data:	
        if i%50 == 0:
            print(i)
        start = f['start']
        if start < prev_time:
              start += (prev_time - start)
        duration += f['duration']
        s = f['text']
        for key in edit['normalize']:
            if key in s:
                s = s.replace(key,edit['normalize'][key])
        t = []
        for word in s.split(" "):
            if any(char.isdigit() for char in word):
                word = num_conv(word,edit['number'])
            t.append(word)
        s = " ".join(t)
        for key in edit['remove']:
            if key in s:
                s = s.replace(key,edit['remove'][key])
        trans = " ".join([trans,s])
        ffmpeg_extract_subclip(".".join([json_file.split(".")[0],"mp4"]), start, start+f['duration'], targetname="./{}/{}{:05d}.mp4".format(out_path,character,i+temp))
        ffmpeg_extract_audio("./{}/{}{:05d}.mp4".format(out_path,character,i+temp),"./{}/{}{:05d}.wav".format(out_path,character,i+temp))
        audio_files.append("./{}/{}{:05d}.wav".format(out_path,character,i+temp))
        os.remove("./{}/{}{:05d}.mp4".format(out_path,character,i+temp))
        temp += 1
        prev_time = f['start']+f['duration']
        if duration > duration_thres:
            sound = AudioSegment.from_wav(audio_files[0])
            os.remove(audio_files[0])
            for audio in audio_files[1:]:
                sound = sound.append(AudioSegment.from_wav(audio))
                os.remove(audio)
            sound.export("./{}/wavs/{}{:05d}.wav".format(out_path,character,i),format="wav")
            name.append('TL{:05d}'.format(i))
            transcript.append(trans)
            Ntranscript.append(trans)
            i+=1
            
            duration = 0
            audio_files = []
            temp = 0
            trans = ''
    
    if len(audio_files) > 0:
        sound = AudioSegment.from_wav(audio_files[0])
        os.remove(audio_files[0])
        for audio in audio_files[1:]:
            sound = sound.append(AudioSegment.from_wav(audio))
            os.remove(audio)
        sound.export("./{}/wavs/{}{:05d}.wav".format(out_path,character,i),format="wav")
        name.append('TL{:05d}'.format(i))
        transcript.append(trans)
        Ntranscript.append(trans)
df = pd.DataFrame({'id': name,'transcript': transcript, 'Ntranscript': Ntranscript})
df.to_csv('./{}/transcript.csv'.format(out_path),header=None ,sep='|' ,index=False)

# df = pd.read_csv('./TL/transcript.csv',header=None ,sep='|')
# with open('sample.txt','w') as file:
# 	for i, row in df.iterrows():
# 		if i%10 == 0:
# 			file.write(". ".join([str(int(i/10+1)),row[1]]))
# 			file.write('\n')