  # Square Pattern Logic

def print_square(n):
  for i in range(n):      # row of the square
      for j in range(n):  # column of the square
          if i == 0 or i == n - 1 or j == 0 or j == n - 1:
              print("*", end=" ")
          else:
              print(" ", end=" ")
      print()

# Rectangle Pattern logic: 

""""
def print_rectangle(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

size = 10  # This variable represents both rows and columns
print_rectangle(size)
"""


# Testing multiple cases
test_cases = [5, 8, 10, 20, 15, 4, 13, 30]  # Add any other sizes you want to test

for size in test_cases:
  print(f"Square of size {size}:")
  print_square(size)
  print()
