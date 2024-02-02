1. Interpolation search makes better use of the sorted nature of the data to find a better mid point to begin searching the data at. For example, if searching a phone book, binary search starts exactly in the middle but interpolation search could make use of the first letter of the name to begin in the middle of that section to increase its speed. Another benefit is that it can adjust to different types of distributions within data sets so it also much more flexible than binary search depending on the data.

2. Yes the preformance of linear interpolation search can be affected by a very scewed distribution of data. For example, if you were searching a phone book for name with an x, linear interpolation search would assume to search very close to the end of the dataset. However, if the dataset is extremely scewed and doesn't have almost any extries from a-y then the search is going to start very close to the end but the data happens to be at the beginning so the search takes longer than if something like binary search was used.

3. Line 5 of the file would have to be modified since it controls how the next position is chosen based on the data within the section of the dataset is being analyzed. With different distributions, this line of code would be modified to put more or less weight on to various parts of the surrounding data.

4. If the data is not sorted then binary and interpolation search may fail since they don't check every single data point, whereas linear search does and has no chance of not finding a specified data point.

5. If the desired data point is in the very first index. Linear search always checks this first where as binary and iterpolation start either in the middle or close to it and thus will take more iterations.

6. If you were to implement some sort of boundary checking then these searches wouldn't miss this point.
