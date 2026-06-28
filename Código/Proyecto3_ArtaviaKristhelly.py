import random

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
        if puntaje_individual > 100 or puntaje_individual < 1:
            raise TypeError("Error: El puntaje individual del futbolista debe estar en el rango de 1-100")
        
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

    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
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

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def registrar_gol(self):
        self.goles += 1
        return "Se registro un gol"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def registrar_asistencia(self):
        self.asistencias += 1
        return "Se registro una asistencia"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
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

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def mostrar_datos(self):
        return (f"\nEl codigo de la selección es: {self.codigo_equipo}"
            f"\nEl país de la selección es: {self.pais.mostrar_datos()}"
            f"\nEl entrenador de la selección es: {self.entrenador}"
            f"\nLos jugadores de la selección son: {self.jugadores}"
            f"\nEl total de goles a favor son: {self.total_goles_favor}"
            f"\nEl total de goles en contra son: {self.total_goles_contra}"
            f"\nEl total de tarjetas amarillas son: {self.total_tarjetas_amarillas}"
            f"\nEl total de tarjetas rojas son: {self.total_tarjetas_rojas}"
            f"\nLa fuerza del equipo es: {self.fuerza_equipo}")
    

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def contar_jugadores(self):
        contador = 0

        for jugador in self.jugadores:
            contador += 1

        return contador

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def agregar_jugador(self, futbolista):
        if not isinstance(futbolista, Futbolista):
            return "Error: Debe agregar un objeto de la clase Futbolista"

        if self.contar_jugadores() >= 23:
            return "Error: No se puede agregar más jugadores ya tiene 23 jugadores"

        self.jugadores += [futbolista]

        return "Jugador agregado con éxito"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def eliminar_jugador(self, dorsal):
        if not isinstance (dorsal, int):
            return "Error: El dorsal debe ser un entero"

        lista_nueva = []
        encontrar = False

        for jugador in self.jugadores:
            if jugador.dorsal == dorsal:
                encontrar = True
            else:
                lista_nueva += [jugador]


        if encontrar == False:
            return "Error: No se encontró un jugador con ese dorsal"

        self.jugadores = lista_nueva

        return "Jugador eliminado"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador, Entrenador):
            return "Error: Debe ser un objeto de la clase Entrenador"

        self.entrenador = entrenador

        return "Entrenador asignado"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def registrar_resultado(self, goles_favor,goles_contra,tarjetas_am, tarjetas_roj):
        if not isinstance (goles_favor, int):
            return "Goles a favor deben ser un entero"
        if not isinstance (goles_contra,int):
            return "Goles en contra debe ser un entero"
        if not isinstance (tarjetas_am, int):
            return "Tarjetas amarillas debe ser un entero"
        if not isinstance (tarjetas_roj,int):
            return "Tarjetas rojas debe ser un entero"

        self.total_goles_favor += goles_favor
        self.total_goles_contra += goles_contra
        self.total_tarjetas_amarillas += tarjetas_am
        self.total_tarjetas_rojas += tarjetas_roj

        return "Se actualizaron los totales del equipo"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def calcular_fuerza_equipo(self):
        if self.entrenador == None:
            return "Se debe asignar un entrenador"
        if self.contar_jugadores() < 11:
            return "Debe haber al menos 11 jugadores"

        self.fuerza_equipo = (self.promedio_jugadores() * 0.6) + (self.factor_entrenador() * 0.25) + (self.factor_ranking() * 0.15)

        return self.fuerza_equipo

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """        
    def promedio_jugadores(self):
        mejores_jugadores = []
        futbolistas = self.jugadores
        contador = 0

        while contador < 11:
            mejor_jugador = None

            for jugador in futbolistas:
                if mejor_jugador == None:
                    mejor_jugador = jugador
                elif jugador.puntaje_individual > mejor_jugador.puntaje_individual:
                    mejor_jugador = jugador

            mejores_jugadores += [mejor_jugador]

            lista_nueva = []

            for jugador in futbolistas:
                if not jugador == mejor_jugador:
                    lista_nueva += [jugador]
            futbolistas = lista_nueva
            contador += 1


        suma_puntajes = 0

        for jugador in mejores_jugadores:
            suma_puntajes += jugador.puntaje_individual

        promedio = suma_puntajes / 11

        return promedio

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def factor_entrenador(self):
       factor = self.entrenador.experiencia_anios * 4

       if factor > 100:
           return 100

       return factor

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def factor_ranking(self):
        factor = 100 - self.pais.ranking_fifa

        return factor

class Partido:

    def __init__(self, id_partido, equipo_1, equipo_2, fase, fecha):
        if not isinstance(id_partido, int):
            raise TypeError("Error: El ID del partido debe ser un número entero")
        if not isinstance (equipo_1, Seleccion):
            raise TypeError("Error: El equipo 1 debe ser de tipo Selección")
        if not isinstance(equipo_2, Seleccion):
            raise TypeError("Error: El equipo 2 debe ser de tipo Selección")
        if not isinstance(fase, str):
            raise TypeError("Error: La fase del torneo a la que pertenece el partido debe ser un texto")
        if not isinstance(fecha, str):
            raise TypeError("Error: La fecha del partido debe ser en formato DD/MM/AAAA")

        self.id_partido = id_partido
        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.fase = fase
        self.fecha = fecha

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def simular(self):

        #diferencia de fuerza
        fuerza_equipo1 = self.equipo_1.calcular_fuerza_equipo()

        fuerza_equipo2 = self.equipo_2.calcular_fuerza_equipo()

        diferencia = fuerza_equipo1 - fuerza_equipo2

        if diferencia > 30:
            self.goles_equipo1 = random.randint(2,7)
            self.goles_equipo2 = random.randint(0,3)
            
        elif diferencia > 15:
            self.goles_equipo1 = random.randint(1,5)
            self.goles_equipo2 = random.randint(0,4)

        elif diferencia < -30:
            self.goles_equipo1 = random.randint(0,3)
            self.goles_equipo2 = random.randint(2,7)

        elif diferencia < -15:
            self.goles_equipo1 = random.randint(0,4)
            self.goles_equipo2 = random.randint(1,5)

        else:
            self.goles_equipo1 = random.randint(0,4)
            self.goles_equipo2 = random.randint(0,4)

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def generar_ganador(self):
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1
        if self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2
        if self.goles_equipo1 == self.goles_equipo2:
            return None

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def mostrar_resultado(self):
        return f"{self.equipo_1.pais.nombre} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo_2.pais.nombre}"

class Grupo():
    def __init__(self, nombre_grupo):
        if not isinstance(nombre_grupo, str):
            raise TypeError("Error: El identificador del grupo debe ser un texto")
        
        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def contar_equipos(self):
        contador = 0

        for equipo in self.equipos:
            contador += 1

        return contador

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def agregar_equipo(self, seleccion):
        if not isinstance(seleccion, Seleccion):
            return "Error: Debe agregar un objeto de la clase Seleccion"

        if self.contar_equipos() >= 4:
            return "Error: No se puede agregar más equipos el grupo ya tiene 4"

        self.equipos += [seleccion]

        return "Equipo agregado"

    
    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def jugar_partidos(self):
        if self.contar_equipos() != 4:
            return "Error: Deben haber 4 equipos para jugar en los partidos"

        i = 0
        id_partido = 1

        while i < 4:
            j = i + 1

            while j < 4:
                equipo_1 = self.equipos[i]
                equipo_2 = self.equipos[j]

                partido = Partido(id_partido, equipo_1, equipo_2, "fase", "sin fecha")
                partido.simular()
                self.partidos += [partido]

                id_partido += 1
                j += 1

            i += 1

    """
    Nombre: 
    Entradas:  
    Salidas:  
    Restricciones:
    """
    def calcular_tabla(self):
        tabla = []

        for equipo in self.equipos:
            puntos = 0
            goles_favor = 0
            goles_contra = 0

            for partido in self.partidos:
                if equipo == partido.equipo_1:
                    goles_favor += partido.goles_equipo1
                    goles_contra += partido.goles_equipo2

                    if partido.goles_equipo1 > partido.goles_equipo2:
                        puntos += 3
                        
                    if partido.goles_equipo1 == partido.goles_equipo2:
                        puntos += 1

                if equipo == partido.equipo_2:
                    goles_favor += partido.goles_equipo2
                    goles_contra += partido.goles_equipo1

                    if partido.goles_equipo2 > partido.goles_equipo1:
                        puntos += 3

                    if partido.goles_equipo2 == partido.goles_equipo1:
                        puntos += 1

            diferencia = goles_favor - goles_contra
            tabla += [[equipo,puntos,goles_favor,goles_contra,diferencia]]

        return tabla
        

        
        
    
        

            
            

        

        
        
        










    
