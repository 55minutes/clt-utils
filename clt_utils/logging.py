from . import env
from colors import green, yellow


def log(level, msg):
    if getattr(env, level, True):
        print(msg)


def debug(msg):
    log('DEBUG', msg)


def info(msg):
    log('INFO', msg)


def warning(msg):
    log('INFO', yellow(msg))


def print_header(label):
    info(green(label))
    info(green('=' * len(label)))
