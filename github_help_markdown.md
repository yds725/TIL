### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m 'test 기능 개발 완료'
   
   $ git log --oneline
   3644c81 (HEAD -> feature/test) test 기능 개발 완료
   2849053 (origin/master, testbranch, master) test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   ```


3. master 이동

   ```bash
   $ git checkout master
   
   $ git log --oneline
   2849053 (HEAD -> master, origin/master, testbranch) test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   ```
   
   


4. master에 병합

   ```bash
   $ git merge feature/test
   Fast-forward
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   
   ```
   
   


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   3644c81 (HEAD -> master, feature/test) test 기능 개발 완료
   2849053 (origin/master, testbranch) test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   ```

   

6. branch 삭제

   ```bash
   $ git 	
   ```
   
   

---

### 상황 2. merge commit

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch signout.txt
   $ git add .
   $ git commit -m 'complete signout'
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   $ touch master.txt
   $ git add .
   $ git commit -m 'update master'
   
   $ git log --oneline
   459eda7 (HEAD -> master) update master
   3644c81 (origin/master, origin/feature/test) test 기능 개발 완료
   2849053 test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   ```

   

5. master에 병합

    ```bash
   $ git checkout master
   $ git merge feature/signout
   ```

   

6. 결과 -> 자동으로 *merge commit 발생*

   

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   1f41bfb (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * db8ac76 (feature/signout) complete signout
   * | 459eda7 update master
   |/
   * 3644c81 (origin/master, origin/feature/test) test 기능 개발 완료
   * 2849053 test branch
   *   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   |\
   | * c9787b5 -main.html
   * | 88c6a1a update
   |/
   * 87dd072 web
   
   ```

   

8. branch 삭제

   ### 1. Fast-forwarding



---

### 상황 3. merge commit 충돌

 -- 동일한 파일을 수정했을 때 (충돌?)

1. feature/board branch 생성 및 이동

   ```bash
   
   ```

   

2. 작업 완료 후 commit

   ```bash
   
   $ git log --oneline
   740e697 (HEAD -> hotfix/test) hotfix test
   1f41bfb (master) Merge branch 'feature/signout'
   459eda7 update master
   db8ac76 (feature/signout) complete signout
   3644c81 (origin/master, origin/feature/test) test 기능 개발 완료
   2849053 test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # test.txt 수정
   $ git add .
   $ git commit -m 'master test'
   ```

   

5. master에 병합

   


6. 결과 -> *merge conflict발생*

   ```
   hotfix branch editing
   <<<<<<< HEAD
   hotfix branch dfasdfasfd
   =======
   hotfix branchlll
   >>>>>>> hotfix/test
   ```
   
   


7. 충돌 확인 및 해결

   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 5 commits.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   ```
   
   


8. merge commit 진행

    ```bash
    $ git add .
    $ git commit
    ```
```
   
   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    ```bash
   $ git log --oneline
   b01a6e5 (HEAD -> master) merge fix
   7d593e1 master new fix
   4b83e3a (hotfix/test) new hotfix
   740e697 hotfix test
   1f41bfb Merge branch 'feature/signout'
   459eda7 update master
   db8ac76 (feature/signout) complete signout
   3644c81 (origin/master, origin/feature/test) test 기능 개발 완료
   2849053 test branch
   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   88c6a1a update
   c9787b5 -main.html
   87dd072 web
   
   $ git log --oneline --graph
   *   b01a6e5 (HEAD -> master) merge fix
   |\
   | * 4b83e3a (hotfix/test) new hotfix
   * | 7d593e1 master new fix
   |/
   * 740e697 hotfix test
   *   1f41bfb Merge branch 'feature/signout'
   |\
   | * db8ac76 (feature/signout) complete signout
   * | 459eda7 update master
   |/
   * 3644c81 (origin/master, origin/feature/test) test 기능 개발 완료
   * 2849053 test branch
   *   ef621fc Merge branch 'master' of https://github.com/yds725/mulcam-scenario
   |\
   | * c9787b5 -main.html
   * | 88c6a1a update
   |/
   * 87dd072 web
   
```

   


10. branch 삭제

```bash
 $ git branch -d hotfix/test
```



## 4. 추가

1. branch merge -no-ff {branch name}

   ```bash
   $ git merge -no-ff branch
   ```

   패스트 포워딩 상황에서 커밋을 억지로 발생시키기 브랜치 이력을 유지할 수 잇음

   

2. Branch rebase 

3. Commit

   `commit를 통해 이력이 확정하면 해쉬값이 부여되면 이 값을 통해 커밋인지를 확인`

   워킹 디렉토리 변화 없고 스테이징 에리어 변화 없고 변경사항 없음

   ```bash
   $ git commit 
   noting to commit, working tree clean
   ```

   ```bash
   $ git commit
   ```

4. commit 메세지 작성

   부제 vim 활요

   ```bash
   $ git commit
   ```

   * 편집모드 (i)
     * 문서 폅징
   * 명령모
     * dd: 해당 줄 삭제
     * :wq - 저장 및 종료
       * w: write(저장)
       * q: quit(종료
     * :q! - 강제 종료
       * ! - 강제로 뭐해라

    log 활용 명령어

   ```bash
   $ git log
   $ git log --oneline
   $ git log -1 (해당 개수?)
   $ git log -1 --oneline
   $ git log --oneline --graph
   ```

   HEAD: 현재 작업하고 있는 커밋 이력 및 브랜치에 대한 포인터

   ```bash
   a26b82b (HEAD -> master)
   # current points to master branch
   ```

   

   직전 커밋 메세지 수정

   ` 아래의 명령어는 커밋 이력을 변경(기존에 있던 걸 대체)하기 때문에 조심해야 한다. 공개된 저장소에 (원격 저장소) 이미 푸시된 이력이라면 절대 해선느 안된다`

   ```bash
   $ git commit --amend
   ```

   ## 커밋시 특정 파일을 빠뜨렷을 떄

   만약 staging area에 특정 파일 (omit_file.txt)을 올리지 않아서 커밋이 되지 않았을 때!

   커밋메시지 작성후 저장 사진이 찍힌다?

   ```bash
   $ git add .(specific file)
   $ git commit --aend
   ```

## Staging area

* 커밋 이력이 있는 파일을 수정한 경우

  ```bash
  $ git status
  On branch master
  Your branch is ahead of 'origin/master' by 8 commits.
    (use "git push" to publish your local commits)
  
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
          modified:   txt1.txt
  
  no changes added to commit (use "git add" and/or "git commit -a")
  ```

* commit history 없는 파일 경우

  ```bash
  $ git status
  On branch master
  Your branch is ahead of 'origin/master' by 8 commits.
    (use "git push" to publish your local commits)
  
  Changes not staged for commit:
    # staged 하게 하기 위한
    (use "git add <file>..." to update what will be committed)
    
    (use "git restore <file>..." to discard changes in working directory)
          modified:   txt1.txt
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          holy.txt
  
  no changes added to commit (use "git add" and/or "git commit -a")
  
  ```

  ```bash
  $ git status
  On branch master
  Your branch is ahead of 'origin/master' by 8 commits.
    (use "git push" to publish your local commits)
  
  Changes to be committed:
  # unstage 하기 위해
    (use "git restore --staged <file>..." to unstage)
          new file:   holy.txt
  
  ```

  add 취소하기

  ```bash
  $ git restore --staged <file>
  ```

  * 구버전은
  *  $ git reset head <file>

  Working dir 변화 삭제

  ```bash
  git 모든 commit 내용은 되돌릴 수 있다
  다만 아래 의 WD 내용은 삭제하는 것은 되돌릴 수 없다
  ```

  $ git restore <file>

  구버전은 $ git checkout -- <file>

## 예시 상황

1. 브랜치에서 파일 변경후 커밋
2. 마스터 브랜치에서 파일 수정 (add / commit x)
3. merge

```bash
$ git merge test
```

## reset vs revert

` commit이력을 되돌리는 작업을 한다`

* reset: 이력을 삭제한다. 
  * 워킹디렉토리 상태로 되돌아간다; 수정된 내용은 유지한 채로 add이전 상태로 되돌아간다
  * --hard: 워킹 디렉토리의 내용까지 바꿈?
  * 노 옵션 : 워킹 디렉토리 는 유지하고 이력만 삭제
  * --soft: add까지 진행된 staging area까지 적용되는 상태; 커밋 이력은 삭제 
* revert: 되돌렸다는 이력을 남긴다
* 