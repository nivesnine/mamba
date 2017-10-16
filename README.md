# Mamba
------------
[![Build Status](https://travis-ci.org/thewhowhatwhere/flask-blog.svg?branch=master)](https://travis-ci.org/thewhowhatwhere/flask-blog)
[![codecov](https://codecov.io/gh/thewhowhatwhere/flask-blog/branch/master/graph/badge.svg)](https://codecov.io/gh/thewhowhatwhere/flask-blog)

Mamba is a blogging platform built on the Flask framework. It is theme-able, customizable, and easy to understand. It is intended to be as user friendly as Wordpress. (we're not quite there yet)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
```
 1. Python 3.x
 2. virtualenv
 3. sqlite3
 4. git 
```

### Installing

```
git clone <repo>
cd mamba
virtualenv -p '/path/to/python3.x' env
source env/bin/activate
pip install -r requirements.txt
Edit config.py (replace 'secret')
Edit init_db.py (email / password)
python init_db.py
python wsgi.py
open browser and go to localhost:5000
```

## Running the tests

you can run tests with pytest

## Deployment

To deploy code into a live environment, you will want to use gunicorn, nginx and mysql. Googling around will get you information on how to make this happen, a more in depth write up / how to section will replace this one in time.

## Built With [Flask](http://flask.pocoo.org/)

## Contributing

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and [CONTRIBUTING.md](CONTRIBUTING.md) for submitting issues and the process for submitting pull requests to us.

## Authors

* **Dustin Farley** - *Initial work* - [TheWhoWhatWhere](https://github.com/thewhowhatwhere)

See also the list of [contributors](https://github.com/thewhowhatwhere/mamba/contributors) who participated in this project.

## License
This project is licensed under the GPLv2 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspired by [m1yag1](https://github.com/m1yag1) for sharing his single file Flask blog app and convincing me to finally start this project
