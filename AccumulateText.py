class AccumulateText:
    def __init__(self, submission):
        self.submission = submission

    def accumulate_text_standard(self):
        text = ""
        text += self.submission.title
        text += "..."
        if self.submission.text is not None:
            text += self.submission.text
        return text

    def accumulate_text_top_reply(self):
        ret_list = []
        text = ""
        authors = []
        text += self.submission.title
        text += "..."
        for comment in self.submission.get_top():
            text += comment.body
            text += "..."
            authors.append(comment.author)
        ret_list.append(text)
        ret_list.append(authors)
        return ret_list

    def accumulate_text_controversial_reply(self):
        ret_list = []
        text = ""
        authors = []
        text += self.submission.title
        text += "..."
        for comment in self.submission.get_controversial():
            text += comment.body
            text += "..."
            authors.append(comment.author)
        ret_list.append(text)
        ret_list.append(authors)
        return ret_list


# text_subs = Scrape.RedditScraper("AskReddit", 2)
# sub_list = text_subs.scrape_submissions(2, 2)
# print(sub_list)
# accumulator = AccumulateText(sub_list[0])
#
# text = accumulator.accumulate_text_standard()
# tts = gTTS(text)
# tts.save('test_standard.mp3')
#
# text = accumulator.accumulate_text_top_reply()
# tts = gTTS(text[0])
# tts.save("test_top.mp3")
#
# text = accumulator.accumulate_text_controversial_reply()
# tts = gTTS(text[0])
# tts.save("test_controversial.mp3")
#
# print("Done!")
