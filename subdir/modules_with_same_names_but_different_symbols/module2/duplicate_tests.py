import unittest

from subdir.modules_with_same_names_but_different_symbols.module2 \
    import duplicate


class DifferentClassTests(unittest.TestCase):

    def test_a_function_works(self):
        o = duplicate.DifferentClass()
        self.assertEqual(o.a_function(), True)
