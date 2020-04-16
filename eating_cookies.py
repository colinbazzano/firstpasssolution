"""Eating cookies

1 Cookie
--------------------
1

2 Cookies
---------------------
11
2

3 Cookies
---------------------
111
12
21
3

4 Cookies
---------------------
1111
121
211
112
22
31
13

5 Cookies
---------------------
11111
1112
1121
113
1211
122
131
2111
212
221
23
311
32

6 Cookies
---------------------
111111
11112
11121
1113
11211
1122
1131
12111
1212
1221
123
1311
132
21111
2121
2211
2112
222
231
213
3111
312
321
33
"""


def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]
