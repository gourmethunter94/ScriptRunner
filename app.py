from script_runner import ScriptRunner
from script_translator import ScriptTranslator
from script import Script
from sys import argv as ARGUMENTS

try:
    path = ARGUMENTS[1]
except IndexError:
    exit(print("Path to the script file was not given."))

script_file = Script(path)
translator = ScriptTranslator(script_file)
runner = ScriptRunner(translator, origin_thread=True)

try:
    runner.run()
except KeyboardInterrupt:
    print("Keyboard Interrupt recieved, terminating the program.")
    exit(print("Program terminated."))