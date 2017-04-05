# lecovi.github.io

Leo's personal site. My very own crap! Enjoy it!

# Installation notes

1. Clone the repo.
2. Checkout to source branch and install requirements.
4. Run `nikola`.
5. Edit your crap.

### Prerequisites

```bash
sudo apt install python-pip
sudo apt install libxml2-dev libxslt1-dev zlib1-dev
```

## Clone

```bash
git clone git@github.com:lecovi/lecovi.github.io.git
```

## Requirements

You need to have `pip` to install *requirements*.

> It would be nice to have `virtualenvwrapper`

```bash
mkvirtualenv -p $(which python3) mis
git checkout src
cd mis
pip install -r requirements
nikola auto
```

## Run nikola

```bash
nikola auto
```

## Edit your crap

- Edit reStructuredText inside `stories`
- Edit reStructuredText inside `posts`