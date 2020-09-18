<h1 class='header'><span>datetime</span></h1>

##### 참고문서

- &mdash; <cite>[[8percent]: django timezone 문제 파헤치기](https://8percent.github.io/2017-05-31/django-timezone-problem/)</cite>
- &mdash; <cite>[[howchoo]: Working with datetime objects and timezones in Python](https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python)</cite>
- &mdash; <cite>[[Django.doc]: Time zones](https://docs.djangoproject.com/ko/2.1/topics/i18n/timezones/)</cite>


# 장고 DateTimeField 

장고의 `models` 에는 `DateTimeField` 라는 필드가 있다. 날짜와 시간을 관리해주는데, 파이썬의 `datetime.datetime` 객체를 사용한다. 그런데 타임존이 반드시 설정되어 있어야 해서, 자동으로 필드를 채울 것이 아니라 직접 입력해주는 로직을 짜고자 한다면 문제가 생길 수 있다. 

> 장고 DB 에는 언제나 UTC 기준의 datetime 이 저장된다. 

## django 프로젝트의 timezone 설정

한국시간을 사용하기 위해서, django settings.py에 다음과 같은 설정이 필요하다. 

```python
TIME_ZONE = 'Asia/Aseoul'

USE_TZ = True
```

이 설정은 다음과 같은 기능에 영향을 미친다. 

1. `datetime.datetime` 의 `now()` 나 `today()` 로 현재 정보를 가져오는 경우, 타임존 설정에 따라 UTC+9 값이 나온다. 그러나 생성된 datetime 객체는 타임존 정보가 없는 naive datetime 객체이다. 
2. 생성된 datetime 객체를 사용해 DB에 저장하면 UTC 기준 시간 값으로 저장된다. time-zone-aware datetime 으로 timezone 을 변경해서 저장해도 DB 에는 늘 UTC로 저장이 된다. 
3. django 모델을 통해 DB 에서 읽은 DateTimeField 타입의 컬럼 값은 UTC 타임존의 time-zone-aware datetime 객체이다. (time-zone-aware datetime 은 naive datetime 에 반대되는 개념으로, timezone 설정 여부로 나뉜다.)

> 참고: [Django.doc - timezone](https://docs.djangoproject.com/ko/2.1/topics/i18n/timezones/)


### 발생하는 문제와 해결

1. DB 에서 읽어온 time-zone-aware datetime 객체는 UTC 기준의 날짜이므로, 한국 시간과 맞지 않는다. 한국 시간으로 9시 전이면, 날짜도 맞지 않게 된다.
2. 이 time-zone-aware datetime 객체와 naive datetime 객체를 비교하면 에러가 발생한다.[^naive-aware]
3. django 모델의 DateField 를 저장하고 읽을 때는 UTC 기준이 아닌 한국 기준으로 동작한다. 

[^naive-aware]: 다음과 같은 에러가 발생한다 'TypeError: can't subtract offset-naive and offset-aware datetimes'

해결방법은 다음과 같다. 

1. 데이터베이스의 시간과 현재 시간을 비교할 때는, `datetime.datetime.now()` 가 아닌 `django.utils.timezone.now()` 를 사용하자. 이 메서드는 UTC 기준 tz-aware datetime 객체를 반환한다. 
2. 한국시간 기준 datetime 객체는 `django.utils.timezone`의 `localtime()` 메서드로 생성할 수 있다. 깔-끔.
3. naive datetime 객체를 어쩔 수 없이 사용해야 하는 경우, 아래와 같은 코드를 사용해 tz-aware datetime 객체로 변경할 수 있다.

##### 장고에서 datetime 객체를 tz-aware 로 변경하기

```python
from datetime import datetime
from django.urtils import timezone
	
dt = datetime.strptime('2018-10-31 07:30:00', '%Y-%m-%d %H:%M:%S')
# 기본적으로 localtime 의 타임존을 이용하는 것으로 보이고, 
# 특정 타임존을 사용하기 위해선 tzinfo 에 tzinfo 클래스 객체를 넣어주어야 한다.
dt_aware = timezone.make_aware(dt)
>>> datetime.datetime(2018, 11, 1, 17, 0, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)
```


## 오류: DateTimeField 에 naive datetime 객체를 넣었을 때

setting.py 에 `USE_TZ = True` 설정이 되어 있는 경우, DateTimeField 에는 tz-aware datetime 객체를 넣어야 한다. 그렇지 않으면 다음과 같은 오류가 난다. 

```bash
RuntimeWarning: DateTimeField Todo.expiration received a naive datetime (2018-11-01 17:00:00) while time zone support is active.
  RuntimeWarning)
```
이는 당연하게도, `USE_TZ = False`로 해당 설정을 끄면 발생하지 않는다. 


# datetime 의 주요 메서드

#### 문자열에서 날짜와 시간 읽기: `datetime.strptime(time_string, time_format)`

```python
from datetime.datetime import strptime

# 시, 분, 초는 모두 대문자로 나타내야 한다.
# 월, 일은 모두 소문자여야 한다.
# 년은 대문자일 때는 2018로, 소문자일 때는 18을 사용한다.
dt = strptime('2018-10-31 07:30:00', '%Y-%m-%d %H:%M:%S')
>>> datetime.datetime(2018, 10, 31, 7, 30)
```

#### 문자열로 시간 출력하기: `datetime.strftime(time_format)`

```python
d.strftime("%B %d, %Y")
>>> 'January 10, 1984'

d.strftime("%Y/%m/%d")
>>> '1984/01/10'

d.strftime("%d %b %y")
>>> '10 Jan 84'

d.strftime("%Y-%m-%d %H:%M:%S")
>>> '1984-01-10 23:30:00'
```

#### time format

- `%a`: Locale’s abbreviated weekday name.
- `%A`: Locale’s full weekday name.
- `%b`: Locale’s abbreviated month name.
- `%B`: Locale’s full month name.
- `%c`: Locale’s appropriate date and time representation.
- `%d`: Day of the month as a decimal number [01,31].
- `%H`: Hour (24-hour clock) as a decimal number [00,23].
- `%I`: Hour (12-hour clock) as a decimal number [01,12].
- `%j`: Day of the year as a decimal number [001,366].
- `%m`: Month as a decimal number [01,12].
- `%M`: Minute as a decimal number [00,59].
- `%p`: Locale’s equivalent of either AM or PM.
- `%S`: Second as a decimal number [00,61].
- `%U`: Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
- `%w`: Weekday as a decimal number [0(Sunday),6].
- `%W`: Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
- `%x`: Locale’s appropriate date representation.
- `%X`: Locale’s appropriate time representation.
- `%y`: Year without century as a decimal number [00,99].
- `%Y`: Year with century as a decimal number.
- `%Z`: Time zone name (no characters if no time zone exists).
- `%%`: A literal '%' character.

#### 국제 표준으로 시간 출력하기: `datetime.isoformat()`

```python
d.isoformat()
>>> '1984-01-10T23:30:00'
```

#### datetime 정보 변경: `datetime.replace()`

`datetime.replace()` 메서드로 `tzinfo`를 바꿀 수 있다. 물론, 시간이나 다른 정보도 바꿀 수 있다. 그냥 바꾸면 바꿀 수 없어서 이 메서드를 사용해야 한다.

datetime 객체 자체를 바꾸는 것이 아니라, 바뀐 객체를 출력한다.

```python
# timezone.utc 는 datetime.timezone.utc 로, 
# utc 시간 정보를 갖고 있는 tzinfo 객체이다.
d.replace(tzinfo=timezone.utc)
>>> datetime.datetime(2018, 11, 1, 17, 0, tzinfo=<UTC>)
```

#### datetime timezone 변경 출력: `datetime.astimezone(tzinfo)`

요 메서드의 특별한 점은, 타임존이 다른 두 datetime 객체를 생성해도, 둘을 비교하면 같은 datetime 으로 인식한다는 것이다. 

```python
import datetime
import pytz

dt = datetime.datetime.utcnow()
dtc = pytz.utc.localize(dt)
dta = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

dtc == dta
>>>> True
```

#### tz-aware datetime: `datetime.datetime(tzinfo=)`

`tzinfo` 객체를 datetime 객체 생성시 넣어줄 수 있다.

```python
from datetime import datetime, timezone

d = datetime(2018, 10, 30, 11, tzinfo=timezone.utc)
```



# django.utils 주요 메서드

#### tz-aware datetime: `timezone.now()`

장고 내장 timezone 은 tz-aware 가 기본이다.

```python
from django.utils import timezone

# 장고 내장 timezone 은 타임존 설정이 기본값이다.
timezone.now()
>>> datetime.datetime(2018, 10, 30, 11, 45, 18, 505033, tzinfo=<UTC>)
```

#### 현재 위치 `tzinfo`: `timezone.get_current_timezone()`

장고 내장 timezone 의 `get_current_timezone` 을 사용해 현재 위치의 `tzinfo` 객체를 얻을 수 있다.

```python
from django.utils import timezone

# 현재 위치의 타임존 설정이 가능하다. 
timezone.get_current_timezone()
>>> <DstTzInfo 'Asia/Seoul' LMT+8:28:00 STD>

# tzinfo 객체 자체를 만들 수 있다. 
tz = timezone.get_current_timezone()
dt = datetime(2018, 11, 1, 15, 0, tzinfo=tz)

dt
>>> datetime.datetime(2018, 11, 1, 15, 0, tzinfo=<DstTzInfo 'Asia/Seoul' LMT+8:28:00 STD>)
```
#### 현재 타임존 aware datetime 객체: `timezone.localtime()`

장고 내장 timezone 에서 바로 로컬 타임존으로 설정된 datetime 객체를 얻을 수 있다.

```python
from django.utils import timezone as djtz

djtz.now()
datetime.datetime(2018, 10, 30, 22, 38, 47, 155070, tzinfo=<UTC>)

djtz.localtime()
datetime.datetime(2018, 10, 31, 7, 39, 20, 352966, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD
```



# pytz 주요 메서드

#### 지역별 타임존 tzinfo 객체 가져오기: `timezone(timezone_string)`

```python
from datetime import datetime
import pytz

d = datetime(2018, 11, 1, 17)

# 타임존 가져오기
# pytz.timezone() 으로 가져온 tzinfo 객체는 시간대 설정이 조금 이상하다. 
tz = pytz.timezone('Asia/Seoul')
>>> <DstTzInfo 'Asia/Seoul' LMT+8:28:00 STD>

# 그런 관계로 그냥 datetime 초기 값으로 설정하면 안 된다.
dtz = datetime(2018, 11, 1, 17, tzinfo=tz)
>>> datetime.datetime(2018, 11, 1, 15, 0, tzinfo=<DstTzInfo 'Asia/Seoul' LMT+8:28:00 STD>)
```

#### tzinfo 로 타임존 설정: `tzinfo.localize(datetime)`

```python
from datetime import datetime
import pytz
# 타임존 객체
tz
>>> <DstTzInfo 'Asia/Seoul' LMT+8:28:00 STD>

# 타임존으로 localize() 함수를 사용해야 정상적인 타임존으로 돌아온다. 
tz.localize(d)
>>> datetime.datetime(2018, 11, 1, 17, 0, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)

# 원래 datetime 객체는 변하지 않는다
d
>>> datetime.datetime(2018, 11, 1, 17, 0)
```

#### timezone 정규화: `pytz.utc.normalize(datetime)`

```python
from datetime import datetime
import pytz

# utc normalize 는 tz-aware 객체만 가능
pytz.utc.normalize(d)
>>> ValueError: Naive time - no tzinfo set

pytz.utc.normalize(tz1.localize(d))
>>> datetime.datetime(2018, 11, 1, 8, 0, tzinfo=<UTC>)
```