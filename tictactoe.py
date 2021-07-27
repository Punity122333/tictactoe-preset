import discord
from discord.ext import commands

class TicTacToe(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(help='Plays TicTacToe with a member.')
	async def tictactoe(self, ctx, member:discord.Member):
		isFinished = False
		cr_player = member
		opp = member
		winner = None
		player = ctx.author
		combinations = [['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],['a1','b2','c3'],['a3','b2','c1']]
		cr = '❌'
		cl = '⭕'
		bl = '⬛'
		tdict = {'a1':bl,'a2':bl,'a3':bl,'b1':bl,'b2':bl,'b3':bl,'c1':bl,'c2':bl,'c3':bl}
		tlist = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
		tttstr = ''
		for item in tlist:
			tttstr += tdict[item]
			if (tlist.index(item)+1) % 3 == 0:
				tttstr += '\n'
		embed = discord.Embed(title=f'TicTacToe | {player.name} vs {opp.name}',description=tttstr,color=discord.Color.orange())
		embed.add_field(name='How to play?',value='The game works on a grid system. For example "a1" for the \ntop left corner and "c3" for the bottom right corner.')
		await ctx.send(embed=embed)
		while isFinished == False:
			
			if cr_player == member:
				def check(m):
					return m.author == member and m.channel == ctx.channel
			else:
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
			await ctx.send(f'{cr_player.mention}, enter your square below!')
			msg2 = ''
			while msg2 not in tdict:
				msg = await self.client.wait_for('message',check=check)
				msg2 = msg.content
				if msg.content.lower() == 'cancel':
					canbed = discord.Embed(title='Canceled',description=f'{cr_player.name} canceled the game :(',color=discord.Color.red())
					await player.send(embed=canbed)
					await member.send(embed=canbed)
					return
				
				
				if msg2 not in tdict:
					em2 = discord.Embed(title='Error',description='Please enter a valid square/coordinate!',color=discord.Color.red())
					await cr_player.send(embed=em2)
			if msg.content.lower() == 'cancel':
				canbed = discord.Embed(title='Canceled',description=f'{cr_player.name} canceled the game :(',color=discord.Color.red())
				await ctx.send(embed=canbed)
				return
			sq = msg.content.lower()
			if tdict[sq] == bl:
				if cr_player == member:
					tdict[sq] = cr
				else:
					tdict[sq] = cl
			
			tttstr = ''
			for item in tlist:
				tttstr += tdict[item]
				if (tlist.index(item)+1) % 3 == 0:
					tttstr += '\n'
			embed = discord.Embed(title=f'TicTacToe | {player.name} vs {opp.name}',description=tttstr,color=discord.Color.orange())
			embed.set_footer(text='The game works on a grid system. For example "a1" for the \ntop left corner and "c3" for the bottom right corner.')
			await ctx.send(embed=embed)
			for item in combinations:
				if (tdict[item[0]] == cl and tdict[item[1]] == cl and tdict[item[2]] == cl) or (tdict[item[0]] == cr and tdict[item[1]] == cr and tdict[item[2]] == cr):
					isFinished = True
					winner = cr_player
					break
				allFilled = False
				if bl not in list(tdict.values()):
					allFilled = True
					isFinished = True
					break
			if cr_player == member:
				cr_player = player 
			else:
				cr_player = member
		if winner == None:
			em2 = discord.Embed(title='No one won :(',description='No one won the tictactoe game!',color=discord.Color.red())
		else:
			em2 = discord.Embed(title='Winner!',description=f'{winner.mention} won the tictactoe game!',color=discord.Color.green())
		await ctx.send(embed=em2)






			


def setup(client):
	client.add_cog(TicTacToe(client))
		
