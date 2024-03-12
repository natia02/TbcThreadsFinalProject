# Geometric Shapes Concurrency Performance Analysis

This project explores the performance of geometric shape calculations under different concurrency paradigms. Three geometric shapes are considered: Trapezoids, Rectangles, and Squares. The performance is measured by calculating the areas of a large number of randomly generated shapes and comparing the execution times under sequential, multi-threaded, multi-processed, and hybrid (multi-processes + multi-threads) scenarios.

## Table of Contents


- [Usage](#usage)
- [Classes](#classes)
- [Concurrency](#concurrency)
- [Performance Testing](#performance-testing)
- [Contributing](#contributing)
- [License](#license)



## Usage

To run the performance tests:

```bash
python main.py
```

## Classes

### Trapezoid

Represents a trapezoid shape with bases and height. Inherits from `object`.

- Attributes:
  - `base1`: Length of the first base of the trapezoid.
  - `base2`: Length of the second base of the trapezoid.
  - `height`: Height of the trapezoid.

- Methods:
  - `__init__(parameters=None)`: Constructor method.
  - `__str__()`: String representation of the trapezoid.
  - `area()`: Calculate the area of the trapezoid.
  - Comparison methods: `__eq__`, `__le__`, `__lt__`, `__ge__`.
  - Arithmetic methods: `__add__`, `__sub__`, `__mod__`.

### Rectangle

Represents a rectangle shape. Inherits from `Trapezoid`.

- Attributes:
  - `base1`: Width of the rectangle.
  - `height`: Height of the rectangle.

- Methods:
  - `__init__(parameters=None)`: Constructor method.
  - `__str__()`: String representation of the rectangle.
  - `area()`: Calculate the area of the rectangle.

### Square

Represents a square shape. Inherits from `Rectangle`.

- Attributes:
  - `base1`: Side length of the square.

- Methods:
  - `__init__(parameters=None)`: Constructor method.
  - `__str__()`: String representation of the square.
  - `area()`: Calculate the area of the square.

## Concurrency

The performance of shape calculations is tested under the following concurrency paradigms:

- Sequential Execution
- Multi-threading
- Multi-processing
- Hybrid (Multi-processes + Multi-threads)

## Performance Testing

Performance testing is conducted by measuring the execution times for each concurrency scenario using a large number of randomly generated shapes.

