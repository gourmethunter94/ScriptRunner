from commands.errors import ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse

class CommandTemplate:
    def __init__(self, name, handle, command_dictionary, command_handles):
        self.NAME = name
        self.HANDLE = handle
        if command_dictionary.get(self.NAME):
            raise ScriptCommandNameAlreadyInUse("Command name: " + self.NAME + ", already in use.")
        else:
            command_dictionary.update({self.NAME:self})
        if command_handles.get(self.HANDLE):
            raise ScriptCommandHandleAlreadyInUse("Command handle: " + self.HANDLE + ", already in use.")
        else:
            command_handles.update({self.HANDLE:self.NAME})