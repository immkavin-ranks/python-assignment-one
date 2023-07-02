# 11. Write a python script to implement Complex Number Operations


class ComplexNumber:

  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

  def __str__(self):
    return f"{self.real} + {self.imaginary}i"

  def __add__(self, other):
    real_sum = self.real + other.real
    imaginary_sum = self.imaginary + other.imaginary
    return ComplexNumber(real_sum, imaginary_sum)

  def __sub__(self, other):
    real_diff = self.real - other.real
    imaginary_diff = self.imaginary - other.imaginary
    return ComplexNumber(real_diff, imaginary_diff)

  def __mul__(self, other):
    real_product = (self.real * other.real) - (self.imaginary *
                                               other.imaginary)
    imaginary_product = (self.real * other.imaginary) + (self.imaginary *
                                                         other.real)
    return ComplexNumber(real_product, imaginary_product)

  def conjugate(self):
    return ComplexNumber(self.real, -self.imaginary)


# Create complex numbers
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)

# Perform complex number operations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
conjugate_result = num1.conjugate()

# Print the results
print("Complex Number Operations:")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Conjugate of Number 1: {conjugate_result}")
