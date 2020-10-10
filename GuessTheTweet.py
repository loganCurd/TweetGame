"""
Logan Curd
10/10/2020
"""

import requests
import random
import sys

# Global Vars
INCLUDE_RTS = 'false'
TWEET_RETURN_COUNT = '200'
BEARER_TOKEN = \
    'AAAAAAAAAAAAAAAAAAAAABkxHwEAAAAAKjt2fpGK4jcPceLPZQFopReK4HA%3DweHzQwUw9w6afoMXOopKZ5x1GsZiGSueNc2QyeJ1F11oIiTBBc'
AT_STRING = '@'
RETWEET_STRING = 'https://t.co/'
URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'


class Tweet:

    # Constructor: creates a tweet object using the twitter handle and message from each tweet
    # params: message = tweet text, handle = username of person who tweeted
    def __init__(self, message, handle):
        self.message = message
        self.handle = handle


class GuessTheTweet:

    # Constructor: takes two twitter handles and creates a tweet object (self.tweets)
    # params: two twitter handles to be used in API calls
    def __init__(self, handles):
        self.handles = handles
        self.tweets = self.get_tweets()
        self.score = 0
        self.streak = 0
        self.rounds_played = 0

    # get_tweets(): performs API call for handle and finds valid tweets to append into tweet_list
    # params: handle = twitter handle of user, tweet_list = list to append Tweet objects to
    def get_tweets(self):
        tweets = []

        for x in self.handles:
            response = requests.get(URL,
                                    params={'screen_name': x, 'include_rts': INCLUDE_RTS, 'count': TWEET_RETURN_COUNT},
                                    headers={'authorization': 'Bearer ' + BEARER_TOKEN})  # GET request

            if response.status_code != 200:  # If API call did not work for this handle
                sys.exit(f'API call unsuccessful. Twitter handle \'{x}\' may be invalid.')

            for y in response.json():
                tweet_string = y['text']
                if AT_STRING not in tweet_string and RETWEET_STRING not in tweet_string:  # If valid tweet
                    tweets.append(Tweet(tweet_string, x))

        return tweets

    # get_random_tweet(): returns and removes random Tweet object in self.tweets
    # return: random Tweet object
    def get_random_tweet(self):
        num_tweets = len(self.tweets)
        if num_tweets > 0:
            index = random.randint(0, num_tweets - 1)
            return self.tweets.pop(index)
        else:  # User has guessed all Tweet objects
            sys.exit('No more tweets remain - Game Over.\n'
                     f'You played {self.rounds_played} round(s) and had {self.score} correct answer(s)')

    # play_round(): handles one round of the game
    # (gets random tweet, prompts input, checks correctness, updates variables)
    def play_round(self):
        rand_tweet = self.get_random_tweet()
        possible_answers = [rand_tweet.handle]

        while len(possible_answers) < 4:
            rand_int = random.randint(0, len(self.handles) - 1)
            if self.handles[rand_int] not in possible_answers:
                possible_answers.append(self.handles[rand_int])

        print(rand_tweet.message)

        random.shuffle(possible_answers)
        input_choices = 'abcd'

        response = input(f'Who tweeted this?\n'
                         f'a. (  {possible_answers[0]}  )\n'
                         f'b. (  {possible_answers[1]}  )\n'
                         f'c. (  {possible_answers[2]}  )\n'
                         f'd. (  {possible_answers[3]}  )\n'
                         f'\n'
                         f'Answer: \n')

        output = ''
        index = -1

        for i in input_choices:
            if i == response:
                index = input_choices.index(i)

        correct_answer = False if index == -1 else True if possible_answers[index] == rand_tweet.handle else False

        if correct_answer:
            self.score += 1
            self.streak += 1
            output += 'Correct. '
        else:
            self.streak = 0
            output += f'Incorrect. The correct answer was {rand_tweet.handle}. '

        if self.streak >= 3:
            output += f'That makes {self.streak} in a row. '

        print(output)

        self.rounds_played += 1

    # play_again(): prompts user to play again and takes input
    # return: bool indicating user response
    def play_again(self):
        response = input('Keep Playing? (y/n) ')

        return response.lower() == 'y'

    # run(): acts as game loop; plays new round while play_again is true and gives final score when game is over
    def run(self):
        play_again = True

        print(len(self.tweets))

        while play_again:
            self.play_round()
            play_again = self.play_again()

        print('Game Over: You played ', self.rounds_played, ' round(s) and had ', self.score, ' correct answer(s)')


def main():
    handles = ['kanyewest', 'elonmusk', 'justinbieber', 'rihanna', 'Oprah', 'Drake', 'BillGates', 'KingJames']

    game = GuessTheTweet(handles)

    game.run()


if __name__ == '__main__':
    main()
