from __future__ import absolute_import

from datetime import datetime
import argparse as _argparse
import os


def is_dir(string):
    """
    Type check for a valid directory for ArgumentParser.
    """
    if not os.path.isdir(string):
        msg = '{0} is not a directory'.format(string)
        raise _argparse.ArgumentTypeError(msg)
    return string


def is_file(string):
    """
    Type check for a valid file for ArgumentParser.
    """
    if not os.path.isfile(string):
        msg = u'{0} is not a file'.format(string)
        raise _argparse.ArgumentTypeError(msg)
    return string


def gt_zero(string):
    """
    Type check for int > 0 for ArgumentParser.
    """
    if not int(string) > 0:
        msg = u'limit must be > 0'
        raise _argparse.ArgumentTypeError(msg)
    return int(string)


def isodate(string):
    try:
        return datetime.strptime(string, '%Y-%m-%d').date()
    except ValueError:
        msg = u'date input must in the format of yyyy-mm-dd'
        raise _argparse.ArgumentTypeError(msg)
