"""
Nombre: class Pais
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos 
Restricciones:
"""
class Pais:
    def __init__(self,codigo_fifa,nombre,continente,ranking_fifa):

        if not isinstance(codigo_fifa,str):
            raise TypeError ("Error: El codigo FIFA debe ser un texto")
        if not isinstance(nombre,str):
            raise TypeError ("Error: El nombre del pais debe ser un texto")
        if not isinstance(continente,str):
            raise TypeError ("Error: La confederación a la que pertenece debe ser un texto")
        if not isinstance(ranking_fifa,int):
            raise TypeError ("Error: La posición en el ranking debe ser un número entero")
        
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
        return (f"Codigo Oficial FIFA: {self.codigo_fifa}\n"
            f"Nombre: {self.nombre}\n"
            f"Continente: {self.continente}\n"
            f"Posición en el ranking FIFA: {self.ranking_fifa}")
    
    """
    Nombre:actualizar_datos  
    Entradas: codigo_fifa, nombre, continente, ranking_fifa
    Salidas: Datos actuaizados
    Restricciones:
    """
    def actualizar_datos(self, nuevoCodigo_fifa = None, nuevoNombre = None, nuevoContinente = None, nuevoRanking_fifa = None):

        if(nuevoCodigo_fifa != None):
            if not isinstance(nuevoCodigo_fifa, str):
                return "El nuevo código FIFA debe ser un texto"
        if(nuevoNombre != None):   
            if not isinstance(nuevoNombre, str):
                return "El nuevo nombre debe ser un texto"
        if(nuevoContinente != None):    
            if not isinstance(nuevoContinente, str):
                return "La nueva confederación debe ser un texto"
        if(nuevoRanking_fifa != None):    
            if not isinstance(nuevoRanking_fifa, int):
                return "El nuevo ranking FIFA debe ser un número entero"

        if(nuevoCodigo_fifa != None):    
            self.codigo_fifa = nuevoCodigo_fifa
        if(nuevoNombre != None):
            self.nombre = nuevoNombre  
        if(nuevoContinente != None):    
            self.continente = nuevoContinente
        if(nuevoRanking_fifa != None):    
            self.ranking_fifa = nuevoRanking_fifa

        return "La actualizacion se realizo con exito"
"""
Nombre: class Persona
Entradas: No hay 
Salidas: Métodos de constructor y mostrar_datos 
Restricciones:
"""
class Persona():
    def __init__(self, nombre, apellido,fecha_nacimiento,nacionalidad):

        if not isinstance (nombre,str):
            raise TypeError("Error: El nombre debe ser un texto")
        if not isinstance (apellido,str):
            raise TypeError ("Error: El apellido debe ser un texto")
        if not isinstance (fecha_nacimiento, str):
            raise TypeError ("Error:  La fecha de nacimiento debe ser un texto en formatto DD/MM/AAAA")
        if not isinstance (nacionalidad,str):
            raise TypeError("Error: La nacionalidad debe ser un texto")
    
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
        return (f"Nombre: {self.nombre}\n"
        f"Apellido: {self.apellido}\n"
        f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
        f"Nacionalidad: {self.nacionalidad}")


"""
Nombre: class Entrenador
Entradas: No hay 
Salidas: Métodos de constructor, mostrar_datos y actualizar_datos
Restricciones:
"""
class Entrenador(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad,licencia, experiencia_anios, sistema_juego):
        if not isinstance(licencia,str):
            raise TypeError ("Error:La licencia debe ser un texto")
        if not isinstance(experiencia_anios, int):
            raise TypeError ("Error: Los años de experiencia debe ser un número entero")
        if not isinstance(sistema_juego, str):
            raise TypeError ("Error: El sistema táctico preferido debe ser un texto")
        
        Persona.__init__(self, nombre, apellido,fecha_nacimiento,nacionalidad)

        self.licencia = licencia
        self.experiencia_anios = experiencia_anios
        self.sistema_juego = sistema_juego

    """
    Nombre: mostrar_datos
    Entradas: No hay 
    Salidas:  
    Restricciones:
    """
    def mostrar_datos(self):
        return (Persona.mostrar_datos(self)
                + f"\nLicencia: {self.licencia}"
                + f"\nAños de experiencia como entrenador: {self.experiencia_anios}"
                + f"\nSistema táctico preferido: {self.sistema_juego}")

    """
    Nombre: actualizar_datos
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def actualizar_datos(self, nuevoNombre = None, nuevoApellido = None, nuevaFecha_nacimiento = None, nuevaNacionalidad = None,nuevaLicencia = None,nuevaExperiencia_anios = None, nuevoSistema_juego = None):
        if(nuevoNombre != None):
            if not isinstance(nuevoNombre, str):
                return "El nuevo nombre debe ser un texto"
        if(nuevoApellido != None):   
            if not isinstance(nuevoApellido, str):
                return "El nuevo apellido debe ser un texto"
        if (nuevaFecha_nacimiento != None):    
            if not isinstance(nuevaFecha_nacimiento, str):
                return "La nueva fecha de nacimiento debe ser un texto en formato DD/MM/AAAA"
        if(nuevaNacionalidad != None):    
            if not isinstance(nuevaNacionalidad, str):
                return "La nueva nacionalidad debe ser un texto"
        if(nuevaLicencia != None):
            if not isinstance (nuevaLicencia, str):
                return "Error: La nueva licencia debe ser un texto"
        if(nuevaExperiencia_anios != None):
            if not isinstance (nuevaExperiencia_anios, int):
                return "Error: Los nuevos años de experiencia deben ser un número entero"
        if(nuevoSistema_juego != None):
            if not isinstance(nuevoSistema_juego,str):
                return "Error: El nuevo sistema táctico preferido debe ser un texto"

        if(nuevoNombre != None):
            self.nombre = nuevoNombre
        if(nuevoApellido != None):
            self.apellido = nuevoApellido
        if(nuevaFecha_nacimiento != None):
            self.fecha_nacimiento = nuevaFecha_nacimiento
        if(nuevaNacionalidad != None):
            self.nacionalidad = nuevaNacionalidad
        if(nuevaLicencia != None):
            self.licencia = nuevaLicencia
        if(nuevaExperiencia_anios != None):
            self.experiencia_anios = nuevaExperiencia_anios
        if(nuevoSistema_juego != None):
            self.sistema_juego = nuevoSistema_juego
        
        
        return "La actualización se realizó con éxito"

class Futbolista(Persona):
    def __init__(self, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):

        if not isinstance(dorsal,int):
            raise TypeError("Error: El dorsal debe ser un número entero")
        if not isinstance(posicion, str):
            raise TypeError("Error: La posición del jugador debe ser un texto")
        if not isinstance(total_tarjetas_amarillas, int):
            raise TypeError("Error: Las tarjetas amarillas deben ser un número entero")
        if not isinstance(total_tarjetas_rojas,int):
            raise TypeError("Error: Las tarjetas rojas deben ser un número entero")
        if not isinstance(goles,int):
            raise TypeError("Error: Los goles anotados deben ser un número entero")
        if not isinstance(asistencias,int):
            raise TypeError("Error:La asistencias deben ser un número entero")
        if not isinstance(asistencias,int):
            raise TypeError("Error:Las asistencias deben ser un número entero")
        if not isinstance(puntaje_individual;int):
            raise TypeError("Error:El puntaje individual debe ser un número entero")
        
        Persona.__init__(self, nombre, apellido,fecha_nacimiento,nacionalidad)
        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual
        
        

    
    

        


    
            
            
        
        
        
