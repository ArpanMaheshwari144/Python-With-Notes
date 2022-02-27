post = input("Enter the post: ")
name = input("Enter your name to check whether your name is getting discussed on the post or not: ")

# find ignores uppercase, lowercase and all other cases specially in string
if(post.find(name)):
    print("Yes given post is talking about", name)
else:
    print("No given post is not talking about", name)


