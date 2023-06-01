# Cache-Management
First in First Out (FIFO), Least Frequently Used (LFU)
In a First in First Out (FIFO) cache memory, the page that is evicted is the one that has the longest time since it was added.
In a Least Frequently Used (LFU) cache memory, the page that is evicted is the page that has had the fewest requests so far. 
In case of two pages having the same amount of requests, the lowest numbered page should be evicted. 
The number of requests that a page has had is maintained throughout the parsing of the whole set of requests, and it is not "forgotten" once a page has been removed from the cache memory.
