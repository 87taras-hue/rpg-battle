import random
from django.shortcuts import render, redirect

HERO_MAX = 100
MONSTER_MAX = 100

def new_battle(request):
    request.session["hero_hp"] = HERO_MAX
    request.session["monster_hp"] = MONSTER_MAX
    request.session["log"] = ["Бій почався! Обери свою дію."]
    request.session["finished"] = False
    request.session["poison_used"] = False
    return redirect("arena")

def arena(request):
    if "hero_hp" not in request.session:
        return new_battle(request)

    if request.method == "POST" and not request.session.get("finished"):
        action = request.POST.get("action")
        hero_hp = request.session["hero_hp"]
        monster_hp = request.session["monster_hp"]
        log = request.session.get("log", [])

        if action == "sword":
            damage = random.randint(15, 25)
            monster_hp = max(0, monster_hp - damage)
            log.insert(0, f"Ти вдарив мечем і завдав {damage} шкоди.")
        elif action == "poison" and not request.session.get("poison_used"):
            damage = random.randint(25, 38)
            monster_hp = max(0, monster_hp - damage)
            request.session["poison_used"] = True
            log.insert(0, f"Отруйна атака! Монстр втратив {damage} здоров'я.")
        else:
            log.insert(0, "Цю дію зараз не можна використати.")

        if monster_hp > 0:
            damage = random.randint(8, 17)
            hero_hp = max(0, hero_hp - damage)
            log.insert(0, f"Монстр атакував у відповідь: -{damage} HP.")
        else:
            log.insert(0, "Перемога! Монстра переможено.")

        if hero_hp <= 0:
            log.insert(0, "Поразка! Герой втратив усе здоров'я.")
        request.session["hero_hp"] = hero_hp
        request.session["monster_hp"] = monster_hp
        request.session["log"] = log[:12]
        request.session["finished"] = hero_hp <= 0 or monster_hp <= 0

    return render(request, "battle/arena.html", {
        "hero_hp": request.session["hero_hp"],
        "monster_hp": request.session["monster_hp"],
        "hero_max": HERO_MAX,
        "monster_max": MONSTER_MAX,
        "log": request.session.get("log", []),
        "finished": request.session.get("finished", False),
        "poison_used": request.session.get("poison_used", False),
        "won": request.session["monster_hp"] <= 0 and request.session["hero_hp"] > 0,
    })
