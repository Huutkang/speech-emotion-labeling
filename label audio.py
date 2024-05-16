from lib import *
import librosa



t = 0.7
tc = 0.1
nguong=0.006
nguongc = 0.004

macdinh=0


run = True
x1 = 0
x2 = 0
y = 1

save = False

data, sr = librosa.load('x3.mp3')
data = xl1(data, t, nguong, macdinh)

ldt = len(data)
ldtc = 0
xh1 = 0
xh2 = 0

if ldt <10:
    h1 = data
else:
    h1 = data[xh1:xh1+10]

sd.play(h1[x1][0], sr)

pygame.init()
clock = pygame.time.Clock()

dis = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Cắt âm thanh')



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if save==False:
                run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if y==1:
                    h1[x1][1] = 0
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 0
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_1:
                if y==1:
                    h1[x1][1] = 1
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 1
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_2:
                if y==1:
                    h1[x1][1] = 2
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 2
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_3:
                if y==1:
                    h1[x1][1] = 3
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 3
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_4:
                if y==1:
                    h1[x1][1] = 4
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 4
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_5:
                if y==1:
                    h1[x1][1] = 5
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 5
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_6:
                if y==1:
                    h1[x1][1] = 6
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 6
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_x:
                if y==1:
                    h1[x1][1] = 'x'
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    h2[x2][1] = 'x'
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_p:
                if y==1:
                    plot(h1[x1][0], t)
                elif y==2:
                    plot(h2[x2][0], tc)
            if event.key == pygame.K_a:
                if y==1 and xh1>0:
                    xh1-=1
                    h1 = data[xh1:xh1+10]
                    if h1[x1][1]==-1:
                        xh2 = h1[x1][3][0]
                        x2 = h1[x1][3][1]
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h1[x1][0], sr)
                elif y==2 and xh2>0:
                    xh2 -= 1
                    h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_d:
                if y==1 and xh1<ldt-11:
                    xh1 += 1
                    h1 = data[xh1:xh1+10]
                    if h1[x1][1]==-1:
                        xh2 = h1[x1][3][0]
                        x2 = h1[x1][3][1]
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h1[x1][0], sr)
                elif y==2 and xh2<ldtc-11:
                    xh2 += 1
                    h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_y:
                run = False
            if event.key == pygame.K_n:
                save = False
            if event.key == pygame.K_l:
                save = True
            if event.key == pygame.K_UP:
                if y ==2:
                    y=1
                    h1[x1][3][0] = xh2
                    h1[x1][3][1] = x2
                    sd.play(h1[x1][0], sr)
            elif event.key == pygame.K_DOWN:
                if y==1:
                    y=2
                    h1[x1][1] = -1
                    if len(h1[x1][2])==0:
                        h1[x1][2] = xl2(h1[x1][0], tc, nguongc, macdinh)
                    h2 = h1[x1][2]
                    xh2 = h1[x1][3][0]
                    x2 = h1[x1][3][1]
                    ldtc = len(h1[x1][2])
                    if ldtc<10:
                        h2 = h1[x1][2]
                    else:
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            if event.key == pygame.K_LEFT:
                if y==1:
                    if x1>0:
                        x1 -=1
                    elif xh1>0:
                        xh1-=1
                        h1 = data[xh1:xh1+10]
                    if h1[x1][1]==-1:
                        xh2 = h1[x1][3][0]
                        x2 = h1[x1][3][1]
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    if x2>0:
                        x2 -= 1
                    elif xh2>0:
                        xh2-=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            elif event.key == pygame.K_RIGHT:
                if y==1:
                    if x1<len(h1)-1:
                        x1 += 1
                    elif xh1<ldt-11:
                        xh1+=1
                        h1 = data[xh1:xh1+10]
                    if h1[x1][1]==-1:
                        xh2 = h1[x1][3][0]
                        x2 = h1[x1][3][1]
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h1[x1][0], sr)
                elif y==2:
                    if x2<len(h2)-1:
                        x2 += 1
                    elif xh2<ldtc-11:
                        xh2+=1
                        h2 = h1[x1][2][xh2:xh2+10]
                    sd.play(h2[x2][0], sr)
            
    pygame.draw.rect(dis, "black", [0, 0, 1200, 700])
    dis.blit(tdat(h1, x1), (0, 300))
    if y==1:
        vx2=-1
    else:
        vx2=x2
    if h1[x1][1]==-1:
        dis.blit(tdat(h2, vx2), (0, 500))
    if y==1:
        x=h1[x1][1]
    else:
        x=h2[x2]
    if save:
        dis.blit(luu(), (0, 0))
    else:
        dis.blit(cx(x), (300, 0))
        dis.blit(su(t, nguong, 1), (0, 0))
        dis.blit(su(tc, nguongc, 2), (900, 0))    

    pygame.display.update()
    clock.tick(10)



if save:
    dis.blit(dtt(), (0, 0))
    pygame.display.update()
    xldt(data)




