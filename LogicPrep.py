
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps
import Util


class LogicPreps(ToolLogicPreps):
    def make_list_to_dict_by_ele(self, data_list, ele_idx):
        result_dict = {}
        for val_arr in data_list:
            key = val_arr[ele_idx]
            if key in result_dict:
                print("[ERROR] aligned_seq dupled", str(val_arr))
            else:
                result_dict.update({key: val_arr})
        return result_dict

    def get_bg_pe_list(self, path_arr):
        util = Util.Utils()

        bg_wt_list, bg_hd_list, pe_wt_list, pe_hd_list = [], [], [], []

        try:
            bg_wt_list += [
                ['_del', 'Not_prime-edited'] + val_arr if int(val_arr[3]) > 0 else ['', 'Not_prime-edited'] + val_arr
                for val_arr in util.read_tsv_ignore_N_line(path_arr[0])]

            bg_wt_list = [[val_arr[0] + '_ins'] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          bg_wt_list]
            bg_wt_list = [[val_arr[0] + '_mut'] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          bg_wt_list]
            bg_wt_list = [['WT'] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in bg_wt_list]
        except Exception as err:
            print("bg_wt path :", path_arr[0], "\n", err)
            pass

        try:
            bg_hd_list += [['_del', 'Prime-edited'] + val_arr if int(val_arr[3]) > 0 else ['', 'Prime-edited'] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[1])]

            bg_hd_list = [[val_arr[0] + '_ins'] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          bg_hd_list]
            bg_hd_list = [[val_arr[0] + '_mut'] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          bg_hd_list]
            bg_hd_list = [['Pure_PE'] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in bg_hd_list]
        except Exception as err:
            print("bg_hdr path :", path_arr[1], "\n", err)
            pass

        bg_list = bg_wt_list + bg_hd_list
        bg_wt_list.clear()
        bg_hd_list.clear()
        del bg_wt_list, bg_hd_list

        try:
            pe_wt_list += [
                ['_del', 'Not_prime-edited'] + val_arr if int(val_arr[3]) > 0 else ['', 'Not_prime-edited'] + val_arr
                for val_arr in util.read_tsv_ignore_N_line(path_arr[2])]

            pe_wt_list = [[val_arr[0] + '_ins'] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          pe_wt_list]
            pe_wt_list = [[val_arr[0] + '_mut'] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          pe_wt_list]
            pe_wt_list = [['WT'] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in pe_wt_list]
        except Exception as err:
            print("pe_wt path :", path_arr[2], "\n", err)
            pass

        try:
            pe_hd_list += [['_del', 'Prime-edited'] + val_arr if int(val_arr[3]) > 0 else ['', 'Prime-edited'] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[3])]

            pe_hd_list = [[val_arr[0] + '_ins'] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          pe_hd_list]
            pe_hd_list = [[val_arr[0] + '_mut'] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          pe_hd_list]
            pe_hd_list = [['Pure_PE'] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in pe_hd_list]
        except Exception as err:
            print("pe_hdr path :", path_arr[3], "\n", err)
            pass
        pe_list = pe_wt_list + pe_hd_list
        pe_wt_list.clear()
        pe_hd_list.clear()
        del pe_wt_list, pe_hd_list

        return bg_list, pe_list