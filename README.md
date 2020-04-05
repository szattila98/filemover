# filemover
A small python script for convenience and learning purposes.
Moves files with the given extensions, under the working directory's subdirectories into a result directory, sorted into directories by file extensions.

## Usage
Be warned that the process is not reversible so use it with care.

- Navigate to the directory, in which you want to sort the subdirectories' files.

- Use the command, and specify any number of extensions, dots before extensions doesn't matter.

```
py filemover.py extensions...
```

- Examples - both work exactly the same
```
py filemover.py mp4 txt .jpg
py filemover.py .mp4 .txt jpg
```