abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i, letra in enumerate(abecedario):
    if (i + 1) % 3 == 0:
        abecedario.remove(letra)
print(abecedario)