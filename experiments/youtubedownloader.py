#import pytube as YouTube
from pytube import YouTube

# help(YouTube)

def Download(link):
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download("c:\foldit")
    except Exception as e:
        print(f"there was some error - {e}")
    print("yuhu!mission succeded!")

# the function takes the video url as an argument
def video_downloader(video_url):
    # passing the url to the YouTube object
    my_video = YouTube(video_url)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title

# video_downloader("https://www.youtube.com/watch?v=dd8BRPWzXgo&list=FLcEV4MImLP82eZfXGFRSZYA&index=420")
video_downloader("https://youtu.be/dd8BRPWzXgo?si=q8wRu7UlNEKLlUgE")
# video_downloader("https://www.youtube.com/embed/dd8BRPWzXgo?si=q8wRu7UlNEKLlUgE")
# link=input("enter url of ur clip")
Download("https://youtu.be/0ihhzayi9WU?si=dUwvtLyef7zfvYvI")