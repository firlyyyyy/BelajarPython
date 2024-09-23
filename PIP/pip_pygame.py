import pygame

# init
# input user, database input
# update asset
# render ke display

# 1. init
pygame.init()

# membuat display surface object
window = pygame.display.set_mode((1000, 1000))

# membuat objek game
# posisi
x = 500
y = 500

# ukuran
panjang = 30
lebar = 30

# kecepatan
kecepatan = 1

while True:

    # 2. user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # keyboard press
    keys = pygame.key.get_pressed()

    # gerak ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= kecepatan
    elif keys[pygame.K_RIGHT] and x < 1000 - panjang:
        x += kecepatan
    elif keys[pygame.K_UP] and y > 0:
        y -= kecepatan
    elif keys[pygame.K_DOWN] and y < 1000 - lebar:
        y += kecepatan

    # 3. update asset
    window.fill((34, 139, 35))
    pygame.draw.rect(window, (165, 42, 42), (x, y, lebar, panjang), (0), (100))

    # 4. render ke display
    pygame.display.update()
