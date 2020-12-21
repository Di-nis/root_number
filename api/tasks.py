from math import sqrt

from .celery import app


@app.task
def root_of_number(input_number):
    return sqrt(input_number)
