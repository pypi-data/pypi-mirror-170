git-darcs - Incremental import of git into darcs
================================================

[![Test](https://github.com/ganwell/git-darcs/actions/workflows/test.yml/badge.svg)](https://github.com/ganwell/git-darcs/actions/workflows/test.yml) [![CodeQL](https://github.com/ganwell/git-darcs/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/ganwell/git-darcs/actions/workflows/codeql-analysis.yml)

[git-darcs on pypi](https://pypi.org/project/git-darcs/)

Just call `git-darcs update`, it will import the current git-commit into darcs.
If you get new commits eg. using `git pull`, you can call `git-darcs update` and
it will try to import each commit into darcs. git-darcs will walk a truly linear
git-history, but it has some caveats. See: `Linearized history`.

By default the first import is shallow, only importing the current git-commit.
If you want to import the whole history use `git-darcs update --no-shallow`,
since we **linearize** the history by checking out each commit this can take
very long.

On the first import you can also supply a custom base-commit `git-darcs update
--base fa2b982` ignoring history you are not interested in.

The options `base` and `shallow` are ignored after the first import.

Use a [global `gitignore`](https://gist.github.com/subfuzion/db7f57fff2fb6998a16c) to ignore
`_darcs` in all your repositories.

With `git-darcs clone <source> <destination>` you can clone a darcs/git dual
repository locally. Both git and darcs will make sure no history-data is
duplicated on disk. To create git revision from my working-repositories I
clone the tracking repo and pull the patches using `git darcs pull <source>`
into the temporary repo. I push the git-repo and open PR. If the code-review
requires changes, I update my working-repository and repeat the process.

⚠️ **NOTE**: The tool is intentionally very minimal. It is for devs, they can
read tracebacks or change the code to fit better. There are no pytests, yet,
just me using it and having done a lot of tests to find the optimal linearized
history.

But why?
--------

I prefer to group changes by topic, so I am constantly amending commits/patches.
This is very easy in darcs and more complicated in git. Yes, I know about
`--fixup` and `--autosquash` in git. Also I can find independent low-risk
patches easily with `darcs show dependencies`, so I can constantly make PRs.
Making the final _breaking_ change/PR much smaller. This is less tedious for the
reviewers.

For darcs beginners
-------------------

* There is a great [video](https://hikari.acmelabs.space/videos/hikari-darcs.mp4) by
  [raichoo](https://hub.darcs.net/raichoo) the maintainer of
  [hikari](https://hikari.acmelabs.space/)
* You have to read the [darcs book](https://darcsbook.acmelabs.space/), you just
  have to
* `_darcs/pref/boring` is the equivalent of `.gitignore`, but has quite a wide
  definition of boring by default

Darcs does not handle `chmod` or symbolic links. The easiest way to work around
this is by letting `git` do the work. I have two git/darcs repositories for each
project:

* `project` (the repository I work in) containing a `.git` and a `_darcs` folder
* `project-tracking` (the repository that tracks changes from upstrream,
   also containing a `.git` and a `_darcs` folder

I then pull new darcs-patches from `project-tracking` into `project`. Once my
the changes are in upstream, I obliterate everything to the checkpoint (tag) I
started with and pull the patches (now via `git`) from `project-tracking`. Or I
remove `project` and clone it again from `project-tracking`.

Since I always make git-commits from the darcs-patches `git` will track `chmod`
and symbolic-links for me.

Usage
-----

<a href="https://asciinema.org/a/518694" target="_blank"><img
src="https://asciinema.org/a/518694.svg" /></a>

Note: this asciinema was made before `shallow` was default and before the
improved linearized history.

```
$> git-darcs --help
Usage: git-darcs [OPTIONS] COMMAND [ARGS]...

  Click entrypoint.

Options:
  --help  Sow this message and exit.

Commands:
  clone   Locally clone a tracking-repository to get a working-repository.
  update  Incremental import o git into darcs.
```

```
$> git-darcs update --help
Usage: git-darcs update [OPTIONS]

  Incremental import of git into darcs.

  By default it imports a shallow copy (the current commit). Use `--no-
  shallow` to import the complete history.

Options:
  -v, --verbose / -nv, --no-verbose
  -w, --warn / -nw, --no-warn     Warn that repository will be cleared
  -b, --base TEXT                 On first update import from (commit-ish)
  -s, --shallow / -ns, --no-shallow
                                  On first update only import current commit
  --help                          Show this message and exit.
```

```
$> git-darcs clone --help
Usage: git-darcs clone [OPTIONS] SOURCE DESTINATION

  Locally clone a tracking repository to get a working-repository.

Options:
  -v, --verbose / -nv, --no-verbose
  --help                          Show this message and exit.
```

```
Usage: git-darcs pull [OPTIONS] SOURCE [DARCS]...

  Pull from source darcs-repository into a tracking repository.

  A tracking repository is created by `git darcs update` and contains a git-
  and a darcs-repository. Arguments after `--` are passed to `darcs pull`.

Options:
  -v, --verbose / -nv, --no-verbose
  -w, --warn / -nw, --no-warn     Warn that repository will be cleared
  -a, --all / -na, --no-all       Pull all patches
  --help                          Show this message and exit.
```

Linearized history
------------------

If the history forks git-darcs will walk the history-branch offered by `git
rev-list --topo-order`. It will try to fast-forward every revision it gets into
the current revision. On the 'main' branch this will always work, so it will
record all these revisions. On the other branches (of the history) this will
fail and it will skip all these revisions, until the branches merge again and
fast-forward is possible.

git-darcs will track any moves that happened when skipping revisions so all
these moves will get recorded. It will add the complete log of the skipped
revisions into the patch that records all these changes.

This git-history:

```
$> git log --oneline --graph
* 74b2d99 (HEAD -> master) end > end0
* 9de72f8 end
*   a5f4bfb Merge branch 'b'
|\
| * 9c5e6c4 (b) bc, start1b1 > start1b2, ba0 > ba1, bb > bb0
| * 00781ed bb, start1b0 > start1b1, ba > ba0
| * 259f647 ba, start1 > start1b0
* | deab3ea start_merged > start_merged1
* |   de04805 Merge branch 'a'
|\ \
| * | 1e6f333 (a) ac, start1a1 > start1a2, aa0 > aa1, ab > ab0
| * | 63ccd72 aa, start1a0 > start1a1, aa > aa0
| * | a28638c aa, start1 > start1a0
| |/
* / c64713f start1 > start2
|/
* 83c267b start0 > start1
* 712ec2d start > start0
* 44d8cd1 start
```

becomes this darcs-history. Note that the moves correspond to the moves I logged,
there is never a `rmfile` or a `move` in the wrong direction. Here darcs
couldn't record branch `a` or `b` so all the changes appear in the patches
corresponding to the merge-commits.

```
* 74b2d99 end > end0
    move ./end ./end0
* 9de72f8 end
    addfile ./end
* a5f4bfb Merge branch 'b'
  9c5e6c4 bc, start1b1 > start1b2, ba0 > ba1, bb > bb0
  00781ed bb, start1b0 > start1b1, ba > ba0
  259f647 ba, start1 > start1b0
    move ./start_merged1 ./start
    addfile ./ba1
    addfile ./bb0
    addfile ./bc
* deab3ea start_merged > start_merged1
    move ./start_merged ./start_merged1
* de04805 Merge branch 'a'
  1e6f333 ac, start1a1 > start1a2, aa0 > aa1, ab > ab0
  63ccd72 aa, start1a0 > start1a1, aa > aa0
  a28638c aa, start1 > start1a0
    move ./start2 ./start_merged
    addfile ./aa1
    addfile ./ab0
    addfile ./ac
* c64713f start1 > start2
    move ./start1 ./start2
* 83c267b start0 > start1
    move ./start0 ./start1
* 712ec2d start > start0
    move ./start ./start0
* 44d8cd1 start
    addfile ./start
```

However if we remove the commit that prevented fast-forward, we get this
git-history:

```
$> git log --oneline --graph
* 4d57edd (HEAD -> master) end > end0
* 6526a18 end
*   f4facb0 Merge branch 'b'
|\
| * 9c5e6c4 (b) bc, start1b1 > start1b2, ba0 > ba1, bb > bb0
| * 00781ed bb, start1b0 > start1b1, ba > ba0
| * 259f647 ba, start1 > start1b0
* | 1e6f333 (a) ac, start1a1 > start1a2, aa0 > aa1, ab > ab0
* | 63ccd72 aa, start1a0 > start1a1, aa > aa0
* | a28638c aa, start1 > start1a0
|/
* 83c267b start0 > start1
* 712ec2d start > start0
* 44d8cd1 start
```

Again, there are no `rmfile` or `move` in the wrong direction, but it could
record the changes on branch `a`.

```

* 4d57edd end > end0
    move ./end ./end0
* 6526a18 end
    addfile ./end
* f4facb0 Merge branch 'b'
  9c5e6c4 bc, start1b1 > start1b2, ba0 > ba1, bb > bb0
  00781ed bb, start1b0 > start1b1, ba > ba0
  259f647 ba, start1 > start1b0
    move ./start1a2 ./start1_merged
    addfile ./ba1
    addfile ./bb0
    addfile ./bc
* 1e6f333 ac, start1a1 > start1a2, aa0 > aa1, ab > ab0
    move ./aa0 ./aa1
    move ./ab ./ab0
    move ./start1a1 ./start1a2
    addfile ./ac
* 63ccd72 aa, start1a0 > start1a1, aa > aa0
    move ./aa ./aa0
    move ./start1a0 ./start1a1
    addfile ./ab
* a28638c aa, start1 > start1a0
    move ./start1 ./start1a0
    addfile ./aa
* 83c267b start0 > start1
    move ./start0 ./start1
* 712ec2d start > start0
    move ./start ./start0
* 44d8cd1 start
    addfile ./start
```

I just realized that I only tried conflicting merges, lets see what happens with
a conflict-free merge:

```
$> git log --oneline --graph
* eef24d8 (HEAD -> master) end > end0
* 841c900 end
*   969ad57 Merge branch 'b'
|\
| * 76ca538 (b) bb2 > bb3
| * 0040cee bb1 > bb2
* | 663168a antiforward > antiforward0
* |   0d94733 Merge branch 'a'
|\ \
| * | d26d325 (a) aa2 > aa3
| * | 8090696 aa1 > aa2
| |/
* / fa7accb antiforward
|/
* 7bc2b76 aa0 > aa1, bb0 > bb1
* 665937d aa > aa0, bb bb0
* 1fd0236 aa, bb
```

git-darcs wasn't able to fast-forward branch 'b', so 969ad57 contains all the
moves done in `b`: `bb1` will skip to `bb3` directly, as expected.

```
* eef24d8 end > end0
    move ./end ./end0
* 841c900 end
    addfile ./end
* 969ad57 Merge branch 'b'
  76ca538 bb2 > bb3
  0040cee bb1 > bb2
    move ./bb1 ./bb3
* 663168a antiforward > antiforward0
    move ./antiforward ./antiforward0
* 0d94733 Merge branch 'a'
  d26d325 aa2 > aa3
  8090696 aa1 > aa2
    move ./aa1 ./aa3
* fa7accb antiforward
    addfile ./antiforward
* 7bc2b76 aa0 > aa1, bb0 > bb1
    move ./aa0 ./aa1
    move ./bb0 ./bb1
* 665937d aa > aa0, bb bb0
    move ./aa ./aa0
    move ./bb ./bb0
* 1fd0236 aa, bb
    addfile ./aa
```
