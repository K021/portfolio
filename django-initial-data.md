




<h1 class='header'><span>Django initial data</span></h1>



## 개괄

##### 이 문서의 목적
장고 테스트 문서 중 [Rollback emulation](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#rollback-emulation) 관한 내용에 사용된 *'Any initial data loaded in migrations'* 라는 표현이 정확히 무엇을 의미하는지를 탐구

##### 알아낸 사실의 요약
- 장고에서는 데이터베이스를 set up 할 때, 초기 데이터를 넣어주는 로직이 있다.
- 초기 데이터를 넣어주는 다양한 방법[^method]이 있는데, 그 중 migration 파일을 작성하는 것이 있다.
- 따라서 [Rollback emulation](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#rollback-emulation) 에서 다루는 *'Any initial data loaded in migrations'* 는 테스트 데이터베이스를 set up 할 때, migration 파일을 통해 생성된 데이터를 말한다. 

[^method]: [migration file](https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations), [fixture](https://docs.djangoproject.com/en/2.0/howto/initial-data/#providing-data-with-fixtures), TestCase 의 setUp() 메서드




<a id='initial-data'></a>

# Providing initial data for models

> — <cite>[Django Doc - Providing initial data for models](https://docs.djangoproject.com/en/2.0/howto/initial-data/#providing-initial-data-for-models) 중 일부</cite>

우리가 앱을 처음으로 set up 할 때, 데이터베이스에 미리 hard-coding 된 데이터를 만들어 두는 것이 유용한 경우가 있다. migrations 또는 fixtures 로 initial data 를 준비할 수 있다. 

> ##### initial data 의 쓰임새
> 앱의 특정 기능을 위해서 필요하나, 나중에 바뀔 수 있는 데이터를 initial data 로 설정해두면 좋다. 보통 가능한 선택지들, 또는 타임 존, 국가 등의 리스트인 경우가 많다. 

## Providing initial data with migrations

특정 앱을 위한 초기 데이터가 자동적으로 로드되길 바란다면, [data migration](https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations)을 작성하자. Migrations 는 test database 를 set up 할 때 실행된다. 따라서 해당 데이터는 만들어진 테스트 데이터베이스 상에 준비되어 있고, 이것에는 [약간의 제약사항(Rollback Emulation Issue)](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#test-case-serialized-rollback)이 있다. 

> [data migration 문서 번역](#data-migrations)





<a id='data-migrations'></a>

# Data Migrations

> — <cite>[Django Doc - Data Migrations](https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations) 중 일부</cite>

데이터베이스 schema 를 변경하면서, 그와 더불어 데이터베이스의 데이터도 migration 으로 바꿀 수 있다. 

데이터를 변경하는 migrations 를 보통 "data migrations"라고 부른다. schema migrations 와 함께 별도의 migrations 로 작성하는 것이 가장 좋다. 

schema migrations 와는 다르게 data migrations 는 자동적으로 생성되지 않는다. 그러나 그것을 작성하는 것은 그리 어렵지 않다. 장고의 migration file 은 [Operations](https://docs.djangoproject.com/en/2.0/ref/migration-operations/) 로 이루어져 있고, data migration 에 사용할 주된 operation 은 [RunPython](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#django.db.migrations.operations.RunPython) 이다. 

> [RunPython 문서 번역](#runpython)

먼저, 작성할 빈 migration file 을 만들자. (장고가 알아서 올바른 위치에 파일을 두고, 적절한 이름과 의존성을 설정해줄 것이다.)

```python
python manage.py makemigrations --empty yourappname
```

이제, 생성된 파일을 열자. 다음과 같이 생겼을 것이다. 

```python
# Generated by Django A.B on YYYY-MM-DD HH:MM
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0001_initial'),
    ]

    operations = [
    ]
```

이제 우리가 해야 할 것은, 새로운 함수를 만들고 [RunPython](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#django.db.migrations.operations.RunPython) 이 그 함수를 사용하게 하는 것이다. [RunPython](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#django.db.migrations.operations.RunPython) 는 두개의 매개변수를 받는 callable 객체를 매개변수로 받는다 — 첫 번째 인자는 우리 모든 모델의 historical version 을 가지고 있는 [app registry](https://docs.djangoproject.com/en/2.0/ref/applications/) 인데, 해당 마이그레이션이 역사적으로 어느 지점에 위치하는지 알기 위한 것이다. 두 번째는, 직접 데이터베이스 스키마를 변경할 수 있는 [SchemaEditor](https://docs.djangoproject.com/en/2.0/ref/schema-editor/) 이다. (그러나 이것을 직접 수정하면 migration autodetector 를 혼란시킬 수 있다는 것을 주의하자.)

`first_name` 값과 `last_name` 값을 합쳐 새로운 `name` 필드를 기록하는(populate) 간단한 migration 을 작성해보자. (정신을 차려보니 모든 사람이 first name 과 last name 을 가진 것은 아니라는 사실을 깨달았다.)

```python
frome django.db import migrations

def combine_names(apps, schema_editor):
    # Person 모델을 직접적으로 import 할 수 없다. 
    # 이 migration 이 기대하는 것보다 새로운 버전일 수 있기 때문이다.
    # 우리는 historical version 을 사용해야 한다. 
    Person = apps.get_model('yourappname', 'Person')
    for person in Person.objects.all():
        persion.name = f'{person.first_name} {person.last_name}'
        person.save()
        
class Migration(migrations.Migration)

    dependencies = [
        ('yourappname', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(combine_names),
    ]
```

작성이 완료되었으면, 하던대로 `python manage.py migrate` 를 실행해주면 된다. 다른 migrations 와 함께 우리의 data migraion 도 실행될 것이다. 

migration 을 되돌리고자 할 때 실행할 또 다른 로직이 있다면, RunPython 의 두 번째 인자로 넣어주면 된다. (Rollback 기능) 
 





<a id='runpython'></a>

# RunPython: one of Operations of Migration

> — <cite>[Django Doc - RunPython](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#runpython) 중 일부</cite>

class RunPython(code, reverse_code=None, atomic=None, hints=None, elidable=False)[source](https://docs.djangoproject.com/en/2.0/_modules/django/db/migrations/operations/special/#RunPython)

historical context 안에서 커스텀 파이썬 코드를 실행한다. `code`는 두 개의 인자를 받는 callable object 이다:

1. project history 중 operation 장소와 일치하는 historical model 을 갖고 있는 django.apps.registry.Apps 의 인스턴스
2. SchemaEditor 의 인스턴스 

`reverse_code` 변수는 해당 migrations 를 적용하지 않을 때 실행된다. 이 callable 객체는 `code` 객체가 한 일을 되돌린다. (Rollback 기능) 







<a id='schema-editor'></a>

# Django Schema Editor

> — <cite>[Django Doc - SchemaEditor](https://docs.djangoproject.com/en/2.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor) 중 일부</cite>

장고의 마이그레이션 시스템은 두 가지 부분으로 나뉜다. 

1. 어떤 operation 이 실행될 것인가를 계산하고 저장하는 로직 (django.db.migrations)
2. '모델 만들기' 또는 '필드 삭제하기' 와 같은 것을 SQL로 바꿔주는 데이터베이스 추상 계층 (SchemaEditor)

장고를 사용하는 일반 개발자라면, SchemaEditor 를 직접적으로 사용하고 싶을 경우는 없을 것이다. 그러나 자신만의 migration system 을 만들고자 하거나, 좀 더 고급 기능이 필요하다면, Schema Editor 는 SQL 보다 훨씬 유용할 것이다. 


