MACRO = "macro"
EXECUTABLE = "executable"
LOOP = "loop"

class Script:
    def __init__(self, path):
        self.path = path
        script_file = open(self.path, "r")
        self._read(script_file)

    def _read(self, script_file):
        lines = self._clean_lines(script_file.readlines())
        self.identifier = lines [0]
        if self.identifier == MACRO or self.identifier == EXECUTABLE or self.identifier == LOOP:
            self.lines = lines[1:]
        else:
            raise FileIdentificationError("\nExpected first line of the file \"" + self.path + "\" to be either \"" + MACRO + "\" or \"" + EXECUTABLE + "\". The value on the first line was instead \"" + self.identifier + "\".")

    def _clean_lines(self, lines):
        return_list = []
        for line in lines:
            if len(line) > 0 and line != "\n":
                new_line = ' '.join(line.split())
                new_line = new_line.replace("\n", "")
                new_line = new_line.lower()
                return_list.append(new_line)
        return return_list

class FileIdentificationError(Exception):
    pass