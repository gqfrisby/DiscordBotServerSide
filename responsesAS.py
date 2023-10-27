#======================================================================
#   Author:         Aaron Shingleton
#   Last Modified:  10/12/2023
#   Purpose:        Skeleton info of implementing bot response messages
#======================================================================

def get_response(message: str) -> str:
    # Parse all input as lowercase variant
    p_message = message.lower()

    if p_message == '!ping':
        # Perform appropriate reaction
        return 'Pong!'
    else:
        return None