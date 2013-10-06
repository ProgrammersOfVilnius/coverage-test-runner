import unittest

from subdir.modules_with_same_names_but_different_symbols.module1 \
    import duplicate


class DuplicateClassTests(unittest.TestCase):

    def test_a_function_works(self):
        o = duplicate.DuplicateClass()
        self.assertEqual(o.a_function(), True)
