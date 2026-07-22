# HackerRank: Lists
# Problem Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        # Splitting the input into the 'command' to execute and '*args' is the rest of the string
        command, *args = input().split()
        
        if command == "print":
            print(my_list)
        else:
            # Working: Convert string arguments to integers and execute dynamically
            
            # Detailed working:
            # getattr(my_list, command) is identical to my_list.command
            # Example: getattr(my_list, insert) -> my_list.insert
            
            # map(int, args) -> maps the 'args' (which are strings as of now) to integers.
            # Example: map(int, ["0", "5"]) => [0, 5]
            
            #Now, reslting to getattr(my_list, insert)(*map([0, 5]))
            
            #*map([0, 5]) => prepares the arguments: (0, 5)
            
            # RESULT: my_list.insert(0, 5)
            
            getattr(my_list, command)(*map(int, args))