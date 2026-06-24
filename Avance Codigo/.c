//COdigo de Ping Pong en base del diagrama de flujp realizado en Raptopr##
//Posiciones Iniciales de la pelota, paletas de los jugadores y marcadores ambos en cero.
//la posicion de la pelota es en 50 por que la cancha va de "0 a 100". 
//de igual manera las dos paletas arrancan alineadas con el centro.
//Posiciiones iniciales : el centro de la cancha es 50, porque la
//cancha va de "0 a 100". Tanto la pelota como las dos paletas

posicion_pelota_x = 50
posicion_pelota_y = 50
posicion_paleta_derecha = 50
posicion_paleta_izquierda = 50
marcador_izquierda = 0
marcador_derecha = 0

//Aqui tenemos nuestro primer loop de confimarcion donde se repite  hasta que ambos jugadorres esten listo para jugar
  // y escriba  "si".

while True:
    inicia = input("¿Iniciar juego? (si/no): ")
    if inicia == "si":
        break    // Aqui tenemos un break ya que sin este el bucle nunca terminaria 
        // y solo ejecuta cuando  la condicion se cumpla en este es "si".   

// Ubicacion donde empieza la pelota y la velocidad con la que se mueve.
//lento y fácil; una velocidad alta lo hace más rápido y difícil. ---
    direccion_x = 1
    direccion_y = 1
    velocidad = 5     
  //La velocidad puede variar con una baja velocidad hace que 
   //el juego sea mas lento y facil, con una alta es mas dificil y rapido.

   //Tenemos el loop principal donde se haya el cuerpo del juego, 
  //donde se repite hasta que uno de los jugadores tenga el marcador tope.
  
while True:

//Movimiento del jugador 1 (paleta izquierda)
    movimiento_jugador1 = int(input("Movimiento del jugador 1 (numero entero, + sube/ - baja): "))
    posicion_paleta_izquierda = posicion_paleta_izquierda + movimiento_jugador1

  // Estos dos  evitan que la paleta se salga de la pantalla
  // (sin esto, la paleta podría terminar fuera de la cancha.
    
    if posicion_paleta_izquierda < 0:
        posicion_paleta_izquierda = 0
    if posicion_paleta_izquierda > 100:
        posicion_paleta_izquierda = 100

    // Movimiento del jugador 2 (paleta derecha) — misma logica
    movimiento_jugador2 = int(input("Movimiento del jugador 2 (numero entero, + sube/ - baja): "))
    posicion_paleta_derecha = posicion_paleta_derecha + movimiento_jugador2       

    if posicion_paleta_derecha < 0:
        posicion_paleta_derecha = 0
    if posicion_paleta_derecha > 100:
        posicion_paleta_derecha = 100

    posicion_pelota_x = posicion_pelota_x + direccion_x * velocidad
   
    posicion_pelota_y = posicion_pelota_y + direccion_y * velocidad

    //Rebote contra el techo o el piso (no afecta el marcador,
    // solo cambia la dirección vertical)
    if posicion_pelota_y <= 0 or posicion_pelota_y >= 100:
        direccion_y = direccion_y * -1

    //Esta es la parte mas importante de todo el juego,
    //¿la pelota llego al borde izquierdo?
    if posicion_pelota_x <= 0:

    // Si llego al borde, hay que revisar si la paleta
    //estaba ahi para devolverla. Se usa un margen de ±10
    //porque la paleta no cuenta como punto.
        if (posicion_pelota_y >= posicion_paleta_izquierda - 10 and
                posicion_pelota_y <= posicion_paleta_izquierda + 10):
            direccion_x = direccion_x * -1  # rebota entonce se sigue jugando.
          
        else:
            //SI la paleta no llego a tiempo: punto para el otro jugador
            marcador_derecha = marcador_derecha + 1
            posicion_pelota_x = 50
            posicion_pelota_y = 50
            direccion_x = 1


    // ¿llego al borde? (mismo razonamiento, en espejo) 
    elif posicion_pelota_x >= 100:
        if (posicion_pelota_y >= posicion_paleta_derecha - 10 and
                posicion_pelota_y <= posicion_paleta_derecha + 10):
            direccion_x = direccion_x * -1
          
        else:
            marcador_izquierda = marcador_izquierda + 1
            posicion_pelota_x = 50
            posicion_pelota_y = 50
            direccion_x = -1

    //La condicion para salida del loop es que uno los jugadores llegue al tope
    //del marcador que este es 2, se puede aumentar o disminuir.
      //alguien llega al puntaje maximo.
  
  
  if marcador_izquierda == 2 or marcador_derecha == 2:
        break
    
    //Aqui tenemos otro "break" cuando uno de los jugadores llegue al marcardor
    / / el juego da por terminador mostrandonos quien fue el jugador ganador.

if marcador_izquierda == 2:
    print("Gana jugador 1")
else:
    print("Gana jugador 2")
