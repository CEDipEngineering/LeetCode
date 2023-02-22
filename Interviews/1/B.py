def one_edit_away(first: str, second: str) -> bool:
    
    # Three cases:
    
    # 1. 1 swap away, len stays the same
    def is_one_swap_away(a, b):
        """
        Loop through both together, if one difference, continue, if another difference, return false
        """
        diff = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if diff:
                    return False
                else:
                    diff = True
        return diff # Note, if diff is still false, both strings are identical, and are therefore not one edit away.
    
    # 2. 1 add away, len increases
    # 3. 1 drop away, lec decreases
    def is_one_insertion_away(big, small):
        """
        Loop through both together, on difference, advance big index by one, and continue. If end without mismatch, true, else false.
        """
        # Create separate indices
        big_i = 0
        small_i = 0
        while big_i<(len(big)-1):
            # Difference found
            if big[big_i] != small[small_i]:
                # First difference
                if big_i == small_i:
                    big_i += 1
                # Second difference
                else:
                    return False
            big_i += 1
            small_i += 1
        return True # Check if both indices are at the end of their strings
    
    # Can change len by 1 at most:
    if abs(len(first) - len(second)) > 1: return False

    # First case
    if len(first) == len(second): return is_one_swap_away(first, second)

    # Second case (same for add and remove, just backwards)
    
    # Sort them into big and small, and assume the original is the smaller, and the bigger is one addition away
    big = first if len(first)>len(second) else second
    small = first if len(first)<len(second) else second
    return is_one_insertion_away(big, small)

if __name__ == "__main__":
    print_test = lambda x,y: print(f"{x} vs. {y}: {one_edit_away(x,y)}")
    print_test("ABCD", "ABDD")
    print_test("ACD", "ABCD")
    print_test("ABCDE", "ABCD")
    print_test("Yogurt", "Yoghurti")
    
    
