import discord
import logging
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from embedded_messages import embedded_messages_templates

# Set logger to this module
logger = logging.getLogger("roleBot.utils.role_manage")

# Set role by role owner's request
async def set_role_by_owner(channel, message, author, authorsRole, server):
    logger.info('Requested by ' + author.name)
    logger.info('Role  == ' + authorsRole.name)
    user_id = message.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
    try:
        user = await server.fetch_member(user_id)
        logger.info('User  == ' + user.name)
        if user.roles.count(authorsRole) == 1:
            error = embedded_messages_templates.set_error_embed("У данного пользователя уже есть эта роль")
            await channel.send(embed=error)
            logger.error('User already has this role')
            logger.info('-------------------------------------------------------------')
            return
        if user.roles.count(authorsRole) == 0:
            try:
                await user.add_roles(authorsRole)
                success = embedded_messages_templates.set_success_embed("Пользователю " + user.mention + " была добавлена роль " + authorsRole.mention)
                await channel.send(embed=success)
                logger.info('Role ' + authorsRole.name + ' has been successfully added to ' + user.name)
                logger.info('-------------------------------------------------------------')
                return
            except:
                error = embedded_messages_templates.set_error_embed("По каким-то непонятным причинам не удалось добавить роль. Пожалуйста, обратитесь к <@!225667885240942592>")
                await channel.send(embed=error)
                logger.error('Can not add role ' + authorsRole.name + ' to ' + user.name)
                logger.info('-------------------------------------------------------------')
                return
    except:
        error = embedded_messages_templates.set_error_embed("Пользователь не найден")
        await channel.send(embed=error)
        logger.error('Such user has not been found')
        logger.info('-------------------------------------------------------------')
        return


# Delete role by role owner's request
async def delete_role_by_owner(channel, message, author, authorsRole, server):
    logger.info('Requested by ' + author.name)
    logger.info('Role  == ' + authorsRole.name)
    user_id = message.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
    try:
        user = await server.fetch_member(user_id)
        logger.info('User  == ' + user.name)
        if user.roles.count(authorsRole) == 0:
            error = embedded_messages_templates.set_error_embed("У данного пользователя нет этой роли")
            await channel.send(embed=error)
            logger.error('User do not has this role')
            logger.info('-------------------------------------------------------------')
            return
        if user.roles.count(authorsRole) == 1:
            try:
                await user.remove_roles(authorsRole)
                success = embedded_messages_templates.set_success_embed("У пользователя " + user.mention + " была удалена роль " + authorsRole.mention)
                await channel.send(embed=success)
                logger.info('Role ' + authorsRole.name + ' has been successfully removed from ' + user.name)
                logger.info('-------------------------------------------------------------')
                return
            except:
                error = embedded_messages_templates.set_error_embed("По каким-то непонятным причинам не удалось удалить роль. Пожалуйста, обратитесь к <@!225667885240942592>")
                await channel.send(embed=error)
                logger.error('Can not remove role ' + authorsRole.name + ' from ' + user.name)
                logger.info('-------------------------------------------------------------')
                return
    except:
        error = embedded_messages_templates.set_error_embed("Пользователь не найден")
        await channel.send(embed=error)
        logger.error('Such user has not been found')
        logger.info('-------------------------------------------------------------')
        return


# Set role by request
async def set_role(channel, message, author, server):
    logger.info('Requested by ' + author.name)
    strRole = message.split(' ', 1)[1]
    logger.info('Role == ' + strRole)
    role = None
    try:
        for rolesList in server.roles:
            if rolesList.name == strRole:
                role = rolesList
                break
    except:
        logger.error('Can not get roles from server')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("По неизвестным причинам не удалось найти роль. За информацией обратитесь к <@!225667885240942592>")
        await channel.send(embed=error)
        return
    if role == None:
        logger.error('Can not find role on server')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("По неизвестным причинам не удалось найти роль. За информацией обратитесь к <@!225667885240942592>")
        await channel.send(embed=error)
        return
    if author.roles.count(role) == 1:
        logger.error('User already has requested role')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("У вас уже есть роль " + role.mention)
        await channel.send(embed=error)
        return
    elif author.roles.count(role) == 0:
        try:
            await author.add_roles(role)
            logger.info('Role ' + role.name + ' has been successfully added to ' + author.name)
            logger.info('-------------------------------------------------------------')
            success = embedded_messages_templates.set_success_embed("Вам добавлена роль " + role.mention)
            await channel.send(embed=success)
            return
        except:
            logger.error('Can not add role ' + role.name + ' to ' + author.name)
            logger.info('-------------------------------------------------------------')
            error = embedded_messages_templates.set_error_embed("Не получилось добавить роль. За информацией обратитесь к <@!225667885240942592>")
            await channel.send(embed=error)
            return


# Delete role by request
async def delete_role(channel, message, author, server):
    logger.info('Requested by ' + author.name)
    strRole = message.split(' ', 1)[1]
    logger.info('Role == ' + strRole)
    role = None
    try:
        for rolesList in server.roles:
            if rolesList.name == strRole:
                role = rolesList
                break
    except:
        logger.error('Can not get roles from server')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("По неизвестным причинам не удалось найти роль. За информацией обратитесь к <@!225667885240942592>")
        await channel.send(embed=error)
        return
    if role == None:
        logger.error('Can not find role on server')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("По неизвестным причинам не удалось найти роль. За информацией обратитесь к <@!225667885240942592>")
        await channel.send(embed=error)
        return
    if author.roles.count(role) == 0:
        logger.error('User do not has requested role')
        logger.info('-------------------------------------------------------------')
        error = embedded_messages_templates.set_error_embed("У вас нет роли " + role.mention)
        await channel.send(embed=error)
        return
    elif author.roles.count(role) == 1:
        try:
            await author.remove_roles(role)
            logger.info('Role ' + role.name + ' has been successfully removed from ' + author.name)
            logger.info('-------------------------------------------------------------')
            success = embedded_messages_templates.set_success_embed("У вас удалена роль " + role.mention)
            await channel.send(embed=success)
            return
        except:
            logger.error('Can not remove role ' + role.name + ' from ' + author.name)
            logger.info('-------------------------------------------------------------')
            error = embedded_messages_templates.set_error_embed("Не получилось удалить роль. За информацией обратитесь к <@!225667885240942592>")
            await channel.send(embed=error)
            return
