from flask import Flask

app = Flask(__name__)  # variável principal

@app.route("/")  # define a rota para a raiz
def index():  # página principal nome index (padrão de fato)
    return "Olá CDF!"

if __name__ == "__main__":
    app.run()

#import pandas as pd
# import re
#df = pd.DataFrame({'$jossknsa':[1,2], '$khsDBb': [10,20]})
#df.columns = ['a', 'b']
#print(df)

#product = lambda x, y : x * y
#print(product(2, 3))

'''def x (a, b):
    return a * b
var = x(2, 3)
print(var)'''

'''var = lambda a, b : a * b
print (var(2,3))'''

'''stringDataFrame = pd.DataFrame({'A':['gdgdg454dgd','147ooo2', '123ss45678'],
                                'B':['gdgdg454dgd','x142', '12345678a'],
                                'C':['gdgdg454dgd','xx142', '12567dd8']})
print (stringDataFrame)
stringDataFrame = stringDataFrame.applymap(lambda x: re.sub(r'[^0-9]', '', x) if (len(x) >= 7) else x)
print (stringDataFrame)'''

'''text1 = 'caixa 1 é azul, caixa 10 está verde, caixa 100 está vazia'
text1 = text1.replace('caixa 1', 'pacote 2')
print(text1)
text2 = 'caixa 1 é azul, caixa 10 está verde, caixa 100 está vazia'
text2 = re.sub(r'caixa 1\b', 'pacote 2', text2)
print(text2)
text3 = 'TÃ tulo e Val. Mob.'
text3 = text3.replace('Ã ', 'i')
print(text3)
text4 = 'TÃ tulo e Val. Mob.'
text4 = re.sub(r'Ã ', 'i', text4)
print(text4)'''