fruta=['manzana','pera','gauyaba','mango']
precio=[30,10,40,50]

val=dict(zip(fruta,precio))
x=input('dime un fruta  ')
print(val.get(x,'no se encuentra'))
