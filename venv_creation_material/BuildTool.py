import os
import sys
import shutil
import subprocess
# import time

WorkingDir = os.getcwd()
SourceCodeDir = os.path.join(WorkingDir, 'SourceCode')
BuildDistDir = os.path.join(SourceCodeDir, 'dist')
BuildDir = os.path.join(SourceCodeDir, 'build')
#LogoDir = os.path.join(SourceCodeDir, 'imgs')
#Logo = os.path.join(LogoDir, 'magnifier.ico')
PyToolFileName = 'DetectCursorPosition.py'
PyToolFilePath = os.path.join(SourceCodeDir, PyToolFileName)
ExeToolFileName = 'DetectCursorPosition.exe' #should be same as PyToolFileName
ExeToolFilePath = os.path.join(BuildDistDir, ExeToolFileName)
ExeToolOutputFilePath = os.path.join(WorkingDir, ExeToolFileName)
# BuildTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# BuildCommand = ['pyinstaller','-F','-w',PyToolFilePath,'-i',Logo]
BuildCommand = ['pyinstaller','-F',PyToolFilePath]

if __name__ == '__main__':
	print("Build Start!")
	os.chdir(SourceCodeDir)
	if os.path.exists(ExeToolFilePath):
		os.remove(ExeToolFilePath)
		print("Remove file: %s" %ExeToolFilePath)
	
	if os.path.exists(ExeToolOutputFilePath):
		os.remove(ExeToolOutputFilePath)
		print("Remove file: %s" %ExeToolOutputFilePath)
	
	if os.path.exists(BuildDir):
		shutil.rmtree(BuildDir)
		print("Remove build tree: %s" %BuildDir)
	
	#Build process
	try:
		print("Build Command = %s" %BuildCommand)
		process = subprocess.Popen(BuildCommand, shell = True, stdout = subprocess.PIPE, stdin=subprocess.PIPE, stderr = subprocess.PIPE)
		process_out, process_err = process.communicate()
		#pOutput = process_out.decode('utf-8')
		print(process_out)
	except:
		print("Build process is failed!!!")
		sys.exit()
	
	if os.path.exists(ExeToolFilePath):
		print("Build Done!")
		shutil.copy2(ExeToolFilePath, os.path.join(WorkingDir))

	os.chdir(WorkingDir)