import os
import sys
import fnmatch
import shutil
import re
from tqdm import tqdm

def file_move(s_path,d_path, s_set):
    processed_files=[]
    pattr = re.compile("[(][0-9]+[)].jpg$")
    pbar = tqdm(total=len(s_set))
    for file in s_set:
        pbar.update(1)
        if file not in processed_files:
            match_obj = pattr.search(file)
            if match_obj:
                search_str = file[:match_obj.start()].rstrip()
                if not set(search_str).isdisjoint(set(processed_files)):
                    pass
                else:
                    new_name = search_str+".jpg"
                    shutil.copy2(s_path + "/" + file, d_path)
                    os.rename(d_path+"/"+file,new_name)
                pass
            else:
                shutil.copy2(s_path +"/" + file, d_path)
                processed_files.append(file[:-4].rstrip())
        else:
            pass



def check_names():
    source_set = frozenset(fnmatch.filter(os.listdir(sys.argv[1]),"*.jpg"))
    dest_set = frozenset(fnmatch.filter(os.listdir(sys.argv[2]),"*.jpg"))
    if source_set.isdisjoint(dest_set):
        print("Ready to Process")
        file_move(sys.argv[1], sys.argv[2], source_set)
    else:
        print("Source and destination contain common files!!!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: sourcedir targetdir")
        exit(0)
    else:
        if not os.path.isdir(sys.argv[1]):
            print("Invalid source directory")
            exit(0)
        elif not os.path.isdir(sys.argv[2]):
            print("Invalid destination directory")
            exit(0)
        elif not (os.access(sys.argv[1], os.W_OK) and os.access(sys.argv[2], os.W_OK)):
            print("No proper source or destination access rights!")
        else:
            check_names()
            print("Operation completed sucessfully!!!")
            exit(0)

