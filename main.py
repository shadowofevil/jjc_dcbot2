from bot import bot
from plugins.jjc_watcher import initialize
#import keep_alive

if __name__ == '__main__':
    import json
    with open('./config.json') as f:
        config = json.load(f)
    initialize(config)
    #keep_alive.keep_alive()
    bot.run(config['token'])
