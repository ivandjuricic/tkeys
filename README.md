# TkKeys

* Have a touch-screen but you think other system keyboards are overkill?
 
* You just need numeric keyboard?

* You want something as simple as possible? 

### Then just go with TkKeys

## Installation

* Clone the repo ```git clone https://github.com/ivandjuricic/tkeys```

* Browse to directory: ```~$: cd tkeys```

* Install: ```~$: python setup.py install```

* Requirements: 
    * for Python2: 
        * future


## Usage

* Make a tkinter gui. Eg:

```python
from tkinter import *


class Main:
    def __init__(self, master):
        self.master = master
        self.entry_widget = Entry(self.master)
        self.entry_widget.pack()
        
root = Tk()
app = Main(root)
root.mainloop()
```

* import tkeys keyboard: ```from tkeys.numeric_keypad import NumKeyPad``` 

* add to class when all entry widgets are loaded ```NumKeyPad(self.master)``` 

* Code you will end up: 

```python
from tkinter import *
from tkeys.numeric_keypad import NumKeyPad


class Main:
    def __init__(self, master):
        self.master = master
        self.entry_widget = Entry(self.master)
        self.entry_widget.pack()
        
        NumKeyPad(parent=self.master)
        
root = Tk()
app = Main(root)
root.mainloop()
```

* Uppon running the script when you focus and Entry widget, Numeric keyboard will show up at in UI

* Use "b" button for backspace



## TODOs

* Make better looking UI

* Add a close key

* Manipulating tkKeys interface to fit any other user interace with simple keyword arguments

* Make a full on-screen keyboard

* Fix bindings of exit keyboard


## Support

Please [open an issue](https://github.com/ivandjuricic/tkKeys/issues/new) for support.

## Contributing

Feel free to contribute, add suggestions and comments