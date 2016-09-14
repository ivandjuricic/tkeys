# tkeys

* Have a touch-screen but you think other system keyboards are overkill?
 
* You just need numeric keyboard?

* You want something as simple as possible? 

#### Then just go with tkeys

## Features

#### - tkinter keyboard with only one line of code

#### - browsing trough all entry widgets of the given parent

#### - work with grid, pack and place layout manager

#### - compatible with tkinter button styles (background, foreground colors, fonts etc)

#### - placement of the keyboard can be changed

## Installation

* Clone the repo ```git clone https://github.com/ivandjuricic/tkeys```

* Browse to directory: ```~$: cd tkeys```

* Install: ```~$: python setup.py install```


or with pip:
```~$: pip install git+https://github.com/ivandjuricic/tkeys```


## Requirements: 
### For Python2: 
* future

### For Python3:
* you're all set


## Usage

* Make a tkinter gui. Eg:

```python
from tkinter import *


class Main:
    def __init__(self, master):
        self.master = master
        self.entry_widget1 = Entry(self.master)
        self.entry_widget1.pack()
        self.entry_widget2 = Entry(self.master)
        self.entry_widget2.pack()
        
root = Tk()
app = Main(root)
root.mainloop()
```

* import tkeys keyboard: ```from tkeys.numeric import NumKeyPad``` 

* add ```NumKeyPad(parent=self.master)``` to  the end of the \__init__ of the tkinter GUI class  

* Code you will look something like this: 

```python
from tkinter import *
from tkeys.numeric import NumKeyPad


class Main:
    def __init__(self, master):
        self.master = master
        self.entry_widget1 = Entry(self.master)
        self.entry_widget1.pack()
        self.entry_widget2 = Entry(self.master)
        self.entry_widget2.pack()
        
        NumKeyPad(parent=self.master)
        
root = Tk()
app = Main(root)
root.mainloop()
```

* Uppon running the script when you focus and Entry widget, Numeric keyboard will show up at in UI

* Use "←" button as backspace (deletes last key entered)

* Use "↵" button when entered correct number to advance to second Entry widget input



## TODOs

* Make better looking UI - done

* Add a close key

* Manipulating tkKeys interface to fit any other user interace with simple keyword arguments

* Make a full on-screen keyboard

* Fix bindings of exit keyboard


## Support

Please [open an issue](https://github.com/ivandjuricic/tkKeys/issues/new) for support.

## Contributing

Feel free to contribute, add suggestions and comments