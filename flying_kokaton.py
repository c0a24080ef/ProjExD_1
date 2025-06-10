import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    original2_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    flipped1_img = pg.transform.flip(bg_img,True,False)
    tmr = 0
    dx=300
    dy=200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            dy-=1
        elif key_lst[pg.K_DOWN]:
            dy+=1
        elif key_lst[pg.K_RIGHT]:
            dx+=2
        elif key_lst[pg.K_LEFT]:
            dx-=1

        dx-=1      
        

        x=tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(flipped1_img, [-x+1600, 0])
        screen.blit(original2_img,[-x+3200,0])
        screen.blit(kk_img,(dx,dy))
        
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()