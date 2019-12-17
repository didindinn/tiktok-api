<center><h1>tiktok-api</h2></center>


## Example
videos = api.get_user_videos("maskofshiva")

```python
for video in videos:
    print(video)
    print(api.get_meta_title(video))
    print(api.get_video_homepage(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
    ```
