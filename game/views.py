from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import random

# Create your views here.
scores = [0, 0]
cur_play = False
def addBox(edges, recentEdge, TYPE):
    global scores, cur_play
    s1 = max(recentEdge)
    s2 = min(recentEdge)
    e1 = e2 = e3 = e4 = e5 = e6 = None
    if TYPE == "|":
        if (len(str(int(s1[1]) + 1)) == 1):
            e1 = {s1, s1[0] + str(int(s1[1]) + 1)}
            e2 = {s2, s2[0] + str(int(s1[1]) + 1)}
            e3 = {s1[0] + str(int(s1[1]) + 1), s2[0] + str(int(s1[1]) + 1)}
        if (len(str(int(s1[1]) - 1)) == 1):
            e4 = {s1, s1[0] + str(int(s1[1]) - 1)}
            e5 = {s2, s2[0] + str(int(s1[1]) - 1)}
            e6 = {s1[0] + str(int(s1[1]) - 1), s2[0] + str(int(s1[1]) - 1)}

    elif TYPE == "__":
        if (len(str(int(s1[0]) + 1)) == 1):
            e1 = {s1, s1[1] + str(int(s1[0]) + 1)}
            e2 = {s2, s2[1] + str(int(s1[0]) + 1)}
            e3 = {s1[1] + str(int(s1[0]) + 1), s2[1] + str(int(s1[0]) + 1)}
        if (len(str(int(s1[0]) - 1)) == 1):
            e4 = {s1, s1[1] + str(int(s1[0]) - 1)}
            e5 = {s2, s2[1] + str(int(s1[0]) - 1)}
            e6 = {s1[1] + str(int(s1[0]) - 1), s2[1] + str(int(s1[0]) - 1)}

    else:
        print(":(")

    scoreAdded = False
    if (e1 in edges and e2 in edges and e3 in edges):
        scores[cur_play] += 1
        scoreAdded = True
        cur_play = not cur_play

    if (e4 in edges and e5 in edges and e6 in edges):
        scores[cur_play] += 1
        if not scoreAdded: cur_play = not cur_play

users = []
def index(request):
    username = request.GET['username']
    if username not in users: users.append(username)
    if (len(users) >= 3):
        return HttpResponse(f"{users[0]} and {users[1]} are playing, wait till they complete!")
    return render(request, 'game/index.html', context={
        "greetUser": username,
        "activePlayers": users
    })

extras = 'init();'
edges = []
def game(request, me, opponent):
    global extras, cur_play, edges, scores
    if (request.method == "POST"):
        if (users[cur_play] == me):
            s1, s2 = request.POST['hidden'].split(',')
            TYPE = request.POST['type']
            extras += 'radPressed(false, '+s1+');'
            extras += 'radPressed(false, '+s2+');'
            recentEdge = {s1, s2}
            edges.append(recentEdge)

            addBox(edges, recentEdge, TYPE)
            cur_play = not cur_play
        
    return render(request, "game/game.html", context={
        "me": me,
        "opponent": opponent,
        "extras": extras,
        "cur_play": users[cur_play],
        "scoreBoard": scores,
        "players": users
    })
    
def logout(request, me):
    global extras, users, scores
    try:
        extras = 'init();'
        scores = []
        users.remove(me)
    except:
        pass
    return HttpResponse("Logged Out, You can now close this window")