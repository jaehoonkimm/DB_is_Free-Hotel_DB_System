## DB Project

### Github Issue 사용법 (꼭 써주세요!)
##### Issue 발행
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
  - 좋은 commit 메시지를 작성하는 방법은 다음 링크 참고 [Git commit 메세지 규약](https://medium.com/hashbox/git-commit-%EB%A9%94%EC%84%B8%EC%A7%80-%EA%B7%9C%EC%B9%99-conventional-commits-71710f7f53c){: target="_blank"}
  
