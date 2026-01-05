# Growtopia-PythonBot

This is a Python-based bot for the game **Growtopia** designed to automate certain tasks and provide an efficient way to interact with the game. It is build using python and can be easily modified.

## Features

- **Cross-platform support** for Windows, Linux.
- Automates common in-game actions.
- Easy to use and extend with additional features.

## Requirements

- C/C++ compiler (Clang, etc) ( Change CXX in Makefile if you use other than clang)
- Python 3.12
- Make

## Install Dependencies

Generate enet shared lib and install the required libraries:
```shell
$ make
$ make dev
```

## Usage

1. Clone the repository:
```shell
$ git clone https://github.com/Freennzzy/Growtopia-PythonBot.git
```
2. Navigate to the project directory:
```shell
$ cd Growtopia-PythonBot
```
3. Run the bot:
```shell
$ python -m core.main
```

## Credits

This project is based on the work by [CLOEI](https://github.com/CLOEI/gt.python), who is the original author of the Growtopia Python bot. This version includes some custom modification and additional features.

- Original author: [CLOEI](https://github.com/CLOEI)
- Code Parser by: [badewen](https://github.com/badewen/Growtopia-Things)

## License

This project is open-source and available under the [MIT License](https://github.com/Freennzzy/Growtopia-PythonBot/blob/main/LICENSE)