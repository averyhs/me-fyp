#!/bin/zsh

# Manually enter path (depends on type of output CellSium produced)
echo "Images directory (eg. GenericMaskOutput-simulate/images)"
read imgdir

# Create video (.mp4)
ffmpeg -r 8 -pattern_type glob -i "$imgdir/*.png" -f mp4 -vcodec libx264 -y ./simvid.mp4

# Create gif
ffmpeg -r 8 -pattern_type glob -i "$imgdir/*.png" -f gif -y ./simgif.gif
