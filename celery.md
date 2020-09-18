Task Queue: 작업 대기열  
Message: 수행할 작업  
Broker: Celery 와 Task Queue 를 중개하는 프로그램  
Celery: 백엔드 다중 작업 프로그램   
Broker - Rabbitmq 설치 `brew install rabittmq`  
Celery 설치 `pip install celery`  

rabbitmq 백그라운드 실행 `brew services start rabbitmq`  
rabbitmq 그냥 실행 `rabbitmq-server`  
: `~/.zshrc`에 `export PATH=$PATH:/usr/local/sbin`를 추가해주어야 한다. rabbitmq 실행 스크립트가 저기에 저장되는데, bash profile (.zshrc)에 자동으로 포함되지 않기 때문이다.  
celery 실행 `celery -A tasks worker --loglevel=info`  
: tasks 는 파일 이름이다. 이 파일이 있는 곳에서 실행해야 한다.  
: Django 에서 커스터마이징을 한 후에는 tasks 대신 config 를 넣어두어야 한다. 

<celery 실행 화면>  
`Connectec to amqp://guest:**@127.0.0.1:5672//`: 셀러리가 local 컴퓨터 5672번 포트로 Broker에 연결된 것을 의미한다.  

백그라운드에서 실행하고 싶다면, 프로그램을 쓰거나, supervisord 를 사용하자.  

Calling the Task  
`app = Celery('celery', broker='pyamqp://guest@localhost//')`라고 정의된 상태에서,  
`@app.task`가 붙은 함수는 `원래함수.delay(원래함수 인자)`라는 속성이 생긴다.  

task 모듈(celery를 사용하는 함수가 적혀있는 파일)을 변경하면, worker를 껐다 켜야 한다. worker를 켤 때 모듈을 로딩해서 켜기 때문이다.  

delay 메서드로 셀러드를 실행하면, 리턴 값으로 AsyncResult 인스턴스를 반환한다. 이 인스턴스는 작업 상태, 결과 값, 또는 에러 등 해당 작업과 관련된 다양한 정보를 저장하고 있는데, 이것을 이용하기 위해서는, 해당 정보가 저장되는 `result backend`를 따로 가지고 있어야 한다. 모듈에서 Celery 인스턴스를 선언할 때 `backend='redis://localhost'` 인자를 넣어주면 된다. (물론 redis는 캐쉬 서버라고.)  

장고에 붙이기  
config folder 안에 `celery.py` 만들기  
config 에서 바로 사용할 수 있게 `__init__.py`에 작성하기  

 
# beat

> todo-management 프로젝트를 참고하자. 

### 1. rabbitmq-server 를 실행한다.

```bash
(todo) ------------------------------------------------------------
~/python/todo-management/todo(master*) » rabbitmq-server

              RabbitMQ 3.6.14. Copyright (C) 2007-2017 Pivotal Software, Inc.
  ##  ##      Licensed under the MPL.  See http://www.rabbitmq.com/
  ##  ##
  ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
  ######  ##        /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
  ##########
              Starting broker...
```

서버 정지는 `rabbitmqctl stop` 으로, 서버 상태는 `sudo rabbitmqctl status` 으로 확인할 수 있다. 

### beat 실행 전 celery worker 실행이 필요하다. 

```bash
celery -A config worker -l info
```

```bash
~/python/todo-management/todo(master*) » celery -A config worker -l info

celery@MacBook-Air.local v4.2.1 (windowlicker)

Darwin-16.7.0-x86_64-i386-64bit 2018-11-05 01:34:57

[config]
.> app:         config:0x10f8b2eb8
.> transport:   amqp://guest:**@localhost:5672//
.> results:     disabled://
.> concurrency: 4 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . send_notification_mail

[2018-11-05 01:34:58,071: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2018-11-05 01:34:58,092: INFO/MainProcess] mingle: searching for neighbors
[2018-11-05 01:34:59,133: INFO/MainProcess] mingle: all alone
[2018-11-05 00:28:45,181: WARNING/MainProcess] /usr/local/var/pyenv/versions/3.6.3/envs/todo/lib/python3.6/site-packages/celery/fixups/django.py:200: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn('Using settings.DEBUG leads to a memory leak, never '
[2018-11-05 00:28:45,181: INFO/MainProcess] celery@MacBook-Air.local ready.
[2018-11-05 00:28:48,887: INFO/MainProcess] Received task: test[e2624650-9123-4850-b518-01123bed6e65]
[2018-11-05 00:28:48,898: INFO/ForkPoolWorker-2] Task test[e2624650-9123-4850-b518-01123bed6e65] succeeded in 0.0018583940109238029s: ': test executed'
```

### 그런 후에 beat 실행

`celery.py` 가 들어있는 `config` 모듈의 바로 상위 폴더에서 다음 명령으로 beat 실행:

```bash
celery -A config beat --loglevel=info
```

```bash
~/python/todo-management/todo(master*) » celery -A config beat --loglevel=info
celery beat v4.2.1 (windowlicker) is starting.
__    -    ... __   -        _
LocalTime -> 2018-11-04 23:56:27
Configuration ->
    . broker -> amqp://guest:**@localhost:5672//
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> 5.00 minutes (300s)
[2018-11-04 23:56:27,283: INFO/MainProcess] beat: Starting...
[2018-11-04 23:56:28,320: INFO/MainProcess] Scheduler: Sending due task add-every-30-seconds (test)
[2018-11-04 23:56:29,296: INFO/MainProcess] Scheduler: Sending due task add-every-30-seconds (test)
[2018-11-04 23:56:30,296: INFO/MainProcess] Scheduler: Sending due task add-every-30-seconds (test)
[2018-11-04 23:56:31,296: INFO/MainProcess] Scheduler: Sending due task add-every-30-seconds (test)
```