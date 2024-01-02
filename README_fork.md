## Fork of music diff 
https://github.com/gregchapman-dev/musicdiff



## remotes

- upstream : reference repository (read only)
  https://github.com/gregchapman-dev/musicdiff
- origin : fork
  https://github.com/florento/musicdiff



## history

- fork ref. repo on GitHub
- clone

````shell
git clone https://github.com/florento/musicdiff.git
````

- in local `mmusicdiff`  : 

```shell
git config remote.pushdefault origin # publish by default on the repository 'origin'
git config push.default current      # Publier par défaut sur une branche 
                                     # portant le même nom que la branche courante 
                                     # dans le dépôt de publication
git remote add upstream https://github.com/gregchapman-dev/musicdiff.git
git fetch upstream
```

new branch `tests` tracking automatically the branch `upstream/main`.

```shell
git checkout -b tests upstream/master
```



## merge edits in origin

les premières modifs ont été faites sur un clone (`musicdiff-GC/`) de `upstream` (sans fork)

on les copie dans le fork



- [x] Only in musicdiff-GC: .idea
- [x] Files musicdiff/.pylintrc and musicdiff-GC/.pylintrc differ
- [x] Files musicdiff/LICENSE and musicdiff-GC/LICENSE differ
- [x] Files musicdiff/README.md and musicdiff-GC/README.md differ
- [x] Only in musicdiff: README_fork.md
- [x] Only in musicdiff: ReleaseNotes_3.0.0.txt
- [x] Only in musicdiff-GC/docs: .nojekyll
- [x] Files musicdiff/docs/index.html and musicdiff-GC/docs/index.html differ
- [x] Only in musicdiff-GC/docs/musicdiff: __main__.html
- [x] Files musicdiff/docs/musicdiff/annotation.html and musicdiff-GC/docs/musicdiff/annotation.html differ
- [x] Files musicdiff/docs/musicdiff/comparison.html and musicdiff-GC/docs/musicdiff/comparison.html differ
- [x] Files musicdiff/docs/musicdiff/visualization.html and musicdiff-GC/docs/musicdiff/visualization.html differ
- [x] Files musicdiff/docs/musicdiff.html and musicdiff-GC/docs/musicdiff.html differ
- [x] Files musicdiff/docs/search.js and musicdiff-GC/docs/search.js differ
- [ ] Files musicdiff/musicdiff/__init__.py and musicdiff-GC/musicdiff/__init__.py differ
- [ ] Files musicdiff/musicdiff/__main__.py and musicdiff-GC/musicdiff/__main__.py differ
- [x] Only in musicdiff-GC/musicdiff: __pycache__
- [ ] Files musicdiff/musicdiff/annotation.py and musicdiff-GC/musicdiff/annotation.py differ
- [ ] Files musicdiff/musicdiff/comparison.py and musicdiff-GC/musicdiff/comparison.py differ
- [ ] Files musicdiff/musicdiff/m21utils.py and musicdiff-GC/musicdiff/m21utils.py differ
- [ ] Files musicdiff/musicdiff/visualization.py and musicdiff-GC/musicdiff/visualization.py differ
- [x] Files musicdiff/pypi_README.md and musicdiff-GC/pypi_README.md differ
- [x] Files musicdiff/setup.py and musicdiff-GC/setup.py differ
- [x] Files musicdiff/tests/test_nl.py and musicdiff-GC/tests/test_nl.py differ
- [x] Files musicdiff/tests/test_scl.py and musicdiff-GC/tests/test_scl.py differ
- [x] Files musicdiff/tests/test_score_visualization.py and musicdiff-GC/tests/test_score_visualization.py differ
- [x] Files musicdiff/tests/test_utils.py and musicdiff-GC/tests/test_utils.py differ





