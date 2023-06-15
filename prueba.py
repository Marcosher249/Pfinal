class suma:
    def sumar(numero):
        return numero +1
class ejemplo:
    sumar = suma
class ejemplo2:
    ejem = ejemplo
    
clase= getattr(ejemplo2,"ejem","sumar")
resultado = clase.sumar(1)
print(resultado)