import pygame, os, librosa
from scipy.signal import find_peaks
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf


def ttm(path):
    if type(path)!=str:
        raise ValueError('Đầu vào là string')
    m=path.split('/')
    if ':' in path:
        p=m[0]+'/'
        for i in m[1:]:
            p=p+i+'/'
            try:
                os.mkdir(p)
            except:
                pass
    else:
        p=''
        for i in m:
            p=p+i+'/'
            try:
                os.mkdir(p)
            except:
                pass


def decode_emotion_vi(encode_emotion):
    match encode_emotion:
        case 0:
            return 'trung lập'
        case 1:
            return 'vui vẻ'
        case 2:
            return 'buồn'
        case 3:
            return 'tức giận'
        case 4:
            return 'sợ hãi'
        case 5:
            return 'cảm thấy ghê'
        case 6:
            return 'ngạc nhiên'
        case _:
            return ''


def decode_emotion(encode_emotion):
    match encode_emotion:
        case 0:
            return 'neutral'
        case 1:
            return 'happy'
        case 2:
            return 'sad'
        case 3:
            return 'angry'
        case 4:
            return 'fear'
        case 5:
            return 'disgust'
        case 6:
            return 'surprise'
        case _:
            return 'x'

def decode_color(n):
    match n:
        case 0:
            return 'white'
        case 1:
            return 'pink'
        case 2:
            return 'gray'
        case 3:
            return 'red'
        case 4:
            return 'purple'
        case 5:
            return 'yellow'
        case 6:
            return 'green'
        case 'x':
            return 'brown'
        case _:
            return 'blue'

def tdat(m, vt=0):
    be_mat = pygame.Surface((1200, 200))
    be_mat.set_colorkey((0, 0, 0))
    # pygame.draw.rect(be_mat, "red", [0, 0, 1200, 200])
    for i in range(len(m)):
        be_mat.blit(ten(m[i][1]), (20+i*118, 40))
        be_mat.blit(so(m[i][1]), (20+i*118, 100))
        be_mat.blit(mau(m[i][1]), (20+i*118, 160))
        if vt==i:
            pygame.draw.rect(be_mat, "orange", [20+i*118, 180, 100, 10])
    return be_mat

def cx(s=6):
    be_mat = pygame.Surface((600, 250))
    be_mat.set_colorkey((0, 0, 0))
    # pygame.draw.rect(be_mat, "purple", [0, 0, 600, 250])
    font = pygame.font.SysFont("Calibri", 80)
    if s==-1:
        text1 = ''
        text2 = ''
    else:
        text1 = font.render(decode_emotion(s), True, "red")
        text2 = font.render(decode_emotion_vi(s), True, "red")
    if s==0:
        be_mat.blit(text1, (180, 30))
        be_mat.blit(text2, (150, 130))
    elif s==1:
        be_mat.blit(text1, (190, 30))
        be_mat.blit(text2, (196, 130))
    elif s==2:
        be_mat.blit(text1, (230, 30))
        be_mat.blit(text2, (210, 130))
    elif s==3:
        be_mat.blit(text1, (200, 30))
        be_mat.blit(text2, (170, 130))
    elif s==4:
        be_mat.blit(text1, (230, 30))
        be_mat.blit(text2, (200, 130))
    elif s==5:
        be_mat.blit(text1, (180, 30))
        be_mat.blit(text2, (85, 130))
    elif s==6:
        be_mat.blit(text1, (170, 30))
        be_mat.blit(text2, (130, 130))
    
    return be_mat

def su(t=0.1,n=0.01, c=0):
    be_mat = pygame.Surface((300, 250))
    be_mat.set_colorkey((0, 0, 0))
    # pygame.draw.rect(be_mat, "yellow", [0, 0, 600, 250])
    font = pygame.font.SysFont("arial", 30)
    text1 = font.render('Time'+str(c)+':', True, "red")
    text2 = font.render(str(t), True, "red")
    text3 = font.render('Threshold'+str(c)+':', True, "red")
    text4 = font.render(str(n), True, "red")
    be_mat.blit(text1, (50, 20))
    be_mat.blit(text2, (200, 20))
    be_mat.blit(text3, (50, 70))
    be_mat.blit(text4, (200, 70))
    return be_mat

def so(s=0):
    be_mat = pygame.Surface((100, 50))
    be_mat.set_colorkey((0, 0, 0))
    # pygame.draw.rect(be_mat, "green", [0, 0, 100, 50])
    font = pygame.font.SysFont("arial", 50)
    text = font.render(str(s), True, "red")
    if s==-1:
        be_mat.blit(text, (30, 0))
    else:
        be_mat.blit(text, (38, 0))
    return be_mat

def luu():
    be_mat = pygame.Surface((1200, 700))
    be_mat.set_colorkey((0, 0, 0))
    pygame.draw.rect(be_mat, "red", [0, 0, 1200, 700])
    font = pygame.font.SysFont("Calibri", 80)
    text1 = font.render('Bạn muốn lưu ?', True, "green")
    text2 = font.render('y = yes', True, "green")
    text3 = font.render('n = no', True, "green")
    be_mat.blit(text1, (350, 150))
    be_mat.blit(text2, (300, 350))
    be_mat.blit(text3, (700, 350))
    return be_mat

def dtt():
    be_mat = pygame.Surface((1200, 700))
    be_mat.set_colorkey((0, 0, 0))
    pygame.draw.rect(be_mat, "green", [0, 0, 1200, 700])
    font = pygame.font.SysFont("Calibri", 100)
    text = font.render('Đang tính toán ...', True, "red")
    be_mat.blit(text, (280, 300))
    return be_mat


def ten(n=0):
    be_mat = pygame.Surface((100, 50))
    be_mat.set_colorkey((0, 0, 0))
    # pygame.draw.rect(be_mat, "gray", [0, 0, 100, 50])
    font = pygame.font.SysFont("arial", 30)
    text = font.render(decode_emotion(n), True, "red")
    if n==0:
        be_mat.blit(text, (10, 5))
    elif n==1:
        be_mat.blit(text, (15, 5))
    elif n==2:
        be_mat.blit(text, (30, 5))
    elif n==3:
        be_mat.blit(text, (17, 5))
    elif n==4:
        be_mat.blit(text, (28, 5))
    elif n==5:
        be_mat.blit(text, (10, 5))
    elif n==6:
        be_mat.blit(text, (6, 5))
    
    return be_mat

def mau(n=0):
    be_mat = pygame.Surface((100, 15))
    be_mat.set_colorkey((0, 0, 0))
    pygame.draw.rect(be_mat, decode_color(n), [0, 0, 100, 15])
    return be_mat


def tach_am_thanh(data, t, nguong):
    t=int(t*20)
    rms = librosa.feature.rms(y=data, frame_length=750*t, hop_length=750*t)
    peaks, _ = find_peaks(-rms.flatten())
    segments = []
    l = len(data)/len(rms[0])
    x1 = 0
    x2 = 0
    peaks = np.append(peaks, len(rms[0])-1)
    for i in range(len(peaks)):
        x2 = peaks[i]
        if np.mean(rms[0][x1:x2])>nguong:
            segment = data[int(x1*l):int(x2*l)]
            segments.append(segment)
            x1 = x2
    return segments

def plot(data, t):
    t=int(t*20)
    rms = librosa.feature.rms(y=data, frame_length=750*t, hop_length=750*t)
    plt.plot(rms[0])
    plt.show()


def xl1(data, t=1, nguong=0.006, md=0):
    data = tach_am_thanh(data, t, nguong)
    dr = []
    for i in data:
        m = []
        m.append(i)
        m.append(md)
        m.append([])
        m.append([0, 0])
        dr.append(m)
    return dr

def xl2(data, t=0.1, nguong=0.006, md=0):
    data = tach_am_thanh(data, t, nguong)
    dr = []
    for i in data:
        m = []
        m.append(i)
        m.append(md)
        dr.append(m)
    return dr


def pat(data, sr):
    sd.stop()
    sd.play(data, sr)

def gat(mdt):
    a = []
    for i in range(7):
        m=[]
        for j in mdt:
            if j[1]==i:
                m.append(True)
            else:
                m.append(False)
        a.append(m)
    dr = []
    for i in range(7):
        n = []
        for j in range(len(mdt)):
            if a[i][j]:
                n=n+mdt[j][0]
            else:
                if n!=[]:
                    dr.append([np.array(n), i])
                    n=[]
        if n!=[]:
            dr.append([np.array(n), i])
    return dr

def id_max(path):
    ds = os.listdir(path)
    idm = 0
    for i in ds:
        n = i.split(' ')[0]
        try:
            n = int(n)
        except:
            continue
        if n > idm:
            idm = n
    return idm

def save_file(path, data):
    sf.write(path, data, 22050)
    print('đã lưu file: '+path)

def gf(data):
    tm = 'output/'+str(id_max('output')+1)
    mtm = []
    for i in range(7):
        p = tm+'/'+decode_emotion(i)
        mtm.append(p)
        ttm(p)
    for i in range(len(data)):
        for j in range(7):
            if data[i][1]==j:
                path = mtm[j]+'/'+str(i)+'.wav'
                save_file(path, data[i][0])
                

def xldt(data):
    m1 = []
    m2 = []
    for i in data:
        if i[1]==-1:
            for j in i[2]:
                if j[1]!='x':
                    m2.append(j)
        elif i[1]=='x':
            # bỏ. k làm gì cả
            pass
        else:
            m1.append(i[:2])
    gf(m1)
    gf(m2)

    

