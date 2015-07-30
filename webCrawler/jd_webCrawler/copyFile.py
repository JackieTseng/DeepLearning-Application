import os,sys, shutil

def sourcecpy(src, des):
    #Get absolute path of folder name
    src = os.path.abspath(src)
    des = os.path.abspath(des)
    if not os.path.exists(src) or not os.path.exists(src):
        print("Folder no exist")
        sys.exit(1)
    #os.chdir(src)
    src_file = [os.path.join(src, file) for file in os.listdir(src)]
    for source in src_file:
        if os.path.isfile(source):
            shutil.copy(source, des)

sourcecpy("test", "test1")
