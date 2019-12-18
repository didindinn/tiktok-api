<h1 align="center" style="font-size: 3rem;">
tiktok-api
</h1>
<p align="center">
<em>TikTok Web Api and Bot.</em></p>
<p>
<h2>RInstall with pip:</h2><p>

pip install tiktok-api
<p>
    
## Quickstart
```python
from tiktokapi import api
api = api.Api()
videos = api.get_user_videos("maskofshiva")
for video in videos:
    print(video)
    print(api.get_meta_title(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
```
