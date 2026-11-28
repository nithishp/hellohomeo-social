#!/bin/bash
# usage: compose.sh A_SRC_START B_SRC_START
set -e; cd "$(dirname "$0")/.."
AS=${1:-0.1}; BS=${2:-0.3}
V="scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,setsar=1,fps=30,format=yuv420p"
ffmpeg -v error -y -f lavfi -i color=c=0x070C1F:s=1080x1920:r=30:d=30 \
 -ss $AS -t 4.75 -i assets/clips/clipA.mp4 -ss $BS -t 3.375 -i assets/clips/clipB.mp4 \
 -framerate 30 -i out/frames/f%04d.png -i assets/audio/mix.wav \
 -filter_complex "[1:v]$V,setpts=PTS-STARTPTS+2.25/TB[a];[2:v]$V,setpts=PTS-STARTPTS+21.625/TB[b];[0:v][a]overlay=eof_action=pass:enable='between(t,2.25,7.0)'[x];[x][b]overlay=eof_action=pass:enable='between(t,21.625,25.0)'[y];[y][3:v]overlay=format=auto,format=yuv420p[v]" \
 -map "[v]" -map 4:a -c:v libx264 -preset slow -crf 19 -profile:v high -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart -t 30 out/final.mp4
ls -la out/final.mp4
