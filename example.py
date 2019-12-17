import tiktokapi

api = tiktokapi.api.Api()

videos = api.get_user_videos("maskofshiva")

for video in videos:
    print(video)
    print(api.get_meta_title(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
