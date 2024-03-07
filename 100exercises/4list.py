"""
Create list with different elements and print information
"""

def getData():
    try:
        numElements = int(input("Cantidad de elementos: "))
        if not numElements or numElements<=0:
            print("Dato inválido")
            return None
        else:
            return numElements
    except ValueError:
        print("\nDato inválido")
        return None
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrumpida.")
        return None
    

def fillList(numElements):
            list = []
            for i in range(numElements):
                list.append(input(f"{i+1}: "))
            return list

numElements = getData()
if numElements is not None:
    print(f"Digite a continuación {numElements} elementos de cualquier tipo:")
    list = fillList(numElements)
    print(f"elementos: {list}")