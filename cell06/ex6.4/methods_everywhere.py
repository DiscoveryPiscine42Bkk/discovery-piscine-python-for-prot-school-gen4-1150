import sys

def shrink(input_string):
    
    print(input_string[:8])

def enlarge(input_string):
    
    while len(input_string) < 8:
        input_string += 'Z'
    print(input_string)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            else:
                enlarge(arg)