##### for statements
words = ['rahul', 'sakshi', 'rohit']
for w in words:
    print(w, len(w))

users = {"hans": "active", "lons": "inactive", "fan": "active", "lolz": "inactive"}
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)

active_users = {}
for user, status in users.items():
    if status == "inactive":
        active_users[user] = status
print(active_users)
