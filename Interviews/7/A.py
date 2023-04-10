from typing import List

def generate_parens(n: int) -> List[str]:
    def add_parens(left, right, result) -> List[str]:
        results = []
        
        if left < 0 or right < left: 
            return results
        
        if left == 0 and right == 0:
            results.append(result)
            return results

        a = add_parens(left-1, right  , result + '(' )
        b = add_parens(left  , right-1, result + ')' )
        return a + b + results
    
    return add_parens(n, n, "")

if __name__ == "__main__":
    print_test = lambda x: print("{}: {}".format(x, generate_parens(x)))

    print_test(1)
    print_test(2)
    print_test(3)

