mespace` is a flexible, mutable version of `collections.namedtuple`.

The API of `Namespace` is as follows:
```python
ns = Namespace(a=1, b=2)
fns = FrozenNamespace(ns)
fns.b # => 2
ns.c # => AttributeError
ns.c = 3
ns.c # => 3
fns.c = 3 # => AttributeError
```

`__getitem__` and `__setitem__` are disabled to avoid accidental access to potentially API-breaking behavior.

`FrozenNamespace` guards against mutations via `__setattr__` but can be mutated if you try hard enough...
> Your colleague may be missing the point of a "consenting adults language" where nothing in pure python code is truly private (in the sense of being enforced).
> - Raymond Hettinger
(http://stackoverflow.com/questions/9997176/immutable-dictionary-only-use-as-a-key-for-another-dictionary)
