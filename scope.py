name = "Dave"
count = 1

def another():
    colour = "blue"
    global count
    count += 1
    print(count)
    
    def greeting(name):
        print(colour)
        print(name)
    greeting("Dave")

another()