#!/bin/bash

if [ -z "$1" ]; then
  echo "USAGE: $0 [www.example.com]"
  exit 1
fi

is_link=`echo $1 |egrep -o "^tt[0-9]+$"`

if [ -z "$is_link" ]; then
  echo "Scraping \"$1\"..."
  link=`python3 scrape_images.py "$1"`
else
  link=$1
fi

echo "Scraping images for ${link}..."
python3 scrape_images.py $link $2
