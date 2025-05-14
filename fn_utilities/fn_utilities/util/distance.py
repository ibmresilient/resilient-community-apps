# -*- coding: utf-8 -*-

""" Damerau-Levenshtein Distance, from Jellyfish 0.5.6
    https://github.com/jamesturk/jellyfish/blob/master/jellyfish/_jellyfish.py """

# Copyright (c) 2015, James Turk
# Copyright (c) 2015, Sunlight Foundation
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import itertools
from collections import defaultdict

IS_PY3 = sys.version_info[0] == 3

if IS_PY3:
    _range = range
    _zip_longest = itertools.zip_longest
else:
    _range = xrange
    _zip_longest = itertools.izip_longest


def damerau_levenshtein_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    infinite = len1 + len2

    # character array
    da = defaultdict(int)

    # distance matrix
    score = [[0]*(len2+2) for x in _range(len1+2)]

    score[0][0] = infinite
    for i in _range(0, len1+1):
        score[i+1][0] = infinite
        score[i+1][1] = i
    for i in _range(0, len2+1):
        score[0][i+1] = infinite
        score[1][i+1] = i

    for i in _range(1, len1+1):
        db = 0
        for j in _range(1, len2+1):
            i1 = da[s2[j-1]]
            j1 = db
            cost = 1
            if s1[i-1] == s2[j-1]:
                cost = 0
                db = j

            score[i+1][j+1] = min(score[i][j] + cost,
                                  score[i+1][j] + 1,
                                  score[i][j+1] + 1,
                                  score[i1][j1] + (i-i1-1) + 1 + (j-j1-1))
        da[s1[i-1]] = i

    return score[len1+1][len2+1]
