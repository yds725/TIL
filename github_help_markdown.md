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

