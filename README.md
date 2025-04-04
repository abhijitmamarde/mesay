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