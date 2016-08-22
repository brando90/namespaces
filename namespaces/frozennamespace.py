from __future__ import unicode_literals
import collections

class FrozenNamespace(collections.Mapping):
  '''Immutable, hashable Namespace.'''

  def __init__(self, *args, **kwargs):
    self._dict = dict(*args, **kwargs)
    self._hash = None

  def __getitem__(self, key):
    return self._dict[key]

  def __len__(self):
    return len(self._dict)

  def __iter__(self):
    return iter(self._dict)

  def __getattr__(self, name):
    return self._dict[name]

  def __repr__(self):
    '''Representation is a valid python expression for creating a FrozenNamespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    kwargs_strs = ['{}={}'.format(k,repr(v)) for k,v in self.iteritems()]
    return '{}({})'.format(type(self).__name__, ', '.join(kwargs_strs))

  def __hash__(self):
    '''Caches lazily-evaluated hash for performance.'''
    if self._hash is None:
      self._hash = hash(frozenset(self.items()))
    return self._hash

  def mutable(self):
    return Namespace(self)
