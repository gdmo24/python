Moving Player Game — Práctica de Pygame

Es un juego de obstáculos. Hay un jugador que está en la parte de abajo y que esquiva objetos que van cayendo de arriba. Cada objeto tiene un tamaño y un color diferentes.

Gameplay

[Ver vídeo del juego](https://github.com/gdmo24/python/blob/main/2026-11-15%2018-01-02.mp4)

Cómo ejecutarlo

Primero probé a instalar Pygame con pip install pygame, pero me dio error. Al final lo instalé con py -m pip install pygame-ce y ya funcionó.

Para jugar, abro la terminal, entro en la carpeta del juego y escribo py .\main.py.

Controles
Flecha derecha: el jugador va a la derecha.
Flecha izquierda: el jugador va a la izquierda.
Flecha arriba: el jugador sube.
Flecha abajo: el jugador baja.
Tecla +: el jugador va más rápido.
Tecla -: el jugador va más lento.
ESC: pausa el juego. Si la vuelves a pulsar, sigue.
R: cuando pierdes, empiezas otra partida.
Archivos
config.py: tiene todas las constantes del juego (tamaños, colores, velocidades, tiempos).
player.py: es la clase Player, con el movimiento con flechas, los límites de pantalla y la vuelta a la posición inicial.
obstacle.py: es la clase Obstacle, con los obstáculos que caen.
main.py: es el bucle principal del juego.

En el código, cada reto está marcado con un comentario # Challenge N.

Retos realizados
1. Límites de pantalla

El jugador ya no puede salir de la ventana. Para ello se ha añadido el método keep_inside_screen() en la clase Player. Así, cada vez que el jugador se mueve, se revisan sus bordes y, si se ha salido por alguno, se le devuelve a la pantalla.

2. Tamaños aleatorios

Los obstáculos ya no tienen todos el mismo tamaño. Para ello, el tamaño se elige al azar entre 20 y 70 con random.randint(). Además, la posición horizontal se calcula teniendo en cuenta ese tamaño, así ningún obstáculo se sale por la derecha.

3. Colisión del segundo jugador

Lo he dejado con un solo jugador, es más jugable. La colisión se comprueba con colliderect(). Así, en cuanto un obstáculo toca al jugador, la partida se termina.

4. Pausa

El juego ya se puede pausar con ESC. Para ello se ha añadido la variable paused, que cambia de valor cada vez que se pulsa la tecla. Así, mientras está en pausa, el jugador y los obstáculos se quedan quietos y aparece el texto PAUSE en pantalla. Al quitar la pausa, el contador de obstáculos se reinicia para que no aparezca uno de golpe.

5. Reiniciar

Tras perder una partida se puede reiniciar el juego pulsando R. Así, la puntuación y el cronómetro vuelven a cero, se eliminan todos los obstáculos y el jugador vuelve a su posición inicial con reset_position().

6. Tiempo de supervivencia

También se cuenta el tiempo que aguanta el jugador usando pygame.time.get_ticks(), que mide los milisegundos que pasan entre un frame y otro. Así, el tiempo solo avanza mientras se está jugando: se para en pausa y en Game Over, y en pantalla se muestra en segundos.

7. Dificultad progresiva

El juego se vuelve más difícil a medida que se consiguen puntos. Para ello, cada 10 puntos se sube de nivel y los obstáculos aparecen 50 ms antes, con un mínimo de 150 ms. Así, la partida empieza un poco tranquila y cada vez va aumentando más la frecuencia de los obstáculos.

8. Cambiar velocidad

La velocidad del jugador se puede cambiar durante la partida. Para ello, con la tecla + se sube la velocidad y con - se baja, siempre entre 2 y 12. Cada pulsación cambia la velocidad una sola vez, y la velocidad actual se muestra en pantalla.

9. Récord de puntuación

El juego guarda la mejor puntuación. Para ello se ha añadido la variable high_score, que se actualiza cada vez que la puntuación la supera. Así, aunque se reinicie la partida, el récord se mantiene mientras el programa esté abierto, y se muestra junto a la puntuación.