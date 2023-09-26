from sympy import *
import os


class funcion:
    
    def __init__(self, demanda, oferta):
        
        self.dda = demanda
        self.off = oferta
    
    def eqq(self):
        p = symbols("p")
        precio_equilibrio = solve(Eq(self.off, self.dda))
        cantidad_equilibrio = self.dda.subs({p: precio_equilibrio[0]})
        return f"""Precio de equilibrio = {precio_equilibrio[0]}\nCantidad de equilibrio = {cantidad_equilibrio}"""
    
    def exc(self):
        p = symbols("p")
        MANTENER = 1
        REEMPLAZAR = 2
        #Encontrando la cantidad del exceso de oferta y de la demanda
        print(f"""Para encontrar el Exceso de Demanda y Oferta, desea mantener el Precio de Equilibrio del Mercado o introducir un nuevo Precio?
            {MANTENER}) Mantener el precio de equilibrio.
            {REEMPLAZAR}) Introducir un nuevo precio. 
            
            """)
        opc = int(input("Seleccione una opcion: "))
        os.system("cls")
        if opc == MANTENER:
            p = symbols("p")
            precio_equilibrio = solve(Eq(self.off, self.dda))
            Xo2 = self.off.subs({p: precio_equilibrio[0]})
            Xd2 = self.dda.subs({p: precio_equilibrio[0]})

            Xo3 = self.off.subs({p: precio_equilibrio[0]})
            Xd3 = self.dda.subs({p: precio_equilibrio[0]})
            
            return f"""Precio de equilibrio: {precio_equilibrio[0]}\nExceso de demanda: {Xd2 - Xo2}\nExceso de oferta: {Xo3 - Xd3}"""
        
        elif opc == REEMPLAZAR:
            #Reemplazando el precio de demanda
            x = int(input("Nuevo precio de demanda: "))
            y = int(input("Nuevo precio de oferta: "))
            Xo4 = self.off.subs({p: x})
            Xd4 = self.dda.subs({p: x})

            Xo5 = self.off.subs({p: y})
            Xd5 = self.dda.subs({p: y})

            return f"""Exceso de demanda: {Xd4 - Xo4}\nExceso de oferta: {Xo5 - Xd5}"""
    
    def precio_expo(self):
        p = symbols("p")
        MANTENER = 1
        REEMPLAZAR = 2

        print(f"""Para encontrar el Precio de Importacion y Exportacion, desea mantener la Cantidad de Equilibrio del Mercado o introducir una nueva cantidad?
            {MANTENER}) Mantener la cantidad de equilibrio.
            {REEMPLAZAR}) Introducir nueva cantidad. 
            
            """)
        opc = int(input("Seleccione una opcion: "))
        os.system("cls")
        if opc == MANTENER:
            #Encontramos el precio de eqq para tener la cantidad de eqq
            precio_equilibrio = solve(Eq(self.off, self.dda))
            cantidad_equilibrio = self.dda.subs({p: precio_equilibrio[0]})

            #Hallamos el precio de exportacion e importacion con la cantidad de eqq de mercado
            ExcesoOferta = self.off - self.dda
            precio_expo = solve(Eq(cantidad_equilibrio, ExcesoOferta))

            ExcesoDemanda = self.dda - self.off
            precio_impo = solve(Eq(cantidad_equilibrio, ExcesoDemanda))

            return f"""El precio de exportacion a una cantidad de {cantidad_equilibrio} unidades es {precio_expo[0]}\nEl precio de importacion a una cantidad de {cantidad_equilibrio} unidades es {precio_impo[0]}"""
        
        elif opc == REEMPLAZAR:
            #Solicitamos las nuevas cantidades
            x = int(input("Nueva cantidad para el precio de importacion: "))
            y = int(input("Nueva cantidad para el precio de exportacion: "))
            Exceso_Oferta = self.off - self.dda
            precioexpo = solve(Eq(y, Exceso_Oferta))

            Exceso_Demanda = self.dda - self.off
            precioimpo = solve(Eq(x, Exceso_Demanda))

            return f"""El precio de exportacion a una cantidad de {y} unidades es {precioexpo[0]}\nEl precio de importacion a una cantidad de {x} unidades es {precioimpo[0]}"""


EQ_MERCADO = 1
EXC_DDA_OFF = 2
PRECIO_EXPO_IMPO = 3

def menu():
    os.system("cls")
    print(f"""          Bienvenido al programa. Que desea realizar?\n
        {EQ_MERCADO}) Equilibrio de Mercado.
        {EXC_DDA_OFF}) Exceso de Demanda y oferta. 
        {PRECIO_EXPO_IMPO}) Precio de Exportacion e Importacion.
        """)

def main():
    
    #Solicitando las funciones
    print("""Introduzca las funciones de Demanda y Oferta en terminos del precio. Por ejemplo:\n
                        Xd = a + b*p
                        Xo = c - p """)
    demanda = input("Demanda: ")
    oferta = input("Oferta: ")

    #Convirtiendo el str a funcion simbolica
    demanda = sympify(demanda)
    oferta = sympify(oferta)

    prueba = funcion(demanda, oferta)

    
    menu()
    opc = int(input("Selecciona una opcion: "))
    os.system("cls")
    if opc == EQ_MERCADO:
        print(prueba.eqq())
    elif opc == EXC_DDA_OFF:
        print(prueba.exc())
    elif opc == PRECIO_EXPO_IMPO:
        print(prueba.precio_expo())
        

if __name__ == "__main__":
    main()