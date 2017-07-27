# Git Commands
* ```git status``` checks on modified and added files
* ```git add -A``` adds all modified and added files
* ```git commit -m "All tests passing"``` commits added object that can be pushed
* ```git push``` pushes all modified objects
* ```git pull``` merges from current repo and master
* ```git checkout -b new-branch-name``` switches branches
* ```git remote -v``` find out where you're fetching/pushing from
* ```git remote set-url origin https://github.com/USERNAME/REPOSITORY.git``` set to url
* ```git rm -r *``` deletes everything

# Bash Commands
* ```pwd``` finds current path
* ```deactivate``` deactivates virtual machine
* ```cd /home/ubuntu/workspace``` in case you ever cd out of workspace
* ```cd ..``` cd to parent
* ```pip install -r dev-requirements.txt``` installs necessary modules in txt
* ```pip install -U module-name``` installs or upgrades module
* ```amixer -D pulse sset Master 5%-``` decreases volume by 5%, replace '-' with '+' to increase it
* ```pytest --help``` gives all pytest flags
* ```ls file``` tells if file is present

# Makefile/Bash
* ```@``` commands won't display (normally command would be printed to console and then the execution)
* ```$(VAR)``` variables have ```$()```
* ```&&``` simultaneously execute two commands (necessary to execute files in other directories as a ```cd``` would change the directory for that command *only*)

# C9 Keybindings
* ```tab``` indents highlighted text
* ```tab``` + ```shift``` outdents highlighted text

# Python
* ```help("modules")``` lists out all modules
* ```sys.path``` PYTHONPATH that finds modules ( ```import sys``` first)
* ```sys.path.insert(0, "/path/to/module")``` inserts to PYTHONPATH

# PyTest
* ```assert(add(1, 2)) == 3```
  * This is what you use to literally check everything. Once something does not match, the testing will end. Put assert inside the main() function or a function that the main() calls.
  * Name of function that assert is in must have ```test_``` such as ```test_simple```

# iPython
* ```%paste``` pastes code for you
* ```%autoindent``` can paste code without random indents
