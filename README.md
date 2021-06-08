# Mamba
------------
[![Build Status](https://travis-ci.org/nivesnine/mamba.svg?branch=master)](https://travis-ci.org/nivesnine/mamba)
[![codecov](https://codecov.io/gh/nivesnine/mamba/branch/master/graph/badge.svg)](https://codecov.io/gh/nivesnine/mamba)

Mamba is a simple blogging platform built on the Flask framework.

## Known Issues

1) user edit form in admin area does not show a users current roles
2) boolean fields do not properly show checked/unchecked in forms
3) tests need to be rewritten / updated

## TODO

1) create an easier way to edit and manage the site menus
2) fix known issues

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
```
 1. Python 3.9
 2. virtualenv
 3. sqlite3
 4. git 
```

### Installing

```
git clone <repo>
cd mamba
virtualenv -p '/path/to/python3.9' env
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

* **Dustin Farley** - *Initial work* - [nivesnine](https://github.com/nivesnine)

See also the list of [contributors](https://github.com/nivesnine/mamba/contributors) who participated in this project.

## License
This project is licensed under the GPLv2 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspired by [m1yag1](https://github.com/m1yag1) for sharing his single file Flask blog app and convincing me to finally start this project
