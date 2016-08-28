import unittest

from namespaces import Namespace

class NamespaceTest(unittest.TestCase):

  def test_create_empty(self):
    foo = Namespace()
    self.assertTrue(True)

  def test_create_via_kwargs(self): # anonymous mapping
    foo = Namespace(a=1, b=2)
    self.assertTrue(True)

  def test_create_via_dict(self): # named mapping
    foo = Namespace({'a': 1, 'b': 2, tuple('three'): 3, 4: 4})
    self.assertTrue(True)

# TODO: test creation from another namespace (frozen?)

  def test_item_setget(self):
    foo = Namespace()
    foo['c'] = 3
    self.assertEqual(foo['c'], 3)

  def test_attr_setget(self):
    foo = Namespace()
    foo.c = 3
    self.assertEqual(foo.c, 3)

  def test_len(self):
    foo = Namespace(a=1, b=2)
    self.assertEqual(len(foo), 2)
    foo['c'] = 3
    self.assertEqual(len(foo), 3)
    foo.d = 4
    self.assertEqual(len(foo), 4)

  def test_iter(self):
    foo = Namespace(a=1, b=2)
    foo_dict = {k: v for k,v in foo.iteritems()}
    self.assertEqual(foo_dict, {'a': 1, 'b': 2})

  def test_del(self):
    foo = Namespace(a=1, b=2)
    del foo['a']
    self.assertNotIn('a', foo)

if __name__ == '__main__':
  unittest.main()

