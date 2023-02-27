# python-example-module
A simple module I created for learning how my other code can import a module like this one from git. I included the `faker` package from PyPi to make sure I could get this module to work even if it uses a third-party package.

### How to use this module in your code
- Add `python-example-module = {git = "git@github.com:joeg3/python-example-module.git"}` to your project's `pyproject.toml` file.
- In your code, add `from fakeutils.name_faker import NameFaker` to import this module, and then use the `NameFaker` class.

### When updating a module like this one
- After updating this module, update the version in the `pyproject.toml` file so users of the module know there's been changes.

