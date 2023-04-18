# Authors
Pooja Mule <pmule@stevens.edu> <br />
Nouman Syed <nsyed1@stevens.edu>

## Github Repo Link
https://github.com/PoojaVM/python_calculator

## Time spent on project
Pooja - 40 hours, Nouman - 40 hours

## How I tested my code
1. This program was tested manually by both the teammates.
2. First we split our tasks to complete the basic implementation.
3. We tested our own tasks when implementing them.
4. After integrating every time, we tested the changes again to verify everything is stable.
5. Then we selected the extensions we wanted to implement and worked on them.
6. After we implemented the extensions and merged them, we tested our code entirely.
4. In the end, we tested out the entire program together and fixed any issues we encountered.

## Any bugs or issues you could not resolve
We have not seen any issues as such that we could not fix.
But the autograder still showed some issues with cases related to precedence. We tried different flows to fix those.

## An example of a difficult bug which you resolved
Issue - We had an infinite loop in our program which was happening only for some expressions.
Fix - We got in a meeting and intensively tested the code and found the issue was caused when particular `variables` were passed in the expression.
We handled it by updating the `while loop` condition which was making it go to infinite loop.

## List of the three extensions chosen to implement
### 1. op= Extension
1. All the operations provided are supported by this extension.
2. Example -
    ```
    >>> a = 4
    >>> b = 4
    >>> b += a
    >>> print b
    ```
    Above commands print result as `8.0` on exit.
3. Arbitrary spaces are allowed in this expression as long as there are no spaces in `op=` <br>
<nbsp> Valid input example: `x      +=    5` <br>
<nbsp> Invalid input example: `x +  = 5`
4. `op=` extension will not work with `print` statement directly since there is assignment in it which is invalid if done in print.

### 2. Compare Extension
1. All types of comparisons can be done with both digits and variables.
2. Example -
    ```
    >>> x = 5
    >>> z = x > 3
    >>> print z
    ```
Above commands prints `1.0` on exit since comparison is `True`.

### 3.Comments Extension

### Extension 4 - Built-in Functions Extensions
1. Support for built-in functions is added as the last extension.
2. Example
    ```
    >>> print min(4, 5)
    >>> x = floor(5.9)
    >>> print x
    ```
    Above input will print following on exit
    ```
    4.0
    5
    ```
