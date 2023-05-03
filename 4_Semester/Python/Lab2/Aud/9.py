def gen_init(cls):
    """Decorate a class with a new constructor method that calls the original constructor."""

    def init(self):
        print('Entered', cls.__name__, "constructor")
        super(cls, self).__init__()
        print('Quit', cls.__name__, "constructor")

    cls.__init__ = init
    return cls


@gen_init
class A:
    pass


@gen_init
class B:
    pass


@gen_init
class C(A, B):
    pass


@gen_init
class D(C, B):
    pass


@gen_init
class E(D):
    pass


print(E.__mro__)
obj = E()