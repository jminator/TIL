# 1. C++ Programming flow
## Overall Flow
<pre> Editor -> Compiler -> Linker & Loader -> Debug </pre>

### 1) Editor
* Produce source file with source codes.
* Use text editor on IDE to write codes.
* Saved as ***filename.cpp*** and the file is called **source file**.

### 2) Compiler
* Computers cannot read source codes directly.
* Source codes must be translated to ***low-level language***.
* Compile: translate high-level language(source code) to low-level language.
* Compilers check the **grammar** of the source code to detect ***syntax errors***.
* Compilers cannot check for logical or semantic errors that are not syntax errors.
* Source file is compiled and saved as ***filename.obj*** and it is called **object file**

### 3) Linker & Loader
* Object files do not include codes from standard or user-created libraries.
* Linker: links std or user-created library modules(~.lib) to the object file.
* Loader: create ***filename.exe*** from object files that are linked with library modules.
** In the past, linkers and loaders were treated as separate programmes but now loaders are usually considered as a part of a linker.

### 4) Debugging
* Execute the source code line-by-line to detect errors.
