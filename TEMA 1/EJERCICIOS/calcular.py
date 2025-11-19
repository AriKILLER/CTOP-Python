import sys

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

if __name__ == "__main__":
    print('No me ejecutes, !solo soy un modulo!')
    print(__name__)
    sys.exit(1)
else: 
    print(__name__)