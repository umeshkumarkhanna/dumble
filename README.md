![media/header.jpg](Dumble App)
## Installation

Make sure you have all the dependencies installed: `pip install -r /path/to/requirements.txt`

## Why?
Because rocking a personal Jarvis (the one from Iron Man) is awesome. The technology's there, but there hasn't been a fully customizable Siri for Mac... until now.

## Example API

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

## [Video Demo](https://fang.ws/scr/2015-02-22_1243.swf)
## [Sample Config](https://gist.github.com/AndyF/f07ace417e0d79fd7d79)