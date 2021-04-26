import discord
import asyncio
import logging
import logging.config
from os import path
import botToken
import owners_and_roles
import approvedRoles
from embedded_messages import embedded_messages_templates
from utils import role_manage

# Set logger
LOGGING_CONFIG = path.join(path.dirname(path.abspath(__file__)), 'logger.conf') 
logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger("roleBot")
logger.info('-------------------------------------------------------------')
logger.info("Bot has been started")

# Server
pupki = None

# Channels
rulesChannel = None
ownersChannel = None
botCommandsChannel = None

# Roles
baseRole = None
ownersRole = None
animeRole = None
animeHaterRole = None

# Admins
vlad = None
slava = None

# Discord client object
client = discord.Client()

@client.event
async def on_ready():

    # Global variables
    global pupki
    global rulesChannel
    global ownersChannel
    global botCommandsChannel
    global baseRole
    global ownersRole
    global animeRole
    global animeHaterRole
    global vlad
    global slava

    # Set server by ID
    pupki = client.get_guild(392581230891106306)

    # Set channels
    rulesChannel = client.get_channel(834935955919208459)
    ownersChannel = client.get_channel(834936205119717397)
    botCommandsChannel = client.get_channel(836351762398052382)

    # Set roles
    baseRole = pupki.get_role(612009586282463301)
    ownersRole = pupki.get_role(754388385967112343)
    animeRole = pupki.get_role(526151771400306694)
    animeHaterRole = pupki.get_role(526151863662411782)

    #Set server admins
    slava = client.get_user(225667885240942592)
    vlad = client.get_user(315531935218794497)

    #Information about bot
    logger.info('Logged in as:    ' + client.user.name)
    logger.info('On server:       ' + pupki.name)
    logger.info('-------------------------------------------------------------')


@client.event
async def on_raw_reaction_add(payload):

    # Global variables
    global rulesChannel
    global pupki
    global baseRole

    if payload.channel_id == rulesChannel.id:       # User added reaction to rules message -> give access to the server
        user = await pupki.fetch_member(payload.user_id)
        logger.info('Reaction has been added by ' + user.name + '#' + user.discriminator)
        try:
            await user.add_roles(baseRole)
            logger.info('Access was granted to ' + user.name + '#' + user.discriminator)
            logger.info('-------------------------------------------------------------')
        except:
            logger.error("Access wasn't granted to " + user.name + '#' + user.discriminator)
            logger.info('-------------------------------------------------------------')
        return


@client.event
async def on_raw_reaction_remove(payload):

    # Global variables
    global rulesChannel
    global pupki
    global baseRole

    if payload.channel_id == rulesChannel.id:       # User removed reaction from rules message -> revoke access to the server
        user = await pupki.fetch_member(payload.user_id)
        logger.info('Reaction has been deleted by ' + user.name + '#' + user.discriminator)
        try:
            await user.remove_roles(baseRole)
            logger.info('Access was canceled to ' + user.name + '#' + user.discriminator)
            logger.info('-------------------------------------------------------------')
        except:
            logger.error("Access wasn't canceled to" + user.name + '#' + user.discriminator)
            logger.info('-------------------------------------------------------------')
        return


@client.event
async def on_message(message):

    # Global variables
    global pupki
    global ownersChannel
    global botCommandsChannel
    global ownersRole
    global animeRole
    global animeHaterRole
    global vlad
    global slava

    if message.channel == ownersChannel:            # If message has been received from 'выдача_ролей'

        if message.author == client.user:           # If sender == bot -> do nothing
            await message.delete(delay=10.0)
            return
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.startswith('.role'):     # If message stareted with '.role' -> starting check if author have access to use set_role_by_owner()
            if message.content.split()[0] == '.role':
                logger.info('Message starts with .role')
                if message.author.roles.count(ownersRole) == 1:     # Check if author has role with permissions
                    if len(message.content.split()) == 3:           # Check if there are 3 parameters in message
                        role = None
                        if owners_and_roles.ownersAndRoles.get(str(message.author.id)).count(message.content.split()[2]):   # Try to get author's role from dictionary
                            role = pupki.get_role(int(message.content.split()[2].replace('<', '').replace('>', '').replace('&', '').replace('@', '')))
                        else:                       # Error with getting author's role from dictionary
                            error = embedded_messages_templates.set_error_embed("У вас нет прав на добавление этой роли")
                            await ownersChannel.send(embed=error)
                            logger.error('User do not have permissions to add this role')
                            logger.info('-------------------------------------------------------------')
                            await message.delete(delay=10.0)
                            return
                        await role_manage.set_role_by_owner(message.channel, message.content, message.author, role, pupki)      # Try to set requested role
                    else:                           # There aren't 3 parameters in message (more than 3 or less than 3)
                        error = embedded_messages_templates.set_error_embed("Неверный формат ввода. Используйте: \n\n```.role @имя#тег @роль```")
                        await ownersChannel.send(embed=error)
                        logger.error('Wrong input format')
                        logger.info('-------------------------------------------------------------')
                        await message.delete(delay=10.0)
                        return
                else:                               # Author hasn't role with permissions
                    error = embedded_messages_templates.set_error_embed("У вас нет прав на использование этой команды")
                    await ownersChannel.send(embed=error)
                    logger.error('User do not have permissions to use this command')
                    logger.info('-------------------------------------------------------------')
                    await message.delete(delay=10.0)
                    return

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.startswith('.delete_role'): # If message stareted with '.delete_role' -> starting check if author have access to use delete_role_by_owner()
            if message.content.split()[0] == '.delete_role':
                logger.info('Message starts with .delete_role')
                if message.author.roles.count(ownersRole) == 1:     # Check if author has role with permissions
                    if len(message.content.split()) == 3:           # Check if there are 3 parameters in message
                        role = None
                        if owners_and_roles.ownersAndRoles.get(str(message.author.id)).count(message.content.split()[2]):   # Try to get author's role from dictionary
                            role = pupki.get_role(int(message.content.split()[2].replace('<', '').replace('>', '').replace('&', '').replace('@', '')))
                        else:                       # Error with getting author's role from dictionary
                            error = embedded_messages_templates.set_error_embed("У вас нет прав на удаление этой роли")
                            await ownersChannel.send(embed=error)
                            logger.error('User do not have permissions to delete this role')
                            logger.info('-------------------------------------------------------------')
                            await message.delete(delay=10.0)
                            return
                        await role_manage.delete_role_by_owner(message.channel, message.content, message.author, role, pupki)  # Try to delete requested role
                    else:                           # There aren't 3 parameters in message (more than 3 or less than 3)
                        error = embedded_messages_templates.set_error_embed("Неверный формат ввода. Используйте: \n\n```.delete_role @имя#тег @роль```")
                        await ownersChannel.send(embed=error)
                        logger.error('Wrong input format')
                        logger.info('-------------------------------------------------------------')
                        await message.delete(delay=10.0)
                        return
                else:                               # Author hasn't role with permissions
                    error = embedded_messages_templates.set_error_embed("У вас нет прав на использование этой команды")
                    await ownersChannel.send(embed=error)
                    logger.error('User do not have permissions to use this command')
                    logger.info('-------------------------------------------------------------')
                    await message.delete(delay=10.0)
                    return
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Delete all received messages in channel 'выдача_ролей' after 10 seconds
        await message.delete(delay=10.0)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    if message.channel == botCommandsChannel:       # If message has been received from 'команды_для_ботов'

        if message.author == client.user:           # If sender == bot -> do nothing
            await message.delete(delay=10.0)
            return
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.startswith(('.role', '.delete_role')):   # If message stareted with '.role' or '.delete_role' -> send user to #выдача_ролей
            information = embedded_messages_templates.set_information_embed('Выполнение данной команды доступно в канале <#834936205119717397>')
            await botCommandsChannel.send(embed=information)
            await message.delete(delay=10.0)
            return


        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.startswith('.роль'):     # If message stareted with '.роль' -> starting check if author have access to get requested role
            if message.content.split()[0] == '.роль':
                logger.info('Message starts with .роль')
                if len(message.content.split()) == 1:   # Message containts only '.роль'
                    logger.error('Received message containts only ".роль"')
                    logger.info('-------------------------------------------------------------')
                    information = embedded_messages_templates.set_information_embed("Пожалуйста укажите роль после .роль\nПример:\n```.роль Бродяги```")
                    await botCommandsChannel.send(embed=information)
                    await message.delete(delay=10.0)
                    return
                approved = False
                for i in approvedRoles.approvedRoles:   # Check if author has permission to get requested role
                    if i == message.content.split(' ', 1)[1]:
                        approved = True
                        break
                if approved == False:
                    logger.error('Requested role is not approved')
                    logger.info('-------------------------------------------------------------')
                    error = embedded_messages_templates.set_error_embed("Данную роль нельзя получить, либо роль была введена неверно")
                    await botCommandsChannel.send(embed=error)
                    await message.delete(delay=10.0)
                    return
                else:
                    if message.author.roles.count(animeRole) and message.content.split(' ', 1)[1] == 'АнимуХейтер':     # if user has '@Анимечъник' and trying to get '@АнимуХейтер' -> send error message
                        logger.error('User is trying to get "@АнимуХейтер" while has "@Анимечъник"')
                        logger.info('-------------------------------------------------------------')
                        information = embedded_messages_templates.set_information_embed('Чтобы получить роль <@&526151863662411782> у вас не должно быть роли <@&526151771400306694>')
                        await botCommandsChannel.send(embed=information)
                        await message.delete(delay=10.0)
                        return
                    if message.author.roles.count(animeHaterRole) and message.content.split(' ', 1)[1] == 'Анимечъник':     # if user has '@АнимуХейтер' and trying to get '@Анимечъник' -> send error message
                        logger.error('User is trying to get "@Анимечъник" while has "@АнимуХейтер"')
                        logger.info('-------------------------------------------------------------')
                        information = embedded_messages_templates.set_information_embed('Чтобы получить роль <@&526151771400306694> у вас не должно быть роли <@&526151863662411782>')
                        await botCommandsChannel.send(embed=information)
                        await message.delete(delay=10.0)
                        return
                    await role_manage.set_role(message.channel, message.content, message.author, pupki)     # Try to set requested role

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.startswith('.удалить'):  # If message stareted with '.удалить' -> starting check if author have access to delete requested role
            if message.content.split()[0] == '.удалить':
                logger.info('Message starts with .удалить')
                if len(message.content.split()) == 1:   # Message containts only '.удалить'
                    logger.error('Received message containts only ".удалить"')
                    logger.info('-------------------------------------------------------------')
                    information = embedded_messages_templates.set_information_embed("Пожалуйста укажите роль после .удалить\nПример:\n```.удалить Бродяги```")
                    await botCommandsChannel.send(embed=information)
                    await message.delete(delay=10.0)
                    return
                approved = False
                for i in approvedRoles.approvedRoles:   # Check if author has permission to remove requested role
                    if i == message.content.split(' ', 1)[1]:
                        approved = True
                        break
                if approved == False:
                    logger.error('Requested role is not approved')
                    logger.info('-------------------------------------------------------------')
                    error = embedded_messages_templates.set_error_embed("Данную роль нельзя удалить, либо роль была введена неверно")
                    await botCommandsChannel.send(embed=error)
                    await message.delete(delay=10.0)
                    return
                else:
                    await role_manage.delete_role(message.channel, message.content, message.author, pupki)     # Try to remove requested role

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Delete all received messages in channel 'команды_для_ботов' after 10 seconds
        await message.delete(delay=10.0)


#Start bot
client.run(botToken.DISCORD_BOT_TOKEN)
