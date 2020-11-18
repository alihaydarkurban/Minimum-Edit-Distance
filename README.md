# Minimum-Edit-Distance
##### This project is an enhanced version of the minimum edit distance algorithm with dynamic programming
***
#### Classical Minimum Edit Distance Algorithm 
The classical edit distance algorithm efficiently finds the distance between given two words using dynamic programming. However, if we want to find the distance between one word against 1000 words, this becomes inefficient.
***
#### Enhanced Minimum Edit Distance Algorithm 
* Instead of using 2D array, I will fill in 3D array as our major dynamic programming table. Previously, Table(I,J) gave me the smallest edit distance between the two words up to letters I and J of these two words. Now, Table(K,I,J) will give me the distance between a given main word and the Kth word (K=0,1,2,...999) up to letters I and J.
* To make my algorithm more efficient, I will not fill all the 3D elements of Table(K,I,J). I will fill this table until I find most similar top 5 words out of 1000 words.
* If the distance for a word with the main word is getting higher, I will stop filling the table for that word.
* First I will fill all costs of 1 in all the table elements for all 1000 words. Then costs of 2, then 3, etc. It means that filling the table element will be rowed by row.
***
#### Comparisons
The percentage of occupancy of the dynamic programming table gives us how the program is efficient.<br/>
* Although [inefficient_min_edit_distance.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/inefficient_min_edit_distance.py) has a 3D array as a dynamic programming table, it is a classical version of the minimum edit distance algorithm. Even though the word has much more distance, the algorithm fills all the cells of the dynamic programming table. So, for all words, the percentage of occupancy of the dynamic programming table will always be %100.
* [min_edit_distance.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/min_edit_distance.py) is the enhanced version of the minimum edit distance algorithm. It can stop filling the table cell if the distance is getting hihger. So, the percentage of occupancy of the dynamic programming table will not be %100. 
* You can see the real comparison based on the percentage of occupancy of the dynamic programming table [here](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/ComparisonReport.pdf).
***
#### Dataset And Random Files
* The folder with name [Files](https://github.com/alihaydarkurban/Minimum-Edit-Distance/tree/master/Files) is the place where I keep the dataset and the files that have 1000 words.
* The program with name [generate_random_files.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/generate_random_files.py) generates five random files which have 1000 words. The main dataset is [dataset.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/dataset.txt) and it includes around 1.1 million words.
* [generate_random_files.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/generate_random_files.py) generates five random files which have 1000 words from the [dataset.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/dataset.txt). These random files are:
  1. [random_file_1.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/random_file_1.txt)
  2. [random_file_2.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/random_file_2.txt)
  3. [random_file_3.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/random_file_3.txt)
  4. [random_file_4.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/random_file_4.txt)
  5. [random_file_5.txt](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/Files/random_file_5.txt)
<br/>
These files are needed to test and compare the enhanced version and the basic version of the minimum edit distance algorithm.

***
#### Requirements 
* It is a [PyCharm](https://www.jetbrains.com/pycharm/) project. So, you may use PyCharm to run it.
* The version of the python interpreter is Python 3.7.5 and you can find it [here](https://www.python.org/downloads/).
***
#### Running 
* [generate_random_files.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/generate_random_files.py) generates five random files. _(I have generated the files so, you do not need to run this file.)_
* [inefficient_min_edit_distance.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/inefficient_min_edit_distance.py) and [min_edit_distance.py](https://github.com/alihaydarkurban/Minimum-Edit-Distance/blob/master/min_edit_distance.py) want a word from the user and report the five most similar five words and the percentage of occupancy of the dynamic programming table.
***
![Static badge](https://img.shields.io/badge/love-coding-success.svg)
![Static badge](https://img.shields.io/badge/dynamic-programming-yellow.svg)
![Static badge](https://img.shields.io/badge/edit-distance-red.svg)
![Static badge](https://img.shields.io/badge/computer-science-blue.svg)
![Static badge](https://img.shields.io/badge/software-engineering-yellowgreen.svg)
![Static badge](https://img.shields.io/badge/python-programming-blueviolet.svg)

