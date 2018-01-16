[깃 설명 페이지](https://git-scm.com/book/ko)

# Git
* https://git-scm.com/book/ko/v2
* 버전관리 도구
* 거의 모든 컴퓨터 파일의 버전관리 가능. 파일 변화를 시간에 따라 기록. 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템. 소스코드 뿐 아니라 디자인도 가능. 
* 프로젝트 하나당 지렉토리 하나. 
* `vi .gitignore` 깃에 커밋하지 않을 파일명 저장. https://en.wikipedia.org/wiki/Glob_(programming) 언어 사용. file-glob pattern
* https://www.gitignore.io/ .gitignore에 적어둬야 하는 내용을 시스템 별로 찾아볼 수 있는 곳이다. ruby, mac, lynux, jekyll 등으로 찾아보면 된다. 
* `doc/**/*.pdf` 중간 디렉토리가 몇이든 상관 없음
* `git diff` 파일 변경 상황 보기
* https://education.github.com
* git 영상 및 설명

* working tree, staging area, git directory
* `Git repository`: 깃 저장소. 파일이나 폴더를 저장해 두는 곳. 파일이 변경 이력 별로 구분되어 저장된다. =`.git directory`: 프로젝트의 메타데이터와 객체 데이터베이스를 저장한다. 다른 컴퓨터에 있는 저장소를 Clone할 때 git directory가 만들어진다.
	* `Remote Repository`원격 저장소 `Local Repository`개인 저장소
	* 내 컴퓨터에 로컬 저장소를 만드는 방법은 두 가지다. 새로 만들거나 이미 만들어진 원격 저장소를 복사해오는 것.

* working tree는 프로젝트의 특정 버전을 checkout한 것. git directory안에 압축된 데이터베이스에서 파일을 가져와서 워킹트리를 만든다.
* staging area는 git directory에 있다. 단순한 파일이고 곧 커밋할 파일에 대한 정보를 저장한다. index라고 불리기도 하지만, staging area가 표준이 되어가고 있다. 
* 깃으로 하는 일은 기본적으로 다음과 같다. 
* 워킹 트리에서 파일 수정
* staging area에 파일 stage. 커밋할 스냅샷 생성.
* staging area에 있는 파일들 커밋. git 디렉토리에 영구적인 스냅샷으로 저장. 

***

* git은 디렉토리 단위로 파일을 관리한다. 특정 폴더를 저장소로 지정하면 해당 폴더에 저장되는 파일과 하위 폴더들이 git의 관리 대상이 된다. 
* git은 파일을 untracked, tracked, unstaged, staged로 나누어 관리한다. 정확히는 세 단계이다. untracked, tracked(unstaged), tracked(staged), 처음 add 명령어를 사용하게 되면 3단계가 되고, 이 파일이 수정될 경우 2단계로 다뤄진다. 따라서 1단계 파일과 2단계 파일 모두 add하면 3단계의 파일이 되는 것. 그리고 한 번 add된 파일은 1단계로 내려가지 않는다. 
* tracked: 이력관리 대상.
* staged: 이력저장(commit) 대상.
![](https://git-scm.com/book/en/v2/images/lifecycle.png)
* 커밋 내용을 쉽게 파악하기 위해 커밋할 때마다 메모를 적어준다. 
* `git add filename`: untraced 파일을 tracked 파일로 변환. git add 명령은 파일 또는 디렉토리의 경로를 인수(argument)로 받는다. 디렉토리를 add할 경우, 그 하위의 모든 파일들을 추가한다. add는 파일을 다음 커밋에 추가한다고 보면된다. 
* `git commit -m '커밋 설명'` : 변경 이력을 개별 파일의 형태로 저장한다. -m 은 메세지를 뜻하며, 해당 커밋이 어떤 내용을 포함하고 있는지를 설명한다. -m 이하를 입력하지 않으면 내장편집기인 vim이 실행된다. 거기서 입력하면 더 자세히 입력할 수 있다. a를 붙여 -am을 사용할 경우, tracked 파일을 staging 시킬 수 있다. git add의 약자인 듯.
* `git log` : commit 명령을 통해 저장된 로그를 볼 수 있다. 각각의 커밋정보는 고유의 해쉬코드(커밋 아이디)가 부여되므로 쉽게 구별할 수 있다. `git log --oneline --decorate`
* `git checkout 커밋아이디` : 이전의 커밋 파일을 불러올 수 있다. 커밋 아이디는 전체를 입력할 필요가 없다. 겹치기 않는 하나의 값을 찾아낼 수 있는 만큼이면 충분하다. checkout은 과거 기록을 불러와 작업하는 것이지 복원을 하는 것이 아니다. 복원을 원한다면 그 뒤에 파일명이 와야 한다. `git checkout 커밋아이디 파일명` 
* `git checkout master` : 마스터 브랜치(최초 프로젝트본, 최초 생성되는 기본 브랜치. 보통 마지막 작업시점)로 이동
* git working flow : git local repository는 git이 관리하는 세 부분으로 구성되어 있다. 
	* working directory : 실제 파일들로 구성
	* index(staging area) : 준비영역
	* head
* `git rm --cached 파일이름` : working directory file은 남겨둔 채로 git의 tracking 대상에서만 삭제한다. --cached를 빼고 `git rm 파일이름`만 쓰면 실제 파일도 삭제된다. 
* staging area를 git index 라고도 부른다.
* `git push [리모트 저장소 이름] [브랜치 이름]` : 커밋정보를 원격 저장소에 올리는 것. 프로젝트를 공유하고자 할 때 리모트 저장소에 Push한다. 
* `git push -u origin master` : -u는 원격 저장소에서 업데이트를 받은 후 push하는 명령어이다. 다른 사람과 함께 작업하는 경우, 다른 사람이 push한 후에 push하는 것이 불가능하기 때문에 -u의 습관적 사용을 권장한다. 
* 기존에 있던 원격 저장소를 복제한 것이 아니라면, 저장소 이름과 서버를 연결해줄 필요가 있다.` git remote add origin [원격서버주소]`
* 결국 변경사할 마다 해야 할 것은 `pull -> commit -> push`이다. 
* `git config credential.helper store `: 아이디와 비밀번호를 저장할 수 있는 기능이다.
* `.gitignore` 작성 규칙 : 
	* 아무것도 없는 줄이나, `#`로 시작하는 줄은 무시한다. 
	* 표준 Glob 패턴을 사용한다. 
	* 디렉토리는 슬래시(/)를 끝에 사용하는 것으로 표현한다. 
	* 느낌표(!)로 시작하는 패턴의 파일은 무시하지 않는다.
* `git reset HEAD 파일명` : unstage 명령
* `git checkout -- 파일명` : 수정정보(modified 상태의 파일)를 삭제하고, 파일을 마지막 커밋 상태로 되돌려 놓는 명령이다. 강력하니 조심하도록.




































## git 최초 설정
* <a name='커밋사용자정보'></a>사용자 정보 설정: git 설치 후 사용자 이름과 메일 설정. commit할 때마다 사용되는 정보이다. 한 번 커밋한 후 에는 정보를 변경할 수 없다. 
* 편집기 설정: 설정하지 않는다면, 시스템의 기본 편집기를 사용한다. `git config --global core.editor 편집기 이름`
* `git config --list` 명령을 실행하면 설정한 모든 것을 보여준다. 
* `git config <key>` 명령으로 Git이 특정 Key에 대해 어떤 값을 사용하는지 확인할 수 있다. `git config user.name`







## 도움말 보기
* 명령어 도움말
	* `git help <verb>`
	* `git <verb> --help`
	* `man git-<verb>`







## Git 저장소 만들기
* git 저장소를 만드는 방법은 두 가지이다. 기존 디렉토리를 깃으로 관리하거나, 다른 원격 저장소를 복사해오는 것.
* 기존 폴더를 저장소로 설정:
	* 폴더 생성
	* 터미널에서 해당 디렉토리 이동
	* `git init` : .git이라는 하위 디렉토리를 만든다. 이 안에는 저장소로 기능하기 위한 뼈대파일(Skeleton)이 들어있다. [.git 디렉토리 구성 상세내용](https://git-scm.com/book/ko/v2/Git과-여타-버전-관리-시스템-Git%3A-범용-Client)
	* 이제 이 디렉토리 안에 있는 파일은 git을 통해 관리할 수 있게 되며, git status로 파일의 관리 상태를 알 수 있다. `git status -s` 또는 `git status --short` 처럼 옵션을 주면 현재 변경 상태를 짤막하게 보여준다. [약식기호 의미](https://git-scm.com/docs/git-status#_short_format)
*  원격 저장소 복사: `git clone [url]` 명령을 사용한다. 이 명령은 원격 저장소 전체를 복사해온다.
	* `git clone git://github.com/schacon/grit.git` 이 명령은 `grit`이라는 디렉토리를 만들고 그 안에 `.grit` 디렉토리를 만든다. 저장소의 모든 정보 중 최신 버전을 `checkout`해 놓는다. `git clone git://github.com/schacon/grit.git mygritname`: 마지막에 폴더 이름을 설정할 수 있다. 
	* git은 다양한 프로토콜을 지원한다. `git://`말고도 `http(s)://`를 사용할 수도 있고 `user@server:/path.git`처럼 SSH 프로토콜을 사용할 수도 있다. [자세한 내용](https://git-scm.com/book/ko/v2/Git-서버-프로토콜)







## 수정하고 저장소에 저장하기
* `git add`
* `git status`

### 변경사항 확인하기
* `git diff`: 단순히 파일이 변경됐다는 사실이 아니라 어떤 내용이 변경됐는지 알 수 있다. 이 명령은 unsatged 상태인 파일의 수정사항만을 보여준다. [git diff 구문읽기](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/diffs)
* 만약 커밋하려고 Staging Area에 넣은 파일의 변경 부분을 보고 싶으면 `git diff --staged` 옵션을 사용한다. 이 명령은 저장소에 커밋한 것과 Staging Area에 있는 것을 비교한다.

### 변경사항 커밋하기
* git commit
	* 편집기 실행.
	* -v 옵션: 편집기에 diff 메세지 추가.
	* :wq
	* -m 옵션: 약식. 메세지를 인라인 첨부 `git commit -m "Story 182: Fix benchmarks for speed"`

### staging area 생략하기
* Staging Area는 커밋할 파일을 정리한다는 점에서 매우 유용하지만 복잡하기만 하고 필요하지 않은 때도 있다. 아주 쉽게 Staging Area를 생략할 수 있다. 
* `git commit -a`: Git은 Tracked 상태의 파일을 자동으로 Staging Area에 넣는다. 그래서 git add 명령을 실행하는 수고를 덜 수 있다.
* 편리한 옵션이긴 하지만 주의 깊게 사용해야 한다. 생각 없이 이 옵션을 사용하다 보면 추가하지 말아야 할 변경사항도 추가될 수 있기 때문이다.  

### 파일 삭제하기
* Git에서 파일을 제거하려면 `git rm <filename>` 명령으로 Tracked 상태의 파일을 삭제한 후에(정확하게는 Staging Area에서 삭제하는 것) 커밋해야 한다. 이 명령은 워킹 디렉토리에 있는 파일도 삭제하기 때문에 실제로 파일도 지워진다.
* `git rm`은 폴더에서 파일 삭제 후 커밋을 위해 stage까지 완료한다. 해당 명령어를 사용하지 않고 디렉토리에서 직접 파일을 삭제했다면, add 후에 commit 하면 된다.
* 이미 파일을 수정했거나 staging area에 추가했다면 `-f`옵션을 주어 강제로 삭제해야 한다. 이 것은 실수로 데이터를 삭제하는 것을 방지하기 위한 안전장치다. 커밋하지 않고 수정한 데이터는 Git으로 복구할 수 없기 때문이다.
* 워킹 디렉토리에는 남겨둔 채로 staging area에서만 제거하려면 `--cached`옵션을 사용한다. file-glob 패턴을 사용해 여러개의 파일이나 디렉토리를 한꺼번에 삭제할 수도 있다. 

### 파일 이름 변경하기
* git은 해쉬코드로 파일을 구분하지, 파일명으로 구분하지 않기 때문에, 파일의 이름 변경사항을 별도로 저장하지 않는다. 
* `git mv <file_from> <file_to>`
* 사실 git mv 명령은 아래 명령어를 수행한 것과 완전 똑같다.
	* `$ mv README.md README`
	* `$ git rm README.md`
	* `$ git add README`
	* git mv 명령은 일종의 단축 명령어이다. 이 명령으로 파일이름을 바꿔도 되고 mv 명령으로 파일이름을 직접 바꿔도 된다. 단지 git mv 명령은 편리하게 명령을 세 번 실행해주는 것 뿐이다. 어떤 도구로 이름을 바꿔도 상관없다. 중요한 것은 이름을 변경하고 나서 꼭 rm/add 명령을 실행해야 한다는 것 뿐이다.








## commit history 조회하기

`git log`: 커밋 로그 보기. 특별한 아규먼트 없이 `git log` 명령을 실행하면 저장소의 커밋 히스토리를 시간순으로 보여준다. 즉, 가장 최근의 커밋이 가장 먼저 나온다. 그리고 이어서 각 커밋의 체크섬, 저자 이름, 저자 이메일, 커밋한 날짜, 커밋 메시지를 보여준다.  

`git log -p`: 각 커밋의 diff(변경사항)를 보여준다.  
`git log -p -2`: 최근 두 개의 결과만 보여주는 옵션이다.   

`git log --stat`: 커밋의 통계 정보 표시 . 어떤 파일이 수정됐는지, 얼마나 많은 파일이 변경됐는지, 또 얼마나 많은 라인을 추가하거나 삭제했는지 보여준다. 요약정보는 가장 뒤쪽에 보여준다.  

`git log --decorate`: 브랜치를 보여준다.   
`git log --graph`: 브랜치와 머지 히스토리 정보까지 아스키 그래프로 보여준다.  
`git log --all`: 전체 로그를 보여준다.  
`git log --oneline --decorate --graph --all`: zsh shortcut: `gloga`


`git log --since=2.weeks`: 2주 전 부터 보여준다. 이 옵션은 다양한 형식을 지원한다. "2008-01-15" 같이 정확한 날짜도 사용할 수 있고 "2.years.1.day.3.minutes" 같이 상대적인 기간을 사용할 수도 있다.  

`git log -- path1 path2` 파일 경로에 제한을 두고 로그를 검색한다.   







## Git 되돌리기
`git commit --amend`: 커밋 되돌리기. 파일을 빼먹었거나 메세지를 잘못 적었을 때 사용한다.   

- 메세지를 잘못 적은 경우, `git commit --amend`
- 편집기가 실행되고, 이전 커밋 메세지가 포함되어 있다. 
- 메세지를 수정하지 않고 그대로 커밋해도 기존의 커밋을 덮어쓰게 된다. 

- 파일을 빠뜨린 경우, `add`하고 `amend`한다.

```bash
$ git commit -m 'initial commit' 
$ git add forgotten_file			# add하고
$ git commit --amend				# amend한다
```

`git reset HEAD <filename>`: staged 파일의 unstaged 변경  
`git checkout -- <filename>`: modified file을 최신 커밋 파일로 덮어씌움. 수정내용 삭제.  
> *git checkout과 reset은 꽤나 위험한 명령이다. 제한적으로 사용하자. 







## Remote 저장소
`git clone <url>`: 원격 저장소 불러오기  
`git remote -v`: 저장소의 단축 이름과 url을 볼 수 있다.  
`git remote add <저장소단축이름> <url>`: 디렉토리에 리모트 저장소 추가  
`git fetch <저장소단축이름>`: 로컬에는 없지만 리모트에는 있는 것을 가져온다.  
`git pull`: 리모트 저장소 브랜치에서 데이터를 가져올 뿐 아니라 자동으로 로컬 브랜치와 merge 시킨다.  
`git push <저장소단축이름> <브랜치이름>`  
`git remote rename <원래이름> <새이름>`: 저장소 이름 변경  
`git remote rm <저장소이름>`: 로컬에 연결된 저장소 삭제.  
`git remote show <저장소단축이름>`: 리모트 저장소의 구체적인 정보를 확인할 수 있다.    






## Git Branch

### 브랜치란 무엇인가

**커밋 개체**: 커밋할 때마다 생성되는 커밋 개체(Object)에는 데이터 스냅샷에 대한 포인터, 저자 혹은 커밋 메세지 같은 메타데이터, 이전 커밋에 대한 포인터 등을 포함한다.  

**Stage**: 파일을 Stage하게 되면, git 저장소에 파일을 저장하고(Blob) staging area에 해당 파일의 체크섬을 저장한다.  

**Commit**: 커밋하면, 트리 개체를 저장소에 저장한다. 트리 개체는 디렉토리 구조와 체크섬을 저장한다. 그리고 커밋 개체를 저장한다. 커밋 개체는 메타데이터와 트리 개체 포인터를 저장한다. 따라서 3 종류의 데이터 개체가 생긴다. 각 파일에 대한 Blob 3개, 트리 개체, 커밋 개체 하나.  

**Branch**: 브랜치는 커밋 사이를 이동할 수 있는 포인터 같은 것이다. 기본적으로 git은 master 브랜치를 만들고, 이후 커밋을 만들면 브랜치는 자동으로 마지막 커밋을 가리킨다. 


### 새 브랜치 만들고 이동하기

`git branch <branchname>`: 브랜치를 만든다. 새로 만든 브랜치는 작업 중이던 커밋을 가리킨다.  
`git checkout <branchname/checksum>`: 해당 브랜치/커밋으로 이동한다. 
`git checkout -b <branchname>`: 새 브랜치를 만들면서 checkout하기   

### 브랜치 관리

`git branch`: 브랜치 목록   
`git branch -v`: 브랜치 목록 및 마지막 커밋 메세지  
`git branch -a`: 리모트 브랜치 목록까지 포함  
`git branch --merged`: 현재 활성 브랜치와 merge되어 있는 브랜치 목록  
`git branch --no-merged`  
`git branch -d <branchname>`: 브랜치 삭제  
`git branch -D <branchname>`: 브랜치 강제 삭제. 커밋이 merge 되지 않은 경우 강제로 삭제 해야만 삭제가 된다. `-D`는 `-d -f`또는 `-df`로 대체될 수 있다.
`git merge <branchname>`: merge branch

### 리모트 브랜치
`<remote-name>/<remote-branch>`: 리모트 저장소의 브랜치를 카리킨다.  
`git ls-remote <remote-name>`: 모든 리모트 Reference를 조회할 수 있다. ref는 리모트 저장소에 있는 브랜치 태그 등등을 의미한다는데 잘 모르겠다.  
`git remote show <remote-name>`: 리모트 저장소의 구체적인 정보를 확인할 수 있다.  
`git fetch <remote-name>`: 리모트 저장소의 정보를 로컬에 업데이트 한다.   


### Remote repository stale branch 로컬에서 삭제하기
`git remote show <저장소단축이름>`: 리모트 저장소의 구체적인 정보를 확인할 수 있다. 리모트 저장소의 URL과 추적하는 브랜치를 출력한다. 이 명령은 git pull 명령을 실행할 때 master 브랜치와 Merge 할 브랜치가 무엇인지 보여 준다.   



```
➜  delta git:(feature/form) ✗ git remote show delta
* remote delta
  Fetch URL: https://github.com/K021/delta.git
  Push  URL: https://github.com/K021/delta.git
  HEAD branch: master
  Remote branches:
    dev                             tracked
    master                          tracked
    refs/remotes/delta/feature/form stale (use 'git remote prune' to remove)
  Local branches configured for 'git pull':
    dev    merges with remote dev
    master merges with remote master
  Local refs configured for 'git push':
    dev    pushes to dev    (local out of date)
    master pushes to master (up to date)
``` 
```
refs/remotes/delta/feature/form stale (use 'git remote prune' to remove)
```

: 리모트 저장소에 있던 브랜치가 삭제되었지만, 로컬 정보에 남아있는 것이다. 이것을 없에주기 위해선 `git remote prune <저장소이름>`을 입력하면 된다. `--dry-run`옵션을 적용하면 프룬 전에 어떤 브랜치를 프룬하게 되는지 확인할 수 있다.







## 조교님 깃, vim 수업
**stash**   
git stash: 변경내역 임시 저장. -u 붙이면 untracked file까지  
git stash pop: 어느 브랜치에서도 팝 가능. 단 해당 변경사항에 필요한 파일이 그 브랜치에 있다면.  
git stash list  
*stash는 로그에 뜬다.   
- git partial stash

**검색**   
git alias (~/.zshrc)   
git zsh shortcut  
vim cheet sheet  

**zsh**   
`/검색어`: 검색. n은 다음 단어   
`caw` 한 단어 삭제 후 편집  
`u`: undo  
`d`: 한 줄 삭제   
`dt*`: * 앞 까지 삭제  
`ci[()]`: change in () 괄호 안 삭제 후 작성.  
* [git-zsh-shortcut](#git-zsh-shortcut)






## 조교님 pyenv 설정

강사님 블로그 : https://lhy.kr/configuring-the-python-development-environment-with-pyenv-and-virtualenv   

`pyenv virtualenv 3.6.2 practice`: practice 이름의 가상환경을 python 3.6.2 버전으로 설치  
`pyenv versions`: 가상 환경 버전 확인  
`pyenv local practice` : 폴더에 가상환경 적용. .python-version 파일 생성. 파일 안에는 가상환경 이름 밖에는 없다.  
`pip install ipython`: ipython 설치. 터미널 파이썬 사용을 편하게 해주는 패키지.
`pyenv uninstall practice`: 가상환경 삭제







# 공부할 것

* `https://git-scm.com/docs/git-status#_short_format`와 같이 html상의 id값을 찾아내어 맨 뒤에 붙이면 그 위치를 불러올 수 있다. id값은 요소검사로 알아낼 수 있다. 
* sorting video (Youtube)








# 질문  

* 한 번 커밋하면 사용자 정보를 바꿀 수 없다고 하던데, 무슨 뜻인가. 커밋한 파일을 누가 썼는지를 바꿀 수 없다는 것인가 아니면 내 로컬 저장소에 설정한 사용자 정보를 바꿀 수 없다는 것인가. [메모](#커밋사용자정보)
*  `git rm log/\*.log`에서 \는 왜 필요하다고? [link](https://git-scm.com/book/ko/v2/Git의-기초-수정하고-저장소에-저장하기#_removing_files)
*  terminal log를 볼 수 있나요






# 기타 정보

맥 영상 플레이어: `IINA`   
애플 제품 살 때는 학생 할인을 받기: `AOC apple on campus.`  
마크다운 프레젠테이션 도구 `Marp`:  [link](https://yhatt.github.io/marp/)  

구도: 화면분할, 닫힘 열림, 내려다보기 올려보기,  
강조: 무엇을 버릴 것인가.  








# 부록

1. **git-zsh-shortcut** <a name='git-zsh-shortcut'></a>   

```
zsh git shortcut (~/.oh-my-zsh/plugins/git/git.plugin.zsh)

alias g='git'

alias ga='git add'
alias gaa='git add --all'
alias gapa='git add --patch'
alias gau='git add --update'

alias gb='git branch'
alias gba='git branch -a'
alias gbd='git branch -d'
alias gbda='git branch --no-color --merged | command grep -vE "^(\*|\s*(master|develop|dev)\s*$)" | command xargs -n 1 git branch -d'
alias gbl='git blame -b -w'
alias gbnm='git branch --no-merged'
alias gbr='git branch --remote'
alias gbs='git bisect'
alias gbsb='git bisect bad'
alias gbsg='git bisect good'
alias gbsr='git bisect reset'
alias gbss='git bisect start'

alias gc='git commit -v'
alias gc!='git commit -v --amend'
alias gcn!='git commit -v --no-edit --amend'
alias gca='git commit -v -a'
alias gca!='git commit -v -a --amend'
alias gcan!='git commit -v -a --no-edit --amend'
alias gcans!='git commit -v -a -s --no-edit --amend'
alias gcam='git commit -a -m'
alias gcsm='git commit -s -m'
alias gcb='git checkout -b'
alias gcf='git config --list'
alias gcl='git clone --recursive'
alias gclean='git clean -fd'
alias gpristine='git reset --hard && git clean -dfx'
alias gcm='git checkout master'
alias gcd='git checkout develop'
alias gcmsg='git commit -m'
alias gco='git checkout'
alias gcount='git shortlog -sn'
compdef _git gcount
alias gcp='git cherry-pick'
alias gcpa='git cherry-pick --abort'
alias gcpc='git cherry-pick --continue'
alias gcs='git commit -S'

alias gd='git diff'
alias gdca='git diff --cached'
alias gdct='git describe --tags `git rev-list --tags --max-count=1`'
alias gdt='git diff-tree --no-commit-id --name-only -r'
alias gdw='git diff --word-diff'

gdv() { git diff -w "$@" | view - }
compdef _git gdv=git-diff

alias gf='git fetch'
alias gfa='git fetch --all --prune'
alias gfo='git fetch origin'

function gfg() { git ls-files | grep $@ }
compdef _grep gfg

alias gg='git gui citool'
alias gga='git gui citool --amend'

ggf() {
  [[ "$#" != 1 ]] && local b="$(git_current_branch)"
  git push --force origin "${b:=$1}"
}
compdef _git ggf=git-checkout

ggl() {
  if [[ "$#" != 0 ]] && [[ "$#" != 1 ]]; then
    git pull origin "${*}"
  else
    [[ "$#" == 0 ]] && local b="$(git_current_branch)"
    git pull origin "${b:=$1}"
  fi
}
compdef _git ggl=git-checkout

ggp() {
  if [[ "$#" != 0 ]] && [[ "$#" != 1 ]]; then
    git push origin "${*}"
  else
    [[ "$#" == 0 ]] && local b="$(git_current_branch)"
    git push origin "${b:=$1}"
  fi
}
compdef _git ggp=git-checkout

ggpnp() {
  if [[ "$#" == 0 ]]; then
    ggl && ggp
  else
    ggl "${*}" && ggp "${*}"
  fi
}
compdef _git ggpnp=git-checkout

ggu() {
  [[ "$#" != 1 ]] && local b="$(git_current_branch)"
  git pull --rebase origin "${b:=$1}"
}
compdef _git ggu=git-checkout

alias ggpur='ggu'
compdef _git ggpur=git-checkout

alias ggpull='git pull origin $(git_current_branch)'
compdef _git ggpull=git-checkout

alias ggpush='git push origin $(git_current_branch)'
compdef _git ggpush=git-checkout

alias ggsup='git branch --set-upstream-to=origin/$(git_current_branch)'
alias gpsup='git push --set-upstream origin $(git_current_branch)'

alias ghh='git help'

alias gignore='git update-index --assume-unchanged'
alias gignored='git ls-files -v | grep "^[[:lower:]]"'
alias git-svn-dcommit-push='git svn dcommit && git push github master:svntrunk'
compdef _git git-svn-dcommit-push=git

alias gk='\gitk --all --branches'
compdef _git gk='gitk'
alias gke='\gitk --all $(git log -g --pretty=%h)'
compdef _git gke='gitk'

alias gl='git pull'
alias glg='git log --stat'
alias glgp='git log --stat -p'
alias glgg='git log --graph'
alias glgga='git log --graph --decorate --all'
alias glgm='git log --graph --max-count=10'
alias glo='git log --oneline --decorate'
alias glol="git log --graph --pretty='%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
alias glola="git log --graph --pretty='%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all"
alias glog='git log --oneline --decorate --graph'
alias gloga='git log --oneline --decorate --graph --all'
alias glp="_git_log_prettily"
compdef _git glp=git-log

alias gm='git merge'
alias gmom='git merge origin/master'
alias gmt='git mergetool --no-prompt'
alias gmtvim='git mergetool --no-prompt --tool=vimdiff'
alias gmum='git merge upstream/master'

alias gp='git push'
alias gpd='git push --dry-run'
alias gpoat='git push origin --all && git push origin --tags'
compdef _git gpoat=git-push
alias gpu='git push upstream'
alias gpv='git push -v'

alias gr='git remote'
alias gra='git remote add'
alias grb='git rebase'
alias grba='git rebase --abort'
alias grbc='git rebase --continue'
alias grbi='git rebase -i'
alias grbm='git rebase master'
alias grbs='git rebase --skip'
alias grh='git reset HEAD'
alias grhh='git reset HEAD --hard'
alias grmv='git remote rename'
alias grrm='git remote remove'
alias grset='git remote set-url'
alias grt='cd $(git rev-parse --show-toplevel || echo ".")'
alias gru='git reset --'
alias grup='git remote update'
alias grv='git remote -v'

alias gsb='git status -sb'
alias gsd='git svn dcommit'
alias gsi='git submodule init'
alias gsps='git show --pretty=short --show-signature'
alias gsr='git svn rebase'
alias gss='git status -s'
alias gst='git status'
alias gsta='git stash save'
alias gstaa='git stash apply'
alias gstc='git stash clear'
alias gstd='git stash drop'
alias gstl='git stash list'
alias gstp='git stash pop'
alias gsts='git stash show --text'
alias gsu='git submodule update'

alias gts='git tag -s'
alias gtv='git tag | sort -V'

alias gunignore='git update-index --no-assume-unchanged'
alias gunwip='git log -n 1 | grep -q -c "\-\-wip\-\-" && git reset HEAD~1'
alias gup='git pull --rebase'
alias gupv='git pull --rebase -v'
alias glum='git pull upstream master'

alias gwch='git whatchanged -p --abbrev-commit --pretty=medium'
alias gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify -m "--wip-- [skip ci]"'

```



