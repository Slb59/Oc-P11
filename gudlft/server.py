from flask import Flask, render_template, request, redirect, flash, url_for

from .db import DataLoader

app = Flask(__name__)
# app.config.from_object(config)
app.secret_key = 'something_special'

# load data
data = DataLoader()


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

    if placesRequired > club.points:
        flash('Not enough points!')
        return render_template(
            'booking.html', club=club, competition=competition
            )
    else:
        competition.number_of_places = \
            int(competition.number_of_places) - placesRequired
        club.points = club.points - placesRequired
        flash('Great-booking complete!')
        return render_template(
            'welcome.html',
            club=club,
            competitions=data.competitions
            )

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
