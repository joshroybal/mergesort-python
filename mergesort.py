#!/usr/bin/env python

import sys, time
from operator import le, ge
from random_module import *
from mergesort_module import *

# main program
if (len(sys.argv) < 2):
    sys.stderr.write("Usage: %s n\n" % sys.argv[0])
    sys.exit(1)
n = int(sys.argv[1])
# integers
print 'integers'
integers = random_list(n, random_integer)
if len(integers) <= 50: print integers
print is_sorted(integers, le)
print 'ascending'
t0 = time.clock()
sorted_integers = merge_sort(integers, le)
t1 = time.clock()
if len(sorted_integers) <= 50: print sorted_integers
print is_sorted(sorted_integers, le)
print "elapsed time =", t1-t0, "secs."
integers = random_list(n, random_integer)
if len(integers) <= 50: print integers
print is_sorted(integers, ge)
print 'descending'
t0 = time.clock()
sorted_integers = merge_sort(integers, ge)
t1 = time.clock()
if len(sorted_integers) <= 50: print sorted_integers
print is_sorted(sorted_integers, ge)
print "elapsed time =", t1-t0, "secs."
# reals
print 'reals'
reals = random_list(n, random_real)
if len(reals) <= 50: print reals
print is_sorted(reals, le)
print 'ascending'
t0 = time.clock()
sorted_reals = merge_sort(reals, le)
t1 = time.clock()
if len(sorted_reals) <= 50: print sorted_reals
print is_sorted(sorted_reals, le)
print "elapsed time =", t1-t0, "secs."
reals = random_list(n, random_real)
if len(reals) <= 50: print reals
print is_sorted(reals, ge)
print 'descending'
t0 = time.clock()
sorted_reals = merge_sort(reals, ge)
t1 = time.clock()
if len(sorted_reals) <= 50: print sorted_reals
print is_sorted(sorted_reals, ge)
print "elapsed time =", t1-t0, "secs."
# strings
print 'strings'
strings = random_list(n, random_record)
if len(strings) <= 50: print strings
print is_sorted(strings, le)
print 'ascending'
t0 = time.clock()
sorted_strings = merge_sort(strings, le)
t1 = time.clock()
if len(sorted_strings) <= 50: print sorted_strings
print is_sorted(sorted_strings, le)
print "elapsed time =", t1-t0, "secs."
strings = random_list(n, random_record)
if len(strings) <= 50: print strings
print is_sorted(strings, ge)
print 'descending'
t0 = time.clock()
sorted_strings = merge_sort(strings, ge)
t1 = time.clock()
if len(sorted_strings) <= 50: print sorted_strings
print is_sorted(sorted_strings, ge)
print "elapsed time =", t1-t0, "secs."
