# sphinx-autopyproject

Move as much Sphinx configuration as possible from `conf.py` to `pyproject.toml`! *Might even be ... everything*

(If you are interested in more automatically generated API documentation, check out [`sphinx-automagicdoc`](https://github.com/csachs/sphinx-automagicdoc) as well.)

## Usage
Either run `spinx-autopyproject-build` to run `sphinx-build` without the need for a `conf.py` to exist, 
or if you want to use a `conf.py`, add the line:
```python
from sphinx_autopyproject.auto import *
```
To configure, set the `[tool.sphinx-autopyproject]` section:

```toml
[tool.sphinx-autopyproject]
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx_rtd_theme",
]

language = "en"
source_suffix = ['.rst']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
```
The `[tool.sphinx-autopyproject.autopyproject]` section is to configure `sphinx-autopyproject` if desired.
Supported is the `dynamic` subsection, which allows to automatically fetch configuration values from other sources,
such as the package metadata. Multiple dynamic fetchers are supported: for `type="package"`, the local package will be built (using `build`), for `type="token"`, a variable assignment will be searched via plain file reading (e.g. to extract `__version__`), or for `type="python"`, the given package/variable will be imported via Python.

```toml
[tool.sphinx-autopyproject.autopyproject.dynamic]
project = { type="package", value="name"}
copyright = { type="package", value="author"}
author = { type="package", value="author"}
version = { type="package", value="version"}
```

The `sys_path` list can be used to add directories to `sys.path`.

## License

MIT