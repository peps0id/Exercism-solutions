EXPECTED_BAKE_TIME = 40
def bake_time_remaining(time_in_oven):
    """Calculate the remaining bake time.
    Parameters:
    time_in_oven (int): The time spent in oven
    Returns the time which is remaining
    """
    return EXPECTED_BAKE_TIME - time_in_oven
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time of preparation.
    Parameters:
    number_of_layers (int): The number of layers
    Returns the time which is needed to prepare the layers for the lasagna
    """
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time  (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
"""
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
