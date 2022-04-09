import praw
from praw.models import MoreComments
import copy

# bot info and keys
user_agent = "0 Effort TikTok Content Creator"

reddit = praw.Reddit(
    client_id="DQuE-pUeXrhxJrkwbGpTjg",
    client_secret="NL3k7yxRMLgmgY89Nd-rvDceNta8VQ",
    user_agent=user_agent
)


# "dataclass" for submissions
class Submission:
    # all submission information to be stored
    def __init__(self):
        self.title = None
        self.text = None
        self.top = []
        self.controversial = []

    """ 
    *************************
    START SETTERS AND GETTERS
    *************************
    """
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_top(self, top):
        self.top = top

    def get_top(self):
        return self.top

    def set_controversial(self, controversial):
        self.controversial = controversial

    def get_controversial(self):
        return self.controversial
    """ 
    *************************
    END SETTERS AND GETTERS
    *************************
    """

    # __str__ method for easy printing
    def __str__(self):
        print_string = f"""\nTitle: {self.title}\nText: {self.text}\nTop Hot: {self.top}\nTop Controversial: {self.controversial}\n"""
        return print_string


class RedditScraper:
    def __init__(self, sub_reddit, submissions):
        self.sub_reddit = reddit.subreddit(sub_reddit)
        self.submissions = submissions

    def start_stream(self, top_num, controversial_num):
        submission_list = []
        for submission in self.sub_reddit.hot(limit=self.submissions):
            curr_submission = Submission()
            curr_submission.set_title(submission.title)
            print(curr_submission.get_title())

            try:
                curr_submission.set_text(submission.text)
                print(curr_submission.get_text())
            except AttributeError:
                pass
            submission_master = reddit.submission(url=submission.url)
            top_comments = []
            top_comments_submission = copy.deepcopy(submission_master)
            top_comments_submission.comment_sort = "top"
            i = 0
            i2 = 0
            while i < top_num:
                if not isinstance(i, MoreComments):
                    if not top_comments_submission.comments[i2].body == "[deleted]":
                        top_comments.append(top_comments_submission.comments[i2])
                        i += 1
                        i2 += 1
                    else:
                        i2 += 1
                else:
                    i2 += 1
            curr_submission.set_top(top_comments)

            controversial_comments = []
            controversial_comments_submission = copy.deepcopy(submission_master)
            controversial_comments_submission.comment_sort = "controversial"
            i = 0
            i2 = 0
            while i < controversial_num:
                if not isinstance(i, MoreComments):
                    if not controversial_comments_submission.comments[i2].body == "[deleted]":
                        controversial_comments.append(controversial_comments_submission.comments[i2])
                        i += 1
                        i2 += 1
                    else:
                        i2 += 1
                else:
                    i2 += 1
            curr_submission.set_controversial(controversial_comments)

            submission_list.append(curr_submission)
        return submission_list


scraper = RedditScraper("AskReddit", 2)
curr_submission_list = scraper.start_stream(2, 2)
print(curr_submission_list)
for submissions in curr_submission_list:
    print(submissions)
    for comment in submissions.get_top():
        print(f"\nAuthor: {comment.author}\nBody: {comment.body}\n")

    for comment in submissions.get_controversial():
        print(f"\nAuthor: {comment.author}\nBody: {comment.body}\n")
