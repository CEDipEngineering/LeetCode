from typing import List

LUT = None


def get_valid_t9_words(number: str, words: List[str]) -> List[str]:
    global LUT
    if LUT is None:
        LUT = dict()
        # First call, build Lookup-table
        revT9 = {
            'a': '2',
            'b': '2',
            'c': '2',
            'd': '3',
            'e': '3',
            'f': '3',
            'g': '4',
            'h': '4',
            'i': '4',
            'j': '5',
            'k': '5',
            'l': '5',
            'm': '6',
            'n': '6',
            'o': '6',
            'p': '7',
            'q': '7',
            'r': '7',
            's': '7',
            't': '8',
            'u': '8',
            'v': '8',
            'w': '9',
            'x': '9',
            'y': '9',
            'z': '9'
        }
        for w in words:
            # Calculate number that could lead to this string
            n = ""
            for c in w.lower():
                if c not in "abcdefghijklmnopqrstuvwxyz": continue # only ascii_lowercase
                n += revT9[c]
            # Store in LUT
            LUT.setdefault(n, []).append(w)
            # print(LUT)
    return LUT.get(number, [])


if __name__ == "__main__":

    vocab = [
        'cab',
        'bat',
        'back',
        'lob',
        'jock',
        'rock',
        'lumbar',
        'button',
        'cliff',
        'epic',
        'doctor',
        'amusing',
        'egg',
        'end',
        'spine',
        'soup',
        'tree',
        'used',
        'limp'
    ]


    # Use linux wordlist for testing
    # with open("/usr/share/dict/american-english", 'r') as f:
    #     vocab = f.read().split("\n")

    print_test = lambda num: print("{} : {}".format(num, get_valid_t9_words(num, vocab)))

    print_test("8733")
    print_test("222")