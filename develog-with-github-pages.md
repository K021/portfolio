

<h1 class='header'><span>GitHub Pages</span></h1>




### 참고 자료

##### 공식 문서
- [깃헙: 정적 사이트 생성기로 Jekyll 사용하기](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)
- [정적사이트생성기](https://staticsitegenerators.net) 

##### 블로그 - Jekyll 기반
- [kakao 기술 블로그: 기술 블로그가 GitHub Pages로 간 까닭은](http://tech.kakao.com/2016/07/07/tech-blog-story/)
- [labs: jekyll을 이용한 Github 블로그 만들기](http://labs.brandi.co.kr/2018/05/14/chunbs.html)
- [dreamgonfly: 쉽고 빠르게 수준 급의 GitHub 블로그 만들기 - jekyll remote theme으로](https://dreamgonfly.github.io/2018/01/27/jekyll-remote-theme.html)

##### 블로그 - Hugo 기반
- [cloudz-labs-tech: Hugo를 활용한 기술 블로그 구축기](http://tech.cloudz-labs.io/posts/hugo/hugo/)


### 참고할 디자인
- [힌 바탕에 파란 글씨](https://mingrammer.com/underscore-in-python/)


# 테마 고르기 - Hugo



## Meghna
[](img/develog-with-github-pages/meghna-hugo.png)
> [Meghna](https://themes.gohugo.io/meghna-hugo/), [미리보기 페이지](https://themes.gohugo.io/theme/meghna-hugo/)

블랙톤의, 이미지를 많이 쓰고 깔끔하며, 전문적이다. 그러면서도 빠르다. 아직 이만한 테마를 보지 못했다.  



## Reveal
[](img/develog-with-github-pages/reveal-hugo.png)
> [Reveal](https://themes.gohugo.io/reveal-hugo/), [미리보기 페이지](https://themes.gohugo.io/theme/reveal-hugo/)

프레젠테이션 스타일 테마. `e02c6c` 위 테마에서 사용한 핫핑크로, 아주 강렬하다. 매력적이다. 다음에 쓸 생각. `101010` 블랙을 사용했다.  



## Doc Dock
[](img/develog-with-github-pages/doc-dock.png)
> [Doc Dock](https://themes.gohugo.io/docdock/), [미리보기 페이지](https://themes.gohugo.io/theme/docdock/)

오픈소스 문서 사이트로 활용하기에 딱 좋은 디자인. 완성도는 100% 라고 보면 된다. 아주 전문적이다. 비슷한 계열로 [Materialdocs](https://themes.gohugo.io/theme/material-docs/), [Alabaster](https://themes.gohugo.io/theme/hugo-alabaster-theme/) 가 있다.



## Even
[](img/develog-with-github-pages/even.png)
> [Even](https://themes.gohugo.io/hugo-theme-even/), [미리보기 페이지](https://themes.gohugo.io/theme/hugo-theme-even/)

간결하고 깔끔하면서도 밉지 않고, 다양한 기능이 있는 테마.



## Elate
[](img/develog-with-github-pages/elate.png)
> [Elate](https://themes.gohugo.io/hugo-elate-theme/), [미리보기 페이지](https://themes.gohugo.io/theme/hugo-elate-theme/)

스타트업 소개 페이지로 사용하면 딱 좋을 것 같은 디자인.



## Orbit	
[](img/develog-with-github-pages/orbit.png)
> [Orbit](https://themes.gohugo.io/hugo-orbit-theme/), [미리보기 페이지](https://themes.gohugo.io/theme/hugo-orbit-theme/)

간단하게 내 이력을 보여줄 수 있는 테마.



## GitHub Pages

GitHub 저장소의 내용을 웹 페이지로 서비스해주는 기능이다. 정적 컨텐트만 서비스할 수 있다. 주로 문서 사이트로 사용된다. 그러나 정적 사이트 생성기를 사용하면 더 고급 기능을 간편하게 사용할 수 있다. `Jekyll` 은 GitHub Pages 가 기본적으로 지원하는 정적 사이트 생성기이다. 주로 markdown 을 사용하는 소스를 깃헙에 올리면, 깃헙 서버는 Jekyll 을 실행해서 정적 사이트를 생성한다.  

> 엄청나게 많은 정적 사이트 생성기를 볼 수 있다. 인기도(stars) 순으로 정렬할 수 있다. &mdash; https://staticsitegenerators.net  
> 오픈소스 라이선스 별 특징 정리 &mdash; [OPEN SOURCE 라이선스 별 특징 정리](https://ldap.or.kr/open-source-라이선스-별-특징-정리/)



## 정적 사이트 생성기
> [nacyot &mdash; 정적 웹사이트 생성기의 역습](https://blog.nacyot.com/articles/2014-01-15-static-site-generator/)

##### 정적 사이트는 서버에서 html를 수정없이 보내주는 것
`SSG` (Static Site Generator) 에서 '정적 사이트'라는 의미는, 우리가 일반적으로 말하는 정적인 웹을 의미하는 것이 아니다. 후자의 경우는 CSS 만을 기반으로 클라이언트 차원에서 HTML의 수정이 없는 웹을 의미한다. 하지만 전자의 경우는 서버 차원에서 템플릿의 수정 없이, 이미 만들어져있는 html을 보내주기만 하는 것을 의미한다. 

##### 정적 사이트의 필요성
- 동적사이트에 비해 가볍다. 
- 동적사이트에 비해 간단하다.
- 동적사이트가 필요 없는 경우가 많다. 



## 정적 사이트 생성기의 대표 2개

> 더 많은 정적 사이트 생성기는 여기서 &mdash; https://staticsitegenerators.net 

#### Jekyll
- Ruby로 제작되었기 때문에 커스터마이징은 Ruby를 알아야 가능하다.
- SSG 시장의 1위이기 때문에 테마나 플러그인 등이 가장 풍부하다. 
- 단점으로는 빌드할 페이지 숫자가 많아질수록 빌드 속도가 기하급수적으로 느려진다.
- Github Pages에 내장되어 있으므로 일반적으로 사용하기에는 제일 무난하다.

#### Hugo
- 인기순위 랭킹 2위 
- Go로 개발되었고, 빌드 속도가 엄청나게 빠르다. 문서 작성 단계에서 실시간으로 브라우저에서 확인이 가능할 정도. 




# Jekyll 로 GitHub Pages 사용하기

> &mdash; <cite>[help.github.com: Using Jekyll as a static site generator with GitHub Pages](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)</cite>





# Hugo 를 정적 사이트 생성기로 사용하기

> &mdash; <cite>[help.github.com: Using a static site generator other than Jekyll](https://help.github.com/articles/using-a-static-site-generator-other-than-jekyll/)</cite>  
> &mdash; <cite>[Hugo 공식 문서](https://gohugo.io)</cite>  
> &mdash; <cite>[cloudz-labs: Hugo를 활용한 기술 블로그 구축기](http://tech.cloudz-labs.io/posts/hugo/hugo/)</cite>

깃헙 페이지는 모든 html 과 정적 파일을 지원한다. 그렇기 때문에 원한다면 어떤 정적 사이트 생성기라도 사용될 수 있다. 심지어는 html 파일만 올려도 되고, build process costomizing 을 로컬 또는 다른 서버에서 할 수도 있다. 

다른 정적 사이트 생성기와 Jekyll 의 가장 큰 차이점은 `build process` 뿐이다. Jekyll 을 사용할 경우, 별도의 Build 과정 없이 저장소에 푸시하기만 하면 배포된다. 그러나 다른 정적 사이트 생성기의 경우 빌드 과정이 핑요하다. 더 많은 정보는 [About GitHub Pages and Jekyll](https://help.github.com/articles/about-github-pages-and-jekyll) 을 참조하자.



## non-Jekyll site 를 위한 build process 

1. 선택한 정적 사이트 생성기의 지침을 따라 로컬에서 빌드하세요. 이 작업은 아마 여러분의 정적 파일들은 특정 branch에 넣는 작업을 포함할 것입니다.
2. 선택한 정적 사이트 생성기가 여러분의 사이트를 로컬에서 빌드할 것입니다.
3. 빌드된 정적 파일을 여러분 페이지의 publishing branch 에 푸시합니다. (유저 사이트의 경우에는 `master`, 프로젝트 사이트의 경우에는 `gh-pages`입니다. 더 자세한 내용은 [User, Organization, and Project Pages](https://help.github.com/articles/user-organization-and-project-pages/)을 참조하세요)
4. GitHub Pages 에서 여러분의 사이트를 배포합니다.

> ##### 주의 사항
> 다른 정적 사이트 생성기를 사용할 경우, 반드시 해당 문서를 참조해 빌드해야 합니다. 빌드 과정에서 그 생성기만의 과정이 있을 수 있기 때문입니다.
> 
> ##### 유저 페이지와 프로젝트 페이지의 차이
> 유저 페이지는 깃헙 저장소를 아예 하나 파고, 프로젝트 페이지는 프로젝트 저장소를 사용한다. 따라서, 유저 페이지는 `master` 브랜치 에서, 프로젝트 페이지는 `gh-pages` 브랜치에서 사이트를 관리하게 된다. 이름이 정해져있다.  
> 
> &mdash; <cite>[help.github.com: User, Organization, and Project Pages](https://help.github.com/articles/user-organization-and-project-pages/)</cite>






# Hugo Site 만들기



## Hugo 설치 (macOS)
```bash
brew install hugo
```
> brew 설치는 어디서 해도 상관없다. 컴퓨터 전체에 설치되기 때문이다.  
> macOS 가 아닐 경우 [설치방법](https://gohugo.io/getting-started/installing)

설치가 완료되면 다음과 같이 출력된다. 

```bash
==> Downloading https://homebrew.bintray.com/bottles/hugo-0.51.sierra.bottle.tar
######################################################################## 100.0%
==> Pouring hugo-0.51.sierra.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/hugo/0.51: 32 files, 37.5MB
```
다음 명령으로 설치가 잘 되었는지 확인하자.

```bash
hugo version
```
```bash
~/projects/develog » hugo version                       
Hugo Static Site Generator v0.51/extended darwin/amd64 BuildDate: unknown
```



## 새로운 사이트 생성

```bash
hugo new site k021
```
> k021 은 내가 만들고자 하는 사이트 이름이다. 해당 이름으로 폴더가 생성된다. 

결과 창:

```bash
Congratulations! Your new Hugo site is created in /Users/ElohimAwmar/projects/develog/k021.

Just a few more steps and you're ready to go:

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/, or
   create your own with the "hugo new theme <THEMENAME>" command.
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

Visit https://gohugo.io/ for quickstart guide and full documentation.
```

생성된 디렉토리 구조:

```bash
k021/
	- archetypes/	- config.toml	- content/	- data/	- layouts/	- static/	- themes/
```



## 테마 적용하기

> 더 많은 테마는 [themes.gohugo.io](https://themes.gohugo.io/) 에서 볼 수 있으며, 약 100 여개의 테마 중 가장 괜찮아보이는 것들을 아래에 정리해두었다.  

아래의 명령은 바로 위에서 생성한 `k021` 폴더에서 실행한다. 

```bash
>>> cd k021
>>> git init
# git submodule add 저장소주소.git themes/테마이름
>>> git submodule add https://github.com/themefisher/meghna-hugo.git themes/meghna
```
그러면 다음과 같은 정보가 출력된다. 

```bash
her/meghna-hugo.git themes/meghna
Cloning into '/Users/ElohimAwmar/projects/develog/k021/themes/meghna'...
remote: Enumerating objects: 193, done.
remote: Counting objects: 100% (193/193), done.
remote: Compressing objects: 100% (147/147), done.
remote: Total 193 (delta 18), reused 192 (delta 17), pack-reused 0
Receiving objects: 100% (193/193), 3.44 MiB | 695.00 KiB/s, done.
Resolving deltas: 100% (18/18), done.
```

테마를 사용하기 전에, 테마 폴더 아래에 있는 `.git` 폴더를 삭제해야 한다. 그렇지 않으면 git 으로 배포할 때 문제가 발생한다.


테마 정보를 설정 파일 `config.toml`에 기록한다. 이 이름은, `k021/theme` 아래에 있는 테마 폴더의 이름이어야 한다. 

```yaml
# config.toml
baseURL = "http://example.org/"
languageCode = "en-us"
title = "My New Hugo Site"
theme = "meghna"
```

간단하게 이렇게도 입력해줄 수 있다.

```bash
echo 'theme = "ananke"' >> config.toml
```



## 글 쓰기

```bash
hugo new posts/my-first-post.md
```

기본적인 설정이 기록된 markdown file 이 `k021/content/posts` 에 생성된다. 기록되는 기본사항은 다음과 같다

```
---
title: "My First Post"
date: 2018-11-16T14:40:27+09:00
draft: true
---
```

작성한 내용을 확인해보기 위해 로컬 서버를 돌려볼 수 있다. 기본 포트는 `1313` 이다. `draft = true` 로 설정되어 있는 문서도 배포하기 위해선 `-D` 옵션을 넣어준다. 

```bash
hugo server -D
```

서버를 실행하면 다음과 같은 정보가 출력된다.

```bash


                   | EN
+------------------+-----+
  Pages            |  71
  Paginator pages  |   0
  Non-page files   |   5
  Static files     | 220
  Processed images |   0
  Aliases          |   4
  Sitemaps         |   1
  Cleaned          |   0

Total in 527 ms
Watching for changes in /Users/ElohimAwmar/projects/develog/k021/{content,data,layouts,static,themes}
Watching for config changes in /Users/ElohimAwmar/projects/develog/k021/config.toml
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```



## Customize the Theme

사이트 설정은 `k021/config.toml`에 담겨있다. 간단한 것을 몇가지 살펴보자.

- `baseURL = "https://example.org/"`: 개인 도메인을 사용하는 경우, 설정한다. 
- `title = 'My Site Name'`: 내 홈페이지 탭에 표시되는 이름
- `theme = 'docdock'`: `k021/themes/` 하위의 테마 디렉토리 이름

사이트의 설정을 변경하면, 배포된 서버에 즉각적으로 반영된다. 바로 반영되지 않는 것 처럼 보인다면, 캐쉬를 지우자. 