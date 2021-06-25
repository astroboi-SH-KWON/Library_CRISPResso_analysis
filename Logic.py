
from astroboi_bio_tools.ToolLogic import ToolLogics


class Logics(ToolLogics):
    def __init__(self):

        super().__init__()

        self.ignr_mut_type = 'WT'

    def get_correct_reads(self, bg_dict, pe_list):
        tot_read = 0.0
        for pe_arr in pe_list:
            mut_type = pe_arr[0]
            alig_seq = pe_arr[2]
            pe_read = float(pe_arr[-1])
            if alig_seq in bg_dict:
                bg_read = bg_dict[alig_seq][-1]
                pe_arr.append(bg_read)
                new_read = pe_read - float(bg_read)
                if new_read < 0:
                    new_read = 0.0
                pe_arr.append(new_read)
                if mut_type != self.ignr_mut_type:
                    tot_read += new_read
            else:
                pe_arr.append('NA')
                pe_arr.append(pe_read)
                if mut_type != self.ignr_mut_type:
                    tot_read += pe_read
        return [pe_arr[:-1] + [100 - tot_read] if pe_arr[0] == 'WT' else pe_arr for pe_arr in pe_list]

    def get_mut_pos_seqs(self, pe_list):
        for pe_arr in pe_list:
            ali_seq = pe_arr[2]
            ref_seq = pe_arr[3]
            mut_idx_arr = []
            ali_cha_arr = []
            ref_cha_arr = []

            for i in range(len(ref_seq)):
                if ali_seq[i] != ref_seq[i]:
                    mut_idx_arr.append(i)
                    ali_cha_arr.append(ali_seq[i])
                    ref_cha_arr.append(ref_seq[i])

            mut_pos_arr = []
            ali_str_arr = []
            ref_str_arr = []

            tmp_ali_str = ""
            tmp_ref_str = ""
            for i in range(len(mut_idx_arr)):

                if i == 0:
                    mut_pos_arr.append(mut_idx_arr[i])
                    tmp_ali_str += ali_cha_arr[i]
                    tmp_ref_str += ref_cha_arr[i]

                elif (mut_idx_arr[i] - 1) == mut_idx_arr[i - 1]:  # is_connected
                    tmp_ali_str += ali_cha_arr[i]
                    tmp_ref_str += ref_cha_arr[i]

                else:  # new mut pos
                    ali_str_arr.append(tmp_ali_str)
                    ref_str_arr.append(tmp_ref_str)
                    tmp_ali_str = ""
                    tmp_ref_str = ""

                    mut_pos_arr.append(mut_idx_arr[i])
                    tmp_ali_str += ali_cha_arr[i]
                    tmp_ref_str += ref_cha_arr[i]

                if (i + 1) == len(mut_idx_arr):  # is_the_last
                    ali_str_arr.append(tmp_ali_str)
                    ref_str_arr.append(tmp_ref_str)

            pe_arr.append(mut_pos_arr)
            pe_arr.append(ref_str_arr)
            pe_arr.append(ali_str_arr)
        return pe_list