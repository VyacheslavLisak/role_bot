import discord
import asyncio
import botToken

client = discord.Client()

botChat = None
rabotyagi = None
afkshnik = None
znatoki = None
anime = None
animeHate = None
podVlad = None


@client.event
async def on_ready():

    """ Global variables """
    global botChat
    global rabotyagi
    global afkshnik
    global znatoki
    global anime
    global animeHate
    global podVlad

    """ Information about bot """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


    """ Set server """
    for guild in client.guilds:
        if guild.id == 392581230891106306:
            pupki = guild
    print('Server: ' + pupki.name)
    print(pupki.id)
    print('-----------')


    """ Set general channel """
    for guild in client.guilds:
        for chat in guild.channels:
            if chat.id == 587554944681246730:
                botChat = chat
    
    rabotyagi = pupki.get_role(529395728330653698)
    afkshnik = pupki.get_role(526152344799412234)
    znatoki = pupki.get_role(529848302397816837)
    anime = pupki.get_role(526151771400306694)
    animeHate = pupki.get_role(526151863662411782)
    podVlad = pupki.get_role(526160205264977931)


@client.event
async def on_message(message):

    if message.channel == botChat:
        
        if message.content == '.роль' or message.content == '.help':
            await botChat.send ('''Используйте команду ".роль <название роли>" для получения общедоступных ролей.
Используйте команду ".удалить роль <название роли>" для удаления общедоступных ролей.

Доступные для получения/удаления роли:

Анимечъник - если вы любите аниме (нельзя получить если вы АнимуХейтер)
АнимуХейтер - если вы хейтите аниме (нельзя получить если вы Анимечъник)
Работяги - если вы считаете себя истиным работягой
АФКашник - если вы любите афкашить в дискорде
Знатоки - если вы считаете себя знатаком
Под Владиславом - специальная роль, если вы хотите оказаться под Владиславом

Для получения ролей, которые здесь не указаны - обратитесь к администраторам сервера

Пример команды для получения роли Работяги:
.роль Работяги

Пример команды для удаления роли Работяги:
.удалить роль Работяги''')
            return

        
        elif message.content == '.роль Работяги':
            if message.author.roles.count(rabotyagi) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            await message.author.add_roles(rabotyagi)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + rabotyagi.mention)
            return

        
        elif message.content  == '.удалить роль Работяги':
            if message.author.roles.count(rabotyagi) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(rabotyagi) == 1:
                await message.author.remove_roles(rabotyagi)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + rabotyagi.mention)


        elif message.content == '.роль АФКашник':
            if message.author.roles.count(afkshnik) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            await message.author.add_roles(afkshnik)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + afkshnik.mention)
            return
        

        elif message.content  == '.удалить роль АФКашник':
            if message.author.roles.count(afkshnik) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(afkshnik) == 1:
                await message.author.remove_roles(afkshnik)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + afkshnik.mention)


        elif message.content == '.роль Знатоки':
            if message.author.roles.count(znatoki) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            await message.author.add_roles(znatoki)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + znatoki.mention)
            return

        
        elif message.content  == '.удалить роль Знатоки':
            if message.author.roles.count(znatoki) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(znatoki) == 1:
                await message.author.remove_roles(znatoki)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + znatoki.mention)

        
        elif message.content == '.роль Анимечъник':
            if message.author.roles.count(anime) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            if message.author.roles.count(animeHate) == 1:
                await botChat.send ('Вы хейтите аниме и не можете получить эту роль')
                return
            await message.author.add_roles(anime)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + anime.mention)
            return
        

        elif message.content  == '.удалить роль Анимечъник':
            if message.author.roles.count(anime) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(anime) == 1:
                await message.author.remove_roles(anime)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + anime.mention)
        

        elif message.content == '.роль АнимуХейтер':
            if message.author.roles.count(animeHate) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            if message.author.roles.count(anime) == 1:
                await botChat.send ('Вы любите аниме и не можете получить эту роль')
                return
            await message.author.add_roles(animeHate)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + animeHate.mention)
            return
        

        elif message.content  == '.удалить роль АнимуХейтер':
            if message.author.roles.count(animeHate) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(animeHate) == 1:
                await message.author.remove_roles(animeHate)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + animeHate.mention)
        

        elif message.content == '.роль Под Владиславом':
            if message.author.roles.count(podVlad) == 1:
                await botChat.send ('У вас уже есть эта роль')
                return
            await message.author.add_roles(podVlad)
            await botChat.send ('Пользователю ' + message.author.mention + ' добавлена роль ' + podVlad.mention)
            return


        elif message.content  == '.удалить роль Под Владиславом':
            if message.author.roles.count(podVlad) == 0:
                await botChat.send('У вас нет такой роли')
                return
            elif message.author.roles.count(podVlad) == 1:
                await message.author.remove_roles(podVlad)
                await botChat.send ('У пользователя ' + message.author.mention + ' была удалена роль ' + podVlad.mention)        


client.run(botToken.DICORD_BOT_TOKEN)
