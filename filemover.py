import os, sys, shutil

fullpath = os.path.join

CURRENT_DIR = os.getcwd()
RESULT_FOLDER_NAME = 'results'
EXTENSIONS = ['.' + arg if len(sys.argv) > 1 and arg[0] != '.' else arg if len(sys.argv) > 1 else '' for arg in sys.argv[1:]]
RESULT_FOLDER_PATHS = [fullpath(CURRENT_DIR, RESULT_FOLDER_NAME, ext) for ext in EXTENSIONS]
SUBFOLDER_PATHS = [f.path for f in os.scandir(CURRENT_DIR) if f.is_dir() and f.name != RESULT_FOLDER_NAME and f.name != '.git']

if EXTENSIONS:
    print("\nfilemover running...")

    files_to_move = []
    for ext in EXTENSIONS:
        for path in SUBFOLDER_PATHS:
            for (dir, dirs, files) in os.walk(path):
                for file in files:
                    if file.endswith(ext):
                        files_to_move.append(fullpath(dir, file))

    if not files_to_move:
        print('There is no file with this extension within any of the sub directories!\n')
        exit()

    for path in RESULT_FOLDER_PATHS:
        for file in files_to_move:
            if file.endswith(os.path.basename(path)):
                newFile = fullpath(path)
                os.makedirs(newFile, exist_ok=True)
                shutil.move(file, newFile)
                print(f'{file} -> {newFile}')
                    
    print(f'Moved {len(files_to_move)} files!\n')
else:
    print('No extension arguments specified!')