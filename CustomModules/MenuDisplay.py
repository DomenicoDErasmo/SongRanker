def DisplayMenu():
    """
    Displays menu options for the program user.
    """
    print("--------------------------------------------------------------------")
    print("Input\t\t\t\t Action")
    print("--------------------------------------------------------------------")
    print("Compare Songs\t\t Rank songs head to head")
    print("Change K Value\t\t Changes the k value used in Elo calculations")
    print("Display Top Songs\t Show your highest ranked songs")
    print("View Song\t\t\t Get info for a specific song")
    print("Exit\t\t\t\t Exits the program")
    print("Reset Songs\t\t\t Reset ELO scores for all songs")
    print("--------------------------------------------------------------------")


def PromptInput():
    """
    Asks the program user for an input command.
    """
    DisplayMenu()
    input_command = input("What would you like to do?\n")
    return input_command
