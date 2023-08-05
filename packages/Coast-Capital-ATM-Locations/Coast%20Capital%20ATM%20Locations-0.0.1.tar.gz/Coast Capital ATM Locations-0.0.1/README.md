# Coast Capital ATM Locations
This is a simple script that will go to the Coast Capital Credit Union website and collect the location of all the ATMs that you can use if you are a member of that credit union.
The script will create two files in the directory it which it was started, _Coast Capital ATMs.csv_ and _Coast Capital ATMs.gpx_. As the names imply the first is a comma separated list of locations and the second is a gpx file that can be read by most geolocation applications (such as Viking). 
I wrote this script so I could load all the locations onto my GPS device and take them when I am traveling.

This is the very first script I have made into a package for upload to PyPI so if you have any suggestions or comments please let me know.
## Installation
Ues the package manager pip to install this script.
```bash
pip install CCatm
```
## Usage
To use this script all you need to do is install it and then type the name to run it.
```bash
get_CC_ATMs.py
```
## Contributing
Pull requests are welcome.
## License
