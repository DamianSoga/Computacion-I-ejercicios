import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a,index=['x','y','z'])
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar['day3'])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar.loc[1])
print(myvar.loc[[0,1]])

juegos=pd.read_csv('videogamesales.csv')
#print(juegos.loc[3])
#print(pd.options.display.max_rows)
#print(len(juegos))
dicci=juegos.loc[[len(juegos)-10,len(juegos)-1]].to_dict()
#print(dicci['Name'][16326])

for item in dicci['Rank'].keys():
  print(dicci['Rank'][item])

print(juegos.loc[0:10,['Rank','Year']])

df = juegos[juegos['Platform']!='NES']
print(df)