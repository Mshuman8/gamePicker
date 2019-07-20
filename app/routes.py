from app import app
from flask import render_template, request
from app.models import model
import random

@app.route('/')
@app.route('/index', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        user_data = request.form
        group_size = user_data["group_size"]
        energy = user_data["energy"]
        risk = user_data["risk"]
        noise_level = user_data["noise"]
        # print("you have selected a " + group_size + " size group, " + energy + " energy level, " + risk + " risk level")
        # print(user_data)
        list_of_games = []
        step1_games = []
        step2_games = []
        step3_games = []
        for game in model.game_list:
            if group_size == game.group_size or group_size == game.other_group_size or group_size == game.other_other:
                step1_games.append(game)
        for game in step1_games:
            if energy == "any":
                step2_games = step1_games
            elif energy == game.energy_level:
                step2_games.append(game)
        for game in step2_games:
            if risk == "any":
                step3_games = step2_games
            elif risk == game.risk_level:
                step3_games.append(game)
        for game in step3_games:
            if noise_level == game.noise_level:
                list_of_games.append(game)
        if len(list_of_games) > 3:
            random.shuffle(list_of_games)
            rand_three_games = [list_of_games[0], list_of_games[1], list_of_games[2]]
        else:
            rand_three_games = list_of_games
        # rand_num1 = random.randint(0, len(list_of_games))
        # rand_num2 = random.randint(0, len(list_of_games))
        # if rand_num1 == rand_num2:
        #     rand_num2 = random.randint(0, len(list_of_games))
        # rand_num3 = random.randint(0, len(list_of_games))
        # if rand_num1 == rand_num3 or rand_num2 == rand_num3:
        #     rand_num3 = random.randint(0, len(list_of_games))
        str_of_names = "You can play: "
        if len(rand_three_games) == 1:
            str_of_names += rand_three_games[0].name
        elif len(rand_three_games) > 1:
            for x in range(len(rand_three_games)):
                if x < len(rand_three_games) - 1:
                    str_of_names = str_of_names + rand_three_games[x].name + ", "
                else:
                    str_of_names = str_of_names + "and " + rand_three_games[x].name + "."
        else:
            str_of_names = "We do not have any games that match your requirements. Please update and try again."

    return render_template('index.html', group_size = group_size, energy = energy, risk = risk, str_of_names = str_of_names, noise_level = noise_level, list_of_games = list_of_games, rand_three_games = rand_three_games)
