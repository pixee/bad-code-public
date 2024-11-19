from flask import session

def process_input(golem):
    """
    Process the user input and store it in the session.
    """
    if golem is not None:
        golem = golem.replace(".", "").replace(
            "_", "").replace("{", "").replace("}", "")

    if "golem" not in session or session['golem'] is None:
        session['golem'] = golem
