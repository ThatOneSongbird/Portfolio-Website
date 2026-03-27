from flask import Flask, render_template, url_for

app = Flask(__name__)

projects = [
    {
        'title': 'Dayelis - A Discord Bot for my Tabletop Group',
        'description': 'A Discord bot designed and maintained by me, built using Python and discord.py, to help manage the server and provide information regarding our game sessions and game system.',
        'link': 'https://github.com/ThatOneSongbird/Dayelis',
        'image': 'images/dayelis.png'
    },
    {
        'title': 'That One Portfolio - My Personal Portfolio Website',
        'description': 'This very website! Built using Flask and Python, it serves as a showcase of my projects and skills.',
        'link': 'https://github.com/ThatOneSongbird/Portfolio-Website',
        'image': 'images/portfolio.png'
    },
    {
        'title': 'Dossier - A Blog focused on Tabletop Role-Playing Games and Roleplay Blogging',
        'description': 'A blog built using Django to share my thoughts and experiences with tabletop role-playing games, as well as a place to make roleplay blogging posts that are in-universe for my TTRPG campaign setting.',
        'link': ''
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html', title='About Me')
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')