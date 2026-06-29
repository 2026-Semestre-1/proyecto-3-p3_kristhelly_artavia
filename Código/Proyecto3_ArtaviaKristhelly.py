import random


"""
Nombre: class Pais
Entradas: codigo_fifa,nombre,continente,ranking_fifa 
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
    Salidas: Mostrar los datos de el país
    Restricciones: No hay
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
    Restricciones: nuevo_codigo_fifa,nuevo_nombre,nuevo_continente, deben ser str, y nuevo_ranking_fifa debe ser int
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
Restricciones: nombre,apellido,fecha_nacimiento,nacionalidad deben ser str
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
    Restricciones: No hay
    """
    def mostrar_datos(self):
        return (f"Nombre: {self.nombre}\n"
        f"Apellido: {self.apellido}\n"
        f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
        f"Nacionalidad: {self.nacionalidad}")


"""
Nombre: class Entrenador
Entradas: Persona
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
    Salidas: Datos de el entrenador sobreescribiendo el método de Persona
    Restricciones:
    """
    def mostrar_datos(self):
        return (Persona.mostrar_datos(self)
                + f"\nLicencia: {self.licencia}"
                + f"\nAños de experiencia como entrenador: {self.experiencia_anios}"
                + f"\nSistema táctico preferido: {self.sistema_juego}")

    """
    Nombre: actualizar_datos
    Entradas: nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento , nueva_nacionalidad ,nueva_licencia,nueva_experiencia_anios, nuevo_sistema_juego
    Salidas:  Se actualizan los datos del entrenador
    Restricciones:nuevo_nombre,nuevo_apellido,nueva_fecha_nacimiento,nueva_nacionalidad,nueva_licencia,nuevo_sistema_juego debe ser un string y  nueva_experiencia_anios debe ser un int
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

"""
Nombre: class Futbolista
Entradas: Persona
Salidas: Métodos de constructor, mostrar_datos,actualizar_datos,registrar_gol,registrar_asistencia,registrar_tarjeta
Restricciones: 
"""
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
    Salidas:Datos de futbolista
    Restricciones:No hay
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
    Nombre: actualizar_datos
    Entradas: nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento, nueva_nacionalidad, nuevo_dorsal, nueva_posicion,
                         nuevo_total_tarjetas_amarillas, nuevo_total_tarjetas_rojas, nuevos_goles, nuevas_asistencias, nuevo_puntaje_individual 
    Salidas: Los datos del futbolista actualizados 
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
    Nombre: registrar_gol
    Entradas: No hay 
    Salidas:  Mensaje de que se regsitro un gol
    Restricciones: No hay
    """
    def registrar_gol(self):
        self.goles += 1
        return "Se registro un gol"

    
    """
    Nombre: registrar_asistencia
    Entradas: No hay  
    Salidas:  Mensaje de que se registro una asistencia
    Restricciones: No hay
    """
    def registrar_asistencia(self):
        self.asistencias += 1
        return "Se registro una asistencia"

    
    """
    Nombre: registrar_tarjeta
    Entradas: tipo
    Salidas: Mensaje de registro de tarjeta ya sea amarilla o roja
    Restricciones: No hay
    """
    def registrar_tarjeta(self, tipo):
        if tipo == "tarjeta amarilla":
            self.total_tarjetas_amarillas += 1
            return "Se registro una tarjeta amarilla"

        if tipo == "tarjeta roja":
            self.total_tarjetas_rojas += 1
            return "Se registro una tarjeta roja"

        return "Tipo de tarjeta no valido"


"""
Nombre: class Seleccion
Entradas: 
Salidas: Métodos de constructor, mostrar_datos,contar_jugadores,agregar_jugador,eliminar_jugador,asignar_entrenador,registrar_resultado,calcular_fuerza_equipo,promedio_jugadores,factor_entrenador,factor_ranking
Restricciones: 
"""
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
    Nombre:mostrar_datos 
    Entradas: No hay  
    Salidas:  Muestra los datos de la selección
    Restricciones: No hay
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
    Nombre: contar_jugadores
    Entradas: No hay 
    Salidas: retorna el contador con la cantidad de jugadores 
    Restricciones:
    """
    def contar_jugadores(self):
        contador = 0

        for jugador in self.jugadores:
            contador += 1

        return contador

    
    """
    Nombre: agregar_jugador  
    Entradas: futbolista   
    Salidas:  Mensaje que confirma que fue agregado
    Restricciones: futbolista debe ser un objeto de Futbolista 
    """
    def agregar_jugador(self, futbolista):
        if not isinstance(futbolista, Futbolista):
            return "Error: Debe agregar un objeto de la clase Futbolista"

        if self.contar_jugadores() >= 23:
            return "Error: No se puede agregar más jugadores ya tiene 23 jugadores"

        self.jugadores += [futbolista]

        return "Jugador agregado con éxito"

    
    """
    Nombre: eliminar_jugador
    Entradas:  dorsal
    Salidas:  Mensaje que confirma que el dorsal se elimino
    Restricciones:dorsal debe ser de tipo int
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
    Nombre: asignar_entrenador
    Entradas:  entrenador
    Salidas: Mensaje que confirma si el entrenador se asigno 
    Restricciones:
    """
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador, Entrenador):
            return "Error: Debe ser un objeto de la clase Entrenador"

        self.entrenador = entrenador

        return "Entrenador asignado"

    
    """
    Nombre: registrar_resultado
    Entradas: goles_favor,goles_contra,tarjetas_am, tarjetas_roj 
    Salidas:  Mensaje qeu indica ue se actuaizaron los totales de el equipo
    Restricciones:goles_favor,goles_contra,tarjetas_am y tarjetas_roj deben ser int
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
    Nombre: calcular_fuerza_equipo
    Entradas:  No hay
    Salidas: Valor de la fuerza del equipo 
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
    Nombre: promedio_jugadores
    Entradas:No hay
    Salidas: Promedio de los puntajes de los 11 mejores jugadores 
    Restricciones: La seleccion debe tener minimo 11 jugadores
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
    Nombre: factor_entrenador
    Entradas: No hay 
    Salidas:  experiencia del entrenador en una escala del 1-100
    Restricciones:Si al realizar la conversion a las escala 1-100 sobre pasa 100 se mantiene en 100
    """
    def factor_entrenador(self):
       factor = self.entrenador.experiencia_anios * 4

       if factor > 100:
           return 100

       return factor

    
    """
    Nombre: factor_ranking
    Entradas: No hay 
    Salidas: El factor calculado al restar a ranking fifa a 100
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
    Nombre: simular
    Entradas: No hay 
    Salidas:  No retorna un valor,Realiza la simulación de goles, diferencia de fuerza,
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
    Nombre: generar_ganador
    Entradas: No hay 
    Salidas: Retorna el equipo ganador 
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
    Nombre: mostrar_resultado
    Entradas:No hay  
    Salidas:  Retorna los resultados del partido (el marcador)
    Restricciones:
    """
    def mostrar_resultado(self):
        return f"{self.equipo_1.pais.nombre} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo_2.pais.nombre}"

"""
Nombre: class Grupo
Entradas:No hay
Salidas:  métodos contar_equipos,agregar_equipo,jugar_partidos,calcular_tabla,obtener_clasificados,mostrar_tabla
Restricciones:
"""
class Grupo():
    def __init__(self, nombre_grupo):
        if not isinstance(nombre_grupo, str):
            raise TypeError("Error: El identificador del grupo debe ser un texto")
        
        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []

    
    """
    Nombre: contar_equipos
    Entradas: No hay  
    Salidas: Cantidad de equipos 
    Restricciones:
    """
    def contar_equipos(self):
        contador = 0

        for equipo in self.equipos:
            contador += 1

        return contador

    
    """
    Nombre: agregar_equipo
    Entradas:seleccion  
    Salidas: Mensaje de que el equipo se agrego 
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
    Nombre: jugar_partidos
    Entradas: No hay  
    Salidas: Mensaje que confirma que se jugaron los partidos 
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

        return "Partidos jugados"

    """
    Nombre: calcular_tabla
    Entradas: No hay  
    Salidas: Retorna las tablas ordenadas con puntos, goles a favor,goles en contra y diferencia 
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

        tabla_ordenada = []
        contador = 0

        while contador < self.contar_equipos():
            mejor_fila = None

            for fila in tabla:
                if mejor_fila == None:
                    mejor_fila = fila
                elif fila[1] > mejor_fila[1]:
                    mejor_fila = fila
                elif fila[1] == mejor_fila[1] and fila[4] > mejor_fila[4]:
                    mejor_fila = fila
                elif fila[1] == mejor_fila[1] and fila[4] == mejor_fila[4] and fila[2] > mejor_fila[2]:
                    mejor_fila = fila

            tabla_ordenada += [mejor_fila]

            lista_nueva = []

            for fila in tabla:
                if fila != mejor_fila:
                    lista_nueva += [fila]

            tabla = lista_nueva
            contador += 1

        
        tabla_con_posiciones = []
        posicion = 1

        for fila in tabla_ordenada:
            tabla_con_posiciones += [[posicion, fila[0], fila[1], fila[2], fila[3], fila[4]]]
            posicion += 1

        return tabla_con_posiciones

    """
    Nombre: obtener_clasificados 
    Entradas: No hay 
    Salidas: Retorna los equipos clasificados 
    Restricciones: 
    """
    def obtener_clasificados(self):
        tabla = self.calcular_tabla()

        clasificado_1= tabla[0][1]
        clasificado_2 = tabla[1][1]

        return [clasificado_1, clasificado_2]

    """
    Nombre: mostrar_tabla
    Entradas:  No hay
    Salidas:  Tabla con las posiciones ordenadas del grupo
    Restricciones:
    """

    def mostrar_tabla(self):
        tabla = self.calcular_tabla()

        resultado = f"Tabla del {self.nombre_grupo}"

        for fila in tabla:
            resultado += (f"\n{fila[0]}. {fila[1].pais.nombre}"
                          f" - Puntos: {fila[2]}"
                          f" - Goles a favor: {fila[3]}"
                          f" - Goles en contra: {fila[4]}"
                          f" - Diferencia: {fila[5]}")

        return resultado


"""
Nombre: class Fase
Entradas:  
Salidas: constructor, contar_partidos, registrar_juego,jugar_fase,mostrar_juegos,obtener_clasificados
Restricciones:
"""
class Fase:
    def __init__(self, nombre_fase):
        if not isinstance(nombre_fase, str):
            raise TypeError("Error: El nombre de la fase debe ser un texto")

        self.nombre_fase = nombre_fase
        self.partidos = []

    """
    Nombre: contar_partidos
    Entradas: No hay 
    Salidas: cuenta cuantos partidos hay 
    Restricciones: No hay
    """
    def contar_partidos(self):
        contador = 0

        for partido in self.partidos:
            contador += 1

        return contador

    """
    Nombre: registrar_juego
    Entradas:  equipo1,equipo2
    Salidas:  Mensaje de que el partido se ha regsitrado
    Restricciones:
    """
    def registrar_juego(self, equipo1,equipo2):
        if not isinstance(equipo1, Seleccion):
            return "Error: El equipo 1 debe ser un objeto de la clase Seleccion"

        if not isinstance(equipo2, Seleccion):
            return "Error: El equipo 2 debe ser un objeto de la clase Seleccion"

        #crea ID automaticamente para identificar los partidos
        id_partido = self.contar_partidos() + 1

        partido = Partido(id_partido, equipo1, equipo2, self.nombre_fase, "Sin fecha")

        self.partidos += [partido]

        return "Partido registrado"
    
    """
    Nombre:jugar_fase 
    Entradas: No hay 
    Salidas: Mensaje de que la fase se jugo, en caso de empate, simula penales  
    Restricciones:
    """
    def jugar_fase(self):
        for partido in self.partidos:
            partido.simular()

            partido.penales_equipo1 = 0
            partido.penales_equipo2 = 0

            if partido.goles_equipo1 == partido.goles_equipo2:
                penales1 = random.randint(2, 5)
                penales2 = random.randint(2, 5)

                while penales1 == penales2:
                    penales1 = random.randint(2, 5)
                    penales2 = random.randint(2, 5)

                partido.penales_equipo1 = penales1
                partido.penales_equipo2 = penales2

        return "La fase se jugó"

    """
    Nombre: mostrar_juegos
    Entradas: No hay  
    Salidas: resultado de todos los partidos de la fase  
    Restricciones: 
    """
    def mostrar_juegos(self):
        resultado = f"Resultados de {self.nombre_fase}"

        for partido in self.partidos:
            resultado += f"\n{partido.mostrar_resultado()}"

            if partido.penales_equipo1 > 0 or partido.penales_equipo2 > 0:
                resultado += f" (Penales: {partido.penales_equipo1}-{partido.penales_equipo2})"

        return resultado
    
    """
    Nombre: obtener_clasificados
    Entradas: No hay 
    Salidas: Retrona la lista de equipos ganadores que avanzan a la otra fase 
    Restricciones:
    """
    def obtener_clasificados(self):
        clasificados = []

        for partido in self.partidos:
            if partido.goles_equipo1 > partido.goles_equipo2:
                clasificados += [partido.equipo_1]

            elif partido.goles_equipo2 > partido.goles_equipo1:
                clasificados += [partido.equipo_2]

            else:
                if partido.penales_equipo1 > partido.penales_equipo2:
                    clasificados += [partido.equipo_1]
                else:
                    clasificados += [partido.equipo_2]

        return clasificados
   
"""
Nombre: class Mundial
Entradas: 
Salidas:  constructor,registrar_pais,registrar_seleccion,crear_grupos,contar_selecciones,jugar_fase_grupos,contar_lista,armar_fase_eliminatoria,jugar_fase_eliminatoria,
determinar_campeon,mostrar_tabla_general,generar_reporte
Restricciones:
"""
class Mundial():
    def __init__(self,nombre,anio):
        if not isinstance(nombre,str):
            raise TypeError("Error: El nombre del torneo debe ser un texto")
        if not isinstance(anio,int):
            raise TypeError("Error:El año del torneo debe ser un número entero")

        self.nombre = nombre
        self.anio = anio
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    """
    Nombre: registrar_pais
    Entradas:pais  
    Salidas:  Mensaje de que se registro un pais
    Restricciones:
    """
    def registrar_pais(self,pais):
        if not isinstance(pais,Pais):
            return "Error: Debe registrar un objeto de la clase pais"

        self.paises += [pais]

        return "Se registró un país"

    """
    Nombre: registrar_seleccion
    Entradas:  seleccion
    Salidas: Mensaje de que se registro una seleccion 
    Restricciones:
    """
    def registrar_seleccion(self, seleccion):
        if not isinstance(seleccion,Seleccion):
            return "Error: Debe registrar un objeto de la clase seleccion"

        self.selecciones += [seleccion]

        return "Se registró una selección"

    """
    Nombre: crear_grupos
    Entradas:  cantidad_grupos
    Salidas:  Mensaje de que los grupos con los equipos se crearon correctamente 
    Restricciones: cantidad_grupos debe ser int,cantidad_grupos debe ser mayor a 0 y debe haber minimo 1 seleccion registrada 
    """
    def crear_grupos(self,cantidad_grupos):
        if not isinstance(cantidad_grupos, int):
            return "Error: La cantidad de grupos debe ser un número entero"

        if cantidad_grupos <= 0:
            return "Error: La cantidad de grupos debe ser mayor a 0"

        if self.contar_selecciones() == 0:
            return "Error: No hay selecciones registradas"

        letras = ["A", "B", "C", "D", "E", "F", "G", "H"]

        contador = 0

        while contador < cantidad_grupos:
            grupo = Grupo("Grupo " + letras[contador])
            self.grupos += [grupo]
            contador += 1

        indice_grupo = 0

        for seleccion in self.selecciones:
            self.grupos[indice_grupo].agregar_equipo(seleccion)

            indice_grupo += 1

            if indice_grupo == cantidad_grupos:
                indice_grupo = 0

        return "Grupos creados correctamente"

    """
    Nombre: contar_selecciones
    Entradas: No hay  
    Salidas:  cantidad de cuantas selecciones hay
    Restricciones:
    """
    def contar_selecciones(self):
        contador = 0

        for seleccion in self.selecciones:
            contador += 1

        return contador

    """
    Nombre: jugar_fase_grupos
    Entradas:  No hay
    Salidas:  Mensaje que confirma que se jugo la fase de grupos
    Restricciones:
    """
    def jugar_fase_grupos(self):
        for grupo in self.grupos:
            grupo.jugar_partidos()

        return "La fase de grupos se jugó"


    """
    Nombre:contar_lista 
    Entradas:  lista
    Salidas:  contador de elementos en una lista
    Restricciones:
    """
    def contar_lista(self, lista):
        contador = 0

        for elemento in lista:
            contador += 1

        return contador
    
    """
    Nombre: armar_fase_eliminatoria
    Entradas:nombre_fase,clasificados
    Salidas: una fase eliminatoria que organiza las selecciones clasificadas en parejas, registra un partido entre cada pareja,
    guarda la fase en el Mundial y devuelve la fase creada.
    Restricciones:
    """
    def armar_fase_eliminatoria(self,nombre_fase,clasificados):
        fase = Fase(nombre_fase)
        
        i = 0
        cantidad =  self.contar_lista(clasificados)

        while i < cantidad:
            fase.registrar_juego(clasificados[i], clasificados[i + 1])
            i += 2

        self.fases += [fase]

        return fase

    """
    Nombre: jugar_fase_eliminatoria
    Entradas:fase  
    Salidas: Retorna los clasificados a la siguiente ronda 
    Restricciones:
    """

    def jugar_fase_eliminatoria(self,fase):

        fase.jugar_fase()

        return fase.obtener_clasificados()

    """
    Nombre: determinar_campeon
    Entradas: No hay
    Salidas: Campeón del mundial
    Restricciones: No hay
    """
    def determinar_campeon(self):
        clasificados = []

        for grupo in self.grupos:
            equipos = grupo.obtener_clasificados()
            clasificados += equipos

        fase = self.armar_fase_eliminatoria("Octavos de Final", clasificados)
        clasificados = self.jugar_fase_eliminatoria(fase)

        fase = self.armar_fase_eliminatoria("Cuartos de Final", clasificados)
        clasificados = self.jugar_fase_eliminatoria(fase)

        fase = self.armar_fase_eliminatoria("Semifinal", clasificados)
        clasificados = self.jugar_fase_eliminatoria(fase)

        fase = self.armar_fase_eliminatoria("Final", clasificados)
        clasificados = self.jugar_fase_eliminatoria(fase)

        self.campeon = clasificados[0]

        return "El campeón es: " + self.campeon.pais.nombre

    """
    Nombre: mostrar_tabla_general 
    Entradas: No hay
    Salidas: La tabla con las posiciones de todos los grupos
    Restricciones: No hay
    """

    def mostrar_tabla_general(self):
        resultado = ""
        
        for grupo in self.grupos:
            resultado += grupo.mostrar_tabla()
            resultado += "\n\n"

        return resultado

    """
    Nombre: generar_reporte
    Entradas: No hay
    Salidas: Mensaje que indica que el reporte se generó
    Restricciones: No hay
    """
    def generar_reporte(self):
        resultado = ""

        resultado += "REPORTE DEL MUNDIAL\n"
        resultado += f"Nombre: {self.nombre}\n"
        resultado += f"Año: {self.anio}\n\n"

        resultado += "TABLAS DE POSICIONES\n\n"
        resultado += self.mostrar_tabla_general()

        resultado += "\nFASES ELIMINATORIAS\n\n"

        for fase in self.fases:
            resultado += fase.mostrar_juegos()
            resultado += "\n\n"

        if self.campeon != None:
            resultado += f"Campeón: {self.campeon.pais.nombre}"
        else:
            resultado += "El campeón todavía no ha sido seleccionado"

        archivo = open("reporte_mundial.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Reporte generado"

###### ARCHIVOS TXT

    """
    Nombre: guardar_paises
    Entradas: No hay
    Salidas: Mensaje que indica que los países se guardaron
    Restricciones: No hay
    """
    def guardar_paises(self):
        resultado = ""

        for pais in self.paises:
            resultado += (f"{pais.codigo_fifa};"
                          f"{pais.nombre};"
                          f"{pais.continente};"
                          f"{pais.ranking_fifa}\n")

        archivo = open("paises.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Países guardados"

    """
    Nombre: cargar_paises
    Entradas: No hay
    Salidas: Mensaje que indica que lo países
    Restricciones: No hay
    """
    def cargar_paises(self):
        try:
            archivo = open("paises.txt", "r")
        except FileNotFoundError:
            return "El archivo paises.txt no existe"

        self.paises = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                pais = Pais(datos[0],datos[1],datos[2],int(datos[3]))

                self.paises += [pais]

        archivo.close()

        return "Países cargados"

    """
    Nombre: guardar_selecciones
    Entradas: No hay
    Salidas: Mensaje que confirma que las selecciones fueron guardadas
    Restricciones: No hay
    """
    def guardar_selecciones(self):
        resultado = ""

        for seleccion in self.selecciones:

            if seleccion.entrenador == None:
                nombre_entrenador = "None"
                apellido_entrenador = "None"
                fecha_nacimiento = "None"
                nacionalidad = "None"
                licencia = "None"
                experiencia = 0
                sistema_juego = "None"

            else:
                nombre_entrenador = seleccion.entrenador.nombre
                apellido_entrenador = seleccion.entrenador.apellido
                fecha_nacimiento = seleccion.entrenador.fecha_nacimiento
                nacionalidad = seleccion.entrenador.nacionalidad
                licencia = seleccion.entrenador.licencia
                experiencia = seleccion.entrenador.experiencia_anios
                sistema_juego = seleccion.entrenador.sistema_juego

            resultado += (f"{seleccion.codigo_equipo};"
                          f"{seleccion.pais.codigo_fifa};"
                          f"{nombre_entrenador};"
                          f"{apellido_entrenador};"
                          f"{fecha_nacimiento};"
                          f"{nacionalidad};"
                          f"{licencia};"
                          f"{experiencia};"
                          f"{sistema_juego};"
                          f"{seleccion.fuerza_equipo}\n")

        archivo = open("selecciones.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Selecciones guardadas"

    """
    Nombre: cargar_selecciones
    Entradas: No hay
    Salidas: Mensaje que confirma que las selecciones fueron cargadas
    Restricciones: Los países deben cargarse antes
    """
    def cargar_selecciones(self):
        try:
            archivo = open("selecciones.txt", "r")
        except FileNotFoundError:
            return "El archivo selecciones.txt no existe"

        self.selecciones = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                pais_encontrado = None

                for pais in self.paises:
                    if pais.codigo_fifa == datos[1]:
                        pais_encontrado = pais

                if pais_encontrado == None:
                    archivo.close()
                    return "Error: No se encontró el país de la selección"

                seleccion = Seleccion(datos[0], pais_encontrado)

                if datos[2] != "None":
                    entrenador = Entrenador(
                        datos[2],
                        datos[3],
                        datos[4],
                        datos[5],
                        datos[6],
                        int(datos[7]),
                        datos[8])

                    seleccion.asignar_entrenador(entrenador)

                seleccion.fuerza_equipo = float(datos[9])

                self.selecciones += [seleccion]

        archivo.close()

        return "Selecciones cargadas"

    """
    Nombre: guardar_jugadores
    Entradas: No hay
    Salidas: Mensaje que indica que los jugadores fueron guardados
    Restricciones: No hay
    """
    def guardar_jugadores(self):
        resultado = ""

        for seleccion in self.selecciones:
            for jugador in seleccion.jugadores:
                resultado += (f"{seleccion.codigo_equipo};"
                              f"{jugador.nombre};"
                              f"{jugador.apellido};"
                              f"{jugador.fecha_nacimiento};"
                              f"{jugador.nacionalidad};"
                              f"{jugador.dorsal};"
                              f"{jugador.posicion};"
                              f"{jugador.total_tarjetas_amarillas};"
                              f"{jugador.total_tarjetas_rojas};"
                              f"{jugador.goles};"
                              f"{jugador.asistencias};"
                              f"{jugador.puntaje_individual}\n")

        archivo = open("jugadores.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Jugadores guardados"

    """
    Nombre: cargar_jugadores
    Entradas: No hay
    Salidas: Mensaje que indica que los jugadores fueron cargados
    Restricciones: Las selecciones deben cargarse primero
    """
    def cargar_jugadores(self):
        try:
            archivo = open("jugadores.txt", "r")
        except FileNotFoundError:
            return "El archivo jugadores.txt no existe"

        for seleccion in self.selecciones:
            seleccion.jugadores = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                seleccion_encontrada = None

                for seleccion in self.selecciones:
                    if seleccion.codigo_equipo == datos[0]:
                        seleccion_encontrada = seleccion

                if seleccion_encontrada == None:
                    archivo.close()
                    return "Error: No se encontró la selección del jugador"

                jugador = Futbolista(
                    datos[1],
                    datos[2],
                    datos[3],
                    datos[4],
                    int(datos[5]),
                    datos[6],
                    int(datos[7]),
                    int(datos[8]),
                    int(datos[9]),
                    int(datos[10]),
                    int(datos[11]))

                seleccion_encontrada.agregar_jugador(jugador)

        archivo.close()

        return "Jugadores cargados"

    """
    Nombre: guardar_partidos
    Entradas: No hay
    Salidas: Mensaje que indica que los partidos fueron guardados
    Restricciones: No hay
    """
    def guardar_partidos(self):
        resultado = ""

        for grupo in self.grupos:
            for partido in grupo.partidos:
                resultado += (f"GRUPO;"
                              f"{grupo.nombre_grupo};"
                              f"{partido.id_partido};"
                              f"{partido.equipo_1.codigo_equipo};"
                              f"{partido.equipo_2.codigo_equipo};"
                              f"{partido.goles_equipo1};"
                              f"{partido.goles_equipo2};"
                              f"{partido.fecha}\n")

        for fase in self.fases:
            for partido in fase.partidos:
                resultado += (f"FASE;"
                              f"{fase.nombre_fase};"
                              f"{partido.id_partido};"
                              f"{partido.equipo_1.codigo_equipo};"
                              f"{partido.equipo_2.codigo_equipo};"
                              f"{partido.goles_equipo1};"
                              f"{partido.goles_equipo2};"
                              f"{partido.fecha}\n")

        archivo = open("partidos.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Partidos guardados"

    """
    Nombre: cargar_partidos
    Entradas: No hay
    Salidas: Mensaje que indica que los partidos fueron cargados
    Restricciones: Las selecciones deben cargarse primero
    """
    def cargar_partidos(self):
        try:
            archivo = open("partidos.txt", "r")
        except FileNotFoundError:
            return "El archivo partidos.txt no existe"

        self.grupos = []
        self.fases = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                tipo = datos[0]
                nombre = datos[1]
                id_partido = int(datos[2])

                equipo_1 = None
                equipo_2 = None

                for seleccion in self.selecciones:
                    if seleccion.codigo_equipo == datos[3]:
                        equipo_1 = seleccion

                    if seleccion.codigo_equipo == datos[4]:
                        equipo_2 = seleccion

                if equipo_1 == None or equipo_2 == None:
                    archivo.close()
                    return "Error: No se encontró una selección del partido"

                partido = Partido(
                    id_partido,
                    equipo_1,
                    equipo_2,
                    nombre,
                    datos[7])

                partido.goles_equipo1 = int(datos[5])
                partido.goles_equipo2 = int(datos[6])

                if tipo == "GRUPO":
                    grupo_encontrado = None

                    for grupo in self.grupos:
                        if grupo.nombre_grupo == nombre:
                            grupo_encontrado = grupo

                    if grupo_encontrado == None:
                        grupo_encontrado = Grupo(nombre)
                        self.grupos += [grupo_encontrado]

                    equipo_registrado = False

                    for equipo in grupo_encontrado.equipos:
                        if equipo == equipo_1:
                            equipo_registrado = True

                    if equipo_registrado == False:
                        grupo_encontrado.equipos += [equipo_1]

                    equipo_registrado = False

                    for equipo in grupo_encontrado.equipos:
                        if equipo == equipo_2:
                            equipo_registrado = True

                    if equipo_registrado == False:
                        grupo_encontrado.equipos += [equipo_2]

                    grupo_encontrado.partidos += [partido]

                if tipo == "FASE":
                    fase_encontrada = None

                    for fase in self.fases:
                        if fase.nombre_fase == nombre:
                            fase_encontrada = fase

                    if fase_encontrada == None:
                        fase_encontrada = Fase(nombre)
                        self.fases += [fase_encontrada]

                    fase_encontrada.partidos += [partido]

        archivo.close()

        return "Partidos cargados"
    """
    Nombre: guardar_ranking_goleadores
    Entradas: No hay
    Salidas: Mensaje que indica que el ranking fue guardado
    Restricciones: Deben existir jugadores registrados
    """
    def guardar_ranking_goleadores(self):
        jugadores = []

        for seleccion in self.selecciones:
            for jugador in seleccion.jugadores:
                jugadores += [[jugador, seleccion]]

        jugadores_ordenados = []
        cantidad = self.contar_lista(jugadores)
        contador = 0

        while contador < cantidad:
            mejor_jugador = None

            for fila in jugadores:
                if mejor_jugador == None:
                    mejor_jugador = fila

                elif fila[0].goles > mejor_jugador[0].goles:
                    mejor_jugador = fila

                elif fila[0].goles == mejor_jugador[0].goles:
                    if fila[0].puntaje_individual > mejor_jugador[0].puntaje_individual:
                        mejor_jugador = fila

            jugadores_ordenados += [mejor_jugador]

            lista_nueva = []

            for fila in jugadores:
                if fila != mejor_jugador:
                    lista_nueva += [fila]

            jugadores = lista_nueva
            contador += 1

        resultado = ""
        posicion = 1

        for fila in jugadores_ordenados:
            jugador = fila[0]
            seleccion = fila[1]

            resultado += (f"{posicion};"
                          f"{jugador.nombre};"
                          f"{jugador.apellido};"
                          f"{seleccion.codigo_equipo};"
                          f"{jugador.goles};"
                          f"{jugador.puntaje_individual}\n")

            posicion += 1

        archivo = open("ranking_goleadores.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Ranking de goleadores guardado"

    """
    Nombre: cargar_ranking_goleadores
    Entradas: No hay
    Salidas: Lista con el ranking de goleadores
    Restricciones: Debe existir el archivo ranking_goleadores.txt
    """
    def cargar_ranking_goleadores(self):
        try:
            archivo = open("ranking_goleadores.txt", "r")
        except FileNotFoundError:
            return "El archivo ranking_goleadores.txt no existe"

        ranking = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                fila = [int(datos[0]),
                    datos[1],
                    datos[2],
                    datos[3],
                    int(datos[4]),
                    int(datos[5])]

                ranking += [fila]

        archivo.close()

        return ranking

    """
    Nombre: guardar_ranking_selecciones
    Entradas: No hay
    Salidas: Mensaje que indica que el ranking fue guardado
    Restricciones: 
    """
    def guardar_ranking_selecciones(self):
        selecciones = []

        for grupo in self.grupos:
            tabla = grupo.calcular_tabla()

            for fila in tabla:
                seleccion = fila[1]
                puntos = fila[2]
                diferencia = fila[5]

                selecciones += [[seleccion, puntos, diferencia]]

        selecciones_ordenadas = []
        cantidad = self.contar_lista(selecciones)
        contador = 0

        while contador < cantidad:
            mejor_seleccion = None

            for fila in selecciones:
                if mejor_seleccion == None:
                    mejor_seleccion = fila

                elif fila[1] > mejor_seleccion[1]:
                    mejor_seleccion = fila

                elif fila[1] == mejor_seleccion[1]:
                    if fila[2] > mejor_seleccion[2]:
                        mejor_seleccion = fila

            selecciones_ordenadas += [mejor_seleccion]

            lista_nueva = []

            for fila in selecciones:
                if fila != mejor_seleccion:
                    lista_nueva += [fila]

            selecciones = lista_nueva
            contador += 1

        resultado = ""
        posicion = 1

        for fila in selecciones_ordenadas:
            seleccion = fila[0]
            puntos = fila[1]
            diferencia = fila[2]

            resultado += (f"{posicion};"
                          f"{seleccion.codigo_equipo};"
                          f"{seleccion.pais.nombre};"
                          f"{puntos};"
                          f"{diferencia}\n")

            posicion += 1

        archivo = open("ranking_selecciones.txt", "w")
        archivo.write(resultado)
        archivo.close()

        return "Ranking de selecciones guardado"

    """
    Nombre: cargar_ranking_selecciones
    Entradas: No hay
    Salidas: Lista con el ranking de selecciones
    Restricciones: 
    """
    def cargar_ranking_selecciones(self):
        try:
            archivo = open("ranking_selecciones.txt", "r")
        except FileNotFoundError:
            return "El archivo ranking_selecciones.txt no existe"

        ranking = []

        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                datos = linea.split(";")

                fila = [int(datos[0]),
                datos[1],
                datos[2],
                int(datos[3]),
                int(datos[4])]

                ranking += [fila]

        archivo.close()

        return ranking
