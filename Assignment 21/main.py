class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current