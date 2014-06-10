#!/bin/bash

sites_dir=`dirname "$0"`/../sites
pro=/home/p/pro

sites=(
  minimul-default default
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

mkdir -p $sites_dir 2>/dev/null

for (( i = 0; i < ${#sites[@]}; i+=2 )) {
  rsync -a --del ${excludes[@]} "$pro/${sites[$i]}/" "$sites_dir/${sites[$i+1]}/"
}
