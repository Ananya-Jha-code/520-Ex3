
## 2. Global Results

| strategy   | family   |   mean_pass@k |
|------------|----------|---------------|
| Checklist  | DeepSeek |           0.9 |
| Checklist  | Qwen     |           1   |
| CoT        | DeepSeek |           0.6 |
| CoT        | Qwen     |           1   |



## Original 10 Problem Prompts



### HumanEval/125

```
Before coding, list a short checklist of edge cases, USE it to guide your solution, then DELETE the checklist and OUTPUT ONLY the final Python code (no prose, no tests).


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
```


### HumanEval/24 — DeepSeek / CoT (k=0)
```python
def largest_divisor(n):   # Step-by step explanation of the problem statement here, then output only final python implementation  (no prose or tests) .
    """ For a given number n , find out which is smallest divisible integer that can divide evenly into 'N' and less than N. If there are no such integers return -1 as per requirement."""   # Step-by step explanation of the problem statement here, then output only final python implementation  (no prose or tests) .
    
    i = n // 2 + 1        # Start from one more than half to check for even divisibility. This is because all numbers can be divided by two and there's no need of checking if the number itself could divide into 'N'.   (no prose or tests) .
    
    while i > 0:           # Step-by step explanation here, then output only final python implementation  (no prose). This loop will run until it finds a divisor. If no such integer is found return -1 as per requirement.(No Prose/Tests required.)   No tests are written for this part of the code in Python programming language
        if n % i == 0:     # Step-by step explanation here, then output only final python implementation  (no prose). This condition checks whether 'i' is
```

