import tkinter as tk
from tkinter import filedialog
def chosefile(obj):
	root = tk.Tk()
	root.withdraw()
	if obj == "file":
		Filepath = filedialog.askopenfilename(title="Select file") #获得选择好的文件
		return Filepath
	elif obj=="folder":
		Folderpath = filedialog.askdirectory(title="Select folder") #获得选择好的文件夹
		return Folderpath
	if obj == "hk":
		root = tk.Tk()
		root.withdraw()
		Filepath = filedialog.askopenfilename(title="Select hash key", filetypes=(("Hash key", "*.hk"),)) #获得选择好的文件
		return Filepath
	if obj == "h2k":
		root = tk.Tk()
		root.withdraw()
		Filepath = filedialog.askopenfilename(title="Select hash key", filetypes=(("Hash key 2", "*.h2k"),)) #获得选择好的文件
		return Filepath
	if obj == "zip":
		root = tk.Tk()
		root.withdraw()
		Filepath = filedialog.askopenfilename(title="Select hash key", filetypes=(("File(zip)", "*.zip"),)) #获得选择好的文件
		return Filepath