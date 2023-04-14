# Description

CloudPlatform testing project.
  
# Launch

```bash
To launch virtual environment:
python3 -m venv venv  #2nd venv - env_name
. venv/bin/activate

Installing essential libraries:
pip install -r requirements.txt

You should enter login/password into the file ./conftest.py before tests launching

Tests launching:
pytest ./tests

Multithreaded tests launching:
pytest -n N ./tests
N - desired number of threads
```
# Launching UI-autotests
- Launch docker-selenium: 
`docker run -d -e SCREEN_WIDTH=1920 -e SCREEN_HEIGHT=1080 -p 4444:4444 -p 7900:7900 -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-4-prerelease-20210517`
  (updated version - https://github.com/SeleniumHQ/docker-selenium)

- Launch tests from IDE or by command `pytest -v tests/ui_test`

- Open `localhost:7900` in a browser (password - `secret`)
