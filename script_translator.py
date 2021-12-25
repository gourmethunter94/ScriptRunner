from script import EXECUTABLE, MACRO, LOOP
from script import Script
from commands.errors import ScriptCommandNotViableInFileType, ScriptInvalidScriptType, ScriptCommandNotRecognized, ScriptCommandNoValueGiven

from commands.input import InputCommand
from commands.wait import WaitCommand
from commands.mouse import MouseCommand
from commands.execute import ExecuteCommand
from commands.mouse_return import MouseReturnCommand
from commands.command import CommandCommand
from commands.program import ProgramCommand
from commands.escape_key import EscapeKeyCommand

from commands.bind import BindCommand

INPUT = "input"
WAIT = "wait"
MOUSE = "mouse"
EXECUTE = "execute"
PROGRAM = "program"
COMMAND = "command"

BIND = "bind"

MOUSERETURN = "mousereturn"

class ScriptTranslator:
    def __init__(self, script):
        self.identifier = script.identifier

        self.recognized_commands = {}
        self.short_handles = {}

        InputCommand(self.recognized_commands, self.short_handles)
        WaitCommand(self.recognized_commands, self.short_handles)
        MouseCommand(self.recognized_commands, self.short_handles)
        ExecuteCommand(self.recognized_commands, self.short_handles)
        MouseReturnCommand(self.recognized_commands, self.short_handles)
        CommandCommand(self.recognized_commands, self.short_handles)
        ProgramCommand(self.recognized_commands, self.short_handles)
        EscapeKeyCommand(self.recognized_commands, self.short_handles)

        self.macro_commands = {}

        BindCommand(self.macro_commands, self.short_handles)

        self.blocks = self._translate(script)
    
    def _translate(self, script):
        blocks = []
        if self.identifier == MACRO:
            for line in script.lines:
                parts = line.split(" ")
                command = self._check_short_handle(parts[0])
                if command in self.recognized_commands and not command in self.macro_commands:
                    raise ScriptCommandNotViableInFileType("Command on line \"" + line + "\" is not supported on macro files.")
                command_object = self.macro_commands.get(command)
                if command_object:
                    values = parts[1:]
                    command_object.confirm_validity(values, line, blocks)

        elif self.identifier == EXECUTABLE or self.identifier == LOOP:
            block = []
            for line in script.lines:
                parts = line.split(" ")
                command = self._check_short_handle(parts[0])
                if command in self.macro_commands and not command in self.recognized_commands:
                    raise ScriptCommandNotViableInFileType("Command on line \"" + line + "\" is not supported on " + self.identifier + " files.")
                command_object = self.recognized_commands.get(command)
                if command_object:
                    values = parts[1:]
                    if len(values) == 0:
                        raise ScriptCommandNoValueGiven("No value given to command on line \"" + line + "\".")
                    command_object.confirm_validity(values, line)
                    if command_object.finalization_exception:
                        command_object.translation_finalization_exception(values, block, line)
                    else:
                        block.append(Command(command, values))
                else:
                    raise ScriptCommandNotRecognized("Line \"" + line + "\" could not be translated.")
            blocks.append((self.identifier, block))
        return blocks

    def _check_short_handle(self, handle):
        if self.short_handles.get(handle):
            return self.short_handles.get(handle)
        return handle

class Command:
    def __init__(self, command, values):
        self.command = command
        self.values = values