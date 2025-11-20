"""
This file separates text generated for visiting buildings from Game
"""

DEGREE_BUILDINGS = {'audio_tech','culinary','network_ops','nursing','philosophy'}
PASSES_REQUIRED_PER_DEGREE = 2

def bathroom(pos, ui, player, client):
    """
    Generate a prompt for when you visit the bathroom and get a response from the player. Return pass or fail.
    """
    prompt = client.generate_scenario('bathroom')
    # ui.render(pos, prompt)
    # ui.show_message(prompt)
    answer = ui.prompt_input(prompt)
    # send to gemini for pass/fail
    result = client.assess(prompt, answer)
    test_result = result.lower().strip()
    if 'pass' in test_result:
        player.reset_pee_counter()
    return result

def admin(pos, ui, player, client):
    """
    Generate a prompt for when you visit admin and get response from player. Return pass or fail message.
    """
    prompt = client.generate_scenario('admin')
    # ui.render(pos, prompt)
    # ui.show_message(prompt)
    answer = ui.prompt_input(prompt)
    result = client.assess(prompt, answer)
    test_result = result.lower().strip()
    if 'pass' in test_result:
        player.register()
    # message = result
    # if result == 'pass':
    #     player.register()
    #     message = 'Registration complete! You can now attempt degrees.'
    # else:
    #     message = 'Registration failed. Convince the registrar stronger.'
    
    return result

def degree_building(pos, building, ui, player, game_map, client):
    """
    Generate prompt for when you visit any degree building and get response from player. Return pass or fail message.
    """
    if not player.registered:
        message = 'You must register at admin before attempting degrees.'
        return message
    
    prompt = client.generate_scenario(building)
    # ui.render(pos, prompt)
    # ui.show_message(prompt)
    answer = ui.prompt_input(prompt)
    result = client.assess(prompt, answer)
    test_result = result.lower().strip()
    if 'pass' in test_result:
        player.add_degree_pass(building)
        progress = player.degrees_progress.get(building,0)
    
    return result + f"\n Pass recorded for {game_map.display_names[building]} ({progress}/{PASSES_REQUIRED_PER_DEGREE})"