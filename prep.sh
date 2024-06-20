#!/bin/bash


pelican content -o output/ -s pelicanconf.py -t pelican-bootstrap3

for file in $(ls output/*.html)
do
sed -i 's/<table>/<table class="table table-hover">/g' $file
sed -i 's/<img/<img class="center" style="border: 8px solid black;"/g' $file
done

cp vss-style.css output/theme/css/style.css

ghp-import output/ -b gh-pages -r origin -p -n