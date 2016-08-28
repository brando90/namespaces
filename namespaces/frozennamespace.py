from __future__ import unicode_literals
from namespaces import Namespace

class FrozenNamespace(FrozenDict):
  '''Immutable, hashable Namespace.'''

  __hash_key = '__hash'

  def __init__(self, *args, **kwargs):
    self.__dict__[FrozenNamespace.__hash_key] = None
    super(self.__class__, self).__init__(*args, **kwargs)

  def __getattr__(self, name):
    '''Behaves similarly to collections.namedtuple#__getattr__.'''
    try:
      return self[name]
    except KeyError:
      raise AttributeError(
        "'{}' object has no attribute '{}'".format(type(self).__name__, name)
      )

  def __repr__(self):
    '''Representation is a valid python expression for creating a FrozenNamespace
    (assuming contents also implement __repr__ as valid python expressions).'''
    items = ('{}={}'.format(k,repr(v)) for k,v in self.iteritems())
    return '{}({})'.format(type(self).__name__, ', '.join(items))

  def __eq__(self, other):
    return isinstance(other, type(self)) and super(Namespace).__eq__(self, other)

  def __ne__(self, other):
    return not self == other

  def __hash__(self):
    '''Caches lazily-evaluated hash for performance.'''
    if self.__dict__[FrozenNamespace.__hash_key] is None:
      self.__dict__[FrozenNamespace.__hash_key] = hash(frozenset(self.items()))
    return self.__dict__[FrozenNamespace.__hash_key]

  def mutable(self):
    return Namespace(self)
