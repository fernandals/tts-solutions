# script to convert the transcriptions file to the appropriate format

import sys

tgt_file = sys.argv[1]

f = open('metadata.csv', 'w')
print('file_name,transcription\n', file=f)
f.close()

with open(tgt_file) as infile:
  for line in infile:
    #print(line.replace('	', ',', 1))
    line = line.replace('	', '.flac,', 1)
    print("data/" + line, file=open('metadata.csv', 'a'))


