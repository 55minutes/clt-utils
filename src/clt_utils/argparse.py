from . import get_production_version
import argparse
import os

VERSION = get_production_version()


def is_dir(string):
    """
    Type check for a valid directory for ArgumentParser.
    """
    if not os.path.isdir(string):
        msg = '{} is not a directory'.format(string)
        raise argparse.ArgumentTypeError(msg)
    return string


def is_file(string):
    """
    Type check for a valid file for ArgumentParser.
    """
    if not os.path.isfile(string):
        msg = '{} is not a file'.format(string)
        raise argparse.ArgumentTypeError(msg)
    return string


def gt_zero(string):
    """
    Type check for int > 0 for ArgumentParser.
    """
    if not int(string) > 0:
        msg = 'limit must be > 0'
        raise argparse.ArgumentTypeError(msg)
    return int(string)
