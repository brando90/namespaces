from __future__ import unicode_literals
import collections
import keyword
from namespaces import isidentifier

class Namespace(collections.MutableMapping):
  '''A dictionary accessible via dot notation.
  Inspired by Javascript Objects.
  '''

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)

  def __getitem__(self, key):
    return self._dict[key]

  def __setitem__(self, key, value):
    self._dict[key] = value

  def __delitem(self, key):
    del self._dict[key]

  def __len__(self):
    return len(self._dict)

  def __iter__(self):
    return iter(self._dict)

  def __getattr__(self, name):
    return self._dict[name]

  def __setattr__(self, name, value):
    self._dict[name] = value

  def __repr__(self):
    '''Representation is a valid python expression for creating a Namespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    kwargs_strs = ['{}={}'.format(k,repr(v)) for k,v in self.iteritems()]
    return '{}({})'.format(type(self).__name__, ', '.join(kwargs_strs))

  def immutable(self):
    from namespaces import FrozenNamespace
    return FrozenNamespace(self)
