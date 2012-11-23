from ConfigParser import SafeConfigParser
import os


def get_production_version():
    version_config = SafeConfigParser()
    version_config.readfp(open(
        os.path.join(os.path.dirname(__file__), 'VERSION.cfg')))
    return version_config.get('version', 'production')


class _AttributeDict(dict):
    """
    Dictionary subclass enabling attribute lookup/assignment of keys/values.

    For example::

        >>> m = _AttributeDict({'foo': 'bar'})
        >>> m.foo
        'bar'
        >>> m.foo = 'not bar'
        >>> m['foo']
        'not bar'
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # to conform with __getattr__ spec
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value
