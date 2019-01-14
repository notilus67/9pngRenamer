'''
Created on 19/1/2019

@author: Refate
'''
import os


def BatchReName(path, oldStr, newStr):
    """
    @note: batch rename
    @param path: folder path of target files
    @param oldStr: string to be removed
    @param newStr: string to be replaced with
    @author: Refate 
    """
    
    # open folder
    dirs = os.listdir(path)
    # output all the files and directories
    for file in dirs:
        # get file path
        filePath = os.path.join(path, file)
        
        # is a directory?
        if os.path.isdir(filePath):
           BatchReName(filePath, oldStr, newStr)
        
        if oldStr in file:
            # ("file：" + file + " is renaming...")
            oldFileName = file
            # sequence the files
            # newFileName = num + "." + oldFileName
            # build new filename
            newFileName = oldFileName.replace(oldStr, newStr)
                    
            # rename
            src = os.path.join(path, oldFileName)
            dst = os.path.join(path, newFileName)
            os.rename(src, dst)
            
            print("file：" + file + " is renamed as：" + newFileName)
        
    
if __name__ == '__main__':
    try:
        # keyboard input folder
        path = input("input a directory：");
        
        # is a directory?
        while(not os.path.isdir(path)):
            # input again
            path = input("please input a directory：");
            
        BatchReName(path, ".9.png", ".png")
    except:
        print("input error")
        raise
