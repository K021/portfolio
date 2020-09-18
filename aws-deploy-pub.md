
# AWS Deploy
<br>

# EC2 Deploy 1 (10.26)
> 페이지: console.aws.amazon.com  
> 오른쪽 위 서버 위치: 서울 선택  

## 유저 생성

: 유저 별로 권한을 제한하기 위한 용도로, 사이트 해킹시 피해를 감소시킨다.  

> / iam 콘솔: 콘솔 검색창에 'iam' 검색/  
> / 왼쪽 내비게이션 'Dashboard'/ 가운데 바디에 'Security Status' 중 'Delete your root access keys' 체크 확인/  
> / 내비게이션 'Users'/ 'Adduser'/  

* User name: EC2-User  
* Select AWS access type: Programmatic access  
(Programmatic access는 terminal 같은 개발 툴로만 접근할 수 있다. 브라우저 로그인은 안 되고, AWS의 SDK/API를 쓰는 경우 신원을 인증하는 데만 사용할 수 있다. 로컬에서 AWS에 서비스 사용 권한을 요청할 때 신원인증. 정확히는 모름) 영상: '171026  EC2 Deploy 1' [7:10-8:30]  

> / next: set permissions/ Attach existing policies directly 선택/ 'AmazonEC2FullAccess' 검색, 선택/ next: **Review**, 'Create user' 선택/ success 페이지/

**Success 페이지**: 생성된 유저의 이름, Access key ID, Secret Access key에 관한 정보가 나온다. 이 정보는 두 번 다시 볼 수 없으므로, 유저 정보 테이블 위의 'Download .csv'를 클릭, 다운로드, 'ec2-user-credentials.csv'로 저장하자. (페이스북 로그인을 할 때 사용하던 정보와 같다.)  

> 다시 iam 콘솔 'Users',  

생성된 유저를 볼 수 있다.  
Amazon ec2: Amazon Elastic Compute Cloud로, 확장식 컴퓨팅 기능을 클라우드로 제공한다.  

> 왼쪽 위 '서비스'/ '컴퓨팅'의 'EC2'/ EC2 Dashboard/  

서버 접속은 공개키 암호화 방식을 사용한다. AWS 상에서 공개키와 개인키를 생성하고, 내가 그 개인 키를 다운로드 받는다. 다운 과정이 https로 이루어지기 때문에 안전하다. (https는 또 다른 공개키 인증 방식으로 사용자 신원을 인증한다. [생활코딩 링크]) 
네비게이션 '네트워크 및 보안'의 '키 페어', '키 페어 생성', '키 페어 이름'=EC2-Deploy-keypair '생성', 생성이 되면 .pem 확장자로 키 정보가 다운로드 된다.(맥 크롬 한정, 나머지는 수동 다운로드) 이 키를 잃어버리면 서비스에 접근할 방법이 없으므로 ~/.ssh 폴더에 저장해두자.  

## 인스턴스 생성 (새 보안 그룹 생성 포함)
> **AWS 콘솔 경로**  
> / 네비게이션 인스턴스, 인스턴스, 인스턴스 시작/ Amazon Machine Image' 중 'Ubuntu Server 16.04 LTS (HVM), SSD Volume Type' 선택/ '인스턴스 유형 선택'에서 '유형' 열에 '프리티어 사용 가능'이라고 표시된 항목만 체크/  
> / '다음'/ 인스턴스 세부 정보 구성 '다음'/ 스토리지 추가 '다음'/ 태그 '다음'/ **보안 그룹 구성 페이지**의 '보안 그룹 이름'=EC2-Deploy-SecurityGroup '설명'=EC2 Instance(EC2-Deploy) Security Group '다음'/ **인스턴스 시작 검토**/ '인스턴스 시작 검토'의 '시작'/ '기존 키페어 선택 또는 새 키페어 생성'의 '인스턴스 시작'/ '인스턴스 보기'/  
*인스턴스를 생성하는데 시간이 좀 걸린다.  

**보안 그룹 구성**: 어떤 포트를 열어놓을 것인가. 다 열어두면 해커 공격의 쉬운 대상이 된다. 아예 연결을 허용하지 않을 수도 있다. 개발을 끝내고 신경을 끌 생각이면 80번 요청만 받으면 된다.

**인스턴스 시작 검토**: '보안 그룹' 중 '소스'는 어느 ip에서 해당 그룹에 접속할 수 있는지를 표시한다.  

* 0.0.0.0/0의 경우, 어디서든지 접속할 수 있다는 의미이다.  
* 22번 포트의 경우, 내 컴퓨터에서만 접근 가능하게 하는 것이 좋다.    

---

<br>

# EC2 Deploy 2, 3 (10.26)

> /대시보드의 네비게이션 '인스턴스' 페이지 하단 '설명'/

**퍼블릭 DNS**가 우리가 만든 서버의 주소이고, 실제 웹 상에 공개되어 있다. 그러나 우리가 생성한 인스턴스는 22번 포트이므로 브라우저로는 접속할 수 없다. ssh client를 통해서만 접속이 가능하다.  

## SSH client로 리눅스 인스턴스 연결하기
참조 문서: [AWS.DOC.SSH로.Linux.인스턴스에.연결]  
ssh 유저명 접근주소 

**사전 확인사항**:

* ssh client 설치 (리눅스와 맥에는 기본적으로 설치되어 있다)
* 개인키(private key)의 위치 (유저 생성시 다운로드 한 .pem 파일)
* 인스턴스와 연관된 보안 그룹이 IP 주소로부터 들어오는 SSH 트래픽을 허용하는가  

**Linux 인스턴스에 연결**:

* shell에서 개인키가 있는 폴더로 이동한다. (~/.ssh)  
* chmod 명령어로 개인키 접근 권한을 소유자에 한정한다.  

> **chmod: 파일/폴더 권한정보 수정**  
> 
> ```shell
> ~/.ssh » l
> drwxr-xr-x   6 ElohimAwmar  staff   204B 10 26 14:07 파일/디렉토리 이름
> ```
> * 맨 앞에 있는 d rwx r-x r-x 에 주목하자. d는 폴더임을 의미하고 rwx는 해당 폴더에 대한 권한을 의미한다. (r,w,x의 순서대로 읽기, 쓰기, 실행 권한을 가진다.)  
> * r,w,x 는 순서대로 4,2,1의 값을 가지며, 조합에 따라 0~7의 값으로 그 권한정보를 나타낼 수 있다.  
> * rwx 정보는 세 부분으로 나누어져 있는데, 순서대로 [파일/폴더의 소유자] [소유 그룹] [나머지 유저]를 의미한다.  
> * `chmod 400 /path/private-key-pair.pem` 으로 권한정보를 수정할 수 있다.  

* ssh 명령으로 인스턴스에 연결한다.  
`ssh -i private-key-path username@public_DNS_name`  
> * 여기서 username 은 접속하려는 서버의 유저이름을 의미한다. 아마존 Ubuntu 서버의 경우 username은 `ubuntu` 이다. 
> * `-i` 는 권한 요청에 사용할 개인키를 선택하는 옵션이다. 이 옵션이 없을 경우, `~./ssh` 폴더에 있는 `id_rsa` 파일을 사용하게 된다. 

* 접근하려는 도메인의 지문을 확인한다. (옵션)  

	> ```
	> $ ssh -i ./EC2-Deploy-Keypair.pem ubuntu@ec2-13-125-9-213.ap-northeast-2.compute.amazonaws.com
	> The authenticity of host 'ec2-13-125-9-213.ap-northeast-2.compute.amazonaws.com (13.125.9.213)' can't be established.
	> ECDSA key fingerprint is SHA256:2flCPgqxuYAKqBSGz5a85M8Q3LhZ70sqCPepvO4wrTI.
	> Are you sure you want to continue connecting (yes/no)?
	> ``` 

	브라우저를 통해 접근할 때는 https 인증서를 통해 해당 브라우저가 신뢰할 만한지를 파악할 수 있다. ssh 접근의 경우는 지문을 확인해주어야 한다. 위 콘솔에 나온 지문은 'ECDSA key'임을 기억하자.   

	> 
	> **aws cli로 접근하려는 서버의 지문 확인하기**  
	> 
	> * `aws cli` 설치하기: `pip install awscli`  
	> * `aws configure`로 aws 설정파일 만들기  
	> 
	> ```
	> $ aws configure
	> 
	> # 유저를 생성할 때 받은 유저 정보 파일인 .csv 파일 정보를 기록한다.
	> AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
	> AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
	> 
	> # aws consle/ 맨 위 '서비스'/ EC2 management console/ 인스턴스/ 설명/ 가용영역 정보
	> # 가용정보 마지막에 붙어있는 'a'는 aws 서울서버의 상세한 위치구분이므로 생략해도 좋다. 
	> Default region name [None]: ap-northeast-2a 
	> # 얘는 그냥 아웃풋 포맷인데, 시키는 대로 json 형식을 설정하자. 
	> Default output format [None]: json 
	> ```
	> 
	> 해당 과정을 완료하면, ~/.aws 폴더가 생긴다. 
	> 
	> * 인스턴스의 지문확인하기  
	> **제한 조건1** : 인스턴스가 pending 상태가 아닌, running 상태여야 한다.  
	> **제한 조건2** : 아래 명령어로 출력되는 정보 중, 지문을 나타내는 `SSH HOST KEY FINGERPRINTS` 섹션은 인스턴스를 처음 부팅한 후에만 사용할 수 있다.  
	> 
	> ```
	> # --instance-id 뒤에는 서비스/EC2/인스턴스/설명 페이지에 있는 '인스턴스 ID' 값을 가져온다. 
	> $ aws ec2 get-console-output --instance-id i-0414722a07ff362ef
	> 
	> ...
	> #############################################################
	> \r\n<14>Oct 26 03:07:56 ec2: 
	> -----BEGIN SSH HOST KEY FINGERPRINTS-----
	> \r\n<14>Oct 26 03:07:56 ec2: 1024 
	> SHA256:CJo818grSh7YXQ5s1a01U8o5pdxZqPmXrvsbbwLmMaw root@ip-172-31-15-11 (DSA)\r\n<14>Oct 26 03:07:56 ec2: 256 
	> SHA256:2flCPgqxuYAKqBSGz5a85M8Q3LhZ70sqCPepvO4wrTI root@ip-172-31-15-11 (ECDSA)\r\n<14>Oct 26 03:07:56 ec2: 256 
	> SHA256:ZNcdCizvz5B4hd0lfRsO5KKjbGgS745cl5ZfXFt1yW4 root@ip-172-31-15-11 (ED25519)\r\n<14>Oct 26 03:07:56 ec2: 2048 
	> SHA256:JAATwlC2MCci8qEsyvCnctFwTY2/g1HRkeA+8SVikCA root@ip-172-31-15-11 (RSA)\r\n<14>Oct 26 03:07:56 ec2: 
	> -----END SSH HOST KEY FINGERPRINTS-----
	> \r\n<14>Oct 26 03:07:56 ec2: 
	> #############################################################
	> ...
	> ```
	> 출력되는 네가지 지문 중에서, 'ECDSA key' 방식으로 해싱된 지문이 우리가 찾는 지문이다.  
	> 
	> **한 번 확인한 지문 다시 확인하기**  
	> 한 번 접속한 ssh host의 정보는 ~/.ssh 폴더의 known_hosts 안에 기록되어 있다. 이 정보를 지우게 되면, 처음 접속하는 것과 마찬가지가 되어 `SSH HOST KEY FINGERPRINTS`를 매번 확인할 수 있다.   


## 리눅스 인스턴스 기본 설정하기
> aws ubuntu는 16.04 버전이기 때문에 업데이트가 필요하다. 

* **ubuntu 패키지 정보 업데이트**: `sudo apt-get update`
* 설치되어 있는 패키지들을 의존성 검사하며 업그레이드: `sudo apt-get dist-upgrade`
* **pip** 설치: `sudo apt-get install python-pip`
* **zsh** 설치: `sudo apt-get install zsh`
* **oh-my-zsh** 설치: `sudo curl -L http://install.ohmyz.sh | sh`
* **Default shell 변경**: `sudo chsh ubuntu -s /usr/bin/zsh`  
(shell 변경 후엔 exit로 연결을 종료한 뒤 재연결)

---

<br>


# EC2 Deploy 12-14 (10.30)



### uwsgi에 django 쓰기 권한 주기  

**nginx(user=deploy) ~ uwsgi(deploy) ~ django(ububtu)**  
uwsgi의 deploy 유저가 django media folder에 쓰기 권한이 없다. django media를 ubuntu:ububtu가 아닌 deploy:deploy로 바꿔준다. 

> S3를 사용하게 되면 이 과정이 필요가 없다. 


### EC2 서버에서 RDS 데이터베이스에 기록  

EC2에 post_create요청을 하면 EC2에서 RDS로 요청한다. 우리가 맨 처음 RDS를 만들어줄 때는 인바운드로 패스트캠퍼스의 ip만 허용했었다. 그러면 다른 곳에서는 EC2가 RDS에 요청을 할 방법이 없다. RDS의 인바운드를 ec2 보안그룹에게 열어준다. 

> 인바운드: 사용자 접근 경로 (RDS는 psql용 포트인 5432만 열어준다.)  
> 아웃바운드: 사용자에게 출력해주는 경로   



## 서버분리

> ec2는 연산할 때만 쓰인다. 없어져도 되는 정보만 올린다. 그래서 장고는 괜찮다. 우리 로컬에서 코드를 관리하고 깃으로 커밋하니까. DB와 스태틱은 다른 서버로 분리시킨다. DB는 RDS에 옮긴다. 스태틱은 S3 서비스로 옮긴다. 그러면 데이터가 날아갈 걱정을 하지 않아도 된다. RDS는 일정 시간 단위로 백업되고(시간을 설정할 수 있다) S3는 세 곳에 복사해서 저장된다. 

**Django Application server**: **(EC2)**  
**DB server**: **(RDS)**  
**Static Server**: **(S3)**  



## S3

RDS는 다른 권한이 필요없지만 S3는 다르다. 프로젝트마다 스태틱 파일을 따로 저장해 주어야 하기 때문에 S3 안에서 폴더단위로 버킷을 나눈다. 

데이터 베이스에 기본 유저모델이 없는 상태에서, 새로운 유저 모델을 만들고 커스터마이징을 하면 충돌이 발생한다. 이런 경우, 이전 DB를 지우고 새로 만드는 방법 밖에는 없다. RDS에 접근해서 지운다. 

```
# DB를 삭제할 때에는 postgres DB로 들어가야 한다. 
$ psql --host=mydbinstance-joo2theeon.ccdyfkfjc58s.ap-northeast-2.rds.amazonaws.com --user=joo2theeon --port=5432 postgres
Password for user joo2theeon:
psql (9.6.5, server 9.6.2)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

# deploy 디비를 버린다. 이 DB를 사용하는 runserver가 켜져있으면 종료해야 한다. 
# 명령문 끝의 세미콜론을 잊어버리지 말자. 
postgres=> DROP DATABASE deploy; 
DROP DATABASE

# OWNER 뒤에는 유저 이름이 들어간다. RDS를 생성할 때 만들었던 유저를 적는다. 
# 그 유저 말고도, 직접 RDS에 접속해서 createuser로 만든 유저가 있다면 그 유저를 사용할 수도 있다. 
postgres=> CREATE DATABASE deploy OWNER joo2theeon;
CREATE DATABASE

postgres=> \q # 종료
```

데이터베이스를 사용하고 있는지 검사

```
(aws)
➜  ~ sudo systemctl stop uwsgi
➜  ~ sudo systemctl stop nginx
➜  ~ ps -ax | grep uwsgi
➜  ~ ps -ax | grep nginx
(local)
» ps -ax | grep runserver
```
 

## django-storage로 s3 사용하기

> 장고는 기본적으로 파일을 장고가 돌아가고 있는 서버(EC2)에 저장한다. ([django.doc.models.filefield]) 그 역할을 하는 것이 Storage class 이다. 다른 서버(S3)에 저장하고 싶다면 이 Storage 클래스를 재정의해야 한다. 재정의한 storage는 파일이름으로 S3에 파일을 요청하고, 받은 응답을 장고에 준다.  
> 
> 직접 장고 storage를 재정의 하는 것은 힘들다. S3 안에 API가 있고, 그 API를 사용하는 장고의 라이브러리(django-storage)도 있다. 그걸 사용하자. (참고 문서: [django-storages.doc.a3])

**django-storage ~ (python) ~ boto3 ~ a3**  
**django-storage**: 장고에서 파일 입출력을 담당하는 라이브러리  
**boto3**: 파이썬의 s3 전용 파일 입출력 SDK(특정서비스 한개를 사용하기 위해 만든 api의 묶음)  
**s3**: 아마존의 스태틱 파일 저장용 서버  

### 1. Django-Storage: Install & Settings
**django-storage install** ([django-storages.doc.install])  

* `pip install django-storages`  
* settings.py `INSTALLED_APPS`에 `'storages'`추가

**django-storage settings**

* `DEFAULT_FILE_STORAGE` 변수 설정: 유저 업로드 파일에만 적용.  
기본값은 'django.core.files.storage.FileSystemStorage'로, 문서에 나와있다. [django.doc.default.file.storage]

```
(settings.py)
# 아마존 s3에 boto3 라이브러리로 파일 요청  
# Default: 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

* `STATICFILES_STORAGE` 변수는 `callectstatic` 명령시 적용

```
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

### 2. boto3 설치, 버킷 생성

**boto3 문서:** [boto3.doc]   
**boto3 install** ([boto3.doc.install]): `pip install boto3`  
**boto3 create bucket** ([boto3.doc.create.bucket], [lhy.kr.aws.1])  

```
~/python/Django/ec2_deploy_pj/mysite(master*) » python

Python 3.6.3 (default, Oct 26 2017, 14:38:59)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import boto3
>>> session = boto3.Session()
>>> client = session.client('s3')
>>> client.create_bucket(Bucket='fc-6th-test', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})

--- 출력 ---
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/var/pyenv/versions/fc-ec2/lib/python3.6/site-packages/botocore/client.py", line 312, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/usr/local/var/pyenv/versions/fc-ec2/lib/python3.6/site-packages/botocore/client.py", line 605, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the CreateBucket operation: Access Denied
>>> client.create_bucket(Bucket='fc-6th-test-joo2theeon', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/var/pyenv/versions/fc-ec2/lib/python3.6/site-packages/botocore/client.py", line 312, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/usr/local/var/pyenv/versions/fc-ec2/lib/python3.6/site-packages/botocore/client.py", line 605, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the CreateBucket operation: Access Denied
```

**EC2 user에 S3 접근 권한 부여하기**  
EC2-user에 AmazonS3FullAccess 권한을 추가해야 Access Denied가 없어진다.  
> 서비스/iam/Users/'EC2-User' 선택/Permissions/Add permissions/
> Attach existing policies directly/AmazonS3FullAccess 검색, 선택/Next Review/Add permissions

<!---->

**S3와 버킷, 버킷 이름 확인하기**  
s3는 서버 인스턴스를 따로 생성할 필요가 없다. 한 곳에 뭉쳐져있고, 버킷으로 나뉘어져 있다. 그래서 버킷의 이름은 유니크하다. 우리가 생성한 버킷 이름은 `fc-6th-test-joo2theeon`이다.  
`list_buckets()` 메서드로 생성된 버킷을 확인할 수 있다. aws콘솔/서비스/s3 에서도 확인할 수 있다.  

> ```python
> # 파이썬으로 버킷 이름 확인
> >>> import boto3
> >>> session = boto3.Session()
> >>> client = session.client('s3')
> >>> buckets = client.list_buckets()['Buckets']
> >>> for bucket in buckets:
> >>> 		print(bucket)
> ```

### 3. S3 settings

* `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`
	
	> ```python
	> # Config paths
	> CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
	> with open(os.path.join(CONFIG_SECRET_DIR, 'settings_common.json'), 'rt') as f:
	> 	config_secret_common_str = f.read()
	> 	config_secret_common = json.loads(config_secret_common_str)
	> 
	> # AWS
	> AWS = config_secret_common['AWS']
	> AWS_ACCESS_KEY_ID = AWS['AWS_ACCESS_KEY_ID']
	> AWS_SECRET_ACCESS_KEY = AWS['AWS_SECRET_ACCESS_KEY']
	> AWS_STORAGE_BUCKET_NAME = AWS['AWS_STORAGE_BUCKET_NAME']
	> ```

* FileStorage

	> **S3 File Storage 적용의 기본적인 형태**
	> 
	> ```
	> DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
	> STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
	> ```
	> 마지막 `S3Boto3Storage`은 field의 `upload to`옵션의 이름으로 그냥 폴더를 만들어 버린다. static file과 media file을 구분해서 저장하고 싶다면, `S3Boto3Storage`을 상속하는 Storage 클래스를 만들어야 한다. 
	> 
	> **S3 File Storage 클래스 커스텀**
	> 
	> ```python
	> (storages.py)
	> from django.conf import settings
	> from storages.backends.s3boto3 import S3Boto3Storage
	> 
	> class StaticStorage(S3Boto3Storage):
	>     location = settings.STATICFILES_LOCATION
	> 
	> class MediaStorage(S3Boto3Storage):
	>     location = settings.MEDIAFILES_LOCATION
	> 
	> (settings)
	> # AWS storage
	> # S3에 저장되는 폴더 이름을 결정한다. 
	> STATICFILES_LOCATION = 'static'
	> MEDIAFILES_LOCATION = 'media'
	> 
	> # S3 FileStorage
	> DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
	> STATICFILES_STORAGE = 'config.storages.StaticStorage'
	> ```
	> * 이제 미디어 파일을 업로드 하거나, collectstatic을 하면 S3 bucket에 저장된다.  
	> 스태틱 파일 참조나, url로 미디어 파일을 참조하는 것도 전부 이전처럼 된다.  
	> * 스태틱 파일과 미디어 파일은 S3 콘솔에서 확인할 수 있다.

### 4. settings 모듈 분리하기. local, debug, deploy
* **local** db: 빠른 개발용으로 인터넷이 필요 없고 간단한 sqlite3를 사용한다. 
* **debug** db: deploy와 최대한 같은 환경으로, 같은 db 프로그램(postgresql)을 사용한다. 가능하다면 RDS 환경을 쓰는 것이 좋다. 
* **deploy** db: 배포용 데이터베이스. RDS 사용. 

> settings module을 분리하게 되면, `./manage.py` 를 실행할 때마다 다음과 같은 조건을 첨부해야 한다. 
> 
> ```
> DJANGO_SETTINGS_MODULE=config.settings.local ./manage.py migrate
> DJANGO_SETTINGS_MODULE=config.settings.local ./manage.py runserver
> DJANGO_SETTINGS_MODULE=config.settings.local ./manage.py createsuperuser
> ```

## 기타

* uwsgi 실행 오류

	> uwsgi 실행 오류가 나면, 창에 다음과 같이 뜬다.  
	> 
	> ```
	> (browser)
	> 502 Bad Gateway nginx/1.12.1
	> ```
	> 이는 nginx 까지는 잘 실행되었다는 의미로 uwsgi 에서 오류가 난 것이다. uwsgi 실행 오류는 nginx 로그에서 확인할 수 있다. 

* 파이썬 기본 설정 파일 `.idea`




<!--링크-->

[생활코딩 링크]: https://opentutorials.org/course/228/4894
[AWS.DOC.SSH로.Linux.인스턴스에.연결]: http://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

[django.doc.models.filefield]:https://docs.djangoproject.com/en/1.11/ref/models/fields/#filefield
[django-storages.doc.install]:https://django-storages.readthedocs.io/en/latest/
[django-storages.doc.a3]:https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
[django.doc.default.file.storage]:https://docs.djangoproject.com/en/1.11/ref/settings/#default-file-storage

[boto3.doc]:https://boto3.readthedocs.io/en/latest/
[boto3.doc.install]:https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation
[boto3.doc.create.bucket]:http://boto3.readthedocs.io/en/latest/guide/s3-example-creating-buckets.html
[lhy.kr.aws.1]:https://lhy.kr/ec2-ubuntu-deploy