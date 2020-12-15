friends = ["Hongjoong", "Seonghwa", "Yunho", "Yeosang", "San", "Mingi", "Wooyoung", "Jongho", 8, 1, True]
#index starts from zero, hongjoong is zero element
print(friends)
print(friends[4])
print(friends[-2])
print(friends[0:])
print(friends[0:8])
#excludes element with index 8, or element whose index is after :
friends[10] = "team"
print(friends[10])