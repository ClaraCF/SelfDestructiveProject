# Self-destructive Project

The title is pretty self explanatory. This is a project that deletes itself in its entirety and then pops back again. That's about it.  
This is literally the most complex project I've ever worked with and it's for such a stupid and mundane task...what is wrong with me?  
  
This little project will basically close, back up all files in the current directory to memory, recursively delete everything, then wait a couple seconds, write all data from memory back to disk and pop back open again.  

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/Claracf/SelfDestructiveProject) 
![GitHub](https://img.shields.io/github/license/ClaraCF/SelfDestructiveProject) 
![GitHub last commit](https://img.shields.io/github/last-commit/ClaraCF/SelfDestructiveProject) 
![This is so dumb](https://img.shields.io/badge/this%20is-so%20dumb-blue)  
<br>


## Installation

To be able to use this project, you first need to install the required packages for it to work. 
Required packages are listed in the requirements.txt file, and you can install them by using pip. 
```bash
pip install -r requirements.txt
```  
The way this project works is it recursively searches for all the files contained in its directory and stores them in memory, so keep that in mind if you (for whatever reason) decide to add to this project.  
You might want at least 400 Mb of RAM available on the target system, though this number will likely go up should you add more files to the project's working directory.  
<br>


## Usage

Just use your usual python installation to run the script, open up a file manager and enjoy the show.  
```bash
python main.py
```  
<br>


## Contributing

Pull requests are welcome and greatly appreciated.  
If you find a bug or think of a suggestion or improvement, opening an issue would help out a lot!  
<br>


## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license, so feel free to use this project to your liking, tweak or change stuff around or whatever. This is a dumb project anyways.  
