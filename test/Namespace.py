import unittest

from namespaces import FrozenNamespace, Namespace

class NamespaceTest(unittest.TestCase):

  def test_create_empty(self):
    ns = Namespace()
    self.assertIsInstance(ns, Namespace)
    self.assertEqual(len(ns), 0)

  def test_create_via_kwargs(self): # anonymous mapping
    ns = Namespace(a=1, b=2)
    self.assertIsInstance(ns, Namespace)
    self.assertEqual(ns.items(), {'a': 1, 'b': 2}.items())

  def test_create_via_dict(self): # named mapping
    d = {'a': 1, 'b': 2, tuple('three'): 3, 4: 4}
    ns = Namespace(d)
    self.assertIsInstance(ns, Namespace)
    self.assertEqual(ns.items(), d.items())

  def test_create_via_frozennamespace(self):
    fn = FrozenNamespace(a=1, b=2)
    ns = Namespace(fn)
    self.assertIsInstance(ns, Namespace)
    self.assertEqual(ns.items(), fn.items())

  def test_item_setget(self):
    ns = Namespace()
    ns['c'] = 3
    self.assertEqual(ns['c'], 3)

  def test_attr_setget(self):
    ns = Namespace()
    ns.c = 3
    self.assertEqual(ns.c, 3)

  def test_len(self):
    ns = Namespace(a=1, b=2)
    self.assertEqual(len(ns), 2)
    ns['c'] = 3
    self.assertEqual(len(ns), 3)
    ns.d = 4
    self.assertEqual(len(ns), 4)

  def test_iter(self):
    ns = Namespace(a=1, b=2)
    d = {k: v for k,v in ns.iteritems()}
    self.assertEqual(d, {'a': 1, 'b': 2})

  def test_del(self):
    ns = Namespace(a=1, b=2)
    self.assertEqual(len(ns), 2)
    del ns['a']
    self.assertNotIn('a', ns)
    self.assertEqual(len(ns), 1)

if __name__ == '__main__':
  unittest.main()

