import unittest

import namespaces as ns

# make them from anonymous/named mappings
# mutable
# accessible via bracket/dot notation
  # get and set
# check for membership
# iterate over keys, values, and items
# deletion

class NamespaceTest(unittest.TestCase):

  def test_create_empty(self):
    foo = ns.Namespace()
    self.assertTrue(True)

  def test_create_via_kwargs(self): # anonymous mapping
    foo = ns.Namespace(a=1, b=2)
    self.assertTrue(True)

  def test_create_via_dict(self): # named mapping
    foo = ns.Namespace({'a': 1, 'b': 2, tuple('three'): 3, 4: 4})
    self.assertTrue(True)

# TODO: test creation from another namespace (frozen?)

  def test_item_setget(self):
    foo = ns.Namespace()
    foo['c'] = 3
    self.assertEqual(foo['c'], 3)

  def test_attr_setget(self):
    foo = ns.Namespace()
    foo.c = 3
    self.assertEqual(foo.c, 3)

  def test_len(self):
    foo = ns.Namespace(a=1, b=2)
    self.assertEqual(len(foo), 2)
    foo['c'] = 3
    self.assertEqual(len(foo), 3)
    foo.d = 4
    self.assertEqual(len(foo), 4)

  def test_iter(self):
    foo = ns.Namespace(a=1, b=2)
    foo_dict = {k: v for k,v in foo.iteritems()}
    self.assertEqual(foo_dict, {'a': 1, 'b': 2})

  def test_del(self):
    foo = ns.Namespace(a=1, b=2)
    del foo['a']
    self.assertNotIn('a', foo)
    # del foo.b
    # self.assertNotIn('b', foo)

# FROZENNAMESPACES
# test creation via a=1, b=2
# test creation from another namespace (frozen?)
# test creation from dict

# test can get via bracket notation
# test can get via dot-notation
# test cannot set (via either bracket- or dot-notation)

if __name__ == '__main__':
  unittest.main()
