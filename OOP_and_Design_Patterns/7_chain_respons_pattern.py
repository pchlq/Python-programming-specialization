class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, val):
        self.val = val


class EventSet:
    def __init__(self, val):
        self.val = val


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.__class__.__name__ is 'EventGet':
            if event.val is int:
                return obj.integer_field
        elif event.__class__.__name__ is 'EventSet':
            if isinstance(event.val, int):
                obj.integer_field = event.val
                return
                
        return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.__class__.__name__ is 'EventGet':
            if event.val is float:
                return obj.float_field
        elif event.__class__.__name__ is 'EventSet':
            if isinstance(event.val, float):
                obj.float_field = event.val
                return

        return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.__class__.__name__ is 'EventGet':
            if event.val is str:
                return obj.string_field
        elif event.__class__.__name__ is 'EventSet':
            if isinstance(event.val, str):
                obj.string_field = event.val
                return

        return super().handle(obj, event)



if __name__ == '__main__':
    obj = SomeObject()
    obj.integer_field = 42
    print(obj.integer_field)
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    chain.handle(obj, EventSet(5.8))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet('test'))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))