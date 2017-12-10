import csv
import os
import shutil

if __name__ == '__main__':
    native_langs = {}
    with open('./data/speech-accent-archive/speakers_all.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            native_lang = row['native_language'].replace(' ', '_')
            if not native_lang:
                continue
            if native_lang not in native_langs:
                os.makedirs('./data/speech-accent-archive/recordings/%s' % native_lang)
                native_langs[native_lang] = 1
            try:
                shutil.move('./data/speech-accent-archive/recordings/%s.mp3' % row['filename'],
                            './data/speech-accent-archive/recordings/%s/%s.mp3' % (
                                native_lang, row['filename']))
            except:
                continue
