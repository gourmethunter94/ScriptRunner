from script import EXECUTABLE, MACRO, LOOP
from time import sleep
from keyboard import is_pressed
from threading import Thread
from os import _exit as forced_exit
from commands.errors import ScriptCommandUndefinedValue

RETURN_TO_OLD_POSITION = "return_to_old_position"
MACRO_RUNNING = "macro_running"
ESCAPE_KEY = "escape_key"

DEFAULT_VARIABLES = [
    RETURN_TO_OLD_POSITION,
    MACRO_RUNNING,
    ESCAPE_KEY
]

class ScriptRunner:
    def __init__(self, script, origin_thread=False):
        self.script = script
        self.identifier = self.script.identifier
        commands = dict(script.recognized_commands)
        commands.update(script.macro_commands)
        self.command_functions = commands
        self.custom_values = {
            RETURN_TO_OLD_POSITION:True,
            MACRO_RUNNING:False,
            ESCAPE_KEY:"f12"
        }
        self.origin_thread = origin_thread
        self.continue_looking_for_escape = True
    
    def run(self):
        if self.origin_thread:
            Thread(target=self._end_program).start()
        print("Script runner has begun execution.")
        if self.identifier == EXECUTABLE:
            for command in self.script.blocks[0][1]:
                self._handle_commands(command)
            self.continue_looking_for_escape = False
        if self.identifier == LOOP:
            while True:
                for command in self.script.blocks[0][1]:
                    self._handle_commands(command)
            self.continue_looking_for_escape = False
        if self.identifier == MACRO:
            while True:
                for block in self.script.blocks:
                    if is_pressed(str(block[0])):
                        self._handle_bind(block[1])
                sleep(0.05)
            self.continue_looking_for_escape = False
    
    def _end_program(self):
        while self.continue_looking_for_escape:
            for block in self.script.blocks:
                if is_pressed(self.custom_values.get(ESCAPE_KEY)):
                    print("Closing the macro execution due to user request.")
                    forced_exit(1)
            sleep(0.05)

    def _handle_bind(self, values):
        from commands.execute import ExecuteCommand
        if self.custom_values.get(MACRO_RUNNING) == False:
            self.custom_values.update({MACRO_RUNNING:True})
            ExecuteCommand(None, None).execute_command(values, self.custom_values)
            self.custom_values.update({MACRO_RUNNING:False})
            sleep(0.15)

    def _handle_commands(self, command):
        try:
            execute_values = []
            for value in command.values:
                if value[0] != "$":
                    execute_values.append(value)
                else:
                    variable_value = self.custom_values.get(value[1:])
                    if variable_value:
                        execute_values.append(variable_value)
                    else:
                        raise ScriptCommandUndefinedValue("Undefined variable used to try to define value for a function.")
            self.command_functions.get(command.command).execute_command(execute_values, self.custom_values)
        except KeyboardInterrupt:
            self.continue_looking_for_escape = False
            forced_exit(1)
        except ScriptCommandUndefinedValue as e:
            self.continue_looking_for_escape = False
            raise e
            forced_exit(1)
        except:
            self.continue_looking_for_escape = False
            raise ScriptCommandNotRecognized("Command " + command.command + " or value of the command " + str(command.values) + " not recognized.")

class ScriptCommandNotRecognized(Exception):
    pass