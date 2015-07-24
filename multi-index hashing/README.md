#Multi-Index Hashing
1. Read binary code data set, length ***b*** and calculate the variance of each bit
2. Sort the bits desceased by the variance
3. Set radius ***r*** and the number of split part or hash table ***m***
4. Binary codes from data set are indexed ***m*** times into ***m*** different hash tables, with the *substring* as key and all *indexes* of dataset as value
5. Given a query code, first split it into ***m*** parts, **h**<sup>(1)</sup>,...,**h**<sup>(m)</sup> each length [***b/m***] and search the proper substrings which differ from **h**<sup>*i*</sup> by at most [***r/m***] bits in the ***i<sup>th</sup>*** hash table as *neighbor candidates*
6. Check the candidates by Hamming Distance and calculate the union of the ***m*** sets as the result

##Reference
[Fast Search in Hamming Space with Multi-Index Hashing]("http://www.cs.toronto.edu/~norouzi/research/papers/multi_index_hashing.pdf")
