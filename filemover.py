import os, sys, shutil

fullpath = os.path.join

CURRENT_DIR = os.getcwd()
RESULT_FOLDER_NAME = 'results'
EXTENSION = '.' + sys.argv[1] if len(sys.argv) > 1 and sys.argv[1][0] != '.' else sys.argv[1] if len(sys.argv) > 1 else ''
RESULT_FOLDER_PATH = fullpath(CURRENT_DIR, RESULT_FOLDER_NAME, EXTENSION)
SUBFOLDER_PATHS = [f.path for f in os.scandir(CURRENT_DIR) if f.is_dir() and f.name != RESULT_FOLDER_NAME]

print("\nfilemover running...")
os.makedirs(RESULT_FOLDER_PATH, exist_ok=True)
files_to_move = []
for path in SUBFOLDER_PATHS:
    for (dir, dirs, files) in os.walk(path):
        for file in files:
            if file.endswith(EXTENSION):
                files_to_move.append(fullpath(dir, file))
print(files_to_move)
print(RESULT_FOLDER_PATH)
for file in files_to_move:
    shutil.move(file, fullpath(RESULT_FOLDER_PATH, os.path.basename(file)))