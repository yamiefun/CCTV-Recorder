# CCTV-Video-Recorder

This program can record multiple CCTV videos at the same time using python3 and opencv.
+ Usage:
    ```
    $ python3 main.py -cf <config file path>

    # for example
    $ python3 main.py -cf ./config/config.json
    ```
    + The default path of config file is `./config/config.json`. So if you're not using other config file, you can run with
    ```
    $ python3 main.py
    ```
    + You can stop recording by pressing `Ctrl+c` in command line.
+ You can modify CCTV url in `config/config.json`.
