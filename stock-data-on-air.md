


<h1 class="header"><span>실시간 주가 데이터 가져오기</span></h1> 

> 임경식 교수님께 실시간 주가 데이터를 가져오는 방법을 가르쳐드리기 위한 문서




# 파이썬으로 하나대투 API 사용하기

## API 설치 

##### 설치 파일을 다운로드 하자
- 설치 방법: [하나대투 1Q Pro 설명 페이지](https://www.hanaw.com/main/customer/customer/CS_050600_T1.cmd) &rarr; 게시판 &rarr; 공지 - API 최신 패치버전 다운로드 후 설치
- 공인인증서 로그인 후에, 투자자 정보를 입력해야 한다. (위험한 투자방식이기 때문에 투자성향 정보를 제공해야한다.)
- 2018.12.04 기준, `1QOpenAPI_20180718.exe (version 1.3)` 파일이다.
- 설치를 진행하면, `c:\1Q OpenAPI` 에 파일들이 저장된다. 

##### 설치된 파일 구조
```
1Q OpenAPI/
	- 1QApiAgent/  # API 에이전트 모듈 폴더
	- Document/  # API 개발 가이드문서 폴더
	- Example/  # API 예제 프로그램 폴더
	- Notice.txt
	- vcredist_x86.txt
	- VersionInfo.txt
	- 폴더구조설명.txt
```
```
1QApiAgent/
	- system/
		- comms.ini  # 통신연결정보 파일
		- realdata.dat  # 실시간 데이터 정보
	- TranRes/
		- *.res  # Tran 조회 I/O Block 정보 리소스 파일
	- RealRes/
		- *.res  # 실시간 I/O Block 정보 리소스 파일
	- Cert/
		- mobile-test-cert.der  # 암호화 인증서
	- AddIn/
		- ScpAgt/  # 패킷 암호화 모듈 폴더
	- HFCommAgent.dll  # Open API 에이전트 컨트롤 모듈
	- regHFCommAgent.bat  # HFCommAgent.dll 모듈 레지스트리 등록 배치파일
	- HFComms.exe  # 통신 모듈
	- CommApi.dll  # 통신 인터페이스 모듈
	- xmclinet260.dll  # 암호화 모듈
	- LinkInfoMng.dll  # 정보 보관 모듈
	- CodeMaster.dll  # 코드정보 관련 모듈
	- SrShare.dll  # 공통함수 라이브러리 모듈
	- bugslayerutil.dll  # Crash Report 모듈
	- fpbp3220.dll  # Device 관련 모듈
	- 기타 공인인증 관련 dll 파일들
```



## DLL 파일을 레지스트리에 등록


### 용어정리

##### 레지스트리란?
윈도우 운영체제 또는 응용프로그램의 실행에 필요한 설정 값을 모아둔 것이다. 사용자의 시스템, 응용프로그램 사용 기록 등을 저장하는 로그가 남겨져 있기도 하다. 

##### DLL 이란?
다양한 기능을 수행하는 로직을 담은 라이브러리로, Dynamic Linking Library 의 약자이다. 다른 프로그램에서 특정 기능을 직접 구현하는 대신, 그냥 가져다 쓰면 되도록 미리 만들어진 코드라고 보면 쉽다. 여러 프로그램에서 한 dll 파일을 공유할 수 있기 때문에 메모리 소모가 적다. 

LIB 파일은 컴파일시에 링크가 되는 반면에, DLL 은 함수가 실행되는 순간에 링크가 된다. 전자는 정적 연결, 후자는 동적 연결이라고 한다. 그런 이유로 속도는 LIB가 약간 더 빠르지만 파일이 프로그램마다 중복되어 삽입되기 때문에 메모리를 많이 차지하는 반면, DLL 은 한 파일을 공유하므로 메모리의 이득이 크다.

##### OCX 란?
컴포넌트 프로그래밍이 가능하도록 여러 프로그램들이 데이터를 공유할 수 있도록한 기술, OLE 가 발전한 것. COM 과 결합되어 Active X 가 된다. 파이썬에의 `pywin32` 패키지로 사용할 수 있는 것은 COM 뿐이고, OCX 는 `PyQt5` 를 사용하여야 한다.

---

### 레지스트리 등록 방법 두 가지

##### 1. `regsvr32` 명령어 실행
- 윈도우 시작에서 cmd 를 검색한다. `명령 프롬프트` 를 우클릭하여 관리자 권한으로 실행한다.
- `cd /1Q OpenAPI/1QApiAgent/` 명령으로 `HFCommAgent.dll` 파일이 있는 디렉토리로 이동한다. 
- `regsvr32 HFCommAgent.dll` 명령으로 dll 파일을 레지스트리에 등록한다. 

##### 2. batch file 실행하기
- 위의 명령어를 알아서 실행해주는 배치파일이 기본적으로 제공된다. 
- 같은 방식으로 커맨드(명령 프롬프트)를 실행하고, `cd /1Q OpenAPI/1QApiAgent/`로 이동한다. 
- `reg HFCommAgent.bat` 을 입력하면, 해당 이름의 배치파일이 실행된다. 

하지만, 이 배치파일은 `regsvr32 /S HFCommAgent.dll` 명령을 실행하는데, `/S` 옵션은 알림창을 뜨지 않게 해주기 때문에, 레지스트리가 등록되었는지 여부를 알 수가 없어 추천하지 않는다. 

---

### 에러 해결

##### 실패 알림 메세지
- HFCommAgent.dll 레지스트리 등록이 오류코드 0x80040200 으로 인해 DLLRegisterServer 호출에 실패했습니다

이 오류는, 관리자 권한이 없기 때문에 발생했을 가능성이 크다. 관리자 권한으로 커맨드를 실행해주어야 한다. 윈도우 시작에서 `cmd` 를 검색하면 나오는 `명령 프롬프트` 를 우클릭하여 `관리자 권한으로 실행하기` 를 눌러주자. 그리고 다시 해당 dll 파일이 있는 디렉토리에서 `regsvr32 HFCommAgent.dll ` 명령을 실행하면 아래와 같은 성공 알림이 뜰 것이다. 

##### 성공 알림 메세지
- HFCommAgent.dll 에서 DllRegisterServer 가 성공했습니다.

---

### 레지스트리의 등록 여부 확인하기
> 더 자세한 정보를 원한다면 &mdash; [serverfault.com: How do I know if a DLL is registered?](https://serverfault.com/questions/576831/how-do-i-know-if-a-dll-is-registered)  

1. 시작에 `regedit` 검색하여 실행하면, `레지스트리 편집기` 가 열린다.
2. 편집 &rarr; 찾기 또는 `ctl+F` 로 찾으려는 `dll` 파일 이름을 검색한다. 
3. `{3F33CE3E-64C1-4437-AE66-3EFA980D304A}` 와 비슷한 형식의 폴더가 나오면 정상적으로 등록된 것. 해당 문자열은 해당 dll 파일의 COM GUID 라고 한다. 

> 보통은 레지스트리 편집기의 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\SharedDLLs\` 에 dll 파일이 있지만, 이것은 윈도우 기본 파일인 듯하고, 새로 레지스트리를 등록한다고 이곳에 들어가는 것 같지는 않다

또는, 레지스트리 편집기에서 아래의 경로에 class id 가 등록된 것을 확인할 수도 있다.

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\HFCOMMAGENT.HFCommAgentControl.1\CLSID
```

# 파이썬에서 OCX 객체 사용하기

##### 주의사항
- OpenAPI 프로그램 실행시 매번 `HFCommAgent.dll` 모듈 정보를 레지스트리에 등록할 것을 강력이 권장한다고 한다. 왠지는 모르겠다.

## AgentControl 사용

`CHFCommAgent` 를 불러와야 하는 것 같다. 

```python

```

# 로그인

# 실시간 OHLC 가격 가져오기

##### 가져올 종목
- 코스닥 150: 주가
- 코스피 선물 200: 옵션가, 베이시스가

##### 실행 순서
- 틱 기준 OHLC 데이터 가져오기

# 가져온 데이터 다루기

- 엑셀 파일로 출력