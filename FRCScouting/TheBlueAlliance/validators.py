def validate_teamkey(teamkey):
    try:
        value = int(teamkey)
    except ValueError:
        return False
    if value < 1:
        return False
    length = len(str(teamkey))
    if length > 4:
        return False
    return True
