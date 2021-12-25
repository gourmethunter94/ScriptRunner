from script import EXECUTABLE, MACRO, LOOP
from script_translator import INPUT, WAIT, MOUSE, LOOP, EXECUTE, BIND, MOUSERETURN, PROGRAM, COMMAND
from time import sleep
from keyboard import is_pressed

class ScriptRunner:
    def __init__(self, script):
        self.script = script
        self.identifier = self.script.identifier
        commands = dict(script.recognized_commands)
        commands.update(script.macro_commands)
        self.command_functions = commands
        self.custom_values = {
            "return_to_old_position":True,
            "macro_running":False
        }
    
    def run(self):
        print("Script runner has begun execution.")
        if self.identifier == EXECUTABLE:
            for command in self.script.blocks[0][1]:
                self._handle_commands(command)
        if self.identifier == LOOP:
            while True:
                for command in self.script.blocks[0][1]:
                    self._handle_commands(command)
        if self.identifier == MACRO:
            while True:
                for block in self.script.blocks:
                    if is_pressed(str(block[0])):
                        self._handle_bind(block[1])
                sleep(0.05)
    
    def _handle_bind(self, values):
        from commands.execute import ExecuteCommand
        if self.custom_values.get("macro_running") == False:
            self.custom_values.update({"macro_running":True})
            ExecuteCommand(None, None).execute_command(values, self.custom_values)
            self.custom_values.update({"macro_running":False})
            sleep(0.15)

    def _handle_commands(self, command):
        try:
            self.command_functions.get(command.command).execute_command(command.values, self.custom_values)
        except KeyboardInterrupt:
            exit()
        except:
            raise ScriptCommandNotRecognized("Command " + command.command + " or value of the command " + str(command.values) + " not recognized.")

class ScriptCommandNotRecognized(Exception):
    pass