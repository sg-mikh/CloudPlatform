# Описание

Проект тестирования Облачной Платформы.
  
# Запуск

```bash
Для запуска виртуального окружения:
python3 -m venv venv  #вторая venv - env_name
. venv/bin/activate

Установка необходимых библиотек:
pip install -r requirements.txt

Перед запуском тестов в файле ./conftest.py необходимо ввести логин/пароль

Запуск тестов:
pytest ./tests

Многопоточный запуск тестов:
pytest -n N ./tests
N - желаемое количество потоков
```
# Запуск UI-автотестов
- Запустить docker-selenium: 
`docker run -d -e SCREEN_WIDTH=1920 -e SCREEN_HEIGHT=1080 -p 4444:4444 -p 7900:7900 -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-4-prerelease-20210517`
  (последняя версия образа - https://github.com/SeleniumHQ/docker-selenium)

- Запустить тесты из IDE или командой `pytest -v tests/ui_test`

- Открыть в браузере `localhost:7900` (пароль - `secret`)