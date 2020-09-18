# Pytest 로 Django test 하기

> ##### 출처 
> <cite>[perhapsspy gist](https://gist.github.com/perhapsspy/fc5521376df87036be2d034d1beaf69b)</cite>
> 
> ##### 주의 사항
> pytest 모듈은, django test 의 실행 순서를 지키지 않는다. 파일을 찾는 대로 실행한다. 이는 하나의 test suit 에서 transaction test 와 non transaction test 를 섞어서 할 경우 문제가 된다고 한다. — <cite>[atodorov.org](http://atodorov.org/blog/2017/12/26/on-pytest-django-and-liveservertestcase-with-initial-data/)</cite>


django 기본 테스트는 데이터베이스 마이그레이션 덕에 느리고 번거롭기 때문에 py.test와 model_mommy를 사용해서 빠르게 테스트를 하는 방법을 소개함.

- py.test : http://pytest.org/
- pytest-django : http://pytest-django.readthedocs.org/
- model_mommy : http://model-mommy.readthedocs.org/

## 테스트 파일 레이아웃

```bash
# Django 기본 test
# django app안에 tests 모듈을 찾아서 실행함.
./manage.py test 
# 엄청 오래걸림 

# pytest-django
# test 접두어가 붙은 파일이나 모듈을 찾아서 테스트로 돌림.
py.test
# 빠름!
```

django 기본 test의 호환성을 유지하면서 py.test를 쓰기 위해 레이아웃을 아래와 같이 잡음

```bash
# django app 생성시 자동으로 생긴 tests.py는 삭제
project/app_name/tests/
    __init__.py
    test_modeltest1.py
    ...
```

## 설치

```bash
pip install pytest-django model_mommy
```

## 설정

pytest.ini 파일을 생성

```ini
[pytest]
DJANGO_SETTINGS_MODULE=store.settings_test
norecursedirs=*/templates/* */templatetags/* */static/* media collected_static .git
addopts=--nomigrations
```

- norecursedirs 부분에 test가 없는 불필요한 폴더들을 제외해줄 수 있음
- addopts에 --nomigrations 옵션이 있어야 마이그레이션 절차를 생략해서 빨라짐

## 테스트 작성 예제

```python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy

from order.models import Order
from payment.point.models import PointAction


class TestPoint(TestCase):
    # setUp 에서 사용할 모델 인스턴스를 미리 만들어두면 편함.
    # 만들때 model_mommy를 써서 만들면 알아서 생성해줌.
    # 모델 만들때만 이렇게 하고나면 나머지는 일반 테스트 코드와 차이가 없음.
    def setUp(self):
        self.user = mommy.make(User) 
        self.order = mommy.make(Order)
        self.order2 = mommy.make(Order, user=self.user)
        self.action = PointAction(user=self.user)

    def test_point_accumulate_and_use(self):
        pa = self.action
        pa.accumulate(1000)
        pa.accumulate(500)
        assert pa.amount() == 1500
        pa.use(1100, self.order)
        assert pa.amount() == 400
        pa.accumulate(100)
        assert pa.amount() == 500
        pa.use(500, self.order2)
        assert pa.amount() == 0
```

맥북에어에서도 0.5초만에 돌아가는 테스트를 볼 수 있습니다.
