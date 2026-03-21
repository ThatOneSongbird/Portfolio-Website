from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Dayelis Discord TTRPG Bot',
        'description': 'A Discord bot designed and maintained by me, built using Python and discord.py, to help manage the server and provide information regarding our game sessions and game system.',
        'link': 'https://github.com/ThatOneSongbird/Dayelis'
    },
    {
        'title': 'Personal Portfolio Website',
        'description': 'This very website! Built using Flask and Python, it serves as a showcase of my projects and skills.',
        'link': ''
    },
    {
        'title': 'Django TTRPG Blog',
        'description': 'A blog built using Django to share my thoughts and experiences with tabletop role-playing games, as well as a place to roleplay blogging posts that are in-universe for my TTRPG campaign setting.',
        'link': ''
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')