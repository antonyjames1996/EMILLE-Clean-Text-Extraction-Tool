#!/bin/bash
echo "Welcome to IISER-B EMILLE Text extractor! "
mkdir tmp
mkdir Result
mkdir Result/final_files
mkdir Result/tag_info
python3 factuality.py
python3 beautifulsoup_parse_p_tags.py
mkdir output1
mkdir output1/tmp
for file in tmp/*.txt; do cat $file | perl -pe 's/\r\n/ /' | sed 's/<\/p><p>/<\/p>\n<p>/g' | sed 's/<\/p>//g' | sed 's/<p>//g' | sed 's/ //g'| awk '$1=$1' | sed 's/&lt;+/\n/g' | awk '$1=$1' | sed '1d' | sed 's/। / । /g' > output1/$file ; done
mkdir output2
mkdir output2/output1
mkdir output2/output1/tmp
for file in output1/tmp/*.txt; do python3 para2sent_indexed.py $file > output2/$file ; done
rm -r output1
rm -r tmp

cp output2/output1/tmp/*.txt Result/final_files
rm -r output2
