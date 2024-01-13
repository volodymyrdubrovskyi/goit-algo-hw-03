import sys, os, shutil
from pathlib import Path


def folder_processor(init_folder:Path, dest_folder:Path):
    for child in init_folder.iterdir():
        if child.is_dir():
            folder_processor(child, dest_folder)
        else:
            target_folder = os.path.join(str(dest_folder), child.suffix.replace('.',''))
            #print(target_folder)
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
            shutil.copy(child, target_folder)
            


def main():
    #print('Argument(s) passed: {}'.format(str(sys.argv)))
    if len(sys.argv) > 1:
        init_folder = Path(sys.argv[1])
        try:
            dest_folder = Path(sys.argv[2])
        except:
            dest_folder = Path('dist')
        #print(init_folder)
        print('Innitial folder corrected? >>> ', init_folder.is_dir())

        if init_folder.is_dir():
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            print('All parameters are correct. Processing...')
            folder_processor(init_folder, dest_folder)
            print('Sucesfully Done.')
        else:
            print("Error: 'folder for parcing' command line parameter incorrect...")    
    else:
        print("Error: 'folder for parcing' command line parameter required...")

if __name__ == "__main__":
    main()