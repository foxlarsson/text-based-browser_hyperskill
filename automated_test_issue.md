Stage 3 of the project and the requirements for it is described [here](https://hyperskill.org/projects/79/stages/438/implement).

The code is supposed to be run from the terminal with a directory name as an argument. If the directory does not exist, it will be created. It is used to write files, and later read them.

The commands the program accepts when giving the prompt "Type URL":

  * bloomberg.com
  * nytimes.com
  after you enter each of these once, the 'website' is saved to a file in your directory and can be retrieved with
  * bloomberg
  * nytimes
  typos and 'URLs' that do not exist will give an 'error' or 'Invalid URL' output
  * exit - to quit the 'browser'
  * back - to view the previous page
  
 'Back' is implemented using a stack (with deque module), and it's the command I am having issues with. When I run the program on my machine, this command behaves as expected. However, when the automated tests are run, I get the following error:
 "Wrong answer in test #7

The site "New York Times" should be displayed 1 time(s).
Actually displayed: 2 time(s)."

I am unable to replicate this behaviour.

Here are the values the tests are run with (up until the 'back' where the error occurs).

bloomberg.com
bloomberg
exit

nytimes.com
nytimes
exit

nytimescom
exit

blooomberg.com
exit

blooomberg.com
nytimes.com
exit

nytimescom
bloomberg.com
exit

bloomberg.com
nytimes.com
back
exit
