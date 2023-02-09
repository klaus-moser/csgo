# csgo

Script to build and run before joining a CS:GO match.
It will drag the mouse to the center of the screen and click, until F11 is pressed or 10 minutes passed.

# Install/Use

1. Clone repo
2. CD to project folder
3. Activate virtual environment
4. use 'pyinstaller' to build an executable:

```bash
pyinstaller --onefile main.py
```
5. Afterwards you'll find a 'main.exe' in the new folder 'dist'.

## License

[MIT](https://choosealicense.com/licenses/mit/)
