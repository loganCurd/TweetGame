# TweetGame
Tweet guessing game using python and twitter api.

# Description
This is a simple game where the user has to guess the author of a random tweet. The tweets are pulled from a variety of different twitter handles which are stored in a 'handles' list. Each handle is used in the param argument of an api call to the twitter api. All tweets are then filtered to check if they are retweets or otherwise invalid before being put inside a Tweet object and appended to a list. A random tweet is then displayed with four possible choices for the author. If the user guesses correctly, their score is incremented, and with enough correct answers in a row the user can earn a streak.

# What I Learned
This project was a good chance to practice my python skills, but the most important thing I learned was how to call APIs programmatically. First, I used Postman to trouble shoot the API endpoint and learn what paramaters to include as well as how to get authorization. Next, I read the documentation on the requests library and then used that library to implement the API calls into my program. Going forwards, I feel as though I have a much better understanding of APIs and am much more confident with making requests, specifically in python.

# What I Would Do Differently
I think this game could be improved with a proper interface. In hindsight, it would have been better to build this game using javascript/HTTML/etc. so that I could create a web page that the user could interact with. It would also be nice if I could display the pictures and emojis that are contained in some of the tweets. It is possible that I may revisit this in the future and make some of these changes. Overall, I was pretty happy with how the game turned out and it was a great learning experience.
