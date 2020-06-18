import  pygame
import sys
import random
pygame.init()

clock = pygame.time.Clock()

Width = 800
Height = 500

red = (255, 0, 0)
background_color = (10, 240, 200)
blue = (0, 0, 255)
textcolor = (55, 25, 133)

player_size = 50
player_pos = [Width/2, Height-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, Width-enemy_size), 0]
enemy_list = [enemy_pos]
speed = 10
score = 0
dropped_enimies = 12


screen = pygame.display.set_mode((Width, Height))
game_over = False
myfont = pygame.font.SysFont("monospace", 35)
def set_level(score, speed):
    if score <20:
        speed = 5
    elif score <40:
        speed = 8
    elif score < 60:
        speed = 12
    else:
        speed = 15
    return speed



def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < dropped_enimies and delay < 0.1:
        x_pos = random.randint(0, Width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (blue), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size) )



def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < Height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_detect(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    px = player_pos[0]
    py = player_pos[1]

    ex = enemy_pos[0]
    ey = enemy_pos[1] 

    if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size)) or (py >= ey and py < (ey + enemy_size)):
                return True
        return False 


while not game_over:
    for event in pygame.event.get():      
        print (event)
        if event.type == pygame.QUIT:
            sys.exit()
        
        
        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key ==pygame.K_LEFT:
                x -= player_size-10
            elif event.key == pygame.K_RIGHT:
                x += player_size-10
            player_pos = [x, y]

    screen.fill((background_color))
    #oppdaaterer pos til enemy
    if enemy_pos[1] >= 0 and enemy_pos[1] < Height:
        enemy_pos[1] += speed
    else:
        enemy_pos[0] = random.randint(0, Width-enemy_size)
        enemy_pos[1] = 0


    drop_enemies(enemy_list)
    draw_enemies(enemy_list)

    score = update_enemy_positions(enemy_list, score)
    speed = set_level(score, speed)

    text = "score:" + str(score)
    label = myfont.render(text, 1, (textcolor))
    screen.blit(label, (Width-200, Height-40))
    
    if collision_detect(enemy_list, player_pos):
        game_over = True
    pygame.draw.rect(screen, (red), (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()
        
