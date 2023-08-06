# Simple calculator3220

> calculator is a python method for simple math actions. Starting memory value = 0

## Installation

```sh
pip install calculator3220
```

## Usage

Make a simple math actions like addition, substraction, divide, multiply, root:

```python
>>> import calculator3220
>>> calculator = calculator3220.Calculator()
```
-   Adding number to memory value(memory value is 0):

```python
>>> calculator.add(5)
5.0
>>> calculator.add(3)
2.0
```

-   Substract number from memory value(memory value is 0):

```python
>>> calculator.sub(5)
-5.0
>>> calculator.sub(-9)
4.0
```

-   Dividing memory value by number(memory value is 80):

```python
>>> calculator.div(5)
16
>>> calculator.div(4)
4
```

-   Multiply memory value by number(memory value is 5):

```python
>>> calculator.mul(10)
50
>>> calculator.mul(2)
100
```

-   Root by number of memory value(memory value is 27):

```python
>>> calculator.root(3)
3
```

-   Reset memory value(memory value is 27):

```python
>>> calculator.reset()
0
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

