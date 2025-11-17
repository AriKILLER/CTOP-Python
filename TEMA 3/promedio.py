def promedio(numeros):
    total = 0
    for n in numeros:
        total += n
 # ERROR: usamos len(numeros)-1 en lugar de len(numeros)
    return total / (len(numeros))

def main():
    nums = [2, 4, 6]
    print('Lista:', nums)
    print('Promedio:', promedio(nums))

if __name__ == '__main__':
    main()