absolute = [1101225873924948069]
noobs = {}

def is_allowed(user_id, command):
    if user_id in absolute: return True
    if user_id in noobs and noobs[user_id] == command: return True
    return False
