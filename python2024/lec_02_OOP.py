
''' 
Confession: 
alias
body
hashtag
id
timestamp
upvotes
comments

'''

'''
Poll : 
alias
body
hashtag
id
timestamp
upvotes
comments

options
vote
'''

import time

class Post:
    id = 0     #class variable
    def __init__(self, p_alias, p_body, hashtag, upvotes, comments) -> None:
        self.alias = p_alias
        self.body = p_body
        self.hashtag = hashtag
        self.id = id
        self.upvotes = upvotes
        self.comments = comments
        self.timestamp = time.time()

        Post.id += 1

    def __repr__(self):
        return f'New Post Id : [{Post.id}] by {self.alias} : {self.body} | \t {self.hashtag} \n {self.upvotes}^ : Upvotes | Comments : {self.comments}'


post1 = Post("lazy-owl-445", 'Great Morning Coffee Makes a great Day!', '#MorningCoffee',0,0)
# print(post1)

post2 = Post("active-user-216", 'What should be new Cafe Name ?','#newcafe',1, 0)
# print(post2)

post3 = Post("witty-kitty-001", "I love cats, they should be allowed in campus.", "#catlover", 0, 1)
print(post2.alias)