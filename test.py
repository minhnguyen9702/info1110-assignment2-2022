"""
Author: Nguyen Nguyen Nhat Minh
SID: 510190381
Unikey: nngu8085
"""

"""
Do not edit the following line - it is required to pass the testcases.
In your test suite, write tests targeting these functions.
They can be called like normal functions, e.g. is_valid_name()
"""
from test_functions import is_valid_name, is_chronological

# the reason I need to use try/except is because I don't want the program to end
# because of errors, mostly assertation errors.

try:
    assert is_valid_name("") == False
    assert is_valid_name(" ") == False
    assert is_valid_name("   ") == False
    assert is_valid_name("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert is_valid_name("abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert is_valid_name("Bilbo Baggins") == True
    assert is_valid_name("abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False
    assert is_valid_name("123456789") == False
    assert is_valid_name("/n") == False
    assert is_valid_name("/t") == False
    assert is_valid_name("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789") == False
    assert is_valid_name([]) == False
    assert is_valid_name(["a", "b", "c"])  == False
    assert is_valid_name(())  == False
    assert is_valid_name(("a", "b", "c"))  == False
    assert is_valid_name(10)  == False
    assert is_valid_name(-10)  == False
    assert is_valid_name(10.0)  == False
    assert is_valid_name(-10.0)  == False
    print("is_valid_name has passed.")
except:
    print("is_valid_name has failed.")
# My tests are split into 2 sections, one for is_valid_name and one for
# is_chronological

try:
    assert is_chronological("x", "y") == False
    assert is_chronological("", "") == False
    assert is_chronological("  ", "  ") == False
    assert is_chronological(4, 5) == False
    assert is_chronological(4.0, 5.0) == False
    assert is_chronological(4, "1996-09-12T16:30:16") == False
    assert is_chronological("1996-09-12T16:30:16", 5) == False
    assert is_chronological(4.0, "1996-09-12T16:30:16") == False
    assert is_chronological("1996-09-12T16:30:16", 5.0) == False
    assert is_chronological("1996", "1998") == False
    assert is_chronological("30/01/1996", "30/01/1998") == False
    assert is_chronological([], []) == False
    assert is_chronological([], "1996-09-12T16:30:16") == False
    assert is_chronological("1996-09-12T16:30:16", []) == False
    assert is_chronological("1996-09-12T16:30:16", "1996-09-12T16:30:16") == False
    assert is_chronological("YYYY-MM-DDTHH:NN:SS ", "1996-09-12T16:30:16") == False
    assert is_chronological("1996-09-12T16:30:16", "1996-09-12T16:30:20") == True
    assert is_chronological("1996-09-12T16:30:16", "1996-09-12T16:35:16") == True
    assert is_chronological("1996-09-12T16:30:16", "1996-09-12T17:30:16") == True
    assert is_chronological("1996-09-11T16:30:16", "1996-09-12T16:30:16") == True
    assert is_chronological("1996-09-12T16:30:16", "1996-10-12T16:30:16") == True
    assert is_chronological("1996-09-12T16:30:16", "1998-09-12T16:30:16") == True
    assert is_chronological("1996-09-12T16:30:16", "1998-10-13T17:35:20") == True
    print("is_chronological has passed.")
except:
    print("is_chronological has failed.")
