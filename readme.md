# ScriptRunner

Simple tool to run and develope scripts that control keyboard and mouse

Dependencies
```
pip install pyautogui
pip install keyboard
pip install opencv-python
pip install numpy
```

Execute
```
python app.py "absolute/path/to/script/file.sff"
```

Commands
```
mouse # # #                    - m  - Mouse button (1, 2, 3), x coordinate, y coordinate.
input c                        - i  - Single keyboard character.
mousereturn #                  - mr - Determines wether mouse returns to original position after mouse command (1, 2).
execute "path"                 - e  - Execute another ScriptRunner file.
wait #                         - w  - Wait given (float) time.
command "command"              - c  - Run a command line command in a thread.
program "command"              - p  - Run a command line command without a thread.
set "variable" #               - s  - Sets numeric value # to given variable "variable".
plus "variable" #              - pl - Increases value of variable "variable" by numeric value #.
minus "variable" #             - mi - Decreases value of variable "variable" by numeric value #.
mouseposition "var1" "var2"    - mp - Sets x coordinate of mouse to variable "var1" and y coordinate to variable "var2".
findimage "var1" "var2" "path" - fi - Tries to find image from "path" from main monitor, sets x coordinate of closest match to variable "var1" and y coordinate to variable "var2".
escapekey c                    - ek - Changes escape key to key c.
bind hotkey "path"             - b  - Bind execution of executable script to a hotkey.
```