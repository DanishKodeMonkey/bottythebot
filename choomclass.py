from discord.ext import commands
import random

class Flatline (commands.Converter):
    async def shoot(self, ctx, gonk, argument:"No reason"):
        gonk = ctx.members.mention
        return f'BANG! {ctx.author} flatlined {gonk} because *{argument}*, he ded!'
    