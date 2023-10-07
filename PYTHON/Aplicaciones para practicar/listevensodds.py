lista = [1,2,3,4,5,6,7,8,9,10]

def split_even_and_odds(nums):
    listodds = []
    listevens = []
    for n in nums:
        if n % 2 == 0:
            listevens.append(n)
        else:
            listodds.append(n)
    return f'La lista de números pares es: {listevens} y la de impares es: {listodds}'

print(split_even_and_odds(lista))
