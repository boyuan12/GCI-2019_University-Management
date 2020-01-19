# GCI-2019 - Fedora Project - BL6 - University Management Task

## Introduction
This project is build based on requirement stated in [University Management Task](https://codein.withgoogle.com/dashboard/task-instances/6412603903967232/). This task is developed by @boyuan12, or bl6 as GCI-2019 username (aka, myself developed this program).


## Syntax
To use this program, please clone this GitHub Repository. Then, `cd` to this directory. Additionlly, you may run `pip3 install -r requirements.txt` to download the only external library. Please also make sure you have `python3` downloaded in order to run this program.

After that, you can run `python3 app.py arg1.ods arg2.ods arg3.ods arg4.ods arg5.ods arg6.ods` with 6 command-line arguments. They are: Term1, Term2, Term3, Term4, IELTS, and Interview. These file extension must be .ods file.

The output of the file will be a .txt file with rank #1 candidate at the top, last one at the bottom, with an empty line at the end.


## Demo
Demo time. There is a folder called input, stored 6 input files, and an output file. To see how demo works, you can run following command: `python3 app.py input/Data1.ods input/Data2.ods input/Data3.ods input/Data4.ods input/IELTS.ods input/Interview.ods`.


## What does it support?
Currently, it only support .ods file. You can change number of subjects in ods column, you can change student count and student detail. As long as you keep student consistent. Also, Algebra & Geometry both count as Maths.


## How does this program ('s math) works?
If you don't want to read the codes in detail, here is how code works. It reads the files, for the first 4 files, it going to find where is the physics, algebra and geometry subject located, and multiply by 2 since it's hold factor of 2. Then times overall factor 0.4.

For 5th file, it basically does the same thing as first 4 files except it multiply by 2 of certain subject, it skipped that parts since everything weight the same. But multiply by 0.3 as overall factor.

For 6th file, it basically does the same thing as first 4 files except it multiply by 2 of certain subject, it skipped that parts since everything weight the same. But multiply by 0.3 as overall factor.

At the end, it add the score up for each candidate, and return a .txt file.