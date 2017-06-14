import unittest
import foo


class FooTests(unittest.TestCase):

    def testTrue(self):
        f = foo.Foo()
        self.failUnlessEqual(f.foo(True), True)

    def testFalse(self):
        f = foo.Foo()
        self.failUnlessEqual(f.foo(False), False)


class SlowTests(unittest.TestCase):

    def testSlow(self):
        foo.Foo().slow(0.11)
