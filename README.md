# FLASK SKELETON
Microservice Skeleton with Flask Framework and SQLAlchemy Djangorized

## Getting started

Install [docker](https://docs.docker.com/engine/installation/) and run:

```shell
docker-compose up
# docker-compose stop
```

Otherwise, for the standalone web service:

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## Development

Create a new branch off the **develop** branch for features or fixes.

After making changes rebuild images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
# docker stop flaskapp_redis_1
```

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```

Integration and unit tests run with:

```shell
docker-compose -f test.yml -p ci build
docker-compose -f test.yml -p ci run test python -m pytest --cov=web/ tests
# docker stop ci_redis_1 ci_web_1
```

Commits tested via [travis-ci.org](https://travis-ci.org/brennv/flask-app). Test coverage reported to [codecov.io](https://codecov.io/gh/brennv/flask-app). Code quality reported via [codeclimate.com](https://codeclimate.com/github/brennv/flask-app). Requirements inspected with [requires.io](https://requires.io/github/brennv/flask-app/requirements).

After testing, submit a pull request to merge changes with **develop**.
