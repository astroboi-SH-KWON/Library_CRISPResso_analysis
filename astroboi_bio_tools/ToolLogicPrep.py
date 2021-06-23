import operator

class ToolLogicPreps:
    def __init__(self):
        pass

    def sort_list_by_ele(self, data_list, ele_idx, up_down_flag=True):
        print("st : sort_list_by_ele_idx", ele_idx)
        result_list = []
        for tmp_arr in sorted(data_list, key=lambda tmp_arr: tmp_arr[ele_idx], reverse=up_down_flag):
            result_list.append(tmp_arr)
        print("DONE : sort_list_by_ele_idx", ele_idx)
        return result_list

    # TODO tuple works???
    """
    :param
        dcnd_f : Descending
    """
    def sort_list_by_multi_idx(self, data_list, idx_tupl, dcnd_f=True):
        # return data_list.sort(key=operator.itemgetter(1, 0), reverse=rev_f)
        return data_list.sort(key=operator.itemgetter(idx_tupl), reverse=dcnd_f)
