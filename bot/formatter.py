def format_player_list(players):
    if players.online == 0:
        return "There is currently nobody online"

    if players.max:
        result = f"There are {players.online}\{players.max} players online"
    else:
        result = f"There are {players.online} players online"

    if players.sample:
        plist = ", ".join([player.name for player in players.sample])
        result += f"\nIncluding: {plist}"
    return result