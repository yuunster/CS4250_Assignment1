Default CSV Output:
    
    Document-Term Matrix
       | love | cat  | dog  |
    d1 | 0.00 | 0.12 | 0.00 |
    d2 | 0.00 | 0.00 | 0.09 |
    d3 | 0.00 | 0.06 | 0.06 |

Example CSV Input:

    Document
    I love cats and cats
    She loves her dog
    They love their dogs and cat
    I love McDonalds and BurgerKing


Example Output:

    Document-Term Matrix
       | love | cat  | dog  | McDonalds | BurgerKing |
    d1 | 0.00 | 0.20 | 0.00 | 0.00      | 0.00       |
    d2 | 0.00 | 0.00 | 0.15 | 0.00      | 0.00       |
    d3 | 0.00 | 0.10 | 0.10 | 0.00      | 0.00       |
    d4 | 0.00 | 0.00 | 0.00 | 0.20      | 0.20       |
