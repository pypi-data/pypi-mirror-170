# sphinx-automagicdoc

## Description

This plugin can create API documentation stubs (akin to [sphinx-autogen](https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html)), with the significant difference that the creation is done dynamically and on the fly, and the files remain _virtual_ and are monkey-patched into Sphinx IO routines.

Creating a whole set of files matching the structure of a module violates DRY (don't repeat yourself) and enhances the risk of documentation becoming out of sync during e.g. refactorings. Therefore, `sphinx-automagicdoc` can be used to dynamically source the rST structure from the Python source as the single source of truth.

Based upon the monkey patched virtual filesystem, additionally, other files or strings can be injected into the Sphinx tree.

## Usage

```python
# e.g. added to conf.py

# name the modules automagicdoc should process
automagic_modules = ["nameOfYourPackage"]
automagic_ignore = ["*test*"]

# README.rst and LICENSE from the root directory (outside of doc directory)
# will appear available as README.rst and LICENSE.rst inside doc/
automagic_copy_files = {
    "README.rst", "README.rst",
    "LICENSE.rst": "LICENSE",
}

# index.rst's content is based upon a string
automagic_files = {
    "index.rst": """
Welcome to the documentation!
=============================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   README
   LICENSE
   nameOfYourPackage
"""
}
```

## Example

This repo builds its documentation using [sphinx-autopyproject](https://github.com/csachs/sphinx-autopyproject) as described in [`.github/workflows/doc.yml`](.github/workflows/doc.yml) using Github Actions and deploys to [Github pages](https://csachs.github.io/sphinx-automagicdoc).


## See also
[sphinx-autopyproject](https://github.com/csachs/sphinx-autopyproject) to use `pyproject.toml` instead of `conf.py`.


## License

MIT
