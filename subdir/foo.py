class Foo:

    def foo(self, a):
        if a:
            return True
        else:
            import time
            time.sleep(0)
            return False
            pass # pragma: no cover
