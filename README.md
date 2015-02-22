![media/header.jpg](Dumble App)
## Installation

Make sure you have all the dependencies installed: `pip install -r /path/to/requirements.txt`

## Why?

## API

Dumble has an API that allows you to create your own commands. To do so, simple create a [GitHub Gist](https://gist.github.com/) titled `Dumble Settings`.

![media/gist.png](Demo Settings)

Each command has a trigger word and its corresponding actions. To define the trigger word, create a new .txt file within that Gist. The contents of that file (in AppleScript) will be executed when the trigger phrase is pronounced while Dumble is listening.

- **Open File**: `activate application "Google Chrome"`
- **Resize Window**: `window/topHalf.scpt`
	- `window/botHalf.scpt`
	- `window/leftHalf.scpt`
	- `window/rightHalf.scpt`
	- `window/botLeft.scpt`
	- `window/botRight.scpt`

