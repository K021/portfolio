<h1 class="header"><span>Python YouTube Crawler</span></h1>


파이썬에서 유튜브 영상을 다운받을 수 있게 해주는 패키지는 `pytube` 와 `pafy` 가 있다. 

##### pytube 관련 문서
- [readthedocs](https://python-pytube.readthedocs.io/en/latest/user/install.html)
- [github](https://github.com/nficano/pytube)

##### pafy 관련 문서
- [readthedocs](https://pythonhosted.org/Pafy/)


### 지금까지 알아낸 사실

- `pafy`의 다운로드 속도가 더 빠르다.
- `pafy`를 사용하려면 `youtube-dl`를 설치해야 한다. 둘다 `pip install`로 설치한다. 
- 그런데 `pytube`를 더 많이 쓰는 것 같다.
- `pytube`의 다운로드 로직은, url 의 response를 chunk 단위로 읽어서 파일로 저장하는 것 같다.