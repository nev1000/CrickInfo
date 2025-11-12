from flask import Blueprint, render_template, request
import requests
from datetime import date, time, datetime

API_KEY = "fake_key" #insert key here

views = Blueprint("views", __name__)
@views.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@views.route("/games", methods=["GET", "POST"])
def games():
    time = request.form.get('time')
    gender = request.form.get('gender')
    format = request.form.get('format')
    response = requests.get(f"https://api.cricapi.com/v1/matches?apikey={API_KEY}&offset=0")
    response = response.json()
    matches = response['data']
    printy = []

    for match in matches:
            game_format = match['matchType'].split(",")
            date = match['date']
            dt = datetime.strptime(date, "%Y-%m-%d").date()
            gen = get_match_gender(match)      
            if game_format[0] == format: 
                if gen == gender or gender == "all":
                    result = determine_match_time(time, dt)
                    if result == True:
                          printy.append(match)

    return render_template("games.html", games=printy)

def get_match_gender(game):
     for team in game['teams']:
          if 'women'in team.lower():
            return "women"     
     return "men"

def determine_match_time(time, dt):
    if time == "completed":
            if dt < datetime.today().date():
                    return True
                                    
    elif time == "live and upcoming":
            if dt >= datetime.today().date():
                    return True

