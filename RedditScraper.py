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

    def get_top_controversial(self):
        return self.controversial
    """ 
    *************************
    END SETTERS AND GETTERS
    *************************
    """

    # __str__ method for easy printing
    def __str__(self):
        print_string = f"""Title: {self.title}\nText: {self.text}\nTop Hot: {self.top}\nTop Controversial: {self.controversial}"""
        return print_string


class RedditScraper:
    def __init__(self, sub_reddit, submissions):
        self.sub_reddit = reddit.subreddit(sub_reddit)
        self.submissions = submissions

    def start_stream(self):
        curr_submission = Submission()
        submission_list = []
        for submission in self.sub_reddit.hot(limit=self.submissions):
            curr_submission.set_title(submission.title)
            print(curr_submission.get_title())

            try:
                curr_submission.set_text(submission.text)
                print(curr_submission.get_text())
            except AttributeError:
                pass

            submission_top = copy.deepcopy(submission)
            submission_controversial = copy.deepcopy(submission)

            submission_top.comment_sort = "top"
            top_list = []
            for i in range(3):
                top_list.append(submission_top.comments[i])
            curr_submission.set_top(top_list)

            submission_controversial.comment_sort = "controversial"
            controversial_list = []
            for i in range(3):
                controversial_list.append(submission_controversial.comments[i])
            curr_submission.set_controversial(top_list)

            submission_list.append(curr_submission)

        return submission_list


scraper = RedditScraper("AskReddit", 2)
submission_list = scraper.start_stream()
print(submission_list)
for submissions in submission_list:
    print(submissions)
    for comment in submissions.get_top():
        if not isinstance(comment, MoreComments):
            print(f"Author: {comment.author}\nBody: {comment.body}")
