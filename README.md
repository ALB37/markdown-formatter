 # markdown-formatter

 ## About

 This is a simple script for the formatting of basic text formats such as
 markdown files. It takes a text file, reads it line by line, and breaks up
 lines that are longer than 80 characters into lines that are 80 characters or
 less. To work best, your files should not have arbitrary line breaks, rather,
 all paragraphs should be written on one line. There may be issues with more
 complicated formatting, however, this should work for general use cases.

 ***

 ## Getting Started

 Fork and clone this repository to your local machine.

 This script can be called locally using python, e.g., from the directory where
 the script is contained:

 `python mdformat.py <input filepath> <output filepath>`

 Make sure that your output file is not the same as your input file,
 else the program will erase your input file and not run correctly.

 If you'd like to make this script executable, you can take the following
 action (this assumes you are on a unix-based operating system):

 Mark the script as executable:

 `chmod +x mdformat.py`

 note you may need the `sudo` prefix if you get a permissions error.

 Add the directory containing it to your PATH variable.

 If you want this env variable to persist after restarting your terminal,
 you'll have to add this line to your .bashrc or .bash_profile in your home
 dir.

 `export PATH=<path to script>:$PATH`

 To get your `<path to script>`, type `pwd` from inside this project's
 directory, and replace `<path to script>` above with the result of that
 command.

 Following the above, you will then be able to call mdformat.py anywhere in
 your system with the command:

 `mdformat.py <input file> <output file>`

 ***

 ## Contributing

 This is a fairly basic script, and opening an issue/pull request is welcome.

 ***

 ## Author

 Created by Andrew Bloom.
