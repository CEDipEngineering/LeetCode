from typing import List, Dict, Set, Tuple

def print_indices_and_elements(elements) -> None:
    [print(i, e) for i,e in enumerate(elements)]


def get_even_numbers_between(start: int, end: int) -> List[int]:
    return [i for i in range(start, end+1) if i % 2 == 0]


def get_char_set_from(s: str) -> Set[str]:
    return {c for c in s}


def get_perfect_squares_between(start: int, end: int) -> Dict[int,int]:
    return {k**2: k for k in range(int(start**0.5+1), int(end**0.5+1))}


def filter_even_from(numbers: List[int]) -> List[int]:
    return [i for i in numbers if i % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: List[int]) -> List[int]:
    return [i if i % 2 == 0 else -1 for i in numbers if i % 5 == 0]


def str_lengths(strings: List[str]) -> List[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return 'Generators are much more memory friendly. They evaluate results in a lazy fashion, and only compute the necessary steps to achieve an answer, when that answer is needed. The list approach needs to store the entire history, which can be more costly. Neither implementation in this case is optimal for large numbers, since they both always compute from scratch. Caching would help alleviate the O(n) time complexity for the operation, while also being generator friendly albeit still using O(n) memory. The generator is also used differently, as it can be used in a loop without pre-computing all possible solutions, unlike the list implementation.'


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.size == 0:
            raise StopIteration
        try:
            out = self.elements[self.index]
        except IndexError:
            raise StopIteration
        self.index += 2
        return out

def my_avg(e1: float, e2: float, *others: Tuple[float]) -> float:
    return (sum(others) + e1 + e2) / (len(others) + 2)


def keys_with_different_value() -> List[int]:
    return list(range(5,10))


def print_out_in(*numbers) -> None:
    
    while len(numbers) > 1:
        a, *numbers, c = numbers
        print(a, c)
    if numbers:
        print(numbers[0])


def append_range(start: int, end: int, step: int=1, to: List[int]=None):
    # You may add code here
    if to is None:
        to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
