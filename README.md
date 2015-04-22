zfscan
====

zfscan is a gui utility to manage zfs.

### Installation
* Install QT
    * mac - `brew install qt`
    * ubuntu - `apt-get install qt-sdk`

Then the following:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pyside_postinstall.py -install
```

### Run
Once installed you can just run the application: `python zfscanui.py`