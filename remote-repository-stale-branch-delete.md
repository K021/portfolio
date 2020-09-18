### Remote repository stale branch 로컬에서 삭제하기
`git remote show <저장소단축이름>`: 리모트 저장소의 구체적인 정보를 확인할 수 있다. 리모트 저장소의 URL과 추적하는 브랜치를 출력한다. 이 명령은 git pull 명령을 실행할 때 master 브랜치와 Merge 할 브랜치가 무엇인지 보여 준다.   



```
➜  delta git:(feature/form) ✗ git remote show delta
* remote delta
  Fetch URL: https://github.com/K021/delta.git
  Push  URL: https://github.com/K021/delta.git
  HEAD branch: master
  Remote branches:
    dev                             tracked
    master                          tracked
    refs/remotes/delta/feature/form stale (use 'git remote prune' to remove)
  Local branches configured for 'git pull':
    dev    merges with remote dev
    master merges with remote master
  Local refs configured for 'git push':
    dev    pushes to dev    (local out of date)
    master pushes to master (up to date)
``` 
```
refs/remotes/delta/feature/form stale (use 'git remote prune' to remove)
```

: 리모트 저장소에 있던 브랜치가 삭제되었지만, 로컬 정보에 남아있는 것이다. 이것을 없에주기 위해선 `git remote prune <저장소이름>`을 입력하면 된다. `--dry-run`옵션을 적용하면 프룬 전에 어떤 브랜치를 프룬하게 되는지 확인할 수 있다.
