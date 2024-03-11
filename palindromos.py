plm = 'anitalavalatina'
inv = ''
for i in range(len(plm)-1,-1,-1):
    inv = inv+plm[i]
if plm == inv:
    print('Es un palindromo')
else:
    print('No es un palindromo')