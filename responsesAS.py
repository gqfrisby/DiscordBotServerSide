#======================================================================
#   Author:         Aaron Shingleton
#   Last Modified:  10/12/2023
#   Purpose:        Skeleton info of implementing bot response messages
#======================================================================

def handle_response(message) -> str:
    # Parse all input as lowercase variant
    p_message = message.lower()

    if (p_message == 'Message to respond to'):
        # Perform appropriate reaction
        return 'Here is a filler response, as a message.'