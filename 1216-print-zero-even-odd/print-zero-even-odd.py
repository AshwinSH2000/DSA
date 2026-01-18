'''
    phew, the description was quite confusing especially when you enter a 
    double digit number. ok from what i understood, you print a 0 and the number.
    then you repeat until 2n numbers are printed (not 2n digits, thats the catch!)
'''
import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.condition = threading.Condition()
        self.zero_printed = False
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and self.zero_printed:
                    self.condition.wait()
                
                if self.i>self.n:
                    break
                printNumber(0)
                self.zero_printed = True
                self.condition.notify_all()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i%2 != 0 or self.zero_printed == False):
                    self.condition.wait()
                
                if self.i>self.n:
                    break
                printNumber(self.i)
                self.zero_printed = False
                self.i += 1
                self.condition.notify_all()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                while self.i <= self.n and (self.i%2 == 0 or self.zero_printed == False):
                    self.condition.wait()

                if self.i > self.n:
                    break
                printNumber(self.i)
                self.zero_printed = False
                self.i += 1
                self.condition.notify_all()
        