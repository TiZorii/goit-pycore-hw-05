## Home task. Working with Files and Modular System

#### Task Description

**Task 1**

Closure in programming is a function that retains references to variables from its lexical context, i.e., from the scope where it was declared.

Implement the **`caching_fibonacci`** function, which creates and utilizes a cache for storing and reusing already computed values of Fibonacci numbers.

The Fibonacci sequence is a series of numbers like: `0, 1, 1, 2, 3, 5, 8, ...,` where each subsequent number in the sequence is obtained by adding the two previous members of the series.

In general, to compute the `n`-th member of the Fibonacci sequence, you need to calculate the expression: 𝐹𝑛 = 𝐹𝑛−1 + 𝐹𝑛−2.

This task can be solved recursively by calling a function that computes the numbers of the sequence until the call reaches members of the series less than `n = 1`, where the sequence is defined.

**Requirements for the task:**

- The **`caching_fibonacci()`** function should return the inner function **`fibonacci(n)`**.
- **`fibonacci(n)`** computes the n-th Fibonacci number. If the number is already in the cache, the function should return the value from the cache.
- If the number is not in the cache, the function should compute it, store it in the cache, and return the result.
- Use recursion to compute Fibonacci numbers.

**Recommendations for execution:**

As a recommendation, we'll provide the pseudo-code for the task.

> [!TIP]
> ☝ **Pseudo-code** is a way of expressing an algorithm or piece of code that is used to describe an idea or process in a format understandable to humans. It is not intended for direct execution on a computer, but it helps developers understand and plan how a program or algorithm will work. Its main purpose is to clearly convey the idea of an algorithm simply and clearly.

Here's the pseudo-code for the **`caching_fibonacci`** function, which computes Fibonacci numbers using caching:

```
FUNCTION caching_fibonacci
Create an empty dictionary named cache

FUNCTION fibonacci(n)
If n <= 0, return 0
If n == 1, return 1
If n is in cache, return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    Return cache[n]

Return the fibonacci function
END FUNCTION caching_fibonacci
```

The **`caching_fibonacci`** function creates the inner **`fibonacci`** function and a dictionary named **`cache`** to store the results of computing Fibonacci numbers. Each time **`fibonacci (n)`** is called, it first checks if the value for **`n`** is already saved in the **`cache`**. If the value is in the cache, it returns it immediately, significantly reducing the number of recursive calls. If the value is not in the cache, it is computed recursively and stored in the **`cache`**. The **`caching_fibonacci`** function returns the inner **`fibonacci`** function, which can now be used to compute Fibonacci numbers using caching.

**Task 2**

You need to create a function called **`generator_numbers`**, which will analyze the text, identify all real numbers considered as parts of income, and return them as a generator. Real numbers in the text are written without errors and are clearly separated by spaces on both sides. You also need to implement a function called **`sum_profit`**, which will use **`generator_numbers`** to sum up these numbers and compute the total profit.

**Requirements for the task:**

- The **`generator_numbers(text: str)`** function should take a string as an argument and return a generator that iterates over all real numbers in the text. Real numbers in the text are considered to be written without errors and are clearly separated by spaces on both sides.
- The **`sum_profit(text: str, func: Callable)`** function should use the **`generator_numbers`** generator to calculate the total sum of numbers in the input string and accept it as an argument when called.

**Recommendations for execution:**

1. Use regular expressions to identify real numbers in the text, considering that the numbers are clearly separated by spaces.
2. Use the **`yield`** construct in the **`generator_numbers`** function to create a generator.
3. Make sure **`sum_profit`** correctly handles data from **`generator_numbers`** and sums up all numbers.

**Task 3**

**Requirements for the task:**

**Recommendations for execution:**

**Task 4**

**Requirements for the task:**

**Recommendations for execution:**
