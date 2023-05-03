import pygame,sys
from turtle import pos
import random

def liik():
    global posX3,posY3,sammX3,sammY3
    if posX3>=screenX-playerImage.get_rect().width or posX3<0:  # Оталкивание от стеноки по оси X
        sammX3=-sammX3

    if posY3>=screenY-playerImage.get_rect().height or posY3<0:  # вверх/вниз после косания нижней границы
        sammY3=-sammY3

    posX3+=sammX3
    posY3+=sammY3

    screen.blit(playerImage,(posX3,posY3))
    pygame.display.flip()
    screen.fill(fon)




while True:
        print("Vali:")
        print("1 - ez")
        print("2 - norm")
        print("3 - hard¤KOR")
        tegevust = int(input("Valige toiming: "))

        #print("Vali music:")
        #print("1 - ТЯГИ_1")
        #print("2 - at_remix_2")
        #print("3 - ONIMXRU_3")
        #tegevust2 = int(input("Valige toiming: "))
            


        if tegevust==1:
            #if tegevust2==1:
            #   pygame.mixer.music.load('music/Тяги.mp3')
            #   pygame.mixer.music.play(0)
            #   pygame.mixer.music.set_volume(0.5)
            #if tegevust2==2:
            #   pygame.mixer.music.load('music/at_remix.mp3')
            #   pygame.mixer.music.play(0)
            #   pygame.mixer.music.set_volume(0.5)
            #if tegevust2==3:
            #   pygame.mixer.music.load('music/ONIMXRU.mp3')
            #   pygame.mixer.music.play(0)
            #   pygame.mixer.music.set_volume(0.5)
            pygame.init()

            red=[255,0,0]
            blue=[0,0,255]
            lblue=[153,204,255]
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)

            fon=[r,g,b]

            screenX=640
            screenY=480
            screen=pygame.display.set_mode([screenX,screenY])
            pygame.display.set_caption("Animatsion")
            screen.fill(fon)
            clock=pygame.time.Clock()


            posX,posY=screenX/2, screenY/2

            posX2,posY2=screenX/2, screenY/2 #

            posX3, posY3 = 0, 0 ##

            sammX3,sammY3=2,2 ##


            speedY=0


            speedY2 =0 #

            speedX3, speedY3 = 3, 3 ##

            directionY=0 

            directionY2= 0 #
            player = pygame.Rect(posX3, posY3, 80, 40)
            playerImage = pygame.image.load("pin2.png")
            playerImage = pygame.transform.scale(playerImage, [player.width, player.height])
            posX3=screenX-playerImage.get_rect().width
            posY3=screenY-playerImage.get_rect().height

            enemies = []
            enemyCounter = 0
            totalenemies = 20
            score = 0
            gameover=False

            while not gameover:
                clock.tick(85)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover=True
                    elif event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_UP:
                            directionY="move_up"
       
                         elif event.key==pygame.K_DOWN:
                                directionY="move_down"
                
                         elif event.key==pygame.K_w:
                                directionY2="K_w"
       
                         elif event.key==pygame.K_s:
                                directionY2="K_s"
                


                    elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                          speedY=0

                        if event.key==pygame.K_w or event.key==pygame.K_s:
                            speedY2=0

                if directionY=="move_up":
                        if posY>0:
                            posY-=3
                elif directionY=="move_down":
                        if posY + 140 <screenY:
                            posY+=3
                if directionY2=="K_w":
                        if posY2>0:
                           posY2-=3
                elif directionY2=="K_s":
                        if posY2 + 140 <screenY:
                           posY2+=3
                events=pygame.event.get()
                for i in pygame.event.get():
                            sys.exit()
                liik()

                if posX3 > screenX - playerImage.get_rect().width or posX3 < 0:
        
                            if posY3 > 150 and posY3 < 368:
                               score += 1
                            print(score)

                if posY3 > screenY - playerImage.get_rect().height or posY3 < 0:
      
                            if posX3 > 150 and posX3 < 368:
                                score += 1
                                print(score)

                for enemy in enemies[:]:
                            if player.colliderect(enemy):
                                enemies.remove(enemy)
                                score += 1
                                print(score)

                ruut=pygame.draw.rect(screen,red,[610,posY,12,140],0,10)
                ruut2=pygame.draw.rect(screen,blue,[20,posY2,12,140],0,10)
            print(score)
            if score == 5:
               gameover = True
               
            pygame.display.flip()
            screen.fill(fon)
            pygame.quit
            break



        if tegevust==2:
            pygame.init()

            red=[255,0,0]
            blue=[0,0,255]
            lblue=[153,204,255]
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)

            fon=[r,g,b]

            screenX=640
            screenY=480
            screen=pygame.display.set_mode([screenX,screenY])
            pygame.display.set_caption("Animatsion")
            screen.fill(fon)
            clock=pygame.time.Clock()


            posX,posY=screenX/2, screenY/2

            posX2,posY2=screenX/2, screenY/2 #

            posX3, posY3 = 0, 0 ##

            sammX3,sammY3=2,2 ##


            speedY=0


            speedY2 =0 #

            speedX3, speedY3 = 3, 3 ##

            directionY=0 

            directionY2= 0 #
            player = pygame.Rect(posX3, posY3, 80, 40)
            playerImage = pygame.image.load("pin2.png")
            playerImage = pygame.transform.scale(playerImage, [player.width, player.height])
            posX3=screenX-playerImage.get_rect().width
            posY3=screenY-playerImage.get_rect().height

            enemies = []
            enemyCounter = 0
            totalenemies = 5
            score = 0
            gameover=False

            while not gameover:
                clock.tick(105)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover=True
                    elif event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_UP:
                            directionY="move_up"
       
                         elif event.key==pygame.K_DOWN:
                                directionY="move_down"
                
                         elif event.key==pygame.K_w:
                                directionY2="K_w"
       
                         elif event.key==pygame.K_s:
                                directionY2="K_s"
                


                    elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                          speedY=0

                        if event.key==pygame.K_w or event.key==pygame.K_s:
                            speedY2=0

                if directionY=="move_up":
                        if posY>0:
                            posY-=3
                elif directionY=="move_down":
                        if posY + 110 <screenY:
                            posY+=3
                if directionY2=="K_w":
                        if posY2>0:
                           posY2-=3
                elif directionY2=="K_s":
                        if posY2 + 110 <screenY:
                           posY2+=3
                events=pygame.event.get()
                for i in pygame.event.get():
                            sys.exit()
                liik()

                if posX3 > screenX - playerImage.get_rect().width or posX3 < 0:
        
                            if posY3 > 110 and posY3 < 368:
                               score += 1
                            print(score)

                if posY3 > screenY - playerImage.get_rect().height or posY3 < 0:
      
                            if posX3 > 110 and posX3 < 368:
                                score += 1
                                print(score)

                for enemy in enemies[:]:
                            if player.colliderect(enemy):
                                enemies.remove(enemy)
                                score += 1
                                print(score)
                ruut=pygame.draw.rect(screen,red,[610,posY,12,110],0,10)
                ruut2=pygame.draw.rect(screen,blue,[20,posY2,12,110],0,10)
            print(score)
            if score == 5:
                    gameover = True
            pygame.display.flip()
            screen.fill(fon)
            pygame.quit
            break


        if tegevust==3:
            pygame.init()

            red=[255,0,0]
            blue=[0,0,255]
            lblue=[153,204,255]
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)

            fon=[r,g,b]

            screenX=640
            screenY=480
            screen=pygame.display.set_mode([screenX,screenY])
            pygame.display.set_caption("Animatsion")
            screen.fill(fon)
            clock=pygame.time.Clock()


            posX,posY=screenX/2, screenY/2

            posX2,posY2=screenX/2, screenY/2 #

            posX3, posY3 = 0, 0 ##

            sammX3,sammY3=2,2 ##


            speedY=0


            speedY2 =0 #

            speedX3, speedY3 = 3, 3 ##

            directionY=0 

            directionY2= 0 #
            player = pygame.Rect(posX3, posY3, 80, 40)
            playerImage = pygame.image.load("pin2.png")
            playerImage = pygame.transform.scale(playerImage, [player.width, player.height])
            posX3=screenX-playerImage.get_rect().width
            posY3=screenY-playerImage.get_rect().height

            enemies = []
            enemyCounter = 0
            totalenemies = 5
            score = 0
            gameover=False

            while not gameover:
                clock.tick(125)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover=True
                    elif event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_UP:
                            directionY="move_up"
       
                         elif event.key==pygame.K_DOWN:
                                directionY="move_down"
                
                         elif event.key==pygame.K_w:
                                directionY2="K_w"
       
                         elif event.key==pygame.K_s:
                                directionY2="K_s"
                


                    elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                          speedY=0

                        if event.key==pygame.K_w or event.key==pygame.K_s:
                            speedY2=0

                if directionY=="move_up":
                        if posY>0:
                            posY-=3
                elif directionY=="move_down":
                        if posY + 85 <screenY:
                            posY+=3
                if directionY2=="K_w":
                        if posY2>0:
                           posY2-=3
                elif directionY2=="K_s":
                        if posY2 + 85 <screenY:
                           posY2+=3
                events=pygame.event.get()
                for i in pygame.event.get():
                            sys.exit()
                liik()

                if posX3 > screenX - playerImage.get_rect().width or posX3 < 0:
        
                            if posY3 > 140 and posY3 < 368:
                               score += 1
                            print(score)

                if posY3 > screenY - playerImage.get_rect().height or posY3 < 0:
      
                            if posX3 > 140 and posX3 < 368:
                                score += 1
                                print(score)

                for enemy in enemies[:]:
                            if player.colliderect(enemy):
                                enemies.remove(enemy)
                                score += 1
                                print(score)
                ruut=pygame.draw.rect(screen,red,[610,posY,12,85],0,10)
                ruut2=pygame.draw.rect(screen,blue,[20,posY2,12,85],0,10)
            print(score)
            if score == 5:
                    gameover = True

            pygame.display.flip()
            screen.fill(fon)
            pygame.quit
            break
