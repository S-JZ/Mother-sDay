import pygame
from time import sleep
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((600,500))

pygame.display.set_caption("Mommy")
pygame.mixer.music.load("meri.mp3")
pygame.mixer.music.play()

sleep(1)

names=['img1.jpg','img2.jpg','img3.jpg','img4.jpg','img5.jpg','img6.jpg','img7.jpg','img8.jpg']
for i in names:
    name=i
    image= pygame.image.load(name).convert_alpha()
    image_size = image_width, image_height = image.get_size()
    if image_size[0] <= 600 and image_size[1] <= 500:
        dsp_width, dsp_height = image_size
    else:
        scale_factor = 500/float(image_height)
        dsp_width = int(scale_factor * image_width)
        dsp_height = int(scale_factor * image_height)
        if dsp_width > 600:
            scale_factor = 600/float(image_width)
            dsp_width = int(scale_factor * image_width)
            dsp_height = int(scale_factor * image_height)
    dsp_size = dsp_width, dsp_height
    if name=='img2.jpg' or name=='img4.jpg' or name=='img8.jpg':
        image=pygame.transform.rotate(image, 180)
    elif name=='img6.jpg':
        image=pygame.transform.rotate(image, 90)
    elif name=='img5.jpg':
        image=pygame.transform.rotate(image, 270)
        
        
    image = pygame.transform.scale(image, dsp_size)
    xleft, ytop, xright, ybottom = image.get_rect()
    xleft = int(600 - dsp_width)/2
    xright += xleft
    ytop = int(500 - dsp_height)/3
    ybottom += ytop
    rect = xleft, ytop, xright, ybottom
    window.blit(image, rect)
    sleep(6)
    pygame.display.update()


running=True
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
