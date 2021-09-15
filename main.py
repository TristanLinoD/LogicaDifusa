import pandas as pd
import traceback

rango = []

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

def membresiaTriangulo(x, a, b, c):
    pass

def main():
    df = pd.read_excel('./entrada.xlsx')
    rangos()
    print(rango)



if __name__ == '__main__':
    try:
         main()
    except:
        traceback.print_exc()
   
    