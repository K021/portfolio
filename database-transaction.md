<h1 class='header'><span>Transaction</span></h1>

> — <cite>[wikipedia](https://ko.wikipedia.org/wiki/데이터베이스_트랜잭션), [개발자 홀로 서기](http://mommoo.tistory.com/62), [limkydev](http://limkydev.tistory.com/100)</cite>

## Transaction 이란

transaction 이란, 데이터베이스를 변경하는 작업의 단위이다. transaction 은 다음 네 가지 질의어(sql) 요청으로 구성되어 있다:

1. select
2. insert
3. update
4. delete


## Transaction 의 특성

transaction 은 다음 네 가지 특성을 지닌다:

1. 비분리성 (Atomicity): 데이터베이스는 transaction 단위로 변경된다. transaction 을 구성하는 일부 쿼리만 반영되는 경우는 없다. transaction 전체가 반영되거나 반영되지 않거나이다. 
2. 일관성 (Consistency): transaction 이 대상으로 하는 데이터베이스는 일관적이어야 한다. transaction 중 데이터베이스에 변경이 있어도, 그 변경사항이 반영되지 않는다.
3. 독립성 (Isolation): 한 transaction 이 다른 transaction 의 연산에 끼어들 수 없다.
4. 영구성 (Durability): 한번 반영된 transaction 은 영구히 반영된다. 

각각의 첫 글자를 모아, 이 성질을 ACID 라고 부르기도 한다. 이론적으로 데이터베이스 시스템은 각각의 transaction 에 대해 상기 성질들을 보장하지만, 실제로는 성능을 위해 종종 무시되기도 한다. transaction 을 지원하는 데이터베이스를 transactional database 라고 한다. 대부분 관계형데이터베이스가 해당된다.  


## transaction 의 실행과정

- Begin the transaction
- Execute several queries: 쿼리를 실행하고 변경된 데이터를 만든다. 그러나 데이터베이스에 적용하지는 않는다.
- Commit the transaction: 변경된 데이터를 데이터베이스에 적용한다. 


## Commit 과 Rollback

transaction 이 완료되면 commit, 중간에 취소되거나 오류가 발생하여 처음으로 되돌리는 경우에는 Rollback.

- commit: transaction 의 쿼리가 성공하면, 변경된 데이터를 데이터베이스에 적용하는 연산. 
- rollback: transaction 이 비정상적으로 종료된 경우, transaction 을 처음부터 다시 시작하거나, 진행된 transaction 을 취소하는 연산. 이것은 DBMS 설정에 따라 다르다. 사용자가 원하는 경우, transaction 은 commit 전에 언제든지 rollback 을 진행할 수 있다.  

> DBMS: Database Management System 의 약자로, 데이터베이스를 수정하고 저장, 관리할 수 있는 소프트웨어이다. Mysql, Postgresql 등이 있다.


## Transaction 의 상태

- Active
- Failed: 오류가 나서 실패
- Aborted: 중지되어 rollback 연산 실행
- Partially committed: transaction 이 완료되었으나 commit 되지 않은 상태
- Committed: 완료후 데이터베이스에 적용까지 된 상태
