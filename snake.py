import pygame, sys, time, random

speed = 15

# tamaño de la ventana

tam_marco_x = 720
tam_marco_y = 480

comprobar_errores = pygame.init()

if(comprobar_errores[1] > 0):
    print("ERROR" + comprobar_errores[1])
else:
    print("Juego Iniciado")

# abrimos ventana del juego

pygame.display.set_caption("Juego Snake")
ventana_juego = pygame.display.set_mode((tam_marco_x, tam_marco_y))

# colores

negro = pygame.Color(0, 0, 0)
blanco = pygame.Color(255, 255, 255)
rojo = pygame.Color(255, 0, 0)
azul = pygame.Color(0, 0, 255)
verde = pygame.Color(0, 255, 0)


fps_controles = pygame.time.Clock()

# tamaño del cuadrado de la serpiente

tam_cuadro = 30

def init_vars():
    global pos_cabeza, cuerpo_serpiente, pos_comida, spawn_comida, puntos, direccion
    direccion = "RIGHT"
    pos_cabeza = [120, 60]
    cuerpo_serpiente = [[120, 60]]
    pos_comida = [random.randrange(1,(tam_marco_x // tam_cuadro)) * tam_cuadro,
                  random.randrange(1,(tam_marco_y // tam_cuadro)) * tam_cuadro]
    spawn_comida = True
    puntos = 0

init_vars()

def mostrar_puntos(choice, color, font, size):
    puntos_font = pygame.font.SysFont(font, size)
    puntos_surface = puntos_font.render("Puntos: " + str(puntos), True, color)
    puntos_rect = puntos_surface.get_rect()
    if choice == 1:
        puntos_rect.midtop = (tam_marco_x / 10, 15)
    else:
        puntos_rect.midtop = (tam_marco_x / 2, tam_marco_y / 1.25)

    ventana_juego.blit(puntos_surface, puntos_rect)

    
# bucle del juego

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ( event.key == pygame.K_UP or event.key == ord("w") and direccion
                and direccion != "DOWN"):
                direccion = "UP"
            elif ( event.key == pygame.K_DOWN or event.key == ord("s") and direccion
                and direccion != "UP"):
                direccion = "DOWN"
            elif ( event.key == pygame.K_LEFT or event.key == ord("a") and direccion
                and direccion != "RIGHT"):
                direccion = "LEFT"
            elif ( event.key == pygame.K_RIGHT or event.key == ord("d") and direccion
                and direccion != "LEFT"):
                direccion = "RIGHT"

    if direccion == "UP":
        pos_cabeza[1] -= tam_cuadro
    elif direccion == "DOWN":
        pos_cabeza[1] += tam_cuadro
    elif direccion == "LEFT":
        pos_cabeza[0] -= tam_cuadro
    else:
        pos_cabeza[0] += tam_cuadro

    if pos_cabeza[0] < 0:
        pos_cabeza[0] = tam_marco_x - tam_cuadro
    elif pos_cabeza[0] > tam_marco_x - tam_cuadro:
        pos_cabeza[0] = 0
    elif pos_cabeza[1] < 0:
        pos_cabeza[1] = tam_marco_y - tam_cuadro
    elif pos_cabeza[1] > tam_marco_y - tam_cuadro:
        pos_cabeza[1] = 0

    # comiendo una manzana

    cuerpo_serpiente.insert(0, list(pos_cabeza))
    if pos_cabeza[0] == pos_comida[0] and pos_cabeza[1] == pos_comida[1]:
        puntos += 1
        spawn_comida = False
    else:
        cuerpo_serpiente.pop()

    # spawn de la comida

    if not spawn_comida:
        pos_comida = [random.randrange(1,(tam_marco_x // tam_cuadro)) * tam_cuadro,
            random.randrange(1,(tam_marco_y // tam_cuadro)) * tam_cuadro]
        spawn_comida = True
    
    # efectos graficos

    ventana_juego.fill(negro)
    for pos in cuerpo_serpiente:
        pygame.draw.rect(ventana_juego, verde, pygame.Rect(
                        pos[0] + 2, pos[1] + 2,
                        tam_cuadro -2, tam_cuadro -2))
    
    pygame.draw.rect(ventana_juego, rojo, pygame.Rect(
                    pos_comida[0], pos_comida[1],
                    tam_cuadro, tam_cuadro))
    
    # condiciones para el game over

    for cuadro in cuerpo_serpiente[1:]:
        if pos_cabeza[0] == cuadro[0] and pos_cabeza[1] == cuadro[1]:
            init_vars()

    mostrar_puntos(1, blanco, "consolas", 20)
    pygame.display.update()
    fps_controles.tick(speed)

