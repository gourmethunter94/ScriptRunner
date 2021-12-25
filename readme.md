## ScriptRunner

Dependencies
```
pip install pyautogui
pip install keyboard
```

Execute
```
python app.py "absolute/path/to/script/file.sff"
```

Commands
```
mouse # # #        - m  - Mouse button (1, 2, 3), x coordinate, y coordinate.
input c            - i  - Single keyboard character.
mousereturn #      - mr - Determines wether mouse returns to original position after mouse command (1, 2).
execute "path"     - e  - Execute another ScriptRunner file.
wait #             - w  - Wait given (float) time.
command "command"  - c  - Run a command line command in a thread.
program "command"  - p  - Run a command line command without a thread.
bind hotkey "path" - b  - Bind execution of executable script to a hotkey. 
```