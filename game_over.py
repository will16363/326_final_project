def game_over(health, round_num):
    """Determines when the game of Zombie Rolls is officially over. The game is 
       considered over if the player has no health left or has defeated the 
       final zombie at round 13.
    
    Args:
        health (int): The health of the player expressed as an integer
        round_num (int): The round number expressed as an integer

    Returns:
        game_status (bool): The status of the game, True if the game is over, 
            otherwise False.
    """
    return health == 0 or round_num == 13