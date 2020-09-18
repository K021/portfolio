## python

- 도움말: `python --help` or `python -h`
- 현 디렉토리에 설치된 파이썬 버전: `python --version` or `python -V`


## pyenv
> python 가상환경 관리 도구

- 도움말: `pyenv --help` or `pyenv -h`
- 설치된 모든 가상환경과 파이썬 버전: `pyenv versions`  
- 현 디렉토리에 설치된 가상환경과 파이썬 버전: `pyenv version` 

<hr class="clear">

- 파이썬 버전별로 설치하기: `pyenv install <version>` 
- 설치할 수 있는 파이썬 버전 목록: `pyenv install --list`
- 파이썬 버전별로 삭제: `pyenv uninstall -f <version>` (`-f` 옵션이 없으면 안 된다)
- `requirements.txt`로 설치하기: `pyenv -r <requirements-path>`

<hr class="clear">

- 특정 파이썬 버전으로 가상환경 만들기: `pyenv virtualenv <version> <env-name>` 

<hr class="clear">

- set virtualenv here: `pyenv local <env-name>`
- set global python version: `pyenv global <env-name>`
- set shell-specific python version: `pyenv shell <env-name>`

<hr class="clear">

- 모든 명령어 목록: `pyenv commands`
- 특정 명령어 도움말: `pyenv <command> --help`

<hr class="clear">
- pyenv update: `brew update pyenv` 파이썬 버전이 잘 뜨지 않는다면 그건 pyenv가 업데이트 되지 않았기 때문이다.

### pyenv shell 

- 쉘의 `PYENV_VERSION` 환경변수를 변경함으로써 로컬 env 설정을 무시하고 특정 버전의 env를 설정하는 것
- 프로그램을 설치할 환경이 필요하나, 그 환경을 특정 디렉토리에 설정할 필요가 없을 때 사용한다. 
- `pyenv shell --unset`으로 되돌릴 수 있다.

vs code 에서 다음과 같은 사항을 설치한 적이 있다. 필요한 건지 모르겠다.

```bash
pyenv shell 3.6.2
/usr/local/var/pyenv/versions/3.6.2/bin/python -m pip install -U pylint
------------------------------------------------------------
~ » pyenv shell 3.6.2                                                                              ElohimAwmar@MacBook-Air
------------------------------------------------------------
~ » /usr/local/var/pyenv/versions/3.6.2/bin/python -m pip install -U pylint                        ElohimAwmar@MacBook-Air
Collecting pylint
  Downloading https://files.pythonhosted.org/packages/60/c2/b3f73f4ac008bef6e75bca4992f3963b3f85942e0277237721ef1c151f0d/pylint-2.3.1-py3-none-any.whl (765kB)
    100% |████████████████████████████████| 768kB 2.0MB/s 
Collecting mccabe<0.7,>=0.6 (from pylint)
  Downloading https://files.pythonhosted.org/packages/87/89/479dc97e18549e21354893e4ee4ef36db1d237534982482c3681ee6e7b57/mccabe-0.6.1-py2.py3-none-any.whl
Collecting isort<5,>=4.2.5 (from pylint)
  Downloading https://files.pythonhosted.org/packages/e5/b0/c121fd1fa3419ea9bfd55c7f9c4fedfec5143208d8c7ad3ce3db6c623c21/isort-4.3.21-py2.py3-none-any.whl (42kB)
    100% |████████████████████████████████| 51kB 9.1MB/s 
Collecting astroid<3,>=2.2.0 (from pylint)
  Downloading https://files.pythonhosted.org/packages/d5/ad/7221a62a2dbce5c3b8c57fd18e1052c7331adc19b3f27f1561aa6e620db2/astroid-2.2.5-py3-none-any.whl (193kB)
    100% |████████████████████████████████| 194kB 187kB/s 
Collecting lazy-object-proxy (from astroid<3,>=2.2.0->pylint)
  Downloading https://files.pythonhosted.org/packages/ad/57/a36f682668ffc453e86ddfb5a2a49848edcb7bd04a210a5a8692a48ed9c4/lazy-object-proxy-1.4.1.tar.gz
Collecting six (from astroid<3,>=2.2.0->pylint)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting typed-ast>=1.3.0; implementation_name == "cpython" (from astroid<3,>=2.2.0->pylint)
  Downloading https://files.pythonhosted.org/packages/4c/16/9a45b107957d9e50ff9c99352516e59966433d5cf9148e6b4ba60bd4ce96/typed_ast-1.4.0-cp36-cp36m-macosx_10_9_x86_64.whl (216kB)
    100% |████████████████████████████████| 225kB 111kB/s 
Collecting wrapt (from astroid<3,>=2.2.0->pylint)
  Downloading https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
Installing collected packages: mccabe, isort, lazy-object-proxy, six, typed-ast, wrapt, astroid, pylint
  Running setup.py install for lazy-object-proxy ... done
  Running setup.py install for wrapt ... done
Successfully installed astroid-2.2.5 isort-4.3.21 lazy-object-proxy-0.0.0 mccabe-0.6.1 pylint-2.3.1 six-1.12.0 typed-ast-1.4.0 wrapt-1.11.2
You are using pip version 18.1, however version 19.2.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```


## pip 
> python package manager. python 에 기본적으로 내장되어 있다. 

- 도움말: `pip --help` or `pip -h`
- 패키지 설치: `pip install <package> <package> ...`
- 패키지 삭제: `pip uninstall <package> <package> ...`
- `requirements.txt`로 설치: `pip install -r <requirements-path>`
- `requirements.txt` 생성: `pip freeze > requirements.txt`

<hr class="clear">

- 현재 pip 버전: `pip --versions` or `pip -V`