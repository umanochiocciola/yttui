# yttui
YouTube TUI - Watch videos without even opening the browser


## Installation

clone and cd in the directory, then run
```./install.sh```
this will make the yttui command avaiable

## Requirements
python 3.8+
mvp (```apt install mpv```)

## Usage
to start, just run
```yttui```
then search for something and follow instrucitons.
There are additional arguments you can use:
```
usage:
    yttui <search prompt> interval-len <len> max-len <len>

interal-len is optional, change <len> to the amount of titles you wish to be displayed per chunk (default 5)
interal-len is optional, change <len> to the amount of titles you wish to be loaded (default 50)
```
type ```yttui help``` to see this message.

## Lag
If your video lags, it's becaus mpv will try to get the best quality, to make it less laggy, put

```
ytdl-format=bestvideo[height<=?480]+bestaudio/best
```

in ```~/.config/mpv/mpv.conf```

(change that 480 to the max quality you wanna accept)
