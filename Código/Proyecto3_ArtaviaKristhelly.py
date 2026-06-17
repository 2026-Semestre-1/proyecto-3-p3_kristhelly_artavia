"""
Nombre: class Pais
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos 
Restricciones:
"""
class Pais:
    def __init__(self,codigo_fifa,nombre,continente,ranking_fifa):

        #FALTA VALIDACIONES
        
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
        + "Nombre: " + self.nombre 
        + "\nContinente: " + self.continente
        + "\nPosición en el ranking FIFA: " + str(self.ranking_fifa)) #revisar si str esta permitido
    
    """
    Nombre:actualizar_datos  
    Entradas: codigo_fifa, nombre, continente, ranking_fifa
    Salidas: Datos actuaizados
    Restricciones:
    """
    def actualizar_datos(self, nuevoCodigo_fifa = None, nuevoNombre = None, nuevoContinente = None, nuevoRanking_fifa = None):

        if (nuevoCodigo_fifa != None):
            if not isinstance(nuevoCodigo_fifa, str):
                return "El nuevo código FIFA debe ser un texto"
            self.codigo_fifa = nuevoCodigo_fifa
            
        if (nuevoNombre != None):   
            if not isinstance(nuevoNombre, str):
                return "El nuevo nombre debe ser un texto"
            self.nombre = nuevoNombre
            
        if (nuevoContinente != None):    
            if not isinstance(nuevoContinente, str):
                return "La nueva confederación debe ser un texto"
            self.continente = nuevoContinente
            
        if (nuevoRanking_fifa != None):    
            if not isinstance(nuevoRanking_fifa, int):
                return "El nuevo ranking FIFA debe ser un número entero"
            self.ranking_fifa = nuevoRanking_fifa      
"""
Nombre: class Persona
Entradas: No hay 
Salidas: Métodos de constructor y mostrar_datos 
Restricciones:
"""
class Persona():
    def __init__(self, nombre, apellido,fecha_nacimiento,nacionalidad):

        #FALTA VALIDACIONES
    
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
        return ("Nombre: " + self.nombre
        + "\nApellido: " + self.apellido
        + "\nFecha de nacimiento: " + self.fecha_nacimiento
        + "\nNacionalidad: " + self.nacionalidad)


"""
Nombre: class Entrenador
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos
Restricciones:
"""
class Entrenador(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad,licencia, experiencia_anios, sistema_juego):

        #Faltan validaciones
        Persona.__init__(self, nombre, apellido,fecha_nacimiento,nacionalidad)

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    def mostrar_datos(self):
        return (Persona.mostrar_datos(self) + "\nLicencia: " + self.licencia
                + "\nAños de experiencia como entrenador: " + str(self.experiencia_anios)#revisar si str esta permitido de esta forma
                + "\nSistema táctico preferido:" + self.sistema_juego) 

        


    
            
            
        
        
        
