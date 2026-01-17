class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1 #this will be the loop variable
        self.condition = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self , printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                # when should it wait? when the numb is <= n and
                # when i is not (multiple of 3 but not a mult of 5)
                while self.i <= self.n and not (self.i%3==0 and self.i%5!=0):
                    self.condition.wait()
                
                if self.i>self.n: break
                printFizz()
                self.i += 1
                self.condition.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition: #dont wait when it is only a mult of 5
                while self.i <= self.n and not (self.i%3 !=0 and self.i%5==0):
                    self.condition.wait()
                
                if self.i > self.n: 
                    break

                printBuzz()
                self.i += 1
                self.condition.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and not (self.i%3==0 and self.i%5==0):
                    self.condition.wait()
                
                if self.i>self.n: break

                printFizzBuzz()
                self.i+=1
                self.condition.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and not (self.i%3!=0 and self.i%5!=0):
                    self.condition.wait()
                
                if self.i > self.n:
                    break
                
                printNumber(self.i)
                self.i+=1
                self.condition.notify_all()