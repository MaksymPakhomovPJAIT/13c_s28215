
from square_generator.square_generator import SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start for square generation.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
