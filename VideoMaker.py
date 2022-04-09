from gtts import gTTS
from moviepy.editor import *


class VideoMaker:
    def __init__(self, video):
        self.video = VideoFileClip(video)

    def create_video_standard(self, text):
        tts = gTTS(text)
        tts.save("Audio/standard_audio.mp3")
        audio = AudioFileClip("Audio/standard_audio.mp3")
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)

        video.write_videofile("Output/standard_video.mp4", fps=60)

    def create_video_top(self, text):
        tts = gTTS(text)
        tts.save("Audio/top_audio.mp3")
        audio = AudioFileClip("Audio/top_audio.mp3")
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)

        video.write_videofile("Output/top_video.mp4", fps=60)

    def create_video_controversial(self, text):
        tts = gTTS(text)
        tts.save("Audio/controversial_audio.mp3")
        audio = AudioFileClip("Audio/controversial_audio.mp3")
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)

        video.write_videofile("Output/controversial_video.mp4", fps=60)


# video_make = VideoMaker("this is the text to the video now", VideoFileClip("Stock/1.mp4"))
# video_make.create_video_standard()
