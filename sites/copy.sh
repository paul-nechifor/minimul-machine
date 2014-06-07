#!/bin/bash

here=`dirname "$0"`
pro=/home/p/pro

sites=(
  paul-scripts paulscripts
  college-website collegesite
  college-website-2 collegesite2
  italia-fascistă italiafascista
  rstsd rstsd
  meet-firefox meetfirefox
  timr timr
)

excludes=(
  --exclude .git
  --exclude '*~'
  --exclude private
  --exclude screenshot.png
  --exclude readme.md
)

for (( i = 0; i < ${#sites[@]}; i+=2 )) {
  rsync -a --del ${excludes[@]} "$pro/${sites[$i]}/" "$here/${sites[$i+1]}/"
}
