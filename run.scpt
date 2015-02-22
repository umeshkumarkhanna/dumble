tell application "iTerm"
make new terminal
tell the current terminal
activate current session
launch session "Default Session"
tell the last session
write text "cd ~/Desktop/dumble; clear; git add -A; git commit -m 'Made with magic'; git push"
end tell
end tell
end tell