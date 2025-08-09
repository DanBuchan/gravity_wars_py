import configparser

config = configparser.ConfigParser()
config.read('config.ini')
settings = {
    'ScreenWidth': int(config['DEFAULT']['ScreenWidth']),
    'ScreenHeight': int(config['DEFAULT']['ScreenHeight']),
    'MinPlanets': int(config['DEFAULT']['MinPlanets']),
    'MaxPlanets': int(config['DEFAULT']['MaxPlanets']),
    'Player1Name': config['DEFAULT']['Player1Name'],
    'Player2Name': config['DEFAULT']['Player2Name'],
    'Blackholes': eval(config['DEFAULT']['Blackholes']),
    'NakedBlackholes': eval(config['DEFAULT']['NakedBlackholes']),
    'RemoveTrails': eval(config['DEFAULT']['RemoveTrails']),
    'MusicVolume': int(config['DEFAULT']['MusicVolume']),
    'SFXVolume': int(config['DEFAULT']['SFXVolume']),
}

def set_settings(player1, player2, planetNum, 
                 allowBlack, allowNakedBlack,
                 remove):
    settings['Player1Name'] = player1.get_value()
    settings['Player2Name'] = player2.get_value()
    settings['MinPlanets'] = planetNum.get_value()[0]
    settings['MaxPlanets'] = planetNum.get_value()[1]
    settings['Blackholes'] = allowBlack.get_value()
    settings['NakedBlackholes'] = allowNakedBlack.get_value()
    settings['RemoverTrails'] = remove.get_value()