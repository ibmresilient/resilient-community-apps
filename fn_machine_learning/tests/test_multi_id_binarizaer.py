from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer
import numpy as py
import pandas as pds
def test_union():
    a = [1, 2, 3, 4, 5]
    b = [1, 3, 4, 5, 6, 7, 8, 9, 10]

    c = MultiIdBinarizer.union(a, b)
    assert c == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_is_multi_selection():
    a = ["[abnc", "efg]", "[123]"]
    assert not MultiIdBinarizer.is_multi_selection(a)
    a = ["a[1,2,3]"]
    assert not MultiIdBinarizer.is_multi_selection(a)
    a = ["[1]", "[1,2,3,4"]
    assert MultiIdBinarizer.is_multi_selection(a)
    a = ["[1,2,3]", "[12]"]
    assert MultiIdBinarizer.is_multi_selection(a)
    a = ["[]", "[12]"]
    assert MultiIdBinarizer.is_multi_selection(a)

def test_fit():
    df_dict= {"col1": ["[1,2,3]", "[5,6]", "[8]"]}
    df = pds.DataFrame(data=df_dict)
    df["col2"] = [1, 2, 3]
    df["col4"] = ["a", "b", "c"]

    mib = MultiIdBinarizer()
    mib.fit(df["col1"], "col1")
    df = mib.transform(df)
    print("\n")
    print(df)
    #
    #   "col1": [1,2,3] becomes
    #   "col1_1": 1
    #   "col1_2": 1
    #   "col1_3": 1
    #
    assert df.loc[0, "col1_3"] == 1
    assert df.loc[0, "col1_2"] == 1
    assert df.loc[0, "col1_1"] == 1

    assert df.loc[1, "col1_5"] == 1
    assert df.loc[1, "col1_6"] == 1

    assert df.loc[2, "col1_8"] == 1
    print("Done1")

