Zut
===

Reusable Python, Django and PostgreSql utilities.

## Install

From PyPI:

    pip install zut

From Git, last version:

    pip install git+https://gitlab.com/ipamo/zut.git@main

Use SSH instead of HTTPS url:

    pip install git+ssh://git@gitlab.com/ipamo/zut.git@main

Specific version, including extra dependencies:

    pip install git+https://gitlab.com/ipamo/zut.git@v0.3.1#egg=zut[extra]

In a `requirements.txt` file, including extra dependencies:

    zut[extra] @ git+https://gitlab.com/ipamo/zut.git@v0.3.1#egg=zut[extra]


## Dev quick start

Install Python, its packet manager (`pip`) and PostgreSql.
Under Linux, also install password manager `pass` (used as _credentials manager_).

Windows pre-requisites:

- Download [Python](https://www.python.org/downloads/) and install it.
- Download [PostgreSql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads), install it, and add binaries (`C:\Program Files\PostgreSQL\14\bin`) to PATH.

Linux (Debian) pre-requisites:

    sudo apt install python3-venv python3-pip postgresql pass

Create Python virtual environment (example for Windows):

    python -m venv .venv      # Debian: python3 -m venv .venv
    .\.venv\Scripts\activate  # Linux: source .venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt

Create test database (cf. parameters in `tests/settings.py`). Example:

    sudo -u postgres psql -c "create database test_zut encoding 'utf8' template 'template0'"
    
For Linux, configure password manager `pass`. Example:

    # Import your GPG key, show key identifier and mark key as trusted
    gpg --import my-private-gpg-key.asc
    gpg --list-secret-keys
    gpg --edit-key mykey@example.org
    trust
    5
    o
    q

    # Initialize "pass" with your GPG key
    pass init mykey@example.org

Run tests:

    python -m unittest

Run commands :

    python -m zut --help


## Publish library

Configure `~/.pypirc`. Example:

```conf
[distutils]
    index-servers =
    pypi
    testpypi
    zut

[pypi]
    username = __token__
    password = # use project-scoped token instead

[testpypi]
    # user-scoped token
    username = __token__
    password = pypi-xxxxx...

# -----------------------------------------------------------------------------
# Project-scoped token
# Usage example: twine --repository zut
#
[zut]
    repository = https://upload.pypi.org/legacy/
    username = __token__
    password = pypi-xxxxx...
```

Prepare distribution:

    pip install twine              # if not already done
    python -m zut checkversion
    python tools.py clean
    python setup.py sdist bdist_wheel
    twine check dist/*

Upload tarball on PyPI:

    # $env:HTTPS_PROXY="..."                         # if necessary
    # $env:TWINE_CERT="C:\...\ca-certificates.crt"   # if necessary
    twine upload --repository zut dist/*
