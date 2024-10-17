
# general pygame setup

import pygame
import button

pygame.init()


screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Kebab Game 0.0")

# fonts

font1 = pygame.font.SysFont("Arial", 25)

# colours
black = (0, 0, 0)
white = (255, 255, 255)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

# load images

testbutton = pygame.image.load("images/testbutton.png").convert_alpha()
Lamb = pygame.image.load("images/Lamb.png").convert_alpha()
Chicken = pygame.image.load("images/Chicken.png").convert_alpha()
Lettuce = pygame.image.load("images/Lettuce.png").convert_alpha()
Chillis = pygame.image.load("images/Chillis.png").convert_alpha()
Tomato = pygame.image.load("images/Tomato.png").convert_alpha()
Onion = pygame.image.load("images/Onions.png").convert_alpha()
Cucumber = pygame.image.load("images/Cucumber.png").convert_alpha()
ChilliSauce = pygame.image.load("images/Chilli Sauce.png").convert_alpha()
Ketchup = pygame.image.load("images/Ketchup.png").convert_alpha()
GarlicMayo = pygame.image.load("images/Garlic Mayo.png").convert_alpha()
Wrap = pygame.image.load("images/Wrap.png").convert_alpha()
Pitta = pygame.image.load("images/Pitta.png").convert_alpha()
Chips = pygame.image.load("images/Chips.png").convert_alpha()
Red = pygame.image.load("images/Red.png").convert_alpha()
Green = pygame.image.load("images/Green.png").convert_alpha()
Submit = pygame.image.load("images/Submit.png").convert_alpha()
Green = pygame.transform.scale(Green, (25,25))
Red = pygame.transform.scale(Red, (25,25))

# create button instances
button1 = button.Button(50,55,Chicken,1)
button2 = button.Button(50,95,Lamb,1)
button3 = button.Button(50,175,Lettuce,1)
button4 = button.Button(50,215,Chillis,1)
button5 = button.Button(50,255,Cucumber,1)
button6 = button.Button(50,295,Onion,1)
button7 = button.Button(50,335,Tomato,1)
button8 = button.Button(50,415,Ketchup,1)
button9 = button.Button(50,455,ChilliSauce,1)
button10 = button.Button(50,495,GarlicMayo,1)
button11 = button.Button(50,575,Pitta,1)
button12 = button.Button(50,615,Wrap,1)
button13 = button.Button(50,655,Chips,1)
button14 = button.Button(650,775,Submit,1.1)

# variables for buttons on or off
b1 = 1
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
b11 = 1
b12 = 0
b13 = 0
sub = 0

# turn on or off buttons

def buttonschangeval():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,sub

    # check button 1
    if button1.draw(screen):
        if b1 == 0:
            b1 = 1
            if b2 == 1:
                b2 = 0

    #check button 2
    if button2.draw(screen):
        if b2 == 0:
            b2 = 1
            if b1 == 1:
                b1 = 0

    # check button3
    if button3.draw(screen):
        if b3 == 1:
            b3 = 0
        elif b3 == 0:
            b3 = 1

    # check button4
    if button4.draw(screen):
        if b4 == 1:
            b4 = 0
        elif b4 == 0:
            b4 = 1

    # check button5
    if button5.draw(screen):
        if b5 == 1:
            b5 = 0
        elif b5 == 0:
            b5 = 1

    # check button6
    if button6.draw(screen):
        if b6 == 1:
            b6 = 0
        elif b6 == 0:
            b6 = 1

    # check button7
    if button7.draw(screen):
        if b7 == 1:
            b7 = 0
        elif b7 == 0:
            b7 = 1

    # check button8
    if button8.draw(screen):
        if b8 == 1:
            b8 = 0
        elif b8 == 0:
            b8 = 1

    # check button9
    if button9.draw(screen):
        if b9 == 1:
            b9 = 0
        elif b9 == 0:
            b9 = 1

    # check button10
    if button10.draw(screen):
        if b10 == 1:
            b10 = 0
        elif b10 == 0:
            b10 = 1

    # check button11
    if button11.draw(screen):
        if b11 == 0:
            b11 = 1
            if b12 == 1:
                b12 = 0
            if b13 == 1:
                b13 = 0

    # check button12
    if button12.draw(screen):
        if b12 == 0:
            b12 = 1
            if b11 == 1:
                b11 = 0
            if b13 == 1:
                b13 = 0

    # check button13
    if button13.draw(screen):
        if b13 == 0:
            b13 = 1
            if b11 == 1:
                b11 = 0
            if b12 == 1:
                b12 = 0

    # check submit button
    if button14.draw(screen):
        if sub == 1:
            sub = 0
        elif sub == 0:
            sub = 1
# display text for buttons

def onofftext():
    global Green,Red
    if b1 == 1:
        screen.blit(Green, (155, 55))
    if b1 == 0:
        screen.blit(Red, (155, 55))
    if b2 == 1:
        screen.blit(Green, (155, 95))
    if b2 == 0:
        screen.blit(Red, (155, 95))
    if b3 == 1:
        screen.blit(Green, (155, 175))
    if b3 == 0:
        screen.blit(Red, (155, 175))
    if b4 == 1:
        screen.blit(Green, (155, 215))
    if b4 == 0:
        screen.blit(Red, (155, 215))
    if b5 == 1:
        screen.blit(Green, (155, 255))
    if b5 == 0:
        screen.blit(Red, (155, 255))
    if b6 == 1:
        screen.blit(Green, (155, 295))
    if b6 == 0:
        screen.blit(Red, (155, 295))
    if b7 == 1:
        screen.blit(Green, (155, 335))
    if b7 == 0:
        screen.blit(Red, (155, 335))
    if b8 == 1:
        screen.blit(Green, (155, 415))
    if b8 == 0:
        screen.blit(Red, (155, 415))
    if b9 == 1:
        screen.blit(Green, (155, 455))
    if b9 == 0:
        screen.blit(Red, (155, 455))
    if b10 == 1:
        screen.blit(Green, (155, 495))
    if b10 == 0:
        screen.blit(Red, (155, 495))
    if b11 == 1:
        screen.blit(Green, (155, 575))
    if b11 == 0:
        screen.blit(Red, (155, 575))
    if b12 == 1:
        screen.blit(Green, (155, 615))
    if b12 == 0:
        screen.blit(Red, (155, 615))
    if b13 == 1:
        screen.blit(Green, (155, 655))
    if b13 == 0:
        screen.blit(Red, (155, 655))
def lambchoice():
    score = 1
    if (b3 == 1 and b8 == 1 and b9 == 1 and b11 == 1 and b4 == 0
        and b5 == 0 and b6 == 0 and b7 == 0 and b10 == 0 and b12 == 0 and b13 == 0):
        return 10
    else:
        if b3 == 1:
            score += 1.75
        if b4 == 1:
            score += 0.75
        if b5 == 1:
            if b7 == 1:
                score -= 3
            else:
                score -= 1.5
        if b6 == 1:
            if b4 == 1:
                score += 1.25
            if b10 == 1:
                score += 0.75
            if b5 == 1:
                score -= 1.75
            else:
                score += 0.5
        if b7 == 1:
            score -= 1.75
            if b5 == 1:
                score += 2.5
        if b8 == 1:
            score += 1.25
        if b9 == 1:
            if b8 == 1:
                score += 2.5
        else:
            score += 1
        if b10 == 1:
            if b8 == 1:
                score -= 1
            else:
                score += 0.25
        if b11 == 1:
            score += 1.5
        if b12 == 1:
            score += 1
        if b13 == 1:
            score -= 0.5
        if b8 and b9 and b10 == 1:
            score = score-2
        if score > 10:
            score = 9.9
        return score

def chickenchoice():
    score = 0
    if b3 == 1:
        score += 1
    if b4 == 1:
        score -= 0.5
        if b5 == 1:
            score -= 1
        if b7 == 1:
            score += 1
        if b9 == 1:
            score += 0.75
    if b5 == 1:
        score -= 0.75
        if b7 == 1:
            score += 1
        if b9 == 1:
            score -= 2
    if b6 == 1:
        if b4 == 1:
            score += 0.75
            if b10 == 1:
                score += 1
    if b7 == 1:
        score -= 0.25
    if b8 == 1:
        if b9 == 1:
            score += 1.5
        score += 0.75
    if b9 == 1:
        if b11 == 1:
            score += 0.75
        if b8 == 1:
            score -= 0.75
    if b10 == 1:
        score += 1.75
    if b11 == 1:
        score += 1.25
    if b12 == 1:
        score += 0.5
    if b13 == 1:
        score -= 0.25
    if b8 and b9 and b10 == 1:
        score -= 2
    if not b8 and not b9 and not b10:
        score -= 3
    if b2 == 1:
        score += 1.25

    if score > 10:
        score == 9.5

    return score


def submitvals():
    global sub
    sub = 0
    score = 0
    if b1 == 1:
        score = chickenchoice()
    if b2 == 1:
        score = lambchoice()
    return score





# gameloop

txt = ""
run = True
while run:
    mainscreen = True
    # screen colour

    screen.fill((52,78,91))

    # buttons pressed turn on / off
    if mainscreen:
        # headers
        draw_text("Meats",font1,black,50,15)
        draw_text("Salad",font1,black,50,135)
        draw_text("Sauces",font1,black,50,375)
        draw_text("Bases",font1,black,50,535)

        # values of buttons on - off

        buttonschangeval()

        # if btn on / off, display text

        onofftext()
        if sub == 1:
            txt = str(submitvals())
        draw_text("Score: "+txt, font1, black,675 , 500)

    # event handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()