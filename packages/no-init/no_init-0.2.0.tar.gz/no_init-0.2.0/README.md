# no_init
- Tool that checks that there are no `__init__.py` in your modules.
- It's opinionated tool, sometimes `__init__.py` files are useful. But often if you use them you end up in a circular import error mess.
- Some packages (eg mypy) works better with `__init__.py`, for this case you can pass `--allow-empty` parameter.

```sh
# install
pip install no_init

# usage (you can also use python -m no_init)
no_init my_module

# require empty __init__.py for each all submodules (recursively)
no_init --require-empty my_module

# require __version__ variable in  my_module/__init__.py (no other content is allowed)
no_init --require-version my_module
```


## pre-commit hook
```yaml
```


## dev install
```sh
pip install -e .[dev]
```
