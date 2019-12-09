# Git 기초

> git은 분산형버전관리시스템 (DVSC)

## 0. 기본

윈도우에서 git를 활용하기 위해 git bash가 필요하다

설정 내용을 git config --global -l

## 1. git 저장소 설정

프로젝트폴더에서 git를 활용

```python
$git init
Initialized empty git repo in (master)
```

* 해당 디렉토리 내에 .git이라는 숨김 폴더 생성, 모든 git과 관련된 동작은 해당폴더에 기록된
* git bash에서 master라는 브랜치가 표시

## 2. add

파일들을 staging area로 옮기는 형태?

```python
$git add a.txt
$git add /image
$git status
```

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        images/
        "\353\247\210\355\201\254\353\213\244\354\232\264 \352\270\260\354\264\210 \353\254\270\353\262\225.md"

nothing added to commit but untracked files present (use "git add" to track)
```

## 3. commit

git에서 이력을 남기기 위해 commit를 통해 진행 commit을 남길 떄에는 항상 커밋 메시지 작성. 메시지는 해당 이력에 대한 정보를 담는다.

```bash
$git status
```

add: 커밋할 대상 파일 선정

commit: 이력의 확정

## 4. 원격 저장소 (remote repos) 활용

### 1. 원격 저장소 설정

```bash
$git remote add origin http://~
```

원격 저장소(remote)를 origin라는 이름으로 유얼엘에 추가? 혹시 잘못 설정 되었으면 명령어를 통해 삭제 가능

'origin' 으로 설정된 원격 저장소에 'push' 함





