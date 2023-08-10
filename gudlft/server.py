import os

from distutils.util import strtobool

from flask import Flask, render_template, request, redirect, flash, url_for

from .models.dataloader import DataLoader

from dotenv import load_dotenv

load_dotenv()

TESTING = strtobool(os.getenv('TESTING'))

# start flask app
app = Flask(__name__)
# app.config.from_object(config)
app.secret_key = 'something_special'


# load data
if TESTING:
    print('load mode testing')
    data = DataLoader(
        club_file='test2_clubs.json',
        competition_file='test2_competitions.json'
        )
else:
    print('load dev')
    data = DataLoader()


# define routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [
            club for club in data.clubs
            if club.email == request.form['email']
            ][0]
        return render_template(
                'welcome.html',
                club=club,
                competitions=data.competitions
                )
    except IndexError:
        flash("!!! Cette adresse email n'est pas reconnue")
        return render_template(
            'index.html'
            )


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in data.clubs if c.name == club][0]
    foundCompetition = [
        c for c in data.competitions if c.name == competition
        ][0]
    if foundClub and foundCompetition:
        return render_template(
            'booking.html',
            club=foundClub,
            competition=foundCompetition
            )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=data.competitions
            )


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [
        c for c in data.competitions
        if c.name == request.form['competition']
        ][0]
    club = [c for c in data.clubs if c.name == request.form['club']][0]
    placesRequired = int(request.form['places'])

    try:
        club.book(competition, placesRequired)
        flash('Great-booking complete!')
        return render_template(
            'welcome.html',
            club=club,
            competitions=data.competitions
            )
    except Exception as e_info:
        flash(str(e_info))
        return render_template(
            'booking.html', club=club, competition=competition
            )


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
