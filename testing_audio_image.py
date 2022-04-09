from gtts import gTTS
from moviepy.editor import AudioFileClip, ImageClip
import argparse

text = "Hello"
tts = gTTS(text)
tts.save('hello.mp3')


audio_clip = AudioFileClip("hello.mp3")
image_clip = ImageClip("vladislav-klapin-SymZoeE8quA-unsplash.jpg")
video_clip = image_clip.set_audio(audio_clip)
video_clip.duration = audio_clip.duration
video_clip.fps = 1
video_clip.write_videofile("video.mp4")

