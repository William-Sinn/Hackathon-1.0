from gtts import gTTS
from moviepy.editor import *


class TextOverlay:
    def __init__(self, submission):
        self.submission = submission

    def place_standard(self, video):
        tts = gTTS(self.submission.get_title())
        tts.save("TempAudio/temp_title.mp3")
        if self.submission.get_text() == "":
            self.submission.set_text("Empty body!")
        tts = gTTS(self.submission.get_text())
        tts.save("TempAudio/temp_text.mp3")
        text_audio = AudioFileClip("TempAudio/temp_text.mp3")

        title_audio = AudioFileClip("TempAudio/temp_title.mp3")

        video = VideoFileClip(video).set_duration(title_audio.duration + text_audio.duration)
        text = TextClip(self.submission.get_text(), size=(video.w, 0), color="white", bg_color="gray").set_position(
            ("center", "center")).set_start(title_audio.duration).set_duration(text_audio.duration)
        title = TextClip(self.submission.get_title(), size=(video.w, 0), color="white", bg_color="gray").set_position(
            ("center", "center")).set_duration(title_audio.duration)

        final = CompositeVideoClip([video, title, text])
        final.write_videofile("TempVideo/temp_standard.mp4")

    def place_top(self, video):
        tts = gTTS(self.submission.get_title())
        tts.save("TempAudio/temp_title.mp3")
        title_audio = AudioFileClip("TempAudio/temp_title.mp3")
        video = VideoFileClip(video).subclip(title_audio.duration)
        title = TextClip(self.submission.get_title(), size=(video.w, 0), color="white", bg_color="gray").set_position(
            ("center", "center")).set_duration(title_audio.duration)
        i = 0
        total_dur = 0
        comments_authors = None
        for comment in self.submission.get_top():
            tts = gTTS(self.submission.get_top()[i].author.name)
            tts.save("TempAudio/temp_author.mp3")
            author_audio = AudioFileClip("TempAudio/temp_author.mp3")
            tts = gTTS(self.submission.get_top()[i].body)
            tts.save("TempAudio/temp_body.mp3")
            body_audio = AudioFileClip("TempAudio/temp_body.mp3")
            author = TextClip(self.submission.get_top()[i].author.name, size=(video.w, 0), color="white",
                              bg_color="gray").set_position(("top", "left")).set_start(
                title_audio.duration + total_dur).set_duration(body_audio.duration)
            comment = TextClip(self.submission.get_top()[i].body, size=(video.w, 0), color="white",
                               bg_color="gray").set_position(("center", "center")).set_start(
                title_audio.duration + total_dur).set_duration(body_audio.duration)
            comments_authors = CompositeVideoClip([author, comment])
            total_dur += author_audio.duration
            total_dur += body_audio.duration

        final = CompositeVideoClip([title, comments_authors])
        final.set_duration(total_dur + title_audio.duration)
        final.write_videofile("TempVideo/temp_top.mp4", fps=60)

    def place_controversial(self, video):
        tts = gTTS(self.submission.get_title())
        tts.save("TempAudio/temp_title.mp3")
        title_audio = AudioFileClip("TempAudio/temp_title.mp3")
        video = VideoFileClip(video).subclip(title_audio.duration)
        title = TextClip(self.submission.get_title(), size=(video.w, 0), color="white", bg_color="gray").set_position(
            ("center", "center")).set_duration(title_audio.duration)
        i = 0
        total_dur = 0
        comments_authors = None
        for comment in self.submission.get_top():
            tts = gTTS(self.submission.get_top()[i].author.name)
            tts.save("TempAudio/temp_author.mp3")
            author_audio = AudioFileClip("TempAudio/temp_author.mp3")
            tts = gTTS(self.submission.get_top()[i].body)
            tts.save("TempAudio/temp_body.mp3")
            body_audio = AudioFileClip("TempAudio/temp_body.mp3")
            author = TextClip(self.submission.get_top()[i].author.name, size=(video.w, 0), color="white",
                              bg_color="gray").set_position(("top", "left")).set_start(
                title_audio.duration + total_dur).set_duration(body_audio.duration)
            comment = TextClip(self.submission.get_top()[i].body, size=(video.w, 0), color="white",
                               bg_color="gray").set_position(("center", "center")).set_start(
                title_audio.duration + total_dur).set_duration(body_audio.duration)
            comments_authors = CompositeVideoClip([author, comment])
            total_dur += author_audio.duration
            total_dur += body_audio.duration

        final = CompositeVideoClip([title, comments_authors])

        final.write_videofile("TempVideo/temp_controversial.mp4", fps=60)
