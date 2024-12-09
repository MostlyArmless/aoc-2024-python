from utils import timer
sample_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

real_input='''8 11 13 14 15 18 17
43 44 47 49 52 52
37 40 42 43 44 47 51
70 73 76 79 86
17 19 17 20 23
61 63 64 66 68 67 68 67
43 44 43 46 48 51 54 54
79 81 82 84 82 83 87
79 80 82 79 86
58 59 59 62 65 66
30 33 35 35 38 40 41 39
3 6 6 9 12 12
48 50 51 52 52 56
66 69 71 71 76
79 82 86 89 90 91
46 49 50 54 51
67 69 71 75 78 80 81 81
30 32 36 38 42
46 49 50 51 52 56 63
7 9 14 17 18 20
27 30 37 39 40 39
32 33 38 40 40
24 25 30 32 34 36 40
42 43 45 52 59
34 31 32 35 36 39
43 40 41 42 43 46 47 44
26 23 24 25 27 27
6 4 6 9 11 13 15 19
22 19 21 22 24 29
11 8 9 12 10 13 16
75 72 71 73 75 76 77 76
73 72 74 72 72
29 27 26 27 31
53 52 49 50 52 59
70 68 68 70 72
37 36 37 37 40 43 40
40 39 41 43 44 44 45 45
12 9 10 13 13 16 20
46 44 44 47 48 50 53 60
68 65 69 72 74 77 80 83
75 73 77 80 79
64 61 62 66 66
74 73 74 76 79 83 84 88
54 52 55 58 59 62 66 72
32 30 31 34 35 41 43
42 41 47 49 47
49 46 49 52 57 57
49 48 53 54 55 56 60
33 32 39 42 45 47 49 56
21 21 22 25 27 30 33
83 83 86 89 88
22 22 25 28 29 31 34 34
66 66 68 69 70 73 77
54 54 56 57 60 65
6 6 7 8 11 8 10
88 88 89 87 90 91 93 91
64 64 67 70 73 72 74 74
71 71 73 76 74 78
23 23 24 25 22 29
75 75 76 76 79 81
18 18 21 22 24 24 23
57 57 60 60 60
80 80 82 82 84 87 89 93
10 10 10 12 13 20
62 62 66 68 69 71 72 73
73 73 76 77 78 82 85 84
59 59 60 64 65 66 68 68
32 32 34 38 40 41 45
63 63 64 68 74
18 18 21 27 28 29 32
75 75 77 84 85 83
44 44 45 47 52 52
80 80 83 86 92 94 98
4 4 6 8 14 21
74 78 80 81 84 86 88
71 75 78 81 83 84 87 86
91 95 97 98 98
67 71 74 76 79 82 83 87
57 61 64 66 68 69 72 79
7 11 14 12 14 16 17 19
48 52 53 56 58 60 59 56
28 32 31 33 34 36 37 37
5 9 7 9 11 12 16
15 19 20 17 19 21 24 30
22 26 27 29 29 31 33
47 51 52 54 54 55 57 55
1 5 8 10 10 13 13
17 21 23 26 26 30
40 44 47 47 53
9 13 15 19 20 21 24 25
61 65 66 69 73 76 75
33 37 41 42 44 46 46
2 6 10 13 14 18
74 78 79 81 85 88 90 97
71 75 77 79 84 87 90
29 33 36 41 40
80 84 87 89 92 98 98
57 61 64 71 75
45 49 51 52 57 62
22 27 30 33 35
4 9 12 13 16 19 16
35 40 41 43 46 49 49
14 20 23 25 27 29 33
12 19 22 25 30
77 82 81 82 85 88 89 91
85 91 93 91 88
50 56 58 61 63 62 62
45 51 54 56 58 60 58 62
4 10 11 12 13 10 12 19
13 20 21 24 24 26 29 30
40 45 46 48 48 49 51 48
83 89 90 91 91 91
13 19 19 22 25 27 30 34
33 40 41 41 44 50
79 84 87 91 94
58 63 64 65 66 70 72 71
69 75 79 82 82
38 45 49 52 56
36 42 45 49 50 51 57
74 81 87 89 92
12 17 19 21 24 25 31 28
58 65 68 69 76 76
13 20 21 23 29 33
30 36 41 44 50
90 88 87 85 82 85
52 50 47 44 44
35 33 31 29 27 25 22 18
77 76 73 70 64
19 17 16 17 16 15 12
76 73 75 72 75
9 8 10 9 9
71 68 71 69 65
79 76 78 76 69
95 93 92 92 90 87
63 60 60 58 55 52 54
11 9 7 7 5 5
77 76 73 73 71 69 65
89 87 85 85 82 81 79 73
34 31 30 26 23
19 16 15 12 10 6 8
17 16 15 13 10 6 5 5
18 16 13 12 9 5 1
98 97 95 93 89 82
18 16 15 8 6
31 29 28 26 25 22 17 19
34 31 30 24 22 22
52 51 46 44 41 39 35
70 68 63 62 56
17 20 17 16 15 14
81 83 81 80 78 79
85 86 84 83 83
38 40 37 36 35 33 30 26
70 72 69 67 66 59
85 87 86 87 86
15 16 15 13 15 14 11 13
28 31 29 31 28 26 26
81 82 83 82 78
44 46 43 42 39 40 38 32
55 56 53 50 47 44 44 42
83 86 83 82 81 80 80 82
54 56 56 55 55
9 11 10 10 9 5
16 18 17 15 14 14 12 7
51 53 50 46 43
80 81 78 75 71 70 73
43 44 43 41 37 35 32 32
88 89 86 83 79 76 74 70
50 53 51 50 49 46 42 37
74 77 70 67 66 65 62 59
28 29 24 21 24
23 25 22 21 20 14 14
56 59 57 52 50 49 47 43
39 41 40 39 37 31 29 22
83 83 82 79 77
83 83 81 78 76 77
58 58 56 55 55
39 39 36 34 31 29 25
96 96 95 94 93 88
35 35 34 32 35 32 30
82 82 80 81 83
72 72 69 68 69 68 68
71 71 70 71 69 65
16 16 17 16 13 6
79 79 76 75 72 72 69
30 30 30 28 29
33 33 30 30 28 27 26 26
42 42 42 39 35
90 90 90 89 86 83 81 75
46 46 43 41 37 34
90 90 87 85 82 78 81
21 21 20 19 15 12 10 10
66 66 63 59 58 57 53
94 94 90 87 82
69 69 66 63 58 57 55 52
64 64 59 56 58
72 72 66 63 62 62
89 89 87 81 77
94 94 93 90 87 80 73
50 46 45 43 40 38 37
22 18 15 12 10 7 4 7
82 78 76 73 73
64 60 57 55 52 51 50 46
93 89 86 84 82 81 80 73
99 95 92 93 90 89 87
97 93 91 94 91 90 91
55 51 54 51 48 48
41 37 34 35 31
88 84 81 83 81 74
38 34 32 29 26 26 25
79 75 75 73 72 70 69 72
93 89 89 88 86 83 81 81
38 34 31 29 29 28 24
84 80 78 77 77 76 75 68
90 86 84 81 77 75
70 66 62 59 56 58
36 32 28 27 27
99 95 93 89 85
98 94 90 87 80
41 37 35 33 27 24 23
38 34 27 24 23 20 18 19
49 45 43 38 35 33 30 30
33 29 28 22 21 17
92 88 86 85 83 77 71
58 52 49 46 44 43 40 37
43 38 37 36 33 31 30 33
69 63 61 59 57 56 56
60 55 54 53 49
96 91 88 85 84 81 78 71
41 35 34 31 29 32 29 27
53 47 46 47 45 42 41 44
68 62 65 62 62
92 86 85 87 83
95 89 88 90 89 86 83 76
78 73 71 70 70 68 65 63
15 8 8 5 2 5
67 61 61 59 58 56 55 55
45 40 38 35 35 31
81 76 76 74 69
14 9 5 4 3
19 14 10 9 11
33 27 23 21 18 16 15 15
86 79 76 72 71 70 68 64
69 64 63 59 54
19 14 13 10 5 3 2 1
21 16 15 12 7 6 7
76 70 64 63 61 59 59
76 71 69 68 61 60 56
65 60 55 52 49 46 39
76 79 80 82 83 80
23 24 27 28 30 30
36 37 40 43 47
43 44 47 48 49 54
22 24 27 24 25 26
41 43 46 49 46 48 50 49
82 85 82 85 88 88
12 14 11 13 14 18
68 69 66 68 70 71 72 79
7 9 9 12 14
29 32 32 34 35 37 38 35
79 82 82 84 84
83 86 87 89 89 92 96
50 53 55 56 56 61
71 74 77 81 82
41 42 45 47 48 49 53 51
33 34 35 38 39 43 43
20 21 24 28 32
44 46 47 51 52 57
35 36 38 40 43 49 52
16 17 18 19 24 25 26 25
65 68 71 77 77
9 10 13 15 16 17 23 27
10 11 13 19 20 23 28
23 22 24 27 28
56 55 56 57 60 61 64 61
9 6 7 8 11 13 13
35 33 34 37 38 42
68 65 67 68 69 70 77
5 3 6 7 6 8 9
84 82 83 81 80
98 96 93 94 94
5 3 5 4 6 7 10 14
27 26 23 24 27 33
22 21 24 24 27 30 32
82 79 81 83 85 85 83
14 12 15 15 18 18
77 75 77 77 80 81 85
83 82 82 85 86 88 94
5 3 5 8 12 15 18
71 70 74 75 76 78 77
76 74 75 78 82 82
23 22 25 28 31 35 37 41
73 72 73 74 78 79 85
33 31 33 39 42 43 46 49
14 12 15 17 20 27 26
67 65 66 67 68 74 74
84 82 83 86 87 89 95 99
77 75 82 84 89
86 86 88 89 90 91 94
26 26 29 31 32 35 38 36
33 33 34 36 39 42 45 45
57 57 58 59 61 63 67
13 13 15 17 23
41 41 44 47 49 51 49 52
93 93 96 93 92
22 22 23 26 28 27 27
16 16 17 19 18 21 25
57 57 58 59 60 58 63
20 20 20 22 25 28 29 32
42 42 42 43 44 46 48 47
28 28 29 30 32 32 34 34
54 54 56 58 60 62 62 66
45 45 46 46 47 52
50 50 52 56 59 62 63
68 68 72 75 76 74
6 6 9 10 14 17 17
60 60 62 66 67 71
7 7 10 14 19
15 15 17 23 25
33 33 36 43 40
80 80 86 88 90 90
4 4 11 14 15 17 18 22
62 62 64 67 74 76 77 82
26 30 32 33 36 39 41
63 67 70 73 74 71
46 50 52 54 57 59 59
11 15 17 18 21 24 25 29
44 48 50 53 56 57 60 66
54 58 56 58 59 60
5 9 8 11 12 13 16 14
52 56 57 58 61 60 60
72 76 74 75 79
56 60 61 60 61 62 67
30 34 37 37 40 43
42 46 46 48 50 48
51 55 55 58 59 62 64 64
34 38 39 39 42 46
72 76 79 79 84
19 23 26 30 31
18 22 25 27 29 30 34 31
82 86 87 90 94 94
79 83 86 90 91 93 97
19 23 24 28 33
20 24 26 32 35 38
67 71 73 78 75
7 11 18 19 19
43 47 52 53 57
68 72 75 82 85 88 93
24 29 30 33 35 36
73 80 82 84 87 90 89
77 83 86 87 88 91 91
80 86 87 90 91 94 98
43 50 51 53 54 61
45 52 50 52 55 57
42 48 51 52 51 49
79 86 84 85 85
53 59 61 62 59 63
47 54 57 59 62 59 64
53 60 60 62 63
13 18 18 20 19
73 80 80 82 82
45 51 52 52 53 54 57 61
24 29 30 32 35 35 38 43
83 90 92 96 98
13 18 19 22 26 27 26
51 57 58 60 62 65 69 69
41 47 48 52 53 57
26 32 33 34 35 39 44
49 55 61 63 66 68 71
67 74 76 77 80 86 84
6 11 12 13 20 22 22
11 16 19 25 29
74 79 85 87 92
52 49 48 46 49
65 64 62 59 59
90 89 86 84 83 79
97 96 93 91 85
50 49 47 45 47 46
58 55 52 49 51 48 50
16 13 12 11 9 10 7 7
29 26 24 25 21
42 41 39 38 41 38 37 32
35 34 31 31 30 29
12 10 7 6 4 4 5
74 73 71 69 67 67 67
87 84 84 83 79
23 22 19 18 17 17 16 11
60 59 57 53 52 49
89 86 85 83 79 82
57 55 51 48 45 43 40 40
65 64 61 60 58 54 53 49
44 41 37 34 28
89 87 84 77 76 74 72
24 23 20 18 11 12
86 84 81 76 74 74
50 47 46 39 36 34 30
45 42 36 33 31 29 23
39 42 39 37 35 32
82 85 84 83 85
87 89 88 85 83 82 79 79
45 46 45 42 38
33 35 32 31 25
10 12 10 13 10 8 6 3
3 6 3 5 4 3 4
70 73 72 73 72 69 66 66
70 71 68 70 66
50 52 54 53 52 50 44
81 82 79 78 76 76 73 70
27 28 25 25 23 22 23
4 6 5 5 5
87 89 86 83 83 80 78 74
30 33 30 29 29 26 23 18
33 35 32 28 25 24 23 21
25 27 26 25 21 23
18 21 17 15 12 9 9
21 22 18 16 12
50 53 51 47 44 43 42 35
16 17 12 11 8 7 4 1
15 17 11 9 6 8
59 60 58 56 51 50 50
94 96 94 89 88 87 85 81
29 30 28 25 22 21 14 9
33 33 30 28 27 24 23
16 16 13 11 14
7 7 6 5 4 3 3
82 82 81 79 77 76 72
18 18 16 15 9
62 62 59 57 60 57 55
69 69 67 66 67 70
18 18 19 17 16 15 12 12
46 46 45 42 44 40
47 47 48 46 40
50 50 50 49 47 45
40 40 38 38 36 33 32 35
41 41 38 36 36 34 34
59 59 56 53 53 49
38 38 35 35 28
65 65 62 58 57 56 55
80 80 77 73 72 70 73
23 23 19 17 17
58 58 57 53 50 47 45 41
96 96 93 91 87 84 81 76
99 99 98 91 89 86 83
91 91 84 82 83
51 51 49 46 43 36 36
41 41 36 35 31
45 45 39 37 32
53 49 47 45 42 40
39 35 33 31 33
65 61 59 57 55 53 53
29 25 22 19 16 13 11 7
58 54 51 49 48 41
74 70 69 71 70 67 64
23 19 21 19 21
34 30 32 31 31
89 85 82 80 78 81 77
71 67 68 65 64 63 62 56
20 16 13 12 12 9 6 3
64 60 59 59 56 54 55
32 28 28 25 22 19 19
79 75 75 73 69
41 37 37 36 35 29
41 37 34 30 28 25
90 86 85 81 80 78 75 76
86 82 79 76 73 69 68 68
83 79 77 74 70 68 67 63
74 70 66 64 62 56
67 63 58 57 56
98 94 92 86 83 80 78 80
55 51 50 49 42 40 40
45 41 40 38 32 30 26
60 56 53 51 46 40
98 91 88 87 85 84 82
48 42 41 38 37 36 37
37 32 31 29 29
69 64 63 61 58 55 51
33 26 25 24 22 21 16
72 66 63 60 63 62 59 56
70 64 61 60 57 60 61
18 12 10 8 9 7 5 5
84 77 74 76 75 71
28 22 23 21 18 11
82 77 75 73 73 70 67
17 10 7 7 10
21 14 11 8 8 8
51 46 43 42 39 37 37 33
48 41 41 39 36 31
50 44 43 40 36 34 31
43 38 36 33 30 27 23 26
89 84 80 78 78
40 33 29 26 24 22 19 15
60 54 52 48 47 46 43 37
76 70 69 66 61 60 58
64 59 57 50 47 49
77 70 68 65 64 61 55 55
93 88 86 83 77 76 72
59 54 53 51 49 47 40 34
38 42 43 46 50
30 28 29 27 29
78 78 82 85 87 87
18 18 18 16 14 7
19 23 25 30 32 38
94 94 93 92 91 86 83 86
2 4 7 14 14
57 53 50 49 46 42 41 39
35 39 41 40 43 47
52 56 60 62 63 60
77 83 86 88 90 90 88
77 77 76 77 79
33 28 25 23 26 22
40 41 43 40 43 47
37 34 31 30 28 25 24
45 43 42 39 38 35 34
99 98 96 95 92 91
30 27 26 24 22
40 39 36 35 33 31
70 68 66 63 62 60
91 89 88 85 84 82
51 53 56 57 58
56 59 61 64 67 70
75 72 69 68 67 65 62
60 63 64 67 69
72 71 69 66 63 62 60 57
85 87 89 91 94
10 12 13 14 16
53 51 48 45 43 40 38 37
22 19 17 15 12 10
47 48 49 52 53 55
38 36 33 30 27 25 22 21
87 86 83 81 80 78 75 74
98 96 94 92 89 86 83
14 13 11 10 9 7 4
81 79 76 74 72 71
54 57 59 60 61 63 64
71 73 75 76 77 80
12 13 16 18 21 23 24 26
17 20 22 25 27
49 50 51 53 55 57 59 61
11 14 15 16 17 19
11 13 15 17 18 20 21
81 80 78 75 73 72 70 69
17 19 22 23 26 27 30 32
31 30 27 25 22
2 5 6 8 9 10
67 70 71 74 75 77
24 22 20 18 16
86 83 82 81 79
72 73 75 76 77
16 13 11 8 6 4
76 73 71 70 69 67 64 63
84 87 88 90 93 96 99
20 17 15 12 9 8 7 5
61 64 67 68 70
23 20 18 16 15 12
77 75 72 70 67 65 63
11 14 16 19 20 21 23 25
47 50 52 55 56 59
77 79 81 83 84
15 13 12 10 9 8 5
76 78 80 81 83 86 87 88
76 78 81 83 85 87 90 93
7 10 12 13 14
46 45 42 41 39 38 35 32
90 88 85 83 82 80 77
6 9 11 12 14 17
91 88 87 85 83 82 80
41 40 37 36 33 31 28
95 93 90 89 86 83 80 79
37 35 33 30 28
84 86 87 88 89 92 95 97
43 42 40 38 37
25 28 31 33 36 39
44 45 47 48 50
85 82 79 77 76
17 20 22 23 26 28
1 4 6 8 9 11 14
73 72 69 66 64 63 61 60
79 81 84 85 86 89
4 6 8 11 13
68 65 64 63 60 59 56
61 60 57 54 51
28 31 33 36 39 41 42
41 44 45 48 50 53
88 87 85 83 82 79
32 33 36 37 39
19 20 23 26 27 30 32 34
82 85 86 89 92 94 97 99
43 45 46 49 52 55 58
63 66 68 69 72 74 77 79
66 68 71 74 76 78 80
60 63 64 65 66 69 72 75
87 85 82 81 78 76 73 70
46 47 49 51 53
23 21 19 18 17 15 12 9
58 56 55 52 50 47 45
67 65 64 61 58 56 55 54
73 72 69 68 66 64 63
36 37 38 39 41 44 47 48
31 34 35 37 38
46 45 42 41 38 36 35
38 37 34 32 31
68 70 72 73 75 78 81 83
34 32 30 27 24
50 49 47 45 42 41 40 39
34 35 38 41 43 46
19 17 15 13 10 7 4
54 51 49 47 45 43
14 11 8 7 5 3
24 23 20 19 18 15 13 10
54 55 56 59 61 63 64
87 84 83 80 78 77
87 90 92 95 97
4 6 9 12 14 16 17
66 69 72 73 76 78 79
36 34 31 29 26 23 20 17
11 10 9 8 5 4
41 39 36 35 33 31 29
25 26 28 30 33 35 36 37
68 65 62 60 59 58
22 19 17 15 13 10 9
5 6 8 9 12 14 17
90 87 85 83 80 77 75
28 25 22 21 20
62 60 57 56 54
90 87 86 84 81 80
48 45 42 39 37 34
63 62 61 58 57 56
75 74 71 70 68 67 65
14 17 20 22 25 26
25 23 22 20 17 16 14 12
29 28 25 24 21 18 16 14
58 60 63 66 67 70 73
3 4 6 7 10 13
11 8 5 3 1
89 86 83 82 79 76 75 72
3 6 7 9 11 13
40 42 44 45 47 50 52
24 22 21 20 19 16 15 12
42 45 48 50 52
4 5 7 10 11 14 15
6 7 9 10 13 15
58 56 53 50 49 46 43 41
17 18 21 24 25 28 30
75 78 79 80 81 83 84 85
54 57 59 60 63
81 79 76 73 70 67 65 62
70 67 64 63 62 60 59 58
21 23 25 26 29 31 32
64 67 69 71 72 74 77
10 9 8 7 6
76 78 81 83 84 85 87 89
80 77 75 74 73
76 79 82 84 85 88
28 30 33 34 36 38 40 43
40 39 38 35 32 29
81 79 77 76 75 72 71 68
46 44 43 41 40 39 38 36
35 32 30 29 28 26
31 28 27 25 24 22
25 27 30 32 35 38 40 41
87 90 93 96 98
79 78 75 72 71 70 68
99 96 93 90 87 86 84
21 20 18 16 13
76 74 72 69 66 64 63
41 39 38 35 33 31 29 28
27 29 31 34 36
72 74 77 78 80 83
36 33 32 29 28 25
28 29 31 33 34
22 20 17 16 13 12 9
69 66 65 64 62 59
81 83 84 86 87 89
22 23 24 25 28 31
67 68 71 72 73 76 78 81
84 81 78 75 72 70 69
67 70 71 74 77 80 82 84
82 84 86 89 90 93 94
20 17 16 13 12
34 36 38 40 41 42 45
87 86 83 81 78 77 75 74
97 96 94 92 91 90 88 86
13 14 17 19 21 24 26
48 45 44 42 40 39
71 68 65 64 63 60 57 54
12 14 17 20 22
68 67 64 62 60 58 56 55
6 8 11 12 15 16
72 69 68 65 64 61 60
28 29 30 32 33 35 38
66 64 63 60 58 55 52
35 38 40 41 42
11 13 16 18 21 24 25
29 31 34 36 37 40
51 52 54 57 60 61 62
80 83 85 88 89 92 95
85 86 88 89 90 93 96 98
58 59 62 65 68 69 72
15 13 12 10 9 7
46 45 42 39 36 34 31
63 64 67 68 70
60 61 63 66 67 69 71 73
8 10 11 13 15 16
17 15 14 11 10 8
27 28 29 31 34 35
40 37 35 32 30 28 25 24
10 9 6 3 1
39 37 35 34 33 31 29 28
10 12 13 16 18 19 21
21 24 26 27 30 33
92 90 88 87 86 85 82 80
92 90 89 87 86 84 81
82 84 85 88 91 92
43 46 49 51 54
40 38 36 34 33 30 28 27
52 53 54 56 57 60 62 65
34 37 39 40 41 43 45
43 45 48 50 53 54 56 57
74 72 69 68 67 66 64 63
68 65 63 60 59
12 13 15 16 18
29 31 34 37 40 43
40 37 36 34 32
60 63 65 66 67 68 70
82 83 85 88 91
70 68 67 66 63
55 52 51 49 46 43 40 38
45 47 50 52 53 54 57 58
41 42 45 47 50 51 52
31 29 28 25 23 20
13 15 18 20 22 24
24 26 28 29 32
65 62 60 57 56
32 35 38 39 42 45 47
12 10 9 6 5
30 27 26 23 22 19
44 41 40 39 38 35 32 29
70 67 64 62 59 58 55
45 46 49 52 54 57 58
82 85 87 90 93 95
45 42 40 39 37
74 77 80 82 83 84 86 88
68 69 72 75 78 79 80
37 36 35 32 30 29 26 24
60 59 56 55 53 52 51 49
66 63 62 60 57 54 52
54 51 48 47 46 45
51 52 53 56 57
76 79 81 83 84 87 90
93 91 90 89 88
75 74 73 70 69
20 23 25 26 27 28 31 33
57 56 53 51 48 45 44 43
31 29 28 25 22 21 18 15
56 58 60 63 64
23 25 28 31 33 36 38
43 40 38 37 36 35
70 73 76 79 81
22 23 24 26 28 29 30 33
80 82 85 87 90 91
12 15 16 17 19 22 23
10 13 15 16 19 20 21 22
1 2 3 5 7 10 13 15
14 17 20 21 24 25 26 27
24 21 20 17 16
43 44 47 48 51 54 57 58
9 11 14 15 18 21
23 25 26 28 29 30 32 35
28 25 22 20 17 16
3 6 8 9 11
61 64 66 69 71 72 75 77
59 60 63 65 68 70 71 73
8 9 12 13 14
21 22 23 25 26 28
74 72 71 70 67
95 92 90 89 87 84 81 78
42 40 37 34 33
14 13 10 8 7 6 4 2
60 57 55 53 52
30 31 34 37 39
85 86 89 90 93
93 91 90 88 87 85
45 46 48 50 53 54
13 15 17 19 20 21 22
63 66 67 70 71 74 77 79
29 32 34 37 40 43 44
50 49 48 46 43 40
45 48 51 54 56
60 63 64 66 69 72 74
64 65 67 69 70
93 90 87 85 83
35 32 31 29 26 25 22 21
52 53 54 55 58
80 78 76 73 72 71
2 4 5 7 8 9 11
21 23 26 28 29 31 33 35
4 7 9 12 14
51 50 47 46 43 41
1 3 6 9 10 13 15
64 65 67 68 70 71
9 11 14 16 19 20 23 24
69 66 65 63 62 60
74 75 78 81 84 86
48 46 43 41 40 37 36
30 27 24 21 18 17 15
80 79 78 77 74 72 69 66
31 28 26 25 23 22 20 17
66 69 71 72 73 75 78 80
9 11 12 14 16 18 19
81 78 76 75 74 73 70 67
5 8 11 12 15 17 19 20
5 6 9 10 12
12 14 17 20 21 23 26
23 26 28 29 31 33 36
81 79 77 74 71
55 52 49 46 43 42
27 25 23 20 18 15
2 3 6 8 11 12 14
47 46 44 43 40 37 36 34
95 93 90 89 86
62 60 57 56 55 52 49 48
58 59 62 65 68 71 73 75
90 87 85 84 81 79
47 44 41 39 38 37 35 34
22 24 26 29 30 31 34
94 93 91 88 87 84 81 80
93 92 89 86 84 82
75 74 73 71 68 66 64
12 13 15 17 19 21
70 71 72 74 75 76
66 68 71 73 74 77 80 81
12 11 10 8 5 2
60 63 64 66 68 70
55 58 60 62 64 66 69
41 40 38 36 33
84 83 80 77 74 72 70
79 78 76 74 73 72 71
29 32 34 36 38
56 58 59 60 63 65 67 68
98 95 94 91 90 88 85 82
39 42 43 44 47 49 51 54
43 42 40 39 37
18 15 13 12 11
59 56 53 52 51 48 47 46
42 44 45 47 48 50 52 53
96 95 92 90 87 85 83
41 40 38 37 36 34 31 28
9 12 13 16 19
65 68 70 73 75 77 78 80
37 38 39 40 42 43
11 13 14 16 18 19 22 23
24 22 19 16 14 12 10 7
13 12 10 9 6
35 34 33 30 28
55 53 52 49 46 43 41
85 82 81 78 77 76 74
96 95 94 93 92 90 87 85
74 77 80 83 84 87 88 89
81 82 85 87 88
35 33 32 29 28 25 23
79 80 83 85 87 89
87 86 84 82 81 79
75 76 78 81 84 86 89
37 38 41 42 44 45 47 49
21 24 26 29 30 33 34 37
78 75 74 71 69 66
62 65 67 69 70 73 75
75 77 79 80 81 83 86 89
16 15 13 12 9 7 5
67 66 65 63 60 57 55
43 41 38 35 34 31
26 23 22 20 17
4 6 9 10 11 12
71 69 67 65 64 61 60
38 37 34 32 31 30 29 28
64 66 67 69 71 72
34 36 37 40 42
31 28 25 24 23
99 98 96 94 91 90 87
31 28 27 24 23 21
78 81 83 85 87 89 91
42 45 47 49 51 53 54
42 44 47 48 49 51 54 57
17 19 22 23 26 28 30
44 43 42 39 38
18 17 16 13 11 10 8 7
67 70 71 73 74
44 41 39 36 33 32
69 71 74 75 77
72 75 76 78 81 83 86
77 74 73 71 69
62 64 67 69 71 72 74
36 39 40 41 44
73 72 69 66 65
16 19 22 24 25 28 31 32
51 49 47 46 43
71 70 69 67 65 64 61
31 34 37 40 41 43 46 49
89 92 94 95 96
48 46 45 42 41 39 36 35
32 31 28 25 22
16 14 12 11 10
61 60 58 57 55
20 19 16 15 13 11 8 7
44 42 40 38 37 36
57 56 53 50 47 44 43
82 80 79 78 76 75 74 73
71 72 73 74 75
15 14 12 10 9
29 28 25 23 21
29 28 25 24 22 20
57 60 63 66 68 70 72
13 11 9 6 5
58 61 63 64 67 70
50 53 56 58 61 63 64
82 85 86 89 90 91 93
27 30 31 32 35 37 38
95 93 91 88 85 82
42 39 37 35 33 30 28
96 93 91 89 88
7 8 11 13 15 17
76 74 73 72 70 67
49 51 54 55 56 59 61
52 49 47 45 42 40 38
65 66 68 70 73 76 78
53 55 58 61 63 66 67 68
28 31 32 35 36 38 39 42
96 95 93 90 87 86 83
73 71 70 67 64 61
41 38 37 34 33 32 29 26
69 70 72 74 77 80
50 53 55 57 60 62 64
65 64 63 62 61
48 47 46 45 42 41
27 25 22 19 16 13 10
15 14 12 10 8 6
44 41 38 36 34
35 32 30 27 26 23 22 19
29 28 25 24 21
84 85 86 87 89 92 93 94
50 51 54 55 58
47 44 43 40 39
68 65 63 62 59 58 57
65 64 63 60 58 56 55
40 37 36 33 32 29
47 49 51 54 55 57
53 50 49 46 44 42
26 23 21 19 18 17 16 13
53 54 56 58 59 60 62
59 61 62 65 68 69 71 74
80 83 86 87 89 90 92
63 62 59 58 55
40 43 46 47 49
24 21 18 17 16 13
47 48 50 52 53 54 57 59
60 63 64 65 68 69 70
88 85 83 81 80 77
90 88 86 83 81 80 79
27 28 29 30 31 32
4 5 8 11 12 14 15 17
33 31 29 27 24 23 22
51 50 49 48 46
96 93 92 90 87 86 83
56 58 60 61 63
46 43 42 40 39 36 33 31
55 58 59 62 63 65
78 76 74 73 72 69 67 65
76 75 74 72 69 66 63 60
39 36 33 31 30 28
18 19 22 23 26 29 32 35
37 39 40 42 45 48
61 59 57 55 54 51 48 47
55 54 51 48 46 43 41 38
87 84 83 82 81 78
61 59 56 55 54
33 34 35 38 41 44 45 47
67 66 64 62 61
41 43 44 46 49 50 51
94 91 90 89 87 86 83 80
88 91 92 95 98 99
17 15 13 12 10 7 5
82 85 86 88 89 91
99 98 97 96 95 92 89 86
54 51 48 45 44
45 43 40 38 37 36 33 31
20 22 24 25 27
12 11 8 7 6 5 4
25 23 22 21 18 15 14 12
25 22 20 18 16
54 53 50 49 46 43 42
82 83 84 87 90 91
23 26 29 31 34 35 37
68 65 63 60 59 57
85 86 87 89 91
4 6 9 11 13 15 16
31 30 27 25 23 21 18
24 25 28 29 31 34 35
25 23 22 20 17 16 15 14
63 61 60 57 54 52 51
77 80 82 84 87 88 89
2 5 8 10 12 14 16'''

@timer
def part1(input: str):
  num_safe_reports = 0
  for report in input.split('\n'):
    is_safe = True
    levels = [int(s) for s in report.split(' ')]
    delta = None
    for i in range(1, len(levels)):
      new_delta = levels[i] - levels[i-1]
      was_increasing = delta and delta > 0
      was_decreasing = delta and delta < 0
      now_increasing = new_delta > 0
      now_decreasing = new_delta < 0
      if delta and (was_increasing and now_decreasing) or (was_decreasing and now_increasing):
        is_safe = False
        break

      delta = new_delta
      abs_delta = abs(delta)
      if abs_delta < 1 or abs_delta > 3:
        is_safe = False
        break
      
    # print(levels, 'Safe' if is_safe else 'Unsafe')
    num_safe_reports += 1 if is_safe else 0

  print(num_safe_reports)


part1(sample_input)
part1(real_input)

