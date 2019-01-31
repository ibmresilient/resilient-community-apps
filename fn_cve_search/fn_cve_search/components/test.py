if isinstance(_browse_data['content'], list):
    if _browse_data['api_call'] == 'search':
        for search_data_dict in _browse_data['content']:
            _search_pub_date = search_data_dict.get('Published')
            _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)
            if published_date_from is not None and published_date_to is not None:
                if (_search_pub_date_timestamp >= published_date_from) and (
                        _search_pub_date_timestamp <= published_date_to):
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(search_data_dict)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
                else:
                    pass
            elif published_date_from is not None and published_date_to is None:
                print("From Date Given To date Not Given")
                if _search_pub_date_timestamp >= published_date_from:
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(search_data_dict)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
            elif published_date_from is None and published_date_to is not None:
                print("From date is None and To Date Given")
                if _search_pub_date_timestamp <= published_date_to:
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(search_data_dict)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
            else:
                print("Published Date is Note return based on the count")
                if _MAX_RESULTS_RETURN != 0:
                    _result_data_dict['content'].append(search_data_dict)
                    _MAX_RESULTS_RETURN -= 1
                else:
                    pass
    elif _browse_data['api_call'] == 'last':
        for last_data_dict in _browse_data['content']:
            if _MAX_RESULTS_RETURN != 0:
                _result_data_dict['content'].append(last_data_dict)
                _MAX_RESULTS_RETURN -= 1
            else:
                pass
    else:
        raise NotImplementedError()
elif isinstance(_browse_data['content'], dict):
    print("The resposne data is dict object")
    if _browse_data['api_call'] == 'browse':
        print("Needs to Parse the Browse Data")
        _result_data_dict['api_call'] = 'browse'
        for key_data, value_data in _browse_data:
            _result_data_dict[key_data] = value_data
    elif _browse_data['api_call'] == 'search':
        _result_data_dict['api_call'] = 'search'
        print("Needs to Parse Search data")
        _list_dict_elements = _browse_data['content']['data']
        for dict_data in _list_dict_elements:
            _pub_date = dict_data.get('Published')
            print(_pub_date)
            _pub_date_miliseconds = self._get_gm_epoch_time_stamp(date_string=_pub_date)
            if published_date_from is not None and published_date_to is not None:
                if (_pub_date_miliseconds >= published_date_from) and (_pub_date_miliseconds <= published_date_to):
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(dict_data)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
                else:
                    pass
            elif published_date_from is not None and published_date_to is None:
                print("From Date Given To date Not Given")
                if _pub_date_miliseconds >= published_date_from:
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(dict_data)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
            elif published_date_from is None and published_date_to is not None:
                print("From date is None and To Date Given")
                if _pub_date_miliseconds <= published_date_to:
                    if _MAX_RESULTS_RETURN != 0:
                        _result_data_dict['content'].append(dict_data)
                        _MAX_RESULTS_RETURN -= 1
                    else:
                        pass
            else:
                print("Published Date is Note return based on the count")
                if _MAX_RESULTS_RETURN != 0:
                    _result_data_dict['content'].append(dict_data)
                    _MAX_RESULTS_RETURN -= 1
                else:
                    pass
    elif _browse_data['api_call'] == 'db':
        _result_data_dict['api_call'] = 'db'
        _result_data_dict['content'].append(_browse_data['content'])
    elif _browse_data['api_call'] == 'cve':
        _result_data_dict['api_call'] = 'cve'
        _result_data_dict['content'].append(_browse_data['content'])