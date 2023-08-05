# `package-installation-test`

This package is designed to verify that you can successfully install Python packages from PyPI using `pip`, and subsequently use them. In particular, it is meant to test that you are installing packages **to the correct Python installation**. It is written to complement a question on Stack Overflow about this problem, to allow for testing the solutions offered there.

## Installation

Install this package from PyPI using `pip install package-installation-test`. Alternately, clone the repository, navigate to the root of the repository, and then use `pip install .` to install it. Note the `.` at the end of the latter command (specifying the current directory).

Note carefully that the installed package has a **different name** from the name used on PyPI and in this repository; although we install `package-installation-test` (notice that this is not a valid Python identifier anyway), code will refer to the package as `example_package`.

## Command-line use

Once installed, you should be able to "run" the package as a module, using `python -m example_package`.

Installation will also create a wrapper executable called `demo-example-package`, which you can run at the command line by that name.

Either of these options should print a diagnostic message that looks like:
```
Version 1.0.0 of example_package successfully installed.
The source code is in <...>.
```
where the `<...>` is replaced by the actual path where the code was installed.

## API

You can verify that the code is usable as a package by `import`ing it from the interactive prompt:
```
>>> import example_package
>>>
```
This provides two functions:

`main` - prints the same message as before.

`home` - returns the path to where the code was installed, as a `pathlib.Path` instance.

Both of these functions take no arguments.

## Troubleshooting

If the above steps don't work as advertised, the problem is **almost certainly** that `pip` installed to a different installation of Python than the one you are trying to use. (If the `demo-example-package` doesn't work, that's because you installed to a Python installation that isn't the first one on the `PATH`. 

Please read the corresponding question and answer on Stack Overflow to understand how to solve the problem.