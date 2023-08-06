# What does it do?

Given the following directory structure:

```
- root
	+ sub_dir_one
	+ ...
	+ main_dir
```

And adhering the following assumptions:

1. Each sub-directory only contains files (no sub sub-directories)
2. Each file in each sub-directory is named in the form ``id_label.extension``. The file name should satisfy the regex ``'^.+_([a-zA-Z]*)\..*'``



This script will generate a CSV file containing the path information for each file in ``main_dir`` and the corresponding path information for the files in the other directories that match both the ``id`` and ``label``

## Arguments

```
  -h, --help 				Show this help message and exit
  -m, --main_dir			The directory name containing the final version of the transformed files
  -o, --output				Full path to output
  -r, --root 				The root directory to create a csv of all subdirs
```