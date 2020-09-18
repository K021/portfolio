## hack process

### 영상 network 감시
1. 영상을 볼 수 있는 노마드 페이지에서 영상 클릭할 때 network 감시
	- 영상 정보를 담은 json 파일을 볼 수 있음
- 영상 설정에서 해상도를 클릭할 때 network 감시
	- 해상도별 영상 링크를 알 수 있으나, 해쉬값이 포함되어 있어 자동화하기 어려움
- 영상 설정에서 자막을 클릭할 때 network 감시
	- 자막 파일을 알 수 있음

1번에서 볼수 있는 json 파일은, 영상 당 하나씩 부여되는 랜덤 key 값을 알면 api 로 받아올 수 있다. 그러므로, 기본 페이지에서 key 값을 가져오는 방법을 알아야 한다. 

### 첫 페이지 html 에서 key 검색
> 찾으려는 key = byrmti58n7

qy3w117hdn

크롬 요소 검사의 html 보기에서 `byrmti58n7` 검색하면, 다음과 같은 태그를 발견할 수 있다.
	
```python
<div class="attachment-wistia-player stillSnap=false wistia_embed videoFoam=true" data-wistia-id="byrmti58n7" id="wistia-byrmti58n7"></div>
```

```python
In [76]: soup.select('div.attachment-wistia-player')
Out[76]: [<div class="attachment-wistia-player stillSnap=false wistia_embed videoFoam=true" data-wistia-id="byrmti58n7" id="wistia-byrmti58n7"></div>]

In [77]: div = soup.select('div.attachment-wistia-player')[0]

In [78]: div['data-wistia-id']
Out[78]: 'byrmti58n7'
```

### key 로 영상 데이터를 담은 json 파일 호출
```python
media_url_base = 'https://fast.wistia.com/embed/medias/'
media_key = div['data-wistia-id']
media_url = media_url_base + media_key +'.json'
r = requests.get(media_url)
r.json()
```

### json 파일에서 영상 url 추출
```python
In [93]: r.json()['media']['assets'][0]
Out[93]:
{'type': 'original',
 'slug': 'original',
 'display_name': 'Original file',
 'width': 2560,
 'height': 1600,
 'ext': 'mp4',
 'size': 13741817,
 'bitrate': 1456,
 'public': True,
 'status': 2,
 'progress': 1.0,
 'url': 'https://embed-ssl.wistia.com/deliveries/210bbec7ff82a21669259d233a14a18bf6971314.bin',
 'created_at': 1508085149}
 
In [94]: r.json()['media']['assets'][0]['url']
Out[94]: 'https://embed-ssl.wistia.com/deliveries/210bbec7ff82a21669259d233a14a18bf6971314.bin'
```

### 해당 url 에서 영상 받아와서 저장
```python
In [94]: video_url = r.json()['media']['assets'][0]['url'][:-3] + 'mp4'
Out[94]: 'https://embed-ssl.wistia.com/deliveries/210bbec7ff82a21669259d233a14a18bf6971314.mp4'

In [95]: stream = requests.get(video_url)

In [96]: with open('test.mp4', 'wb') as f:
    ...:     f.write(stream.content)
    ...:
```


## wistia data source
- [영상 정보 json 파일](https://fast.wistia.com/embed/medias/byrmti58n7.json)
- [자막 web vtt file](https://fast.wistia.net/embed/captions/byrmti58n7.vtt)

## Requests package
- [Document](http://docs.python-requests.org/en/master/user/advanced/#post-multiple-multipart-encoded-files)


## wistia video download search
- [google search: download video from fast.wistia.net](https://www.google.co.kr/search?q=download+video+from+fast.wistia.net&rlz=1C5CHFA_enKR720KR720&oq=fast+wistia+video+downlo&aqs=chrome.1.69i57j0.19779j0j7&sourceid=chrome&ie=UTF-8)
- [quora: How to download embedded Wistia videos](https://www.quora.com/How-can-you-download-embedded-Wistia-videos)
- [reddit: Does anyone know how to download Wistia videos?](https://www.reddit.com/r/Piracy/comments/7odrt9/does_anyone_know_how_to_download_wistia_videos/)
- [Wistia Video Downloader, Online Video Downloader](http://wistia.online-downloader.com/)


## python executable file argument
- [google search: python executable file argument](https://www.google.co.kr/search?q=python+executable+file+argument&rlz=1C5CHFA_enKR720KR720&oq=python+executable+file+argument&aqs=chrome..69i57.8707j0j7&sourceid=chrome&ie=UTF-8)
- [quora: How do I make executable file from python which should take arguments?](https://www.quora.com/How-do-I-make-executable-file-from-python-which-should-take-arguments)
