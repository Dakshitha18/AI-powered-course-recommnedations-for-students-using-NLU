#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\..\..\..\..\Jupyter Notebook\.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass

