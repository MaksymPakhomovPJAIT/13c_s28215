squares = [x**2 for x in range(1, 11)]
print("List of squares of numbers from 1 to 10:", squares)
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares
start = 1
end = 10
squares = generate_squares(start, end)
print("List of squares of numbers from", start, "to", end, ":", squares)

class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end + 1)]
        return squares
square_gen = SquareGenerator()
start = 1
end = 10
squares = square_gen.generate_squares(start, end)
print("List of squares of numbers from", start, "to", end, ":", squares)

