# MCFC
Python module for color print using Minecraft color codes.


## Compatibility
MCFC works with Linux, Windows. On Windows true color needed Windows Terminal, classic terminal is limited to 16 colors. 
Requirements Python 3.8+.


## Functions
- `f_print(*__prompt: str)`


## Installing
#### Linux:
> ```bash
>    python3 -m pip install mcfc
> ```
#### Windows:
> ```bash
>    pip install mcfc
> ```


## Using
### Input
> ```py
> import mcfc
> 
> 
> def hello(opt):
>     mcfc.f_print('&aHello', opt, '!')
> 
>
> hello('World')
> ```

### Output
![image](https://cdn.discordapp.com/attachments/1004866892466495538/1027243927620833330/unknown.png)
