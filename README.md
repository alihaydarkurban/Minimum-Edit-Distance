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
* You can see the real comparison based on the percentage of occupancy of the dynamic programming table here.
***
