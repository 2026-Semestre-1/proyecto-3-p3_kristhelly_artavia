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
    def actualizar_datos(self, nuevo_codigo_fifa = None, nuevo_nombre = None, nuevo_continente = None, nuevo_ranking_fifa = None):

        if(nuevo_codigo_fifa != None):
            if not isinstance(nuevo_codigo_fifa, str):
                return "El nuevo código FIFA debe ser un texto"
        if(nuevo_nombre != None):   
            if not isinstance(nuevo_nombre, str):
                return "El nuevo nombre debe ser un texto"
        if(nuevo_continente != None):    
            if not isinstance(nuevo_continente, str):
                return "La nueva confederación debe ser un texto"
        if(nuevo_ranking_fifa != None):    
            if not isinstance(nuevo_ranking_fifa, int):
                return "El nuevo ranking FIFA debe ser un número entero"

        if(nuevo_codigo_fifa != None):    
            self.codigo_fifa = nuevo_codigo_fifa
        if(nuevo_nombre != None):
            self.nombre = nuevo_nombre  
        if(nuevo_continente != None):    
            self.continente = nuevo_continente
        if(nuevo_ranking_fifa != None):    
            self.ranking_fifa = nuevo_ranking_fifa

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
    def actualizar_datos(self, nuevo_nombre = None, nuevo_apellido = None, nueva_fecha_nacimiento = None, nueva_nacionalidad = None,nueva_licencia = None,nueva_experiencia_anios = None, nuevo_sistema_juego = None):
        if(nuevo_nombre != None):
            if not isinstance(nuevo_nombre, str):
                return "El nuevo nombre debe ser un texto"
        if(nuevo_apellido != None):   
            if not isinstance(nuevo_apellido, str):
                return "El nuevo apellido debe ser un texto"
        if (nueva_fecha_nacimiento != None):    
            if not isinstance(nueva_fecha_nacimiento, str):
                return "La nueva fecha de nacimiento debe ser un texto en formato DD/MM/AAAA"
        if(nueva_nacionalidad != None):    
            if not isinstance(nueva_nacionalidad, str):
                return "La nueva nacionalidad debe ser un texto"
        if(nueva_licencia != None):
            if not isinstance (nueva_licencia, str):
                return "Error: La nueva licencia debe ser un texto"
        if(nueva_experiencia_anios != None):
            if not isinstance (nueva_experiencia_anios, int):
                return "Error: Los nuevos años de experiencia deben ser un número entero"
        if(nuevo_sistema_juego != None):
            if not isinstance(nuevo_sistema_juego,str):
                return "Error: El nuevo sistema táctico preferido debe ser un texto"

        if(nuevo_nombre != None):
            self.nombre = nuevo_nombre
        if(nuevo_apellido != None):
            self.apellido = nuevo_apellido
        if(nueva_fecha_nacimiento != None):
            self.fecha_nacimiento = nueva_fecha_nacimiento
        if(nueva_nacionalidad != None):
            self.nacionalidad = nueva_nacionalidad
        if(nueva_licencia != None):
            self.licencia = nueva_licencia
        if(nueva_experiencia_anios != None):
            self.experiencia_anios = nueva_experiencia_anios
        if(nuevo_sistema_juego != None):
            self.sistema_juego = nuevo_sistema_juego
        
        
        return "La actualización se realizó con éxito"

class Futbolista(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):

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
        if not isinstance(puntaje_individual,int):
            raise TypeError("Error:El puntaje individual debe ser un número entero")
        
        Persona.__init__(self, nombre, apellido,fecha_nacimiento,nacionalidad)
        self.dorsal = dorsal
        self.posicion = posicion
        self.total_tarjetas_amarillas = total_tarjetas_amarillas
        self.total_tarjetas_rojas = total_tarjetas_rojas
        self.goles = goles
        self.asistencias = asistencias
        self.puntaje_individual = puntaje_individual

    """
    Nombre: mostrar_datos
    Entradas: No hay 
    Salidas:  
    Restricciones:
    """
    def mostrar_datos(self):
        return (Persona.mostrar_datos(self)
                + f"\nDorsal:{self.dorsal}"
                + f"\nPosición:{self.posicion}"
                + f"\nTotal de tarjetas amarillas: {self.total_tarjetas_amarillas}"
                + f"\nTotal de tarjetas rojas: {self.total_tarjetas_rojas}"
                + f"\nGoles: {self.goles}"
                + f"\nAsistencias: {self.asistencias}"
                + f"\nPuntaje: {self.puntaje_individual}")
    
    def actualizar_datos(self, nuevo_nombre = None, nuevo_apellido = None, nueva_fecha_nacimiento = None, nueva_nacionalidad = None, nuevo_dorsal = None, nueva_posicion = None,
                         nuevo_total_tarjetas_amarillas = None, nuevo_total_tarjetas_rojas = None, nuevos_goles = None, nuevas_asistencias = None, nuevo_puntaje_individual = None):
        if( nuevo_nombre != None):
            if not isinstance(nuevo_nombre, str):
                return "El nuevo nombre debe ser un texto"
        if( nuevo_apellido != None):   
            if not isinstance(nuevo_apellido, str):
                return "El nuevo apellido debe ser un texto"
        if (nueva_fecha_nacimiento != None):    
            if not isinstance(nueva_fecha_nacimiento, str):
                return "La nueva fecha de nacimiento debe ser un texto en formato DD/MM/AAAA"
        if(nueva_nacionalidad != None):    
            if not isinstance(nueva_nacionalidad, str):
                return "La nueva nacionalidad debe ser un texto"
        if(nuevo_dorsal != None):
            if not isinstance(nuevo_dorsal,int):
                return "El nuevo dorsal debe ser un número entero"
        if(nueva_posicion != None):
            if not isinstance(nueva_posicion,str):
                return "La nueva posición del jugador debe ser un texto"
        if(nuevo_total_tarjetas_amarillas != None):
            if not isinstance(nuevo_total_tarjetas_amarillas, int):
                return "El nuevo total de tarjetas amarillas debe ser un número entero"
        if(nuevo_total_tarjetas_rojas != None):
            if not isinstance(nuevo_total_tarjetas_rojas,int):
                return "El nuevo total de tarjetas rojas debe ser un número entero"
        if(nuevos_goles != None):
            if not isinstance(nuevos_goles, int):
                return "La nueva cantidad de goles debe ser un número entero"
        if(nuevas_asistencias != None):
            if not isinstance(nuevas_asistencias,int):
                return "La nueva cantidad de asistencias debe ser un número entero"
        if(nuevo_puntaje_individual != None):
            if not isinstance(nuevo_puntaje_individual,int):
                return "El nuevo puntaje debe ser un número entero"
            
        if(nuevo_nombre != None):
            self.nombre = nuevo_nombre
        if(nuevo_apellido != None):
            self.apellido = nuevo_apellido
        if(nueva_fecha_nacimiento != None):
            self.fecha_nacimiento = nueva_fecha_nacimiento
        if(nueva_nacionalidad != None):
            self.nacionalidad = nueva_nacionalidad
        if(nuevo_dorsal != None):
            self.dorsal = nuevo_dorsal
        if(nueva_posicion != None):
            self.posicion = nueva_posicion
        if(nuevo_total_tarjetas_amarillas != None):
            self.total_tarjetas_amarillas = nuevo_total_tarjetas_amarillas
        if(nuevo_total_tarjetas_rojas != None):
            self.total_tarjetas_rojas = nuevo_total_tarjetas_rojas
        if(nuevos_goles != None):
            self.goles = nuevos_goles
        if(nuevas_asistencias != None):
            self.asistencias = nuevas_asistencias
        if(nuevo_puntaje_individual != None):
            self.puntaje_individual = nuevo_puntaje_individual
        
        return "La actualización se realizó con éxito"

    def registrar_gol(self):
        self.goles += 1
        return "Se registro un gol"

    def registrar_asistencia(self):
        self.asistencias += 1
        return "Se registro una asistencia"

    def registrar_tarjeta(self, tipo):
        if tipo == "tarjeta amarilla":
            self.total_tarjetas_amarillas += 1
            return "Se registro una tarjeta amarilla"

        if tipo == "tarjeta roja":
            self.total_tarjetas_rojas += 1
            return "Se registro una tarjeta roja"

        return "Tipo de tarjeta no valido"

class Seleccion():
    def __init__(self,codigo_equipo, pais ):
        if not isinstance (codigo_equipo,str):
            raise TypeError("Error: El codigo del equipo debe ser un texto")
        if not isinstance (pais,Pais):
            raise TypeError ("Error: El pais debe ser un objeto asociado a la clase Pais")
            
        self.codigo_equipo = codigo_equipo
        self.pais = pais
        self.entrenador = None #un entrenador asignado
        self.jugadores = []
        self.total_goles_favor = 0
        self.total_goles_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.fuerza_equipo = 0
            

            

    
            
