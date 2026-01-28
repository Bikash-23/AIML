# Modes
# r : reading[defult]
# w : writing,truncates file first
# x : create new & open for writing
# a : writing, appends at end 
# b : binary mode 
# t : text mode[defult] 
# + : opens disk file for update(r & w)


# f = open("sample3.txt","x")
# f.write("Hello sample file 3")

# f.close()


# Opening file:
# reading: r 
# writing : truncate ? yes -> w ; no -> a
# reading & writing : truncate ? yes -> w+ ; no -> intial Posidion? begin-> r+ ; end -> a+