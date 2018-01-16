[Subicura - 도커란 무엇인가](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)  
[Subicura - 도커 설치, 컨테이너 실행](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)  
[Subicura - 도커 이미지 생성, 배포](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)  

pyenv는 파이썬 버전 관리를 위해서  
pyenv virtualenv는 파이썬 패키지를 관리하기 위해서  
docker는 서버가 돌아가기 위한 모든 환경을 관리하기 위해 존재한다.  

-리눅스에서는 네이티브로 돌아가고 나머지 운영체제에선 가상머신으로 돌아간다.(도커)  
-프로세스 격리기법으로 만든 것으로, 가볍다. 

도커에는 이미지와 컨테이너가 있다. 이미지는 개발에 관한 모든 설정 및 프로그램을 포함하고 있는 환경이고, 컨테이너는 그 이미지를 기반으로 실행되는 하나의 컴퓨터(프로세스)라고 할 수 있다.  

레이어 저장방식  
도커는 레이어 단위로 저장되기 때문에, 자원의 낭비가 없다. 어떤 이미지를 베이스로 새로운 이미지를 생성할 때, 추가된 정보를 저장하는 새 레이어가 생기고, 중복되는 레이어는 공유한다. 컨테이너도 이 레이어 저장방식에 따라 관리된다. 새로운 컨테이너를 생성하게 되면, 읽기/쓰기 레이어가 생기고, 컨테이너 변경사항은 모두 해당 레이어에 저장이된다. 따라서 이미지 파일에는 아무런 변화가 일어나지 않으며, 한 이미지를 기반으로 여러 컨테이너가 생성되어도 많은 용량을 차지하지 않는다.  

도커 이미지는 Docker hub를 통해 url 방식으로 관리된다.  
`docker.io/library/ubuntu:16.04`=`Dockerhub defalt url`/`<image name>`:`<tag name>`  

도커 이미지 생성 메타 정보는 `Dockerfile`에 작성한다.  


</br>


</br>


## 맥용 도커 설치  


[맥용 도커 설치 파일](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)  
맥에다 도커를 설치하는 과정은 여느 프로그램 설치와 다를 바 없어 보이지만, 도커는 리눅스 컨테이너이므로 실제로는 가상머신 위에 설치된다. (사용자가 가상머신을 사용하는 느낌이 들지 않도록 설계되었다. 포트 같은 경우, 맥의 포트와 도커의 포스 사이에 가상머신을 연결해줘야 하는데, 그 과정을 알아서 해준다. 또한 디렉토리를 연결하는경우에도, 해당 디렉토리를 가상머신과 공유하는 과정을 알아서 해준다.)  


### 설치 확인: 
`docker version`  
: 도커 클라이언트와 서버 정보가 출력된다.  
(도커 명령을 사용하기 위해서는 docker가 실행되고 있어야 한다. 그렇지 않으면 Server 버전 정보가 나오지 않는다.)(docker의 실행은 docker deamon의 실행을 말한다. `deamon`은 백그라운드에서 실행된다는 점에서, 사용자가 직접 통제하는 프로그램들과은 다르다.)(deamon: a computer program that runs as a background process, rather than being under the direct control of an interactive user)  
  
> 터미널을 통한 도커 명령 수행 과정  
`도커 커맨드 입력` - `도커 클라이언트` - `도커 서버`(Docker deamon - container) - `도커 클라이언트` - `터미널 출력`  
`docker version` 명령어로 확인한 도커 버전정보는 클라이언트와 서버로 나뉘어져 있다. 하나의 실행파일인 도커는 클라이언트와 서버의 역할을 동시에 수행한다. 터미널 명령어를 서버에 전달해주는 클라이언트와, 디먼을 통해 그 명령을 수행하는 서버가 있다. (여기서 서버는 호스트라고 하기도 한다.)  
![사진](./img/docker_client&server.png)  


</br>


</br>


## 컨테이너 실행하기  


### 컨테이너 실행  
`docker run ubuntu:16.04`=`docker run``<image name>`:`<tag name>`  

컨테이너 실행 옵션  
`-d`: `detached mode` 백그라운드 모드  
`-p`: 호스트(도커 서버)와 컨테이너의 포트를 연결 (포워딩) (예: `-p 1234:6379`=`-p``호스트포트`:`컨테이너포트`)  
`-v`: 호스트와 컨테이너의 디렉토리를 연결 (마운트)  
`-e`: 컨테이너 내에서 사용할 환경변수 설정  
`-name`: 컨테이너 이름 설정  
`--rm`: 프로세스 종료시 컨테이너 자동 제거  
`-it`: 터미널로 실행 (`i`와 `t` 옵션 중복 적용)  
`-link`: 컨테이너 연결  
([환경변수 설정에 관한 간단한 링크](https://hub.docker.com/_/mysql/))


### 우분투 컨테이너 생성
: `docker run ubuntu:16.04`  
`run` 명령어는 해당 이미지가 존재하지 않으면 다운로드(`pull`)한 후 컨테이너를 생성(`create)`하고 시작(`start`)한다.  
생성된 컨테이너는 특별히 실행해야할 명령이 없다면 바로 종료된다. 컨테이너는 프로세스임을 기억하자. 실행중인 프로세스가 없으면 컨테이너가 종료된다.  


### 우분투 컨테이너를 bash shell로 생성하기  
: `docker run --rm -it ubuntu:16.04 /bin/bash`  
우분투 이미지의 `/bin/bash` 프로그램을 터미널로 실행, 종료시 컨테이너 제거. 생성된 쉘은 늘 하듯 `exit`으로 종료하자. (`zsh`이 설치된 이미지라면 `bin/zsh`을 이용하자.)  


### 컨테이너 실행하면서 포트 연결하기
: `docker run --rm -it -p 8013:80 instagram /bin/zsh`  
instagram 이미지를 기반으로 생성된 컨테이너는 listen port 가 80 번 포트이다. 내 컴퓨터의 8013번 포트를 컨테이너의 80번 포트로 연결해주는 것. `-p 8012:8000 -p 8013:80`와 같이 한 번에 여러 포트를 열 수도 있다. 


### Request 에서 도커 기반 서버까지 요청이 전달정는 과정
: `Request` > `Ubuntu 가상환경` > `Docker` > `Ubuntu(in docker)` > `Nginx` > `Uwsgi` > `Django` 


</br>


</br>



## 도커 이미지 관리하기


* 목록 보기: `docker images` (다운로드 혹은 생성한 이미지를 볼 수 있다)
* 다운로드: `docker pull <image_name>:<tag_name>`  
* 제거: `docker rmi <img_ID>`  
* 이름 없는 이미지 모두 제거하기: `docker rmi -f $(docker images --filter "dangling=true" -q)` 


</br>


</br>


## 컨테이너 관리하기  


* 실행 목록: `docker ps` (ps: process)  
`-a`: 종료된 컨테이너까지 보여준다. 컨테이너는 종료되어도 삭제되지 않고 남아있으며, `STATUS` 값을 `Exited (0)`로 가진다. 종료된 컨테이너는 다시 시작할 수 있다. (`--rm` 옵션으로 실행하면 종료시  자동 삭제된다.)   
* 중지: `docker stop <container ID>` (컨테이너 ID 대신 이름을 입력할 수도 있다. ID는 전체를 입력할 필요가 없다.)  
* 제거: `docker rm <container ID>`  
* 중지된 컨테이너 한 번에 제거하기: `docker rm -v $(docker ps -a -q -f status=exited)`
* **실행중인 컨테이너에 들어가기**: `docker exec -it <container ID> /bin/zsh`  
\*`/bin/zsh`은 도커 이미지 안에 있는 하나의 경로일 뿐이다. 원한다면 DB 프로그램을 직접 실행할 수도 있다. 프로그램 실행 명령어를 입력할 수도, 프로그램이 있는 경로를 입력할 수도 있다.   


### 컨테이너의 로그 관리 방식  
도커는 표준 스트림(Standard streams) 중 stdout, stderr를 수집하는 방식으로 로그를 인식한다. 따라서 컨테이너 프로그램의 로그 설정이 파일이 아닌 표준출력이면, 같은 방식으로 모든 로그를 관리할 수 있다.  
컨테이너의 로그파일은 json 형식으로 어딘가에 저장이 된다. 로그가 용량을 잡아먹지 않도록 주의해야 한다. 도커는 다양한 플러그인을 지원하기 때문에, 외부 로그 서비스에 스트림을 전달할 수 있다. 프로그램의 규모가 어느 정도 이상으로 커지면 로그서비스를 이용하는 것을 고려해야 한다.  


### 컨테이너 로그 보기
: `docker logs --tail 10 <container_ID>`  
`--tail 10`: 마지막 10 줄만 출력한다.  
`-f`: 실시간 로그를 보여준다.  


### 도커에서 컨테이너 업데이트 하기  
1. 새 버전의 이미지를 `pull` 또는 `build` 하기  
2. 기존 이미지의 컨테이너 `stop` 후 삭제하기 `rm`   
3. 새 이미지로 새 컨테이너 실행 `run`  


### 컨테이너 삭제시 내장 파일도 삭제되는 문제 해결  
컨테이너를 삭제하면, 컨테이너에서 생성된 모든 파일이 삭제된다. 따라서 `DB` 또는 `media file`과 같은 중요한 데이터는 외부에 저장해야 한다. 데이터베이스 서버는 AWS RDS를, Static file 및 Media file은 AWS S3에 저장하자.  
컨테이너 폴더를 호스트 폴더에 마운트 시키는 것도 이 문제의 또 다른 해결방법이다. `-v /my/own/datadir:/var/lib/mysql` 옵션을 추가함으로서 호스트 디렉토리(`/my/own/datadir`)를 컨테이너 디렉토리(`/var/lib/mysql`)에 연결할 수 있다. 이제 데이터가 연결된 호스트 폴더에 저장이 된다. 새로운 컨테이너를 실행할 때 같은 디렉토리를 연결해주면 저장된 데이터를 그대로 사용할 수 있다.  


</br>


</br>


## 도커 이미지 만들기 (Docker build)  

> #### Pycharm 에서 도커파일 인식하기  
> 
> 1. 도커 플러그인 설치  
> : `Preferences` > `Plugins` > `docker 검색` > `Docker integration 설치` > `파이참 재시작`
> 2. Pycharm 기본 설정에선, `Dockerfile` 하나만 도커파일로 인식된다. `Dockerfile.base`와 같은 것도 인식하게 하려면 설정을 변경해준다.  
> : `Preferences` > `Editor/File Types` > `Docker` 에 패턴을(`Dockerfile.*`) 추가해준다.  


충분히 숙련되어 있다면 바로 Dockerfile을 만들 수도 있다. 그러나 일반적으로는 리눅스 서버를 켜고 한 줄씩 실행해보면서 작성하는 것이 버그 해결에 좋다. (우분투 기반으로 작업하는 경우 `docker run --rm -it ubuntu:16.04 /bin/bash` 실행 후 한 줄씩 작성)  


### 1) 도커파일 작성  

##### 예시 1

```docker
# 1. ubuntu 설치 (패키지 업데이트 + 만든사람 표시)
FROM       ubuntu:16.04
MAINTAINER subicura@subicura.com
RUN        apt-get -y update  # 기본적으로 OS 가 설치되면 업데이트를 해줘야 한다. 

# 2. ruby 설치
RUN apt-get -y install ruby
RUN gem install bundler

# 3. 소스 복사
COPY . /usr/src/app

# 4. Gem 패키지 설치 (실행 디렉토리 설정)
WORKDIR /usr/src/app
RUN     bundle install

# 5. Sinatra 서버 실행 (Listen 포트 정의)
EXPOSE 4567
CMD    bundle exec ruby app.rb -o 0.0.0.0
```
`apt-get`: `Apt`는 ubuntu의 패키지 관리자이고, `apt-get`은 그 명령어 중 하나이다. 패키지를 다운로드하고 설치할 때 사용한다.  
`-d`: 다운로드만 하고 설치 혹은 압축해제하지 않는다.  
`-y`: 모든 질문에 Yes로 답한다.  
`-V`: 자세한 버전 정보 표시  

`gem`: 루비 패키지 관리 프로그램
`WORKDIR`: 프로그램 실행 디렉토리  
`EXPOSE`: 실행될 서버의 Listen 포트  

##### 예시 2

```docker
FROM        ubuntu:16.04
MAINTAINER  joo2theeon@gmail.com

# 우분투 이미지는 루트권한 유저 밖에 없기 때문에 sudo를 입력할 필요가 없다. sudo 또한 하나의 패키지이고, 설치되어 있지 않다.
RUN         apt-get -y update  # 기본적으로 OS 가 설치되면 업데이트를 해줘야 한다.
RUN         apt-get -y dist-update  # 의존성 검사하며 업데이트. 왜 해야 하는지는 아직 모르겠다
RUN         apt-get install -y python-pip git vim  # 필요한 프로그램 설치
# 의존성이란 한 패키지가 정상적으로 동작하기 위해서 다른 패키지나 라이브러리 패키지등이 필요한 경우를 말한다.

# pyenv
# 우분투에서 pyenv를 설치 전 필요한 requirement 설치 명령어를 그대로 가져와 붙여 넣은 것 (pyenv 공식 문서에서 common build를 검색하자)
RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
            libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
            xz-utils tk-dev

# pyenv installer 로 검색
RUN         curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH  # pyenv가 설치된 경로 설정
RUN         pyenv install 3.6.3
# $PATH : 프로그램이 설치된 경로가 ':' 로 구분되어 연결되어 있다.

# zsh
RUN         apt-get install -y zsh
# oh-my-zsh
RUN         wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN         chsh -s /usr/bin/zsh  # default shell 을 zsh 로 바꾸는 것

# pyenv zsh settings
RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.zshrc  # PATH= 에서 =는 띄어쓰기 없이 써야 한다
RUN         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# pyenv virtualenv
# 이 Base 이미지는 웬만해선 바뀔 일이 없으므로, 공통적으로 사용하기 위해 가상환경 이름을 app 이라고 한다.
RUN         pyenv virtualenv 3.6.3 app

# uWGSI install
# pyenv 가상환경 app 의 pip 로 uwsgi 설치 
RUN         /root/.pyenv/versions/app/bin/pip install uwsgi

# Nginx install
RUN         apt-get -y install nginx

# supervisor install
RUN         apt-get -y install supervisor

# pip
ENV         LANG C.UTF-8

COPY        requirements.txt /srv/requirements.txt
RUN         /root/.pyenv/versions/app/bin/pip install -r \
            /srv/requirements.txt
```


### 2) 도커 이미지 만들기  
**Working Directory**: `Dockerfile`이 존재하는 폴더  
**명령어**: `docker build -t <만드려는_이미지_이름> [-f Dockerfile.base] .`  
`.`은 현재 폴더 기준으로 `Dockerfile` 라는 이름의 문서를 참조하라는 것이다. 도커파일의 이름이 다를 경우(`Dockerfile.base` 처럼), `-f` 옵션과 함께 그 파일의 이름을 입력해준다. (`t`는 tag, `-f`는 file)


### 3) Dockerfile 작성시 사용되는 명령어  
: 더 많은 정보는 [도커 공식 문서](https://docs.docker.com/engine/reference/builder/)

#### `FROM <image>:<tag>`  
: 베이스 이미지를 지정한다. 반드시 지정해야 하며, 이 이미지를 기반으로 새로운 이미지가 만들어진다. `tag`는 될 수 있으면 기본값인 `latest` 보다는 구체적인 버전을 지정하는 것이 좋다. 이미 만들어진 다양한 베이스 이미지는 Dockerhub 에서 확인할 수 있다. (`FROM ubuntu:16.04`)
  
#### `MAINTAINER <name>`  
: 해당 도커파일을 관리하는 사람의 이름 또는 이메일 정보를 적는다. 반드시 필요한 과정은 아니다. (`MAINTAINER joo2theeon@gmail.com`)  

#### `COPY <src_path> <dest_path>`  
: 파일 또는 디렉토리 복사. 타겟 디렉토리가 없다면 자동으로 생성한다.  

#### `ADD <src_path> <dest_path>`  
: `COPY`와 비슷하나 추가 기능이 있다. `<src_path>`에 파일 대신 URL을 입력할 수 있고, 압축 파일이 있는 경우 자동으로 압축이 해제된다.  

#### `RUN 명령어`  
: 명령어를 그대로 실행합니다. 내부적으로 `/bin/sh -c` 뒤에 명령어를 실행하는 방식입니다. (`RUN bundle install`)  

#### `CMD 명령어`  
: 도커 실행 후에 실행되는 명령어를 정의한다. 도커 빌드시 사용되지 않으며, 여러 `CMD`가 존재할 경우 맨 마지막 하나만 실행된다. 여러 명령을 실행하고 싶다면 `run.sh` 파일을 작성하여 deamon으로 실행하거나 `supervisord`나 `forego`와 같은 여러 개의 프로그램을 실행하는 프로그램을 사용하자.  

#### `WORKDIR 경로`  
: `RUN`, `CMD`, `ADD`, `COPY`등이 이루어질 기본 디렉토리를 설정한다. 각 명령어의 현재 디렉토리는 한 줄 한 줄마다 초기화되기 때문에 `RUN cd /path`를 하더라도 다음 명령어에선 다시 위치가 초기화 된다. 같은 디렉토리에서 작업하려면 `WORKDIR`을 사용하여야 한다.  

#### `EXPOSE 포트 번호`  
: 도커 컨테이너가 실행되었을 때 요청을 기다리고 있는(Listen) 포트를 지정합니다. 여러개의 포트를 지정할 수 있습니다.  

#### `VOLUME ["/data"]`  
: 컨테이너 외부에 파일시스템을 마운트 할 때 사용한다. 반드시 지정하지 않아도 마운트 할 수 있지만, 기본적으로 지정하는 것이 좋다.  

#### `ENV <key> <value>` or `ENV <key>=<value> ...`  
: 컨테이너에서 사용할 환경변수를 지정한다. 컨테이너를 실행할 때 -e옵션을 사용하면 기존 값을 오버라이딩 하게 된다.  


</br>


</br>


## Docker의 Build 과정 분석

```
Sending build context to Docker daemon  5.12 kB   <-- (1)
Step 1/10 : FROM ubuntu:16.04                     <-- (2)
 ---> f49eec89601e                                <-- (3)
Step 2/10 : MAINTAINER subicura@subicura.com      <-- (4)
 ---> Running in f4de0c750abb                     <-- (5)
 ---> 4a400609ff73                                <-- (6)
Removing intermediate container f4de0c750abb      <-- (7)
Step 3/10 : RUN apt-get -y update                 <-- (8)
...
...
Successfully built 20369cef9829                   <-- (9)
```

1. 빌드 명령어를 실행한 디렉토리를 `Build Context`라고 하고, 이 파일 들을 docker demon (도커 서버)로 전송한다. 도커는 서버-클라이언트 구조이므로 도커 서버가 작업하려면 미리 파일을 전송해야 한다.  
2. Dockerfiledmf 한 줄 한 줄 수행한다. 
3. 명령어 실행 결과를 화살표로 표시한다. 여기서는 우분투 이미지를 가져왔으므로, 이미지 ID가 표시된다.  
4. 두 번째 명령어 실행
5. 바로 이전에 생성된 `f49eec89601e` 이미지를 기반으로 임시 컨테이너 `f4de0c750abb`를 생성하여 실행한다.  
6. 실행 결과를 이미지로 저장한다. 
7. 임시 컨테이너를 제거한다.  
8. 세 번째 명령어를 수행한다.  
9. 마지막으로 생성된 이미지 ID를 출력한다.  

도커 빌드는 `임시 컨테이너 생성` > `명령어 실행` > `이미지 저장` > `임시 컨테이너 삭제`의 반복이라고 할 수 있다. 이것이 이미지 레이어의 개념이다.  


</br>


</br>


## Dockerhub: 도커 이미지 저장소

> Dockerhub는 도커 이미지 파일을 저장(`push`)하고 불러올 수 있는(`pull`) 저장소이다.  
> 도커 레지스트리를 사용할 수도 있지만, 이는 설치형이라 많이 사용하지 않는다. 대신 private 하게 사용할 수 있다. Dockerhub 의 경우 비개방형 이미지는 한 개 까지만 가능하다.  


### Docker deamon 으로 로그인
: `docker login`  
username 과 password 를 입력하면 로그인이 되고, `~/.docker/config.json`에 인증정보가 저장되기 때문에 로그아웃하기 전까지 로그인이 유지된다. 


### 도커 이미지 이름의 구성 요소:

1. 기본 라이브러리를 사용하는 경우: `<이미지 이름>:[태그]`  
2. 사용자 라이브러리를 사용하는 경우: `<사용자 ID>/<이미지 이름>:[태그]`  


### 이미지에 태그 붙이기
: `docker tag <sorce_img_name>[:tag] <target_img_name>[:tag]`
기존 이미지에 이름을 새로 붙여줄 수 있다. `docker images`를 통해 확인하면 마치 두 개의 이미지가 있는 것 처럼 보이지만, 사실은 같은 이미지를 공유하는 것이다. 그러나 소스 이미지가 변경된다고 해도 이름이 붙은 타겟 이미지가 변경되지는 않는데, 이것은 이미지가 레이어 단위로 관리되기 때문이다. 깃에서 브랜치를 새로 만드는 느낌.  (예: docker tag app subicura/sinatra-app:1)


### Dockerhub 에 이미지 전송하기 
: `docker push subicura/sinatra-app:1`  
방금 생성한 이미지를 전송해보자. Dockerhub 에 `subicura` 계정으로 전송되었다.  

### Dockerhub 에서 이미지 다운받기
: `docker pull 계정이름/이미지이름:태그`  
Dockerhub 에서 해당 이미지를 다운 받는다. `Dockerfile`의 `FROM` 항목에 써있는 이미지가 존재하지 않을 경우, 알아서 `pull` 작업을 수행한 후에 그 이미지를 바탕으로 새로운 이미지를 생성한다. 하지만, 이미 존재하는 경우에는 그 이미지를 가져다 사용한다. 따라서, Dockerhub 의 이미지가 수정되었을 경우, 다시 `pull`을 해주어야 한다.  



## 배포 


