#Proyector Integrador Evaluacion en Contacto con el Docente.
# Codigo de Ping-Pong con algunos añadidos:
# Version con velocidad progresiva.

posicion_pelota_x = 50
# Posicion horizontal de la pelota. Empieza en 50 porque la
# cancha va de 0 a 100, y 50 es justo el centro.
posicion_pelota_y = 50
# Posicion vertical de la pelota. Tambien centro (50), para que
# no salga ya inclinada hacia arriba o abajo desde el inicio.
posicion_paleta_derecha = 50
# Posicion vertical de la paleta derecha (jugador 2). Empieza
# alineada con la pelota, en el centro.
posicion_paleta_izquierda = 50
# Posicion vertical de la paleta izquierda (jugador 1). Misma
# manera: empieza en el centro.
marcador_izquierda = 0
marcador_derecha = 0
# Cuenta los puntos de ambos jugadores. Arranca en 0 porque nadie ha
# anotado todavia.

# Aqui tenemos nuestro primer loop de confimarcion donde se repite  hasta que ambos jugadorres esten listo para jugar
# y escriba  "si".
# LOOP DE CONFIRMACION: ¿ambos jugadores estan listos para jugar?

while True:
# "while True" repite para siempre el unico que puede detenerlo 
# es el "break" de abajo.    
    inicia = input("¿Iniciar juego? (si/no): ")
# Pregunta al usuario y guarda lo que escriba en la variable
# "inicia".  
    if inicia == "si":
# Comparamos contra el texto "si" exactamente. Si el
# usuario escribio otra cosa como "no", o con mayuscula
# "Si" esta comparacion es falsa y el loop se repite.
        break                                     
        # Rompe el bucle y ya se puede seguir con el resto del
        # programa.
# --- Dirección y velocidad inicial de la pelota ---
direccion_x = 1
direccion_y = 1
velocidad = 40
incremento_velocidad = 1   # cuánto sube la velocidad en cada rebote
velocidad_maxima = 100     # límite para que no se vuelva imposible        
while True:

#DIRECCION Y VELOCIDAD INICIAL DE LA PELOTA
# LOOP PRINCIPAL DEL JUEGO    
    
    # Movimiento del jugador 1 (paleta izquierda)
    movimiento_jugador1 = int(input("Movimiento del jugador 1 (numero entero, + sube/ - baja): "))

    # Pide un numero al jugador 1. El "int()" convierte el texto
    # que escribio en un número real, porque "input()" siempre
    # devuelve texto por defecto.
    posicion_paleta_izquierda = posicion_paleta_izquierda + movimiento_jugador1
    # Suma ese movimiento a la posicion actual de la paleta. Si
    # escribio un numero entero positivo, sube; si escribo numero negativo, 
    # baja.
    
    if posicion_paleta_izquierda < 0:
        posicion_paleta_izquierda = 0
        # Si por seguir presionando "bajar" la paleta quedo en un
        # número negativo, la regresamos a 0 (el borde de la
        # cancha). Sin esto, la paleta podría "desaparecer" fuera
        # de la pantalla.
    if posicion_paleta_izquierda > 100:
        posicion_paleta_izquierda = 100

    # Movimiento del jugador 2 (paleta derecha) es la misma logica que la del jugador 1.
    movimiento_jugador2 = int(input("Movimiento del jugador 2 (numero entero, + sube/ - baja): "))
    posicion_paleta_derecha = posicion_paleta_derecha + movimiento_jugador2       

    if posicion_paleta_derecha < 0:
        posicion_paleta_derecha = 0
    if posicion_paleta_derecha > 100:
        posicion_paleta_derecha = 100

    #MOVIMIENTO DE LA PELOTA
    posicion_pelota_x = posicion_pelota_x + direccion_x * velocidad
    # Avanza la pelota horizontalmente: direcciOn (1 o -1) por la
    # velocidad. Si direccion_x es -1 y velocidad es 5, esto resta
    # 5 a la posicion (se mueve a la izquierda).

    posicion_pelota_y = posicion_pelota_y + direccion_y * velocidad
    # Lo mismo, pero en el eje vertical.

    #REBORE CONTRA EL PISO O TECHO.
    if posicion_pelota_y <= 0 or posicion_pelota_y >= 100:
        direccion_y = direccion_y * -1
        # Si la pelota toco arriba o abajo de la cancha, se invierte
        # su direccion vertical. Multiplicar por -1 convierte un 1
        # en -1, y un -1 en 1 — así "rebota" en automatico.
    
    #¿LLEGO AL BORDE IZQUIERDO?
    if posicion_pelota_x <= 0:

        if (posicion_pelota_y >= posicion_paleta_izquierda - 10 and
                posicion_pelota_y <= posicion_paleta_izquierda + 10):
            # Revisamos si la altura de la pelota (y) esta cerca de
            # la altura de la paleta, con un margen de ±10 unidades.
            # Ese margen representa el "tamaño" de la paleta.
            
            direccion_x = direccion_x * -1  
            # La paleta si alcanzo la pelota: rebota, invirtiendo
            # la direccion horizontal.
            
            # VELOCIDAD PROGRESIVA
            if velocidad < velocidad_maxima:
                velocidad = velocidad + incremento_velocidad

        else:
        # La paleta NO estaba en la posición correcta: se anota el punto.    
            marcador_derecha = marcador_derecha + 1
            # El punto es para el jugador 2 (derecha), porque fue
            # el jugador 1 (izquierda) perdio.
            posicion_pelota_x = 50
            posicion_pelota_y = 50
            # Reiniciamos la pelota al centro de la cancha para empezar una nueva ronda.
            direccion_x = 1     
            # La mandamos de nuevo hacia la derecha hacia el
            # jugador que acaba de anotar, como en el Ping-Pong real.      
            velocidad = 40 
            # Se reinicia la velocidad al anotar un punto.
            print( "Punto para jugador 2 ")
            # Muestra el marcador actualizado en pantalla.
    
    # ¿LLEGO AL BORDE DERECHO?
    elif posicion_pelota_x >= 100:
        # "elif" significa que esto solo se revisa si la condicion
        # de arriba (borde izquierdo) fue falsa la pelota no
        # puede estar en los dos bordes a la vez.
        if (posicion_pelota_y >= posicion_paleta_derecha - 10 and
                posicion_pelota_y <= posicion_paleta_derecha + 10):
            direccion_x = direccion_x * -1
            
            # VELOCIDAD PROGRESIVA 
            # La velocidad va en aumento 
            if velocidad < velocidad_maxima:
                velocidad = velocidad + incremento_velocidad
        else:
            marcador_izquierda = marcador_izquierda + 1
            posicion_pelota_x = 50
            posicion_pelota_y = 50
            direccion_x = -1
            # La mandamos hacia la izquierda esta vez, porque el
            # jugador 1 fue quien gano.
            velocidad = 40 
            # Se reinicia la velocidad la anotar un punto.
            print ( "Punto para jugador 1")

    # ¿ALGUN JUGADOR CONSIGUIO LOS PUNTOS NECESARIOS?
    if marcador_izquierda == 2 or marcador_derecha == 2:
        # Revisa si cualquiera de los dos jugadores ya llego al
        # puntaje maximo 2, en este caso.
        break
    # Si se rompe el loop principal, el juego termina aqui.
    
# ANUCIAMOS AL GANADOR!
if marcador_izquierda == 2:
    print("Gana jugador 1")
    # Si el marcador izquierdo llego al puntaje maximo, 
    # gano el jugador 1.
else:
    print("Gana jugador 2")
    # Si no fue el izquierdo, por descarte tuvo que ser el derecho
    # (porque el "break" de arriba solo se activa cuando uno de
    # los dos llega a 3).