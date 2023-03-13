ODDMASK  = 0b10101010101010101010101010101010
EVENMASK = 0b01010101010101010101010101010101

def swap_odd_even_bits(x: int) -> int:
    return ((x&ODDMASK) >> 1) | ((x&EVENMASK) << 1)

if __name__ == "__main__":
    print_test = lambda x: print("{:032b}: {:032b}".format(x, swap_odd_even_bits(x)))

    print_test(int(0b101010))



