# lecovi.github.io
Leo's personal site

Mi sitio personal

# Installation notes

## Requirements

You need to have `pip` to install `requirements.txt`.
It would nice to have `virtualenvwrapper`

```console
$ git checkout src
$ cd mis
$ nikola auto
```

### Debian

```console
$ sudo apt install python-pip
$ sudo apt install libxml2-dev libxslt1-dev zlib1-dev
```

### Virtualenvwrapper

```console
$ sudo pip install virtualenvwrapper
```

Add to your `.bashrc`:

```bash
export WORKON_HOME=~/.envs
source /usr/local/bin/virtualenvwrapper.sh
```

Create virtualenv:

```console
$ mkvirtualenv -p $(which python3) mis
$ pip install -r mis/requirements.txt
```

