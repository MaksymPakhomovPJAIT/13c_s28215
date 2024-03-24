class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass