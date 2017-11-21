import csv
import os
import shutil

if __name__ == '__main__':
    countries = {}
    with open('./data/speech-accent-archive/speakers_all.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row['country'].replace(' ', '_')
            if not country:
                continue
            if country not in countries:
                os.makedirs('./data/speech-accent-archive/recordings/%s' % country)
                countries[country] = 1
            try:
                shutil.move('./data/speech-accent-archive/recordings/%s.mp3' % row['filename'],
                            './data/speech-accent-archive/recordings/%s/%s.mp3' % (
                            country, row['filename']))
            except:
                continue
