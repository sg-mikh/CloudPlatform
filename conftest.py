# -*- coding: utf-8 -*-
import time
import pytest


@pytest.fixture(autouse=True)
def duration():
    start = time.time()
    yield
    end = time.time()
    print(f'\nВремя выполнения: {end - start} секунд.')
