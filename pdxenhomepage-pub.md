# (주)피디젠 홈페이지

> 유전체 분석 관련 의료 스타트업 (주)피디젠의 홈페이지입니다.  
> Homepage &mdash; <cite>http://pdxen.com</cite>  
> Github Repository &mdash; <cite>https://github.com/K021/pdxen-homepage</cite> (현재 private 상태라 볼 수 없습니다.)

이 프로젝트는 (주)피디젠의 홈페이지로, 회사와 회사의 서비스를 소개하고 바이어들이 쉽게 연락할 수 있도록 하기 위한 목적을 갖고 있으며, 프로젝트 완료 후 인수인계 당시 인수자가 프로그래머가 아니라는 문제를 해결하기 위해, 홈페이지의 글을 쉽게 편집할 수 있는 mark-up 언어인 `Xenmark`를 만들었습니다. 

![](img/pdxenhomepage/mac-main-1.png)
![](img/pdxenhomepage/mac-main-2.png)
![](img/pdxenhomepage/mac-main-3.png)
![](img/pdxenhomepage/mac-main-4.png)
![](img/pdxenhomepage/mac-footer.png)

> [더 많은 이미지 보기](./img/pdxenhomepage)

## 구현된 페이지 및 기능 개괄

- 메인 페이지
	- 스타트업 느낌의 메인페이지 디자인
	- 한 페이지의 회사 소개 메인 페이지
- about, products, services 페이지를 통해 회사와 회사의 서비스 소개
- contacts 페이지를 통한 메일 보내기 기능
- signup 및 login 기능
- editor 페이지에서 xenmark 를 통한 편집 기능
- 모바일 반응형 페이지


# editor 의 xenmark 편집기능

피디젠의 홈페이지의 관리자가 비개발자라고 하더라도, 글을 작성하고 수정하기 편하도록 일종의 마크업 언어를 만들었다. 그것이 Xenmark 이다. 피디젠 홈페이지는 아주 간단한 형태의 웹앱으로, 이 Xenmark 편집 기능을 제외하면 아주 초보적인 수준이라 딱히 상술할 것이 없다. Xenmark 에 관해 더 자세히 알 고 싶다면 다음의 두 글을 참고하자:

- [Xenmark 사용 가이드](./xenmark-guide-pub.md)
- [Xenmark 코드 분석](xenmark-ko-pub.md)
