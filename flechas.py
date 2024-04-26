import sys
import pygame

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 300, 300
BLOCK_SIZE = WIDTH // 3

# Definir números en el tablero
numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, None]]  # None representa el espacio vacío

# Función para encontrar la posición del espacio vacío
def find_empty():
    for i in range(3):
        for j in range(3):
            if numbers[i][j] is None:
                return i, j

# Función para intercambiar dos fichas
def swap(row1, col1, row2, col2):
    numbers[row1][col1], numbers[row2][col2] = numbers[row2][col2], numbers[row1][col1]

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Deslizante")
clock = pygame.time.Clock()

# Ciclo principal del juego
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            row, col = find_empty()
            if event.key == pygame.K_LEFT and col < 2:
                swap(row, col, row, col + 1)
            elif event.key == pygame.K_RIGHT and col > 0:
                swap(row, col, row, col - 1)
            elif event.key == pygame.K_UP and row < 2:
                swap(row, col, row + 1, col)
            elif event.key == pygame.K_DOWN and row > 0:
                swap(row, col, row - 1, col)

    for i in range(3):
        for j in range(3):
            rect = pygame.Rect(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if numbers[i][j] is not None:
                font = pygame.font.SysFont(None, 50)
                text = font.render(str(numbers[i][j]), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)
