class FooBar:
    def __init__(self, n):
        self.n = n
        self.isFoo = True 
        self.condition = threading.Condition()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                with self.condition:
                    while not self.isFoo:
                        self.condition.wait()
                    
                    printFoo()
                    self.isFoo = False
                    self.condition.notify_all()
                    break
                        


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                with self.condition:
                    while self.isFoo:
                        self.condition.wait()

                    printBar() 
                    self.isFoo = True
                    self.condition.notify_all()
                    break
                