import discord
import asyncio
import botToken

client = discord.Client()

""" Server """
pupki = None

""" Channels """
botChat = None

""" Publick roles"""
rabotyagi = None
afkshnik = None
znatoki = None
anime = None
animeHate = None
podVlad = None

""" Roles owners """
arkadiy = None
slava = None

""" Private roles """
arkadiy_role = None

@client.event
async def on_ready():

    """ Global variables """
    global pupki
    global botChat
    global rabotyagi
    global afkshnik
    global znatoki
    global anime
    global animeHate
    global podVlad
    global arkadiy
    global slava
    global arkadiy_role

    """ Information about bot """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


    """ Set server """
    pupki = client.get_guild(392581230891106306)
    print('Server: ' + pupki.name)
    print(pupki.id)
    print('-----------')


    """ Set general channel """
    botChat = client.get_channel(587554944681246730)
    
    """ Set publick roles """
    rabotyagi = pupki.get_role(529395728330653698)
    afkshnik = pupki.get_role(526152344799412234)
    znatoki = pupki.get_role(529848302397816837)
    anime = pupki.get_role(526151771400306694)
    animeHate = pupki.get_role(526151863662411782)
    podVlad = pupki.get_role(526160205264977931)

    """ Set roles owners """
    arkadiy = client.get_user(321961105335255042)
    slava = client.get_user(225667885240942592)

    """ Set private roles """
    arkadiy_role = pupki.get_role(451026809761562626)


@client.event
async def on_message(message):

    
    """ Global variables """
    global pupki
    global botChat
    global rabotyagi
    global afkshnik
    global znatoki
    global anime
    global animeHate
    global podVlad
    global arkadiy
    global slava
    global arkadiy_role


    if message.channel == botChat:
        
        mes = message.content
        if mes.startswith('.role'):
            print('\nStarts with .role')
            if len(mes.split()) == 3:
                if message.author == arkadiy:
                    print('Requested by ' + message.author.name)
                    if mes.split()[2] != ('<@&' + str(arkadiy_role.id) + '>'):
                        await botChat.send('```У вас нет прав для добавления пользователю этой роли, либо роль была введена неверно```')
                        print('Нет прав на добавление этой роли, либо неверный формат записи роли')
                        return
                    if mes.split()[2] == ('<@&' + str(arkadiy_role.id) + '>'):
                        print('mes[2] == ' + mes.split()[2] + '\nRole  == ' + arkadiy_role.name) 
                        user_id = mes.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
                        print('mes[1] == ' + mes.split()[1])
                        try:
                            user = await pupki.fetch_member(user_id)
                            print('user == ' + user.name)
                            if user.roles.count(arkadiy_role) == 1:
                                await botChat.send('```У данного пользователя уже есть эта роль```')
                                print('User already has this role')
                                return
                            if user.roles.count(arkadiy_role) == 0:
                                try:
                                    await user.add_roles(arkadiy_role)
                                    await botChat.send('```Пользователю ' + user.name + ' была добавлена роль ' + arkadiy_role.name + '```')
                                    print('Successfully added \n\n')
                                    return
                                except:
                                    await botChat.send('```По каким-то непонятным причинам не удалось добавить роль. Пожалуйста, обратитесь к администратору```')
                                    print('CAN NOT ADD ROLE. ERROR IS HERE')
                                    return
                        except:
                            await botChat.send('```Пользователь не найден```')
                            print('User did not found')
                            return
                else:
                    await botChat.send('```У вас нет прав на использование этой команды```')
                    print('User do not have permissions for using this format')
                    return
            else:
                await botChat.send('```Неверный формат ввода. Используйте: \n.role @Пользователь @Роль```')
                print('Wrong input format')
                return
        



        if mes.startswith('.delete_role'):
            print('\nStarts with .delete_role')
            if len(mes.split()) == 3:
                if message.author == arkadiy:
                    print('Requested by ' + message.author.name)
                    if mes.split()[2] != ('<@&' + str(arkadiy_role.id) + '>'):
                        await botChat.send('```У вас нет прав для удаления у пользователя этой роли, либо роль была введена неверно```')
                        print('Нет прав на удаление этой роли, либо неверный формат записи роли')
                        return
                    if mes.split()[2] == ('<@&' + str(arkadiy_role.id) + '>'):
                        print('mes[2] == ' + mes.split()[2] + '\nRole  == ' + arkadiy_role.name) 
                        user_id = mes.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
                        print('mes[1] == ' + mes.split()[1])
                        try:
                            user = await pupki.fetch_member(user_id)
                            print('user == ' + user.name)
                            if user.roles.count(arkadiy_role) == 0:
                                await botChat.send('```У данного пользователя нет этой роли```')
                                print('User do not has this role')
                                return
                            elif user.roles.count(arkadiy_role) == 1:
                                try:
                                    await user.remove_roles(arkadiy_role)
                                    await botChat.send('```У Пользователя ' + user.name + ' была удалена роль ' + arkadiy_role.name + '```')
                                    print('Successfully removed \n\n')
                                    return
                                except:
                                    await botChat.send('```По каким-то непонятным причинам не удалось удалить роль. Пожалуйста, обратитесь к администратору```')
                                    print('CAN NOT REMOVE ROLE. ERROR IS HERE')
                                    return
                        except:
                            await botChat.send('```Пользователь не найден```')
                            print('User did not found')
                            return
                else:
                    await botChat.send('```У вас нет прав на использование этой команды```')
                    print('User do not have permissions for using this format')
                    return
            else:
                await botChat.send('```Неверный формат ввода. Используйте: \n.delete_role @Пользователь @Роль```')
                print('Wrong input format')
                return


        if message.content == '.роль Работяги':
            if message.author.roles.count(rabotyagi) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            await message.author.add_roles(rabotyagi)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + rabotyagi.mention + '```')
            return

        
        elif message.content  == '.удалить роль Работяги':
            if message.author.roles.count(rabotyagi) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(rabotyagi) == 1:
                await message.author.remove_roles(rabotyagi)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + rabotyagi.mention + '```')
                return


        elif message.content == '.роль АФКашник':
            if message.author.roles.count(afkshnik) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            await message.author.add_roles(afkshnik)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + afkshnik.mention + '```')
            return
        

        elif message.content  == '.удалить роль АФКашник':
            if message.author.roles.count(afkshnik) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(afkshnik) == 1:
                await message.author.remove_roles(afkshnik)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + afkshnik.mention + '```')
                return


        elif message.content == '.роль Знатоки':
            if message.author.roles.count(znatoki) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            await message.author.add_roles(znatoki)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + znatoki.mention + '```')
            return

        
        elif message.content  == '.удалить роль Знатоки':
            if message.author.roles.count(znatoki) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(znatoki) == 1:
                await message.author.remove_roles(znatoki)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + znatoki.mention + '```')
                return

        
        elif message.content == '.роль Анимечъник':
            if message.author.roles.count(anime) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            if message.author.roles.count(animeHate) == 1:
                await botChat.send ('```Вы хейтите аниме и не можете получить эту роль```')
                return
            await message.author.add_roles(anime)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + anime.mention + '```')
            return
        

        elif message.content  == '.удалить роль Анимечъник':
            if message.author.roles.count(anime) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(anime) == 1:
                await message.author.remove_roles(anime)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + anime.mention + '```')
                return
        

        elif message.content == '.роль АнимуХейтер':
            if message.author.roles.count(animeHate) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            if message.author.roles.count(anime) == 1:
                await botChat.send ('```Вы любите аниме и не можете получить эту роль```')
                return
            await message.author.add_roles(animeHate)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + animeHate.mention + '```')
            return
        

        elif message.content  == '.удалить роль АнимуХейтер':
            if message.author.roles.count(animeHate) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(animeHate) == 1:
                await message.author.remove_roles(animeHate)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + animeHate.mention + '```')
                return
        

        elif message.content == '.роль Под Владиславом':
            if message.author.roles.count(podVlad) == 1:
                await botChat.send ('```У вас уже есть эта роль```')
                return
            await message.author.add_roles(podVlad)
            await botChat.send ('```Пользователю ' + message.author.mention + ' добавлена роль ' + podVlad.mention + '```')
            return


        elif message.content  == '.удалить роль Под Владиславом':
            if message.author.roles.count(podVlad) == 0:
                await botChat.send('```У вас нет такой роли```')
                return
            elif message.author.roles.count(podVlad) == 1:
                await message.author.remove_roles(podVlad)
                await botChat.send ('```У пользователя ' + message.author.mention + ' была удалена роль ' + podVlad.mention + '```')      
                return  


client.run(botToken.DISCORD_BOT_TOKEN)
