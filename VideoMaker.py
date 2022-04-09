from gtts import gTTS
from moviepy.editor import *


# takes text and stock video and combines them into new video
class VideoMaker:
    def __init__(self, video):
        self.video = VideoFileClip(video)

    # creates a video from title and body text, if it exists
    def create_video_standard(self, text):
        # saves the given text to audio file
        tts = gTTS(text)
        tts.save("Audio/standard_audio.mp3")
        audio = AudioFileClip("Audio/standard_audio.mp3")

        # takes generated audio file and creates looping video
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)
        video.write_videofile("Output/standard_video.mp4", fps=60)

    # creates a video from top comments
    def create_video_top(self, text):
        # saves the given text to audio file
        tts = gTTS(text)
        tts.save("Audio/top_audio.mp3")
        audio = AudioFileClip("Audio/top_audio.mp3")

        # takes generated audio file and creates looping video
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)
        video.write_videofile("Output/top_video.mp4", fps=60)

    # creates a video from controversial comments
    def create_video_controversial(self, text):
        # saves the given text to audio file
        tts = gTTS(text)
        tts.save("Audio/controversial_audio.mp3")
        audio = AudioFileClip("Audio/controversial_audio.mp3")

        # takes generated audio file and creates looping video
        video = self.video
        video = video.set_audio(audio)
        video = video.loop(duration=audio.duration)
        video.write_videofile("Output/controversial_video.mp4", fps=60)
