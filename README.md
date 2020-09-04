# juegoTorosVacas
Juego para practicar python

Es un Juego sencillo por consola
la idea es adivinar (o razonar) el número oculto que tiene en la memoria el ordenador
para ello hay unas reglas.

1. El ordenador eligirá un número de 4 dígitos que no empieza por cero: 
ejemplo: 1234, 5693, 4560, 1034
puede tener ceros en cualquier parte menos al inicio.

2. Los dígitos no se repiten:
bien: 1278 - 3857 -  1860
mal:  0925 - 1224 - 2792 (uno empieza en cero, en los otros se repite el 2)

3. El jugador deberá adivinar que número pensó la computadora, para ello escribirá un número de 4 dígitos al azar
con las mismas reglas explicadas: no se deben repetir los digitos, no puede empezar de cero.

4. La computadora devolverá la cantidad de VACAS: 
esta cantidad indica que ha acertado los dígitos, pero no están en su posición correcta
y también responderá TOROS: 
esta cantidad indica que ha acertado los dígitos y también ha acertado la posición que ocupa.
5. El número de intentos es 12 turnos. pero esta versión no tiene limites de seguir intentando adivinar.


ejemplo: 
computadora: eligé 2467 (pero está oculto, no lo podemos ver)
Jugador: tantea el número 1637
respuesta: 1 6 3 7  =>  1 TOROS .. 1 VACAS     "Hay un número que acertó y otro que está fuera de lugar"

Jugador: tantea el número 2857
respuesta: 2 8 5 7 =>  2 TOROS ..  0 VACAS      "Se acertó dos dígitos"

jugador: tantea el número 2647
respuesta: 2 6 4 7 =>  2 TOROS .. 2 VACAS       "2 y 7 se concluye puedan ser los toros y 6 con 4 las vacas, nos queda solo ordenar a 6 y 4"

jugador: tantea el número 2467
respuesta: "HAZ ACERTADO" (aún no tiene la memoria para saber las veces que se intentó adivinar el número)


