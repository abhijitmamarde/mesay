# Installation 

```bash
uv tool install git+https://github.com/abhijitmamarde/mesay 
```

if already installed same version, do reinstall - 

```bash
uv tool install --reinstall git+https://github.com/abhijitmamarde/mesay
```

Then run using:

```bash
uvx mesay
```

Or on the fly use with different python versions. 
Version should be supported / higher than mentioned in `pyproject.toml` 
example: for `requires-python = ">=3.7"`, would run on 3.7 and higher, but 3.7 below would not work!

```bash
uvx --python 3.10 git+https://github.com/abhijitmamarde/mesay
uvx --python 3.11 git+https://github.com/abhijitmamarde/mesay
```

can even specify the branch or commit sha or release tag

```bash
# specify branch main
uvx --python 3.11 git+https://github.com/abhijitmamarde/mesay@main

# specify branch dev
uvx --python 3.11 git+https://github.com/abhijitmamarde/mesay@dev

# specify specific gitsha - ae3bf9c
uvx --python 3.11 git+https://github.com/abhijitmamarde/mesay@ae3bf9c

# specify the release tag - rel0.1.0
uvx --python 3.11 git+https://github.com/abhijitmamarde/mesay@rel_0.1.0
```

Test commit to main!

# Bump Version

```bash
# patch: 0.0.X -> 0.0.X+1
uv run bump2version patch

# minor: 0.X.0 -> 0.X+1.0
uv run bump2version minor

# major: X.0.0 -> X+1.0.0
uv run bump2version major
```

- only advised to run from master/main branch
- if there is any specific release branch, do it from there, and then merge the release to main branch
- never advised to do from feature/dev branch
- if there is CI/CD pipeline setup, do this release bump from there

for pushing create tag, use command:

```bash
git push --tag
```
