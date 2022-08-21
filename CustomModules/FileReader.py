class FileReader:

    def __init__(self, input_file):
        self.file = input_file
        self.list_of_lines = []

    def GetLineNumber(self, input_string):
        """
        Gets the line number where a specified string occurs at.

        Keyword Arguments:
            input_string -- The string to search for

        Returned Values:
            line_number -- The line number that input_string occurs at.
        """

        for line_number, line in enumerate(self.list_of_lines, 0):
            if input_string in line:
                return line_number

    def GetFileLines(self):
        """
        Gets all of the file's lines and stores them in memory for use.

        Keyword Arguments:
            file -- The file to read from.
        Returned Values:
            list_of_lines -- A list containing all of the lines of text in the file.
        """
        self.list_of_lines = []
        a_file = open(self.file, "r", encoding='utf8')
        self.list_of_lines = a_file.readlines()
        a_file.close()

    def WriteChangesToFile(self):
        """
        Replaces the given file's contents with the provided text.

        Keyword Arguments:
            file -- The file to write to.
            list_of_lines -- A list containing all of the lines of text in the file.
        """
        a_file = open(self.file, "w", encoding='utf8')
        a_file.writelines(self.list_of_lines)
        a_file.close()
