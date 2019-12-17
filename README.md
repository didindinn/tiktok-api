<center><h1>tiktok-api</h2></center>


## Example
```python
videos = api.get_user_videos("maskofshiva")
for video in videos:
    print(video)
    print(api.get_meta_title(video))
    print(api.get_video_homepage(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
    ```
