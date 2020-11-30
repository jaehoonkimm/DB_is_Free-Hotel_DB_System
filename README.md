# DB Project
## 변경점 및 참고사항(수시로 업데이트)  
#### django-admin-rangefilter 추가  
- pip install django-admin-rangefilter
#### <html에서 관리자계정/일반계정 로그인 여부에 따라 서로 다른 내용 띄우기> (20.11.26 AM 03:13 )
- Django의 템플릿 언어 사용
  - 예시 : {% 문법 %}  
  - [참고 링크](https://velog.io/@hidaehyunlee/Django-%ED%85%9C%ED%94%8C%EB%A6%BF-%EC%96%B8%EC%96%B4)  
    - {% if user.is_authenticated %}
      - 일반 유저로 로그인 된 경우, 해당 태그 이하 내용을 실행
    - {% else %}  
      - if 조건에 걸리지 않을 경우(현재 예시에선 일반 유저 로그인 되지 않았을 경우), 태그 이하 내용을 싱행
    - {% endif %}
      - 템플릿 언어로 if문 사용했으면 해당 태그 반드시 사용해서 닫아주어야 합니다. (if문 중첩으로 2번 썼으면, 2번 다 닫아줘야함)
  - 관리자 계정 검증의 경우,
    - {% if request.user.is_superuser %} 
- __현재 index.html 페이지는 아래와 같은 구조로 로그인 검증이 구현되어 있음__
- IF 관리자로 로그인 되어 있는가?
  - True -> 관리자용 페이지 표출
- Else
  - IF 일반 유저 계정으로 로그인 되어 있는가?
    - True -> 일반 유저용 페이지 표출
  - Else
    - 로그인 페이지 표출 (일반유저, 관리자 둘다 여기서 로그인 가능)
    
#### <DB의 대대적인 구조조정> (20.11.23 PM 23:21 기준)
- git pull origin main으로 꼭 로컬에서 pull 받고 작업해주세요!  
  - 일부 Table 삭제 (프로젝트 핵심이 아닌 것들)  
  - Foreign Key, Primary Key 조정 및 오류 나는 부분들 수정  
  - 각 Table별 Primary Key type 전부 Int로 변경 및 Auto Increment 적용  
  - 필요없는 필드 삭제 및 기타 등등...  
#### <base.html 추가 및 기존 html 파일에 base.html 상속 적용> (20.11.23 PM 21:53 기준)
- base.html 파일이 추가되어, 모든 html 페이지에 공통적으로 적용될 내용들(Ex. Nav, Footer, 기타 기초 레이아웃 등)을 한번에 담고 있게 됩니다.
  - {% block ~~~ %} 이런 형태로 생긴 내용들이 base.html 파일과 다른 html 파일들에 적용이 되어 있습니다.
  - base.html이 모든 파일에 공통적으로 적용될 title, body의 내용을 담고 있으며, 각각 html 파일들은 기본적으로 base.html 파일의 내용을 상속 받으며, 여기에 더해 각각 html 파일의 block title, block contents 안에 든 내용을 같이 합쳐진다고 생각하시면 됩니다. 
  - [참고 링크](https://pyrois.tistory.com/7)
----------
### Github Issue 사용법 (꼭 써주세요!)
#### Issue 발행
- Github 저장소 내 Issues 메뉴에서 'New issue' 버튼을 통해 새로운 이슈 발행. 

  - Title에 issue의 주제 기입 (Ex. Reservation HTML Page 생성 및 views 연결)
    - 아래 본문에는 필요한 정보나 기타 사항 기입
    
  - 당장 본인이 작업을 시작할 Issue라면 우측 메뉴에서 Assignees에 본인 클릭해서 등록
  
  - 또한, Assignees 밑 Project 메뉴에서 Main Function Board 클릭하기 
    - Github 저장소의 Issues, Pull requests, Actions 메뉴 우측의 Projects 메뉴에 들어가면 현재 Main Function Board가 생성되어 있으며, 이곳에 본인이 방금 생성한 이슈를 보드 쪽으로 끌어다놔서 팀원들에게 현재 본인이 진행중인 일정을 알릴 수 있고, 통합적인 일정 관리가 가능함 (해야 될 일은 ToDo에 쌓아놓고, 작업 진행중인건 In Progress, 완료된건 Done으로 끌어서 옮기기)
----------
##### Issue에 대한 Branch 생성
- Issue가 발행되면 아래에 issue 번호가 #N 형태로 붙음. (Ex. #3 opened 2 hours ago by jaehoonkimm)

- 본인 Local의 Terminal에서 다음 코드와 같은 형태로 Issue에 대한 Branch 생성 (issue# 뒤에 이슈번호 기입, 뒤에는 간략하게 이슈의 주제)
  ```terminal
    git branch issue#3-Add_reservation_page
  ```
- 이제 해당 Branch에서 해당 Issue에 대한 작업을 진행
  - 반드시 작업 전에 터미널에서 Git pull해서 Github 서버 저장소에 현재까지 업로드된 작업 내역을 최신화하고 진행하기
---------- 
##### Branch에서의 작업 프로세스
- 본인의 Local PC에서 작업한 것을 Git에 알려주기 위해 Git add를 사용
  ```terminal
    git add . (.을 붙이면 현재 위치한 디렉토리 기준으로 변경이 발생한 모든 파일을 git에 알려줌)
    git add index.html (특정 파일명, 또는 디렉토리를 지정해주면 해당 파일만 지정 가능)
    git reset (Add를 잘못 했을 경우, 해당 명령어로 지금까지 Add된 내역을 모두 취소 가능, But, Add 이후에 이미 
                commit 했으면 Add가 아니라 commit을 취소해야함)
  ```
  
- git add가 되었으면, 현재 git은 우리가 수정한 내역을 추적하고 있음 (알고 있음)
  - git commit을 통해 현재까지의 작업 내역을 Git의 History에 추가하여 저장이 가능 (이 덕분에, 나중에 문제가 생겨도 commit 단위로 롤백이 가능함. 게임의 세이브 같은 느낌)
  ```terminal
    git commit -m 'commit message 쓰는 부분 (따옴표 꼭 써줘야함)'
  ```
  
  - 위 코드를 통해 commit 가능
  
  - 좋은 commit 메시지를 작성하는 방법은 다음 링크 참고 [Git commit 메세지 규약](https://medium.com/hashbox/git-commit-%EB%A9%94%EC%84%B8%EC%A7%80-%EA%B7%9C%EC%B9%99-conventional-commits-71710f7f53c/)
  
    - Commit을 하면, 이제 현재까지 작업 내역(add 해준 파일들만)을 여러분의 Local PC에 저장된(Clone된) 저장소 안의 Git 파일이 저장하고 있게 됩니다. 즉, 서버에는 아직 안 올라갔습니다.
    - Commit 후에 Push를 하면 최종적으로 서버(Github 저장소)에 올라갑니다. But, 매번 Commit 할때마다 꼬박꼬박 Push를 할 필요 없습니다. Commit 여러번 쌓인 상태로 Push해도 똑같습니다.
    
    - 우리는 매번 Branch에서 작업을 하고 있으므로, 다음과 같이 Push 합니다.
      ```terminal
        git push origin issue#3-Add_reservation_page (git push origin Branch이름)
      ```
-------------
- github로 돌아와서, 저장소 메뉴에서 Pull Requests 메뉴로 들어간 후에, New pull request 버튼을 눌러 
  - base를 main으로 가만히 두고, compare를 여러분이 방금 push한 Branch로 선택하면 됩니다. Create Pull Request를 눌러서 생성하면 끝!
  - compare의 의미 그대로, Github가 자동으로 여러분의 코드와 base(main Branch)의 코드를 비교합니다. 충돌나는 부분이 없으면 바로 Merge를 눌러서 합칠 수 있습니다.
  
    - But, 만약 충돌나는 부분이 있다면, 일정 부분을 수동으로 수정해줘야 될 수도 있습니다. 이 경우 수정 버튼을 눌러서 충돌이 생겼다고 표시되는 부분에
    - 새로 작성한 코드를 남기고, 지워야 할 코드를 지우면 최종적으로 Merge(main Branch와 issue Branch를 합쳐서 최종적으로 메인 프로젝트에 반영)가 가능합니다.
    
      - __Merge하는 것과, 코드를 지우는 것은 반드시 신중하게! 지워도 될지, Merge해도 될지 모르겠다면 꼭 코드 리뷰를 요청해주세요!__
