<h1 align="center" style="font-size: 3rem;">
tiktok-api
</h1>
<p align="center">
<em>TikTok Web Api and Bot.</em></p>

## Quickstart
```python
videos = api.get_user_videos("maskofshiva")
for video in videos:
    print(video)
    print(api.get_meta_title(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")

Run this in bash or cmd:
git clone git@github.com:instabotai/tiktok-api.git
pip3 install -r requirements.txt
python3 example.py
