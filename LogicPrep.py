
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps
import Util


class LogicPreps(ToolLogicPreps):
    def __init__(self):

        super().__init__()

        self.del_str = '_del'
        self.ins_str = '_ins'
        self.mut_str = '_mut'

        self.wt_str = 'WT'
        self.pure_pe_str = 'Pure_PE'

        self.not_prm_edit_str = 'Not_prime-edited'
        self.prm_edit_str = 'Prime-edited'

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
            bg_wt_list += [[self.del_str, self.not_prm_edit_str] + val_arr if int(val_arr[3]) > 0 else ['',
                                                                                                        self.not_prm_edit_str] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[0])]

            bg_wt_list = [[val_arr[0] + self.ins_str] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          bg_wt_list]
            bg_wt_list = [[val_arr[0] + self.mut_str] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          bg_wt_list]
            bg_wt_list = [[self.wt_str] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in bg_wt_list]
        except Exception as err:
            print("bg_wt path :", path_arr[0], "\n", err)
            pass

        try:
            bg_hd_list += [[self.del_str, self.prm_edit_str] + val_arr if int(val_arr[3]) > 0 else ['',
                                                                                                    self.prm_edit_str] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[1])]

            bg_hd_list = [[val_arr[0] + self.ins_str] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          bg_hd_list]
            bg_hd_list = [[val_arr[0] + self.mut_str] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          bg_hd_list]
            bg_hd_list = [[self.pure_pe_str] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in bg_hd_list]
        except Exception as err:
            print("bg_hdr path :", path_arr[1], "\n", err)
            pass

        bg_list = bg_wt_list + bg_hd_list
        bg_wt_list.clear()
        bg_hd_list.clear()
        del bg_wt_list, bg_hd_list

        try:
            pe_wt_list += [[self.del_str, self.not_prm_edit_str] + val_arr if int(val_arr[3]) > 0 else ['',
                                                                                                        self.not_prm_edit_str] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[2])]

            pe_wt_list = [[val_arr[0] + self.ins_str] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          pe_wt_list]
            pe_wt_list = [[val_arr[0] + self.mut_str] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          pe_wt_list]
            pe_wt_list = [[self.wt_str] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in pe_wt_list]
        except Exception as err:
            print("pe_wt path :", path_arr[2], "\n", err)
            pass

        try:
            pe_hd_list += [[self.del_str, self.prm_edit_str] + val_arr if int(val_arr[3]) > 0 else ['',
                                                                                                    self.prm_edit_str] + val_arr
                           for val_arr in util.read_tsv_ignore_N_line(path_arr[3])]

            pe_hd_list = [[val_arr[0] + self.ins_str] + val_arr[1:] if int(val_arr[6]) > 0 else val_arr for val_arr in
                          pe_hd_list]
            pe_hd_list = [[val_arr[0] + self.mut_str] + val_arr[1:] if int(val_arr[7]) > 0 else val_arr for val_arr in
                          pe_hd_list]
            pe_hd_list = [[self.pure_pe_str] + val_arr[1:] if val_arr[0] == '' else val_arr for val_arr in pe_hd_list]
        except Exception as err:
            print("pe_hdr path :", path_arr[3], "\n", err)
            pass
        pe_list = pe_wt_list + pe_hd_list
        pe_wt_list.clear()
        pe_hd_list.clear()
        del pe_wt_list, pe_hd_list

        return bg_list, pe_list