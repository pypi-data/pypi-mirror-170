import pygame
import random as r
import keyboard as kb
import sys
import time as t
import datetime

pygame.init()
rect = []
clock = pygame.time.Clock()
pygame.display.set_caption('PyEasy Game Window')

last_time = t.time()

time = -10
frames = 60
screens = []
screen_sizes = []
camera = False
change_x = ''
change_y = ''
player_speed = 0
left_key = ''
right_key = ''
up_key = ''
down_key = ''

right_speed = 0
left_speed = 0
up_speed = 0
down_speed = 0

def collide(rect1, rect2, mouse_boolean=False, mouse_x=0, mouse_y=0):
    if not mouse_boolean:
        if 'playerx' not in rect1 and 'playery' not in rect1:
            if pygame.Rect(rect1).colliderect(pygame.Rect(rect2)):
                return True
        if 'playerx' in rect1 and 'playery' in rect1:
            if len(rect) >= 1:
                if rect[0].colliderect(pygame.Rect(rect2)):
                    return True
    if mouse_boolean:
        if 'playerx' not in rect1 and 'playery' not in rect1:
            if pygame.Rect(rect1).collidepoint((mouse_x, mouse_y)):
                return True
        if 'playerx' in rect1 and 'playery' in rect1:
            if len(rect) >= 1:
                if rect[0].collidepoint((mouse_x, mouse_y)):
                    return True
    pass

drawimg = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
button_click = ''

def button(image, xy,click='left', draw_button=True):
    mouse = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()
    br = list(xy)
    mouse = pygame.mouse.get_pressed()
    if draw_button:
        screens[0].blit(image, (br[0],br[1]))
        if len(screens) >= 1:
            if click == 'left':
                if pygame.Rect(br[0],br[1],image.get_width(),image.get_height()).collidepoint((mx,my)):
                    if mouse[0] == True:
                        return True
            if click == 'right':
                if pygame.Rect(br[0],br[1],image.get_width(),image.get_height()).collidepoint((mx,my)):
                    if mouse[2] == True:
                        return True
    pass

def pickup_item(image,xy,condition,pickup_value,camera=True,rect1=(0,0,0,0),rect2=(0,0,0,0)):
    mx,my = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    pir = list(xy)
    if drawimg[pickup_value - 1]:
        screens[0].blit(image, (pir[0],pir[1]))
        if condition == 'Player' or 'player' or 'PLAYER':
            if pygame.Rect(pir[0],pir[1],image.get_width(), image.get_height()).colliderect(rect[0]):
                drawimg[pickup_value - 1] = False
                return True 
        if condition == 'Mouse' or 'mouse' or 'MOUSE':
            if pygame.Rect(pir[0],pir[1],image.get_width(),image.get_height()).collidepoint((mx,my)):
                if mouse[0]:
                    drawimg[pickup_value - 1] = False
                    return True
        if condition == 'Other' or 'other' or 'OTHER':
            if pygame.Rect(rect1).colliderect(pygame.Rect(rect2)):
                drawimg[pickup_value - 1] = False
                return True
pass

def player_pos(xy,change_xy=False,value=0):
    if xy != '':
        if not change_xy:
            if xy == 'x':
                return rect[0].x
            if xy == 'y':
                return rect[0].y
        if change_xy:
            if xy == 'x':
                rect[0].x = value
            if xy == 'y':
                rect[0].y = value
    # if rect[0].x < 0:
    #     rect[0].x = 0
    # if rect[0].x + rect[0].width > screen_sizes[0]:
    #     rect[0].x = screen_sizes[0] - rect[0].width
    # if rect[0].y < 0:
    #     rect[0].y = 0
    # if rect[0].y + rect[0].height > screen_sizes[1]:
    #     rect[0].y = screen_sizes[1] - rect[0].height
    pass

def insert_text(text,font,color,x,y,show_text=False, variable_boolean=False, variable=0):
    if variable_boolean == False:
        screens[0].blit(font.render(text, show_text, color), (x,y))
    if variable_boolean:
        screens[0].blit(font.render(text + str(variable), show_text, color), (x,y))
    pass

run_once = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
def timer(stop_time,start=True,timer_value=1):
    global start_ticks,timerTime
    if start:
        if run_once[timer_value - 1]:
            start_ticks = pygame.time.get_ticks()
            run_once[timer_value - 1] = False
        timerTime = float((pygame.time.get_ticks()-start_ticks)/1000)
        if timerTime >= stop_time:
            timerTime = stop_time
        return timerTime
    if not start:
        return timerTime
    pass

# current_time = int(t.time())

# def timer(stop_time,start=True):
#     if start:
#         time_now = int(t.time()) # Gets time during the timer's running
#         if time_now >= current_time + stop_time:
#             time_now = stop_time
#         if int(str(time_now)[-3:]) >= int(str(current_time)[-3:]):
#             print(int(str(time_now)[-3:]))
#             return (int(str(time_now)[-3:]) - int(str(current_time)[-3:]))
#     pass

# currentDT = datetime.datetime.now().second
# def timer(stop_time,start=True):
#     if start:
#         current_sec = datetime.datetime.now().second
#         actual_time = currentDT + stop_time
#         timerTime = current_sec - currentDT
#         if current_sec >= actual_time:
#             timerTime = stop_time
#         return timerTime          
#     pass

key_function_run = False

def create_screen(width, height, fullscreen=False, resizable=False):
    global key_function_run
    if len(screens) < 1:
        if not fullscreen:
            screen = pygame.display.set_mode((width,height))
            screens.append(screen)
            screen_sizes.append(width)
            screen_sizes.append(height)
        if not resizable:
            screen = pygame.display.set_mode((width,height))
            screens.append(screen)
            screen_sizes.append(width)
            screen_sizes.append(height)
        if fullscreen:
            screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0],pygame.FULLSCREEN)
            screens.append(screen)
            screen_sizes.append(width)
            screen_sizes.append(height)
        if resizable:
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            screens.append(screen)
            screen_sizes.append(width)
            screen_sizes.append(height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pass

boxes = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
run_once_box = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
col_right = False
col_left = False
col_up = False
col_down = False
camera_pos = []

def Rect(x,y,width,height):
    return pygame.Rect(x,y,width,height)

def collision_box(image,xy,collision=True,box_value=0):
    global col_up,col_down,col_left,col_right,right_speed,up_speed,down_speed,left_speed,right_speed,up_speed,down_speed,change_x,change_y, left_key,down_key,up_key,right_key
    cbxr = list(xy)
    if run_once_box[box_value -1]:
        boxes[box_value-1] = pygame.Rect(cbxr[0],cbxr[1],image.get_width(),image.get_height())
        run_once_box[box_value -1] = False
    col_box = pygame.Rect(list(boxes[box_value-1])[0],list(boxes[box_value-1])[1],image.get_width(), image.get_height())
    if collision:
        if not camera:
            if rect[0].colliderect(col_box):
                if rect[0].right >= col_box.x and rect[0].right <= col_box.x + (player_speed + 2) :
                    rect[0].x = col_box.x - rect[0].width
                if rect[0].left >= col_box.right - (player_speed + 2) and rect[0].left <= col_box.right:
                    rect[0].x = col_box.right
                if rect[0].top <= col_box.bottom and rect[0].top >= col_box.bottom - (player_speed + 2):
                    rect[0].y = col_box.bottom
                if rect[0].bottom >= col_box.top and rect[0].bottom <= col_box.top + (player_speed + 2):
                    rect[0].y = col_box.top - rect[0].height
        if camera:
            if rect[0].colliderect(col_box):
                if rect[0].right >= col_box.x and rect[0].right <= col_box.x + (player_speed + 2):
                    boxes[box_value - 1].x = rect[0].right
                if rect[0].left >= col_box.right - (player_speed + 2) and rect[0].left <= col_box.right:
                    boxes[box_value - 1].x  = rect[0].left - boxes[box_value - 1].width
                if rect[0].top <= col_box.bottom and rect[0].top >= col_box.bottom - (player_speed + 2):
                    boxes[box_value - 1].y = rect[0].top - boxes[box_value - 1].height
                if rect[0].bottom >= col_box.top and rect[0].bottom <= col_box.top + (player_speed + 2):
                    boxes[box_value - 1].y = rect[0].y + rect[0].height
    if change_x == 'x-':
        boxes[box_value - 1].x += player_speed
    if change_x == 'x+':
        boxes[box_value - 1].x -= player_speed
    if change_y == 'y-':
        boxes[box_value - 1].y += player_speed
    if change_y == 'y+':
        boxes[box_value - 1].y -= player_speed
    screens[0].blit(image, boxes[box_value - 1])
    pass

def fill_screen(red,green,blue):
    if len(screens) >= 1:
        screens[0].fill((red,green,blue))
    pass

def set_name(name):
    pygame.display.set_caption(name)
    pass

def set_icon(image):
    pygame.display.set_icon(image)
    pass

images = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
run_once2 = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]

def draw_image(image, xy, camera=False,image_value=0,draw_img=True):
    global player_speed, change_x,change_y, run_once2
    img_rect = list(xy)
    if camera:
        if run_once2[image_value -1]:
            images[image_value-1] = pygame.Rect(img_rect[0],img_rect[1],image.get_width(),image.get_height())
            run_once2[image_value -1] = False
    if camera:
        if draw_img:
            if len(screens) >= 1:
                screens[0].blit(image, (images[image_value-1].x,images[image_value-1].y))
    if not camera:
        if draw_img:
            if len(screens) >= 1:
                screens[0].blit(image, xy)
    if camera:
        if change_x == 'x-':    
            images[image_value -1].x += player_speed
        if change_x == 'x+':
            images[image_value -1].x -= player_speed
        if change_y == 'y-':
            images[image_value -1].y += player_speed
        if change_y == 'y+':
            images[image_value -1].y -= player_speed
    pass

def set_fps(fps):
    global frames
    frames = fps
    pass

rects = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
run_once4 = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]

def draw_rect(xy,width,height,color,draw_rect=True,camera=False,rect_value=0,radius_boolean=False, radius_value=0):
    global change_x,change_y
    rect_rect = list(xy)
    if camera:
        if run_once4[rect_value -1]:
            rects[rect_value-1] = pygame.Rect(rect_rect[0],rect_rect[1],width,height)
            run_once4[rect_value -1] = False
        if draw_rect:
            if len(screens) >= 1:
                if radius_boolean == False:
                    pygame.draw.rect(screens[0], color, (rects[rect_value - 1].x,rects[rect_value - 1].y,width,height))
                if radius_boolean:
                    pygame.draw.rect(screens[0], color, (rects[rect_value - 1].x,rects[rect_value - 1].y,width,height), radius_value)
    if not camera:
        if draw_rect:
            if len(screens) >= 1:
                if radius_boolean == False:
                    pygame.draw.rect(screens[0], color, (rect_rect[0],rect_rect[1],width,height))
                if radius_boolean:
                    pygame.draw.rect(screens[0], color, (rect_rect[0],rect_rect[1],width,height), radius_value)
    if camera:
        if change_x == 'x-':
            rects[rect_value - 1].x += player_speed
        if change_x == 'x+':
            rects[rect_value - 1].x -= player_speed
        if change_y == 'y-':
            rects[rect_value - 1].y += player_speed
        if change_y == 'y+':
            rects[rect_value - 1].y -= player_speed
    pass

def resize(image, new_width, new_height):
    return pygame.transform.scale(image, (new_width, new_height))
    pass

player_width = 0
player_height = 0
jumped = False
jump_velocity = 0
run_once3 = True
run_once6 = True

def player(image,xy,move_left='a',move_right='d',move_up='w',move_down='s',jump='space',speed=3,jump_height=20, collide_sides=False, sticky_keys=True, camera_follower=False):
    image_player = None
    global col_up,col_down,col_left,col_right,right_speed,left_speed,up_speed,down_speed,left_key,up_key,down_key,jump_velocity, left_key,right_key,up_key,down_key,run_once6,run_once3,jumped, time, last_time, camera,change_x,player_speed,change_y
    dt = t.time() - last_time
    dt *= frames
    last_time = t.time()
    player_speed = speed
    player_rect = list(xy)
    if camera_follower:
        camera = True
    if run_once6:
        jump_velocity = jump_height
        left_key = move_left
        right_key = move_right
        up_key = move_up
        down_key = move_down
        right_speed = speed
        left_speed = speed
        up_speed = speed
        down_speed = speed
        run_once6 = False
    if move_left != '':
        if kb.is_pressed(move_left) != True:
            change_x = ''
    if move_right != '':
        if kb.is_pressed(move_right) != True:
            change_x = ''
    if move_up != '':
        if kb.is_pressed(move_up) != True:
            change_y = ''
    if move_down != '':
        if kb.is_pressed(move_down) != True:
            change_y = ''
    if len(screens) >= 1:
        player_width = image.get_width()
        player_height = image.get_height()
        if run_once3:
            rect.append(pygame.Rect(player_rect[0],player_rect[1],image.get_width(),image.get_height()))
            run_once3 = False
        image_player = image
        if jump != '':
            if jumped == False and kb.is_pressed(jump):
                jumped = True
        if camera_follower:
            if sticky_keys:
                if collide_sides == False:
                    if move_left != '':
                        if kb.is_pressed(move_left):
                            if not col_left:
                                change_x = 'x-'
                    if move_right != '':
                        if kb.is_pressed(move_right):
                            if not col_right:
                                change_x = 'x+'
                    if move_up != '':
                        if kb.is_pressed(move_up):
                            if not col_up:
                                change_y = 'y-'
                    if move_down != '':
                        if kb.is_pressed(move_down):
                            if not col_down:
                                change_y = 'y+'
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < -jump_height:
                                jumped = False
                                jump_velocity = jump_height
                if collide_sides == True:
                    if move_left != '':
                        if kb.is_pressed(move_left) and rect[0].x >= 0:
                            if not col_left:
                                change_x = 'x-'
                    if move_right != '':
                        if kb.is_pressed(move_right) and rect[0].x <= screen_sizes[0] - player_width:
                            if not col_right: 
                                change_x = 'x+'
                    if move_up != '':
                        if kb.is_pressed(move_up) and rect[0].y >= 0:
                            if not col_up:
                                change_y = 'y-'
                    if move_down != '':
                        if kb.is_pressed(move_down) and rect[0].y <= screen_sizes[1] - player_height:
                            if not col_down:
                                change_y = 'y+'
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                    if rect[0].x < 0:
                        rect[0].x = 0
                    if rect[0].x + rect[0].width > screen_sizes[0]:
                        rect[0].x = screen_sizes[0] - rect[0].width
                    if rect[0].y < 0:
                        rect[0].y = 0
                    if rect[0].y + rect[0].height > screen_sizes[1]:
                        rect[0].y = screen_sizes[1] - rect[0].height
            if not sticky_keys:
                if collide_sides == False:
                    if move_left != '':
                        if kb.is_pressed(move_left):
                            if kb.is_pressed(move_right) != True and kb.is_pressed(move_up) != True and kb.is_pressed(move_down) != True:
                                if not col_left:
                                    change_x = 'x-'
                    if move_right != '' :
                        if kb.is_pressed(move_right):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                if not col_right:
                                    change_x = 'x+'
                    if move_up != '':
                        if kb.is_pressed(move_up):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_right) != True  and kb.is_pressed(move_down) != True:
                                if not col_up:
                                    change_y = 'y-'
                    if move_down != '':
                        if kb.is_pressed(move_down):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_right) != True:
                                if not col_down:
                                    change_y = 'y+'
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                if collide_sides == True:
                    if move_left != '':
                        if kb.is_pressed(move_left) and rect[0].x >= 0:
                            if kb.is_pressed(move_right) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                if not col_left:
                                    change_x = 'x-'
                    if move_right != '':
                        if kb.is_pressed(move_right) and rect[0].x <= screen_sizes[0] - player_width:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                if not col_right:
                                    change_x = 'x+' 
                    if move_up != '':
                        if kb.is_pressed(move_up) and rect[0].y >= 0:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_right) != True  and kb.is_pressed(move_down) != True:
                                if not col_up:
                                    change_y = 'y-'
                    if move_down != '':
                        if kb.is_pressed(move_down) and rect[0].y <= screen_sizes[1] - player_height:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_right) != True:
                                if not col_down:
                                    change_y = 'y+'
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                    if rect[0].x < 0:
                        rect[0].x = 0
                    if rect[0].x + rect[0].width > screen_sizes[0]:
                        rect[0].x = screen_sizes[0] - rect[0].width
                    if rect[0].y < 0:
                        rect[0].y = 0
                    if rect[0].y + rect[0].height > screen_sizes[1]:
                        rect[0].y = screen_sizes[1] - rect[0].height
        if not camera_follower:
            if sticky_keys:
                if collide_sides == False:
                    if move_left != '':
                        if kb.is_pressed(move_left):
                            rect[0].x -= left_speed * dt
                    if move_right != '':
                        if kb.is_pressed(move_right):
                            rect[0].x += right_speed * dt 
                    if move_up != '':
                        if kb.is_pressed(move_up):
                            rect[0].y -= up_speed * dt
                    if move_down != '':
                        if kb.is_pressed(move_down):
                            rect[0].y += down_speed * dt
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                if collide_sides == True:
                    if move_left != '':
                        if kb.is_pressed(move_left) and rect[0].x >= 0:
                            rect[0].x -= left_speed * dt
                    if move_right != '':
                        if kb.is_pressed(move_right) and rect[0].x <= screen_sizes[0] - player_width:
                            rect[0].x += right_speed * dt 
                    if move_up != '':
                        if kb.is_pressed(move_up) and rect[0].y >= 0:
                            rect[0].y -= up_speed * dt
                    if move_down != '':
                        if kb.is_pressed(move_down) and rect[0].y <= screen_sizes[1] - player_height:
                            rect[0].y += down_speed * dt
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                    if rect[0].x < 0:
                        rect[0].x = 0
                    if rect[0].x + rect[0].width > screen_sizes[0]:
                        rect[0].x = screen_sizes[0] - rect[0].width
                    if rect[0].y < 0:
                        rect[0].y = 0
                    if rect[0].y + rect[0].height > screen_sizes[1]:
                        rect[0].y = screen_sizes[1] - rect[0].height
            if not sticky_keys:
                if collide_sides == False:
                    if move_left != '':
                        if kb.is_pressed(move_left):
                            if kb.is_pressed(move_right) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                rect[0].x -= left_speed * dt
                    if move_right != '' :
                        if kb.is_pressed(move_right):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                rect[0].x += right_speed * dt 
                    if move_up != '':
                        if kb.is_pressed(move_up):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_right) != True  and kb.is_pressed(move_down) != True:
                                rect[0].y -= up_speed * dt
                    if move_down != '':
                        if kb.is_pressed(move_down):
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up)  != True and kb.is_pressed(move_right) != True:
                                rect[0].y += down_speed * dt
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < -jump_height:
                                jumped = False
                                jump_velocity = jump_height
                if collide_sides == True:
                    if move_left != '':
                        if kb.is_pressed(move_left) and rect[0].x >= 0:
                            if kb.is_pressed(move_right) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                rect[0].x -= left_speed * dt
                    if move_right != '':
                        if kb.is_pressed(move_right) and rect[0].x <= screen_sizes[0] - player_width:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_down) != True:
                                rect[0].x += right_speed * dt 
                    if move_up != '':
                        if kb.is_pressed(move_up) and rect[0].y >= 0:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_right) != True  and kb.is_pressed(move_down) != True:
                                rect[0].y -= up_speed * dt
                    if move_down != '':
                        if kb.is_pressed(move_down) and rect[0].y <= screen_sizes[1] - player_height:
                            if kb.is_pressed(move_left) != True  and kb.is_pressed(move_up) != True  and kb.is_pressed(move_right) != True:
                                rect[0].y += down_speed * dt
                    if jump != '':
                        if jumped:
                            rect[0].y -= jump_velocity
                            jump_velocity -= 1
                            if jump_velocity < - jump_height:
                                jumped = False
                                jump_velocity = jump_height
                    if rect[0].x < 0:
                        rect[0].x = 0
                    if rect[0].x + rect[0].width > screen_sizes[0]:
                        rect[0].x = screen_sizes[0] - rect[0].width
                    if rect[0].y < 0:
                        rect[0].y = 0
                    if rect[0].y + rect[0].height > screen_sizes[1]:
                        rect[0].y = screen_sizes[1] - rect[0].height
        if jump == '':
            jump_velocity = jump_height
            jumped = False
        screens[0].blit(image_player, rect[0])
        pygame.time.delay(time)
    pass

def load_img(img_location):
    return pygame.image.load(img_location).convert_alpha()
    pass

def get_image_pos(image_value):
    return images[image_value - 1]
    pass

def lives(lives_image1, lives_image2, x,y,lives_amount,lives_amount2, draw_lives=True):
    if len(screens) >= 1:
        if draw_lives:
            for i in range(lives_amount2):
                screens[0].blit(lives_image2,(x + lives_image2.get_width() * i ,y))
            for i in range(lives_amount):
                screens[0].blit(lives_image1, (x + lives_image1.get_width() * i,y))
    # if len(screens) >= 1:
    #     if draw_lives:
    #         for i in range(lives_amount2):
    #             if i < lives_amount:
    #                 screens[0].blit(lives_image1,(x + lives_image1.get_width() * i,y,lives_image1.get_width(),lives_image1.get_height()))
    #             else:
    #                 screens[0].blit(lives_image2,(x + lives_image2.get_width() * i,y,lives_image2.get_width(),lives_image2.get_height()))
    if lives_amount <= 0:
        lives_amount = 0
    return lives_amount
    pass

def delay_time(time_delay):
    global time
    time = time_delay
    pass

def rotate_img(image, angle):
    return pygame.transform.rotate(image, angle)

def update_screen():
    global frames
    clock.tick(frames)
    pygame.display.flip()
    pass

keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space','1','2','3','4','5','6','7','8','9','0']
pygame_keys = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z,pygame.K_SPACE,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_0]
key_dict = dict(zip(keys, pygame_keys ))

def key_pressed(key_press,one_click =False):
    global key_function_run
    if one_click:
        key_function_run = True
    if not one_click:
        if kb.is_pressed(key_press):
            return True
    if one_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for i in range(len(keys)):
                if event.type == pygame.KEYDOWN:
                    if key_press == keys[i]:
                        if event.key == pygame_keys[i]:
                            return True

    pass

def get_fps():
    return clock.get_fps()

def render_font(font, size):
    return pygame.font.SysFont(font, size)
    pass

def mouse_pos(xy):
    mx,my = pygame.mouse.get_pos()
    if xy == 'x':
        return mx
    if xy == 'y':
        return my
    pass

def mouse_click(click):
    mouse = pygame.mouse.get_pressed()
    if click == 'left':
        if mouse[0] == True:
            return 'down'
        if mouse[0] == False:
            return 'up'
    if click == 'right':
        if mouse[2] == True:
            return 'down'
        if mouse[2] == False:
            return 'up'
    pass
