import RedditScraper as RScrape
import AccumulateText as AText
import VideoMaker as VMaker

if __name__ == '__main__':
    scraper = RScrape.RedditScraper("AskReddit", 1)
    submission_list = scraper.scrape_submissions(2, 2)
    accumulator = AText.AccumulateText(submission_list[0])
    video_maker = VMaker.VideoMaker("Stock/1.mp4")
    video_maker.create_video_standard(accumulator.accumulate_text_standard())
    video_maker.create_video_top(accumulator.accumulate_text_top_reply()[0])
    video_maker.create_video_controversial(accumulator.accumulate_text_controversial_reply()[0])
    print("All Done!")
