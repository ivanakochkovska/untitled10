from PIL import Image, ImageFont
from tkinter import Tk, Canvas, Button

import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
import matplotlib.pyplot as plt
import networkx as nx
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import random
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas, FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import numpy as np
import io
import os
from os import path



def basic_seir_model(request):
    num_of_people=request.GET['num']

    f = matplotlib.figure.Figure()
    ax = f.add_subplot(111)
    t_max = 100
    dt = .1
    t = np.linspace(1, t_max, int(t_max / dt) + 1)
    print(t)
    N = int(num_of_people)
    init_vals = 1 - 1 / N, 1 / N, 0, 0
    alpha = 0.2
    beta = 1.75
    gamma = 0.5
    params = alpha, beta, gamma
    # Code that sets up figure goes here; in the question, that's ...
    FigureCanvasAgg(f)
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]

    for _ in t[1:]:
        next_S = S[-1] - (beta * S[-1] * I[-1]) * dt
        next_E = E[-1] + (beta * S[-1] * I[-1] - alpha * E[-1]) * dt
        next_I = I[-1] + (alpha * E[-1] - gamma * I[-1]) * dt
        next_R = R[-1] + (gamma * I[-1]) * dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)


    plt.xlim(0, len(t))
    plt.ylim(-0.1, 1.1)
    plt.plot(E, label="E", color="yellow")
    plt.plot(S, label="S", color="green")
    plt.plot(I, label="I", color="red")
    plt.plot(R, label="R", color="blue")
    plt.xlabel('Time')
    plt.ylabel('Population')


    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(f)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    return response

def seir_model_wth_social_distancing(request):
    numm=request.GET['numm']
    f = matplotlib.figure.Figure()
    ax = f.add_subplot(111)
    t_max = 100
    dt = .1
    t = np.linspace(1, t_max, int(t_max / dt) + 1)
    print(t)
    N = int(numm)
    init_vals = 1 - 1 / N, 1 / N, 0, 0
    alpha = 0.2
    beta = 1.75
    gamma = 0.5
    quar=request.GET['quar']
    qq=int(quar)
    rho = float(qq/100)
    params = alpha, beta, gamma, rho
    # Code that sets up figure goes here; in the question, that's ...
    FigureCanvasAgg(f)
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma, rho = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (rho * beta * S[-1] * I[-1]) * dt
        next_E = E[-1] + (rho * beta * S[-1] * I[-1] - alpha * E[-1]) * dt
        next_I = I[-1] + (alpha * E[-1] - gamma * I[-1]) * dt
        next_R = R[-1] + (gamma * I[-1]) * dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    plt.figure(figsize=(10, 5))

    plt.xlim(0, len(t))
    plt.ylim(-0.1, 1.1)
    plt.plot(E, label="E", color="yellow")
    plt.plot(S, label="S", color="green")
    plt.plot(I, label="I", color="red")
    plt.plot(R, label="R", color="blue")
    plt.xlabel('Time')
    plt.ylabel('Population')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(f)


    response = HttpResponse(buf.getvalue(), content_type='image/png')

    return response

def network(request):

    people_number=request.GET['people_number']
    sick=request.GET['sick']
    if path.exists("foo.png"):


        print("Postoi")
        print(path.isfile("foo.png"))
        os.remove("foo.png")
    if path.exists("foo.png") is False:
        print("izbrisano e")
    if path.exists("fo1.png"):
        os.remove("foo1.png")
    if path.exists("result.png"):
        os.remove("result.png")
    if path.exists("image_data"):
        print("pstoi i ovaaa")
        os.remove("image_data")

    # os.remove('foo.png')
    # os.remove('foo1.png')

    class Person:
        def __init__(self, id, range, healthy, infected):
            self.id = id
            self.range = range
            self.healthy = healthy
            self.infected = infected

    n = int(people_number) # broj na licnosti vo mrezata
    infected_people = int(sick)  # kolku zarazeni licnosti ima vo mrezata
    people = []
    g = nx.Graph()
    node_sizes = list()

    for i in range(0, len(people)):
        node_sizes.append(int(100))

    def check(list1, list2, number1, number2):
        flag = 0
        for j in range(0, len(list1)):
            if list1[j] == number1 or list2[j] == number2:
                flag += 1
        return flag

        # gi dodavame licnostite vo mrezata
        # potoa odreduvame brojka na zarazeni vo mrezata
    for i in range(0, n):
        person = Person(i, 2, None, None)
        people.append(person)

    for i in range(0, infected_people):
        people[i].infected = 1
        random_values_x = list()
        random_values_y = list()

    def generate():
        random_x = int(random.uniform(0, 100))
        random_y = int(random.uniform(0, 100))
        return random_x, random_y

    for i in range(0, len(people)):
        flag = 0
        random_x, random_y = generate()

        random_values_x.append(random_x)
        random_values_y.append(random_y)

        person = people[i]
        g.add_node(person, pos=(random_x, random_y), name='nod', id=int(i))
        one_random_number = random.uniform(0, 1)  # verojatnost deka licnostite imaat direkten kontakt megu sebe
        print(one_random_number)
        probabbility = float(0.01)
        if one_random_number >= probabbility:
            if i + 1 < (len(people) - 1) and i > 0:
                person1 = people[i]
                person2 = people[i + 1]
                g.add_edge(person1, person2)
    pos = nx.get_node_attributes(g, 'pos')
    color_map = list()
    ids = nx.get_node_attributes(g, 'id')
    ids_numbers = list(ids.values())

    for i in range(0, len(people)):
        p = people[i]
        if i in ids_numbers and i < infected_people and p.infected == 1:
            color_map.append('red')
        else:
            color_map.append('blue')

    nx.draw(g, pos, node_color=color_map)
    plt.savefig('foo.png')

    #plt.show()

        # =================================================MREZATA NA KONTAKTI E ZAVRSENA================================
        # ==========================================kontaktite se direktni odnosno nema 2 metri rastojanie===============

    new_color_map = list()
    m = 0
    while m <= (len(people) * 1000):
        for i in range(0, len(people)):
            node = people[i]
            if node.infected == 1:
                neighbors_of_node = [ng for ng in g.neighbors(node)]
                for neighbor in neighbors_of_node:
                    if neighbor.infected is not 1:
                        neighbor.infected = 1
                        infected_people += 1
        m += 1
    print(infected_people)

    for i in range(0, len(people)):
        p = people[i]
        if i in ids_numbers and i < infected_people and p.infected == 1:
            new_color_map.append('red')
        else:
            new_color_map.append('blue')


    nx.draw(g, pos, node_sizes=node_sizes, node_color=new_color_map)
    plt.savefig('foo1.png')
    im=Image.open('foo.png')

    im1=Image.open('foo1.png')
    dst = Image.new('RGB', (im.width + im1.width, im.height))
    dst.paste(im, (0, 0))
    dst.paste(im1, (im.width, 0))
    dst.save('result.png')
    image_data=open('result.png','rb').read()
    response=HttpResponse(image_data, content_type='image/png')

    return response

def network_with_social_distancing(requst):
    total=requst.GET['total']
    infe=requst.GET['infe']
    quar=requst.GET['quar']
    class Person:
        def __init__(self, id, range, healthy, infected, karantin):
            self.id = id
            self.range = range
            self.healthy = healthy
            self.infected = infected
            self.karantin = karantin

    n =int(total)  # broj na licnosti vo mrezata
    infected_people = int(infe)  # kolku zarazeni licnosti ima vo mrezata
    karantin = int(quar)
    people = []
    g = nx.Graph()
    node_sizes = list()
    for i in range(0, len(people)):
        node_sizes.append(int(100))

    def check(list1, list2, number1, number2):
        flag = 0
        for j in range(0, len(list1)):
            if list1[j] == number1 or list2[j] == number2:
                flag += 1
        return flag

    # gi dodavame licnostite vo mrezata
    # potoa odreduvame brojka na zarazeni vo mrezata
    for i in range(0, n):
        person = Person(i, 2, None, None, None)
        people.append(person)

    for i in range(0, infected_people):
        people[i].infected = 1

    for i in range(0, karantin):
        num = int(random.uniform(0, n - 2))
        people[num].karantin = 1
    random_values_x = list()
    random_values_y = list()

    def generate():
        random_x = int(random.uniform(0, 100))
        random_y = int(random.uniform(0, 100))
        return random_x, random_y

    for i in range(0, len(people)):
        flag = 0
        random_x, random_y = generate()

        random_values_x.append(random_x)
        random_values_y.append(random_y)

        person = people[i]
        g.add_node(person, pos=(random_x, random_y), name='nod', id=int(i))
        one_random_number = random.uniform(0, 1)  # verojatnost deka licnostite imaat direkten kontakt megu sebe
        print(one_random_number)
        probabbility = float(0.01)
        if one_random_number >= probabbility:
            if i + 1 < (len(people) - 1) and i > 0:
                person1 = people[i]
                person2 = people[i + 1]
                g.add_edge(person1, person2)
    pos = nx.get_node_attributes(g, 'pos')
    color_map = list()
    ids = nx.get_node_attributes(g, 'id')
    ids_numbers = list(ids.values())
    # crno ------ zarazeni i staveni pod karantin
    # zeleno - zdravi pod karantin
    # crveni --- zarazeni no ne se pod karantin
    # plavi --- ne se zarazeni ama ne se pod karantin, nitu se bolni
    for i in range(0, len(people)):
        p = people[i]
        if i in ids_numbers and p.infected == 1 and p.karantin == 1:
            color_map.append('black')
        if i in ids_numbers and p.karantin == 1 and p.infected is None:
            color_map.append('green')
        if i in ids_numbers and p.karantin is None and p.infected == 1:
            color_map.append('red')
        if i in ids_numbers and p.karantin is None and p.infected is None:
            color_map.append('blue')

    nx.draw(g, pos, node_color=color_map)

    plt.savefig('first.png')

    # #=================================================MREZATA NA KONTAKTI E ZAVRSENA================================
    # #==========================================kontaktite se direktni odnosno nema 2 metri rastojanie===============
    new_color_map = list()
    m = 0
    plot_infected = list()
    while m <= (len(people) * 1000):
        current_infected = infected_people
        for i in range(0, len(people)):
            node = people[i]
            if node.karantin == 1:
                continue
            if node.infected == 1:
                neighbors_of_node = [ng for ng in g.neighbors(node)]
                for neighbor in neighbors_of_node:
                    if neighbor.karantin == 1:
                        continue
                    else:
                        if neighbor.infected is not 1:
                            neighbor.infected = 1
                            infected_people += 1
                            if infected_people is not current_infected:
                                plot_infected.append(infected_people)
            m += 1
    print(infected_people)
    for i in range(0, len(people)):
        p = people[i]
        if i in ids_numbers and i < infected_people and p.infected == 1:
            if p.karantin == 1:
                new_color_map.append('black')
            else:
                new_color_map.append('red')
        else:
            new_color_map.append('blue')

    nx.draw(g, pos, node_sizes=node_sizes, node_color=new_color_map)
    plt.savefig('second.png')
    im = Image.open('first.png')

    im1 = Image.open('second.png')

    dst = Image.new('RGB', (im.width + im1.width, im.height))
    dst.paste(im, (0, 0))
    dst.paste(im1, (im.width, 0))
    dst.save('result.png')
    image_data = open('result.png', 'rb').read()
    response = HttpResponse(image_data, content_type='image/png')

    return response

def redirect(request):
    return HttpResponseRedirect('http://localhost:3000' )