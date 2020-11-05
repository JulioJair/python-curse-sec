# DuckTyping
class Duck:
    def talk(self):
        print("Quak Quak")


class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):
    obj.talk()


if __name__ == "__main__":
    d = Duck()
    callTalk(d)
    h = Human()
    callTalk(h)


# Ducktyping for Dependancy Injection
class Flight():
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")


class BoeingEngine:
    def start(self):
        print("Starting Boeing engine")


if __name__ == "__main__":
    ae = AirbusEngine()
    f1 = Flight(ae)
    f1.start_engine()

    be = BoeingEngine()
    f2 = Flight(be)
    f2.start_engine()

# Operator Overloading
x = 10
y = 20
print(x + y)

s1 = "Hello"
s2 = " How are you"
print(s1 + s2)

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L1)
