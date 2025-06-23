### 🎧 What I Learned by looking through the MP3 Media Player Code

I want to do a mp3 player or something similar as my final project, so this gave me some helpful insights

* I know now how a simple GUI with `tkinter`is build -> like creating labels and linking them to a variable using `StringVar()`.

  ```python
  v = StringVar()
  songlabel = Label(root, textvariable=v, width=35)
  ```

* I also found out how to play MP3 files by using `pygame.mixer.music` for that

  ```python
  pygame.mixer.init()
  pygame.mixer.music.load(listofsongs[0])
  pygame.mixer.music.play()
  ```

* I learned how to read metadata stuff like song titles from MP3 files using `mutagen` and ID3 tags:

  ```python
  audio = ID3(realdir)
  realnames.append(audio["TIT2"].text[0])
  ```

* Antoher thing that I got from the file is how to loop through files in a folder and filter only the MP3 files:

  ```python
  for files in os.listdir(directory):
      if files.endswith(".mp3"):
          listofsongs.append(files)
  ```

* The `askdirectory()` function opens a folder selection dialog, which I didn’t know existed:

  ```python
  directory = askdirectory()
  ```

* The code uses global variables like `index` to keep track of the current song. When it goes to the next song, it does this:

  ```python
  index += 1
  pygame.mixer.music.load(listofsongs[index])
  pygame.mixer.music.play()
  ```

* I guess, I learned how to combine file handling, audio playback, and GUI elements into a little mp3 in python

---
