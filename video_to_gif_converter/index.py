from moviepy.editor import *

clip = VideoFileClip("video.mp4")

clip.write_gif("newfile.gif")
