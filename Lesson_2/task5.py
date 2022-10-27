userList = [int(x) for x in input().split(',')]

print("Maximum element of thr list: " + str(max(userList)))
userList.remove(max(userList))

print("Minimum element of thr list: " + str(min(userList)))
userList.remove(min(userList))

print("Sum of the other elements of the list: " + str(sum(userList)))
