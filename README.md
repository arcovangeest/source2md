Source to MD
============
- [./autodoc.md](autodoc.md)

This scriptset creates automatic documentation from several types of scripts and configs.

There are several usages:
- create a single auto.md file from all files
- create a directory with a md file per file
- create autodoc.md for ansible roles

The main scripts are:
- [./dir2dirmd.sh](autodoc/dir2dirmd.sh.md)
- [./dir2md.sh](autodoc/dir2md.sh.md)
- [./role2md.sh](autodoc/role2md.sh.md)

The filter script is:
- [./md_filter.py](autodoc/md_filter.py.md)

## Requirements

At this moment it needs python3 and bash (linux or wsl)

## Usage

### role source to autodoc.md

```bash
cd to role directory
start /PathTo/role2md.sh 
```

output goes to autodoc.md in current directory

### directory to single autodoc.md

```bash
cd to source directory
start /PathTo/dir2md.sh 
```

output goes to autodoc.md in current directory

If pandoc exists also an autodoc.html is created

### directory to autodoc directory

```bash
cd to source directory
start /PathTo/dir2dirmd.sh 
```

index goes to autodoc.md in current directory and a md-file is created per file in autodoc.


## Why
Previously I used doxygen filters to create documentation from "non-code" files like sql and shell. This is an easier way for me to create documentation without having a large setup.

## Todo
unknown files are passed as a stream, it does not handle js, c or c++ yet. For larger C/C++ projects doxygen is a much better choice.

## Known issues
The autodoc links only work in gitlab now.