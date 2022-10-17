from cgi import test
import telebot
from credentials import secrets

key_api = secrets.get('API_KEY_IMPORT')

bot = telebot.TeleBot(key_api)

github_entry = "github.com/LuizFSvr"
instagram_entry = "instagram.com/luizFSvr"
twitter_entry = "twitter.com/LuizFSvr"
steam_entry = "steamcommunity.com/profiles/76561198196975498/"

name = "test"

@bot.message_handler(commands=["GitHub"])
def option1(message):
    bot.send_message(message.chat.id, f'Óla {name}, fico feliz que tenha interesse no meu GitHub. O GitHub é onde coloco meus projetos que estou realizando no momento, lá você pode ver todo o meu desenvolvimento como Dev. 😎' )
    bot.send_message(message.chat.id, github_entry )
    
@bot.message_handler(commands=["Instagram"])
def option2(message):
    bot.send_message(message.chat.id, f'Óla {name}, fico feliz que tenha interesse no meu Instagram, utilizo pouco mas sempre tento atualizar. 😃')
    bot.send_message(message.chat.id, instagram_entry)

@bot.message_handler(commands=["Twitter"])
def option3(message):
    bot.send_message(message.chat.id, f'Óla {name}, fico feliz que tenha interesse no meu Twitter, geralmente é sempre onde atualizo primeiro além de usar majoritariamente como rede pessoal. 👀')
    bot.send_message(message.chat.id, twitter_entry)

@bot.message_handler(commands=["Steam"])
def option4(message):
    bot.send_message(message.chat.id, f'Óla {name}, fico feliz que tenha interesse na minha Steam é onde sempre costumo estar jogando, caso queira ter um contato menos profissional podemos jogar algumas coisas. 🎮')
    bot.send_message(message.chat.id, steam_entry)


def verificar(message):
    global name
    name = message.from_user.first_name
    return True


@bot.message_handler(func=verificar)
def responder(message):
    text = """
Central de rede sociais (Clique no item): 
/GitHub
/Instagram
/Twitter
/Steam
Outras opções são invalidas no momento.
"""
    bot.reply_to(message, text)


bot.polling()


