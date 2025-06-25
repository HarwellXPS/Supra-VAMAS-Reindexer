# Supra-VAMAS-Reindexer
Python code to Reindex VAMAS files for CasaXPS as output by the Kratos ESCApe software

## Credits:
This is an updated version of that from skoopsy (https://github.com/skoopsy/reindex-VAMAS/) to add a basic graphical interface for multiple uses.
Full credit is given to them for the initial version.

## Description:
   This script will read a directory of VAMAS files (.vms) and attempt to re-index the blocks so that each block
   is on the same row. It is very limited and will only work for VAMAS files where every scan set up is similar.
   
## Comments:
  v1.0 is set up so that you can compile it with pyinstaller (with --onfile option) and run a standalone .exe <br />
  Python Version: 3.6.1<br />
  Uses numpy and tkinter<br />
  Note the python executable is significantly larger than the original CLI version
  An executable is also included in the repository
  
## Instructions for use:
  1. Run the Python script and select directory containing your VMS files
  2. Re-indexed files will be saved with the prefix ReIndexed_
  3. Alternatively Use the pre-compiled EXE file
