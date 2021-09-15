import pandas as pd
import traceback
import numpy as np

rango = []
resultado = []

def traslape():
    for i in range(1,len(rango)):
        if rango[i-1]["min"] <= rango[i]["min"] <= rango[i-1]["max"]:
            continue
        else:
            print(f'No hay traslape entre: {rango[i-1]["descripcion"]} y {rango[i]["descripcion"]}')
            return True
    return False

def validarMinMax(minimo, maximo):
    return False if minimo > maximo else True

def pertenencia(linea, valor):
    indice = linea.index(max(linea))
    if valor > rango[len(rango)-1]["max"]:
        return rango[len(rango)-1]["descripcion"]
    return rango[indice]["descripcion"]

def rangos():
    while(True):     
        n = int(input('Cuantos rangos serían: '))
        if 2 <= n <= 4:
            break
    i = 0
    while(i < n):
        descripcion = input(f'Introduce la descripción del rango {i+1}: ')
        while(True):
            valorMin = int(input(f'Introduce el valor minimo del rango {i+1}: '))
            valorMax = int(input(f'Introduce el valor maximo del rango {i+1}: '))
            if validarMinMax(valorMin, valorMax):
                break
        item = {
            "descripcion": descripcion,
            "min": valorMin,
            "max": valorMax
        }
        rango.append(item)
        if len(rango) > 1:
            if traslape():
                rango.pop()
                print('Vuelve a introducir el ultimo rango')
        i += 1

def triangulo(x, a, b, c):
    # print(f'{a}, {b}, {c}')
    if x <= a:
        return 0
    elif a <= x <= b:
        return ((x-a)/(b-a))
    elif b <= x <= c:
        return ((c-x)/(c-b))
    else:
        return 0
            

def proceso(valores):
    linea = []
    for valor in valores:
        for i in range(len(rango)):
            r1 = float(triangulo(valor, rango[i]["min"],  (rango[i]["min"]+rango[i]["max"])/2 , rango[i]["max"]))
            linea.append(r1)
        linea.append(max(linea))
        linea.append(pertenencia(linea, valor))
        resultado.append(linea)
        linea = []

def salida(valores):
    r = np.transpose(np.array(resultado))
    titulos = ['Valores']
    datos = {'Valores': valores}
    for i in range(len(rango)):
        datos['GV ' + rango[i]["descripcion"]] = r[i]
        titulos.append('GV ' + rango[i]["descripcion"])
    datos["GV MAX"] = r[len(r)-2]
    titulos.append("GV MAX")
    datos["Pertenencia"] = r[len(r)-1]
    titulos.append("Pertenencia")
    sd = pd.DataFrame(datos, columns= titulos)
    sd.to_excel('./salida.xlsx', sheet_name='Resultados')

def main():
    df = pd.read_excel('./entrada.xlsx', sheet_name='LogicaDifusa')
    tamanio = len(df["Valores"])
    valores = [float(df["Valores"][valor]) for valor in range(tamanio)]
    rangos()
    proceso(valores)
    salida(valores)
    



if __name__ == '__main__':
    try:
         main()
    except:
        traceback.print_exc()
   
    