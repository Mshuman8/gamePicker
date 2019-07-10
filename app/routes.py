from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        user_data = formopener.dict_from(request.form)
        group_size = user_data["group_size"]
        energy = user_data["energy"]
        risk = user_data["risk"]
        noise_level = user_data["noise"]
        # print("you have selected a " + group_size + " size group, " + energy + " energy level, " + risk + " risk level")
        # print(user_data)
        list_of_games = []
        for game in model.game_list:
            if group_size == game.group_size or group_size == game.other_group_size or group_size == game.other_other:
                list_of_games.append(game)
            elif game not in list_of_games:
                if energy == game.energy_level:
                    list_of_games.append(game)
            elif game not in list_of_games:
                if risk == game.risk_level:
                    list_of_games.append(risk)
        str_of_names = "You can play: "
        list_no_repeats = []
        for x in range(len(list_of_games)):
            if x < len(list_of_games) - 1:
                str_of_names = str_of_names + list_of_games[x].name + ", "
            else:
                str_of_names = str_of_names + "and " + list_of_games[x].name + "."

    return render_template('index.html', group_size = group_size, energy = energy, risk = risk, str_of_names = str_of_names, noise_level = noise_level, list_of_games = list_of_games)
