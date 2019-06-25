
def get_teaminfo(teamkey):
    #TODO : Send Request to TBA.com

    #TODO : Parse Request

    #TODO : Save to database

    #TODO : return
    return teamkey

def validate_teamkey(teamkey):
    try:
        value = int(teamkey)
    except ValueError:
        return False
    length = len(str(teamkey))
    if length > 4 and length < 3:
        return False
    return True
