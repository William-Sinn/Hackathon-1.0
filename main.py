import RedditScraper as RScrape
import AccumulateText as AText
import VideoMaker as VMaker

if __name__ == '__main__':
    # creates scraper and scrapes specified number of submissions
    scraper = RScrape.RedditScraper("AskReddit", 3)
    submission_list = scraper.scrape_submissions(2, 2)

    # takes formatted text and creates video using it and a stock video for background
    video_maker = VMaker.VideoMaker("Stock/1.mp4")

    # loops for every submission in the list
    i = 0
    for submission in submission_list:

        # accumulates the text into easily TTSed format
        accumulator = AText.AccumulateText(submission_list[i])
        # tells user currently building submission
        print(f"Now Building: {submission.get_title()}")

        # creates a video for title, text, top, and controversial comments
        video_maker.create_video_standard(accumulator.accumulate_text_standard(), i+1)
        video_maker.create_video_top(accumulator.accumulate_text_top_reply()[0], i+1)
        video_maker.create_video_controversial(accumulator.accumulate_text_controversial_reply()[0], i+1)
        i += 1

    # All Done!!! :)
    print("All Done!")
