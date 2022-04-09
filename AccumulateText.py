class AccumulateText:
    # takes submission dataclass
    def __init__(self, submission):
        self.submission = submission

    # accumulates title and body text, if body text exits
    def accumulate_text_standard(self):
        text = ""
        text += self.submission.title
        text += "..."
        if self.submission.text is not None:
            text += self.submission.text
        print(self.submission.text)
        return text

    # accumulates all top comments stored in object
    def accumulate_text_top_reply(self):
        ret_list = []
        text = ""
        authors = []
        # stores authors for later display
        text += self.submission.title
        text += "..."
        for comment in self.submission.get_top():
            text += comment.body
            text += "..."
            authors.append(comment.author)
        ret_list.append(text)
        ret_list.append(authors)
        return ret_list

    # accumulates all controversial posts stored in object
    def accumulate_text_controversial_reply(self):
        ret_list = []
        text = ""
        # stores authors for later display
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
