class Foo:

    def foo(self, a):
        if a:
            return True
        else:
            import time
            time.sleep(12)
            return False
