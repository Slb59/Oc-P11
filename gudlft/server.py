import os
from datetime import datetime
from distutils.util import strtobool
from http import HTTPStatus

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
def show_summary():
    try:
        club = [
            club for club in data.clubs
            if club.email == request.form['email']
            ][0]
        return render_template(
                'welcome.html',
                club=club,
                future_competitions=data.future_competitions,
                past_competitions=data.past_competitions
                )
    except IndexError:
        flash("!!! Cette adresse email n'est pas reconnue")
        return render_template(
            'index.html'
            )


@app.route('/book/<competition>/<club>')
def book(competition, club):
    status_code = HTTPStatus.OK
    try:
        found_club = [c for c in data.clubs if c.name == club][0]
        found_competition = [
            c for c in data.competitions if c.name == competition
            ][0]
        if found_club and found_competition:
            date_competition = datetime.strptime(
                found_competition.date, '%Y-%m-%d %H:%M:%S')
            if date_competition < datetime.now():
                flash("Error: This competition is over !", "error")
                status_code = HTTPStatus.BAD_REQUEST
            else:
                return render_template(
                    'booking.html',
                    club=found_club,
                    competition=found_competition
                    )
        else:
            flash("Something went wrong-please try again", "error")
            status_code = HTTPStatus.NOT_FOUND

    except IndexError:
        flash("Something went wrong-please try again", "error")
        status_code = HTTPStatus.NOT_FOUND

    return render_template(
                'welcome.html',
                club=club,
                future_competitions=data.future_competitions,
                past_competitions=data.past_competitions
                ), status_code


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
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
            future_competitions=data.future_competitions,
            past_competitions=data.past_competitions
            )
    except Exception as e_info:
        flash(str(e_info))
        return render_template(
            'booking.html', club=club, competition=competition
            )


@app.route('/showPointsDisplayBoard')
def view_board():
    return render_template('board.html', clubs=data.clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
