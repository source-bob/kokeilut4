import textwrap

story = '''Welcome, adventurer! You're about to embark on a thrilling journey across the globe, starting at a randomly selected airport. Your ultimate goal: reach a distant destination using only your knowledge and a bit of luck!

You begin your quest with only half the kilometers needed to reach your destination. Along the way, you'll visit various airports and have the chance to earn more kilometers.

How? By putting your skills to the test! Guess the country, municipality, or even the elevation of your current airport. For the risk-takers, you can also roll the dice and try your hand at exciting mini-games.

But beware! If your available kilometers drop to 45 or less, your journey will come to an abrupt end, leaving you stranded. Additionally, incorrect guesses while trying to identify your current airport's details will not only set you back but will now cost you 40% of your remaining kilometers—so choose wisely!

On the flip side, success is rewarding! Winning mini-games or making accurate guesses about the municipality or elevation will add 15% to your available kilometers. However, if you correctly guess the country, you'll receive a massive 40% boost to your kilometers—but at a cost: you'll be sent to a completely random airport, which may throw off your progress.

The game ends when you've gathered enough kilometers to reach your final airport, or you find yourself out of kilometers. Will you have the wits and luck to make it? Time will tell.\n

Best of luck, traveler!'''

wrapper = textwrap.TextWrapper(width=80, break_long_words=False)

word_list = wrapper.wrap(text=story)

def getStory():
    return "\n".join(word_list)