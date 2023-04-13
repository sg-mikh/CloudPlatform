FROM python:3.6
COPY . /cp-api-tests
WORKDIR /cp-api-tests

RUN pip install --no-cache-dir -r requirements.txt
#123
RUN ["pytest", "-v", "--alluredir=allure-results"]

CMD tail -f /dev/null