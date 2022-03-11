from datetime import datetime
from cachetools import cached, LRUCache

def test_cachetools():
    # test that the cache is working as expected
    results = {}
    for x in range(0, 150):
        group, ts = _get_endpoint_group("group{}".format(x))
        results[group] = ts

    # test the cache in reverse order. The newest entries will exist and older
    #  ones will have been pushed out
    for x in range(149, 0, -1):
        group, ts = _get_endpoint_group("group{}".format(x))
        if x < 50:
            assert ts != results[group], group
        else:
            assert ts == results[group], group


@cached(cache=LRUCache(maxsize=100))
def _get_endpoint_group(group_name):
    """ cached API call to get group information """
    return group_name, datetime.now()
