def safe_number_input(prompt, valid_inputs=None, no_reprompt=False):
    """A simple helper function that will safely ask the user for a number input.

    If the user's input is not a number, the user will be re-prompted for another
    input. This will continue until a proper input is given. This behavior can be
    avoided by providing the no_reprompt argument. A list of valid parameters can
    be provided which will prompt a reprompt as well.

    Parameters
    ----------
    prompt: str
        The input prompt given to the user
    valid_inputs: list, optional
        A list of valid inputs. Even if the user's input is a number, if it is not
        in this list, it will be considered invalid (if provided). (default is None).
    no_reprompt: boolean, optional
        Do not reprompt the user for another input if the initial input is invalid.
        (default is False).
    """

    user_input = input(prompt)
    while not user_input.isnumeric() or (valid_inputs and not any([user_input == str(x) for x in valid_inputs])):
        if not user_input.isnumeric():
            print(f'{user_input} is not a valid number.')
        elif valid_inputs and not any([user_input == str(x) for x in valid_inputs]):
            print(f'{user_input} is not a valid input. Valid inputs are {valid_inputs}')
        if no_reprompt:
            break
        user_input = input(prompt)


safe_number_input('input: ', [1, 2, 3], no_reprompt=True)
