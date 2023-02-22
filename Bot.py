import Game_math_functions as gm
botv = 0.1
# versions: 0.1; 0.2


def direct(mass):
    if botv == 0.1:
        bot_mass = mass
        score = gm.score
        direction = "up"
        max_score = 0
        gm.key_up(bot_mass)
        if gm.score - score > max_score:
            max_score = gm.score - score
            direction = "up"
        gm.score = score
        bot_mass = mass
        gm.key_down(bot_mass)
        if gm.score - score > max_score:
            max_score = gm.score - score
            direction = "down"
        gm.score = score
        bot_mass = mass
        gm.key_left(bot_mass)
        if gm.score - score > max_score:
            max_score = gm.score - score
            direction = "left"
        gm.score = score
        bot_mass = mass
        gm.key_right(bot_mass)
        if gm.score - score > max_score:
            max_score = gm.score - score
            direction = "right"
        gm.score = score
        bot_mass = mass
    elif botv == 0.2:
        bot_mass = mass
        direction = "up"
        max_score = 0
        score = 0
        bot_score = 0
        score_save = gm.score
        gm.key_up(bot_mass)
        for i in range(gm.x):
            for g in range(gm.y):
                if mass[g][i]:
                    score += 1
        for i in range(gm.x):
            for g in range(gm.y):
                if bot_mass[g][i]:
                    bot_score += 1
        if bot_score - score > max_score:
            max_score = bot_score - score
            direction = "up"
        gm.score = score_save
        bot_mass = mass
        gm.key_down(bot_mass)
        for i in range(gm.x):
            for g in range(gm.y):
                if mass[g][i]:
                    score += 1
        for i in range(gm.x):
            for g in range(gm.y):
                if bot_mass[g][i]:
                    bot_score += 1
        if bot_score - score > max_score:
            max_score = bot_score - score
            direction = "down"
        gm.score = score_save
        bot_mass = mass
        gm.key_left(bot_mass)
        for i in range(gm.x):
            for g in range(gm.y):
                if mass[g][i]:
                    score += 1
        for i in range(gm.x):
            for g in range(gm.y):
                if bot_mass[g][i]:
                    bot_score += 1
        if bot_score - score > max_score:
            max_score = bot_score - score
            direction = "left"
        gm.score = score_save
        bot_mass = mass
        gm.key_right(bot_mass)
        for i in range(gm.x):
            for g in range(gm.y):
                if mass[g][i]:
                    score += 1
        for i in range(gm.x):
            for g in range(gm.y):
                if bot_mass[g][i]:
                    bot_score += 1
        if bot_score - score > max_score:
            max_score = bot_score - score
            direction = "right"
        gm.score = score_save
        bot_mass = mass
    return direction
