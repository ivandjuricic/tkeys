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
from tkeys.keyboards import NumKeyPad
# for alphanumeric keyboard use:
from tkeys.keyboards import AlphaNumericKeyPad


class Main:
    def __init__(self, master):
        self.master = master
        self.entry_widget1 = Entry(self.master)
        self.entry_widget1.pack()
        self.entry_widget2 = Entry(self.master)
        self.entry_widget2.pack()
        
        NumKeyPad(parent=self.master)  # or
        # AlphaNumericKeyPad(parent=self.master)
        
root = Tk()
app = Main(root)
root.mainloop()
```

* Uppon running the script when you focus and Entry widget, Numeric keyboard will show up at in UI

* Use "←" button as backspace (deletes last key entered)

* Use "↵" button when entered correct number to advance to second Entry widget input


## Keyboard usage

* Two types of keyboard available: Numeric and AlphaNumeric

* Since everything is done to be compact, alphanumeric keyboard was built as a telephone keyboard

* Two layouts are available: "line" or "grid"

* Keyboards can have two way of placement:
    * side(*bottom* or *right*) - places keyboard to the respective side
    * place (*relx*, *rey*, *anchor*) - places keyboard to relative
        * relx: place on relative horizontal(x) position - values from 0 to 1
        * rely: place on relative vertical(y) position - values from 0 to 1
        * anchor: point that will be place to position taken as side of world
            * values= "center", "n", "ne", "e", "se", "s", "sw", "w", "nw"
            
* **Keys Styling**: You can add styling to keyboards button in the style of tkinter buttons stylings
    * eg
    
        ```python    
        class Main:
            def __init__(self, master):
                self.master = master
                self.entry_widget1 = Entry(self.master)
                self.entry_widget1.pack()
                self.entry_widget2 = Entry(self.master)
                self.entry_widget2.pack()
                
                NumKeyPad(self.master,
                          layout="line",
                          side="bottom",
                          bg="dark blue",
                          fg="white",
                          font=("tahoma", 20))
        ```

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