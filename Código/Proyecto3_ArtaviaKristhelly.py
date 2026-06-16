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
        + "Posición en el ranking FIFA: " + str(self.ranking_fifa)) #revisar si str esta permitido
    
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

"""
Nombre: class Persona
Entradas: No hay 
Salidas: Métodos de constructor y mostrar_datos 
Restricciones:
"""
class Persona():
    def __init__(self, nombre, apellido,fecha_nacimiento,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        
    """
    Nombre: mostrar_datos
    Entradas: No hay 
    Salidas: Datos de persona, la cual lo heredan Entrenador y Futbolista 
    Restricciones:
    """
    def mostrar_datos(self):
        return ("Nombre: " + self.nombre + "\n"
        + "Apellido: " + self.apellido + "\n"
        + "Fecha de nacimiento: " + self.fecha_nacimiento + "\n"
        + "Nacionalidad: " + self.nacionalidad)


"""
Nombre: class Entrenador
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos
Restricciones:
"""
class Entrenador(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad,licencia, experiencia_anios, sistema_juego):
        Persona.__init__(self, nombre, apellido,fecha_nacimiento,nacionalidad)

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego
        


    
            
            
        
        
        
