# github 활용한 협업 활동

## 1. 준비사항

* 로컬 저장소

  ` $ git clone `

* 로컬 저장소 (B)

  `$ git init  `

## 2. 시나리오

작업 전 pull 작업 후 push

## 3. Git Branch

```
Git 개발 흐름에서 branch 매우 중요; 독립적인 개발환경을 제공하여 동시에 다양한 작업을 진행
일반적 브랜치 이름은 해당 작업 나타냄
```

### 1. 기초 명령어

```bash
$ git branch # branch확인
$ git branch {name} # branch name 생성
$ git checkout {name} # move to branch
$ git branch -d # delete
$ git checkout -b # 생성 및 이동

브랜치 병합
$ git merge feature (master)
# master branch로 feature 브랜치 이력 가져오기 (병합)
```

