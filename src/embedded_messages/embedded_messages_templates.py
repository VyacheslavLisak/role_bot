import discord

#Create success embed
def set_success_embed(embedDescription):
    success = discord.Embed()
    success.color = 65280
    success.set_author(name = "УСПЕХ", icon_url="https://cdn.discordapp.com/emojis/530403526573162509.png")
    success.description = embedDescription
    return success


#Create error embed
def set_error_embed(embedDescription):
    error = discord.Embed()
    error.color = 16711680
    error.set_author(name="ОШИБКА", icon_url="https://cdn.discordapp.com/emojis/530401936063594498.png")
    error.description = embedDescription
    return error


#Create information embed
def set_information_embed(embedDescription):
    information = discord.Embed()
    information.color = 49151
    information.set_author(name="ИНФОРМАЦИЯ", icon_url="https://cdn.discordapp.com/emojis/530405208405311488.png")
    information.description = embedDescription
    return information


#Create notification embed
def set_notification_embed(embedDescription):
    notification = discord.Embed()
    notification.color = 16753920
    notification.set_author(name="УВЕДОМЛЕНИЕ", icon_url="https://cdn.discordapp.com/emojis/530401936533356544.png")
    notification.description = embedDescription
    return notification
