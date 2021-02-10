import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "not_an_eay_one_that_can_BE_guessed!!"
