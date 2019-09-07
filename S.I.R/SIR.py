# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap
import random as rand
import numpy as np


# define residents
class Person(object):
    def __init__(self, types, no, latent=None):
        self.type = types
        self.no = no
        self.x = 0
        self.y = 0
        self.latent = latent


# define the size of the village
gx = 30
gy = 30

# define the numbers of residents
Total = 900
origS = 880
origI = 20
origR = 0

# define the probability of a successful transmission
a = 1

# define the probability of recovery
b = 0.05

# define the latent period
latent_min = 2
latent_max = 3

# define a period
Days = 120

# define canvas and types' colors
#             S          I          R          E
#             蓝         红         绿          粉
size = (5, 5)
colors = ['#FFC0CB', '#FF0000', '#3CB371', '#870EFA']
colormap = ListedColormap(colors)
fig = plt.figure(figsize=size)


# check if (px, py) has been occupied in q
def if_occupied(q, px, py):
    occupied = False
    for i in q:
        if i.x == px and i.y == py:
            occupied = True
    return occupied


# locate residents in q
def rand_locate(q):
    for i in q:
        while True:
            rx = rand.randint(0, gx - 1)
            ry = rand.randint(0, gy - 1)
            if not(if_occupied(q, rx, ry)):
                break
        i.x = rx
        i.y = ry


# count residents according to types
def count(q):
    s = 0
    i = 0
    r = 0
    e = 0
    for j in q:
        if j.type == 1:
            s = s + 1
        elif j.type == 2:
            if j.latent > 0:
                e = e + 1
            else:
                i = i + 1
        elif j.type == 3:
            r = r + 1
    return s, i, r, e


# return an 2d array with types of people
def get_data(q):
    p_types = np.zeros(shape=(gx, gy))
    for i in q:
        if i.type == 2:
            if i.latent > 0:
                p_types[i.x][i.y] = 4
            else:
                p_types[i.x][i.y] = 2
        else:
            p_types[i.x][i.y] = i.type
    return p_types


# yield next infected resident
def find_next_i(q):
    for i in q:
        if i.type == 2 and i.latent <= 0:
            yield i


# return the list of infected residents
def find_i_group(q):
    ni = find_next_i(q)
    return list(ni)


# return the resident with (px, py)
def find_xy(q, px, py):
    for i in q:
        if i.x == px and i.y == py:
            return i


# return the next coordinate
def next_xy(x, y):
    if x == gx - 1 and y == gy - 1:
        return rand.randint(0, gx - 1), rand.randint(0, gy - 1)
    if x == gx - 1:
        x = 0
        y = y + 1
    else:
        x = x + 1
    return x, y


# define the process of recovery
def recover(q):
    s, i, r, e = count(q)
    dr = int(b * i)
    i_group = find_i_group(q)
    if i_group:
        for i in range(dr):
            picked_i = rand.randint(0, len(i_group) - 1)
            for j in q:
                if i_group[picked_i].no == j.no:
                    j.type = 3
            i_group.pop(picked_i)


# define the process of infection
def infect(q):
    i_group = find_i_group(q)
    if i_group:
        n = []
        for i in i_group:
            n.append(find_xy(q, i.x + 1, i.y))
            # n.append(find_xy(q, i.x + 1, i.y + 1))
            # n.append(find_xy(q, i.x + 1, i.y - 1))
            n.append(find_xy(q, i.x - 1, i.y))
            # n.append(find_xy(q, i.x - 1, i.y + 1))
            # n.append(find_xy(q, i.x - 1, i.y - 1))
            n.append(find_xy(q, i.x, i.y + 1))
            n.append(find_xy(q, i.x, i.y - 1))
            for j in n:
                if j and j.type != 3 and j.type != 2:
                    if rand.random() <= a:
                        j.type = 2
                        j.latent = rand.randint(latent_min, latent_max)


# define the decay of latency
def latency(q):
    for i in q:
        if i.type == 2:
            i.latent = i.latent - 1


# generate Susceptible and Infected residents
pS = []
pI = []

for i in range(Total):
    if i < origI:
        pI.append(Person(2, i, rand.randint(latent_min, latent_max)))
    else:
        pS.append(Person(1, i))


# locate Infected residents, and then the Susceptible
rand_locate(pI)
cx = 0
cy = 0
for i in pS:
    if not(if_occupied(pI, cx, cy)):
        i.x = cx
        i.y = cy
        cx, cy = next_xy(cx, cy)
    else:
        while if_occupied(pI, cx, cy):
            cx, cy = next_xy(cx, cy)
        i.x = cx
        i.y = cy
        cx, cy = next_xy(cx, cy)


p = pI + pS


# denote these when animation is applied
# init = plt.imshow(get_data(p), cmap=colormap, vmin=1, vmax=4)
# ims = [[init] * 100]
ims = []


# Run SIR Model
for i in range(Days):
    # Spread the epidemic
    recover(p)
    infect(p)
    latency(p)

    # Save
    im = plt.imshow(get_data(p), cmap=colormap, vmin=1, vmax=4)
    plt.axis('off')
    ims.append([im])


# Visualization
ani = animation.ArtistAnimation(fig, ims, interval=500,
                                repeat=False)
plt.show()

# Animation
# download ffmpeg, and set rc to its execution file path
# plt.rcParams['animation.ffmpeg_path'] = 'D:/ffmpeg/bin/ffmpeg'
# movie_writer = animation.FFMpegWriter()
# ani.save('im.mp4', writer=movie_writer)
