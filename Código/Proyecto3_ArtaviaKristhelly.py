"""
Nombre: class Pais
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos 
Restricciones:
"""
class Pais:
    def __init__(self,codigo_fifa,nombre,continente,ranking_fifa):
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa
        
    """
    Nombre: mostrar_datos 
    Entradas: No hay 
    Salidas: 
    Restricciones:
    """
    def mostrar_datos(self):
        return ("Codigo Oficial FIFA: " + self.codigo_fifa + "\n" 
        + "Nombre: " + self.nombre + "\n" 
        + "Continente: " + self.continente + "\n" 
        + "Posición en el ranking FIFA: " + str(self.ranking_fifa))
    
    """
    Nombre:actualizar_datos  
    Entradas: codigo_fifa, nombre, continente, ranking_fifa
    Salidas: Datos actuaizados
    Restricciones:
    """
    def actualizar_datos(self, codigo_fifa = None, nombre = None, continente = None, ranking_fifa = None):
        if (codigo_fifa != None):
            self.codigo_fifa = codigo_fifa
        if (nombre != None):
            self.nombre = nombre
        if (continente != None):
            self.continente = continente
        if (ranking_fifa != None):
            self.ranking_fifa = ranking_fifa
            
            
        
        
        
