import os

from astroboi_bio_tools.ToolUtil import ToolUtils


class Utils(ToolUtils):

    def get_files_recursively(self, path):
        files_list = []
        for tmp_tup in os.walk(path):
            root = tmp_tup[0]
            sub_dirs = tmp_tup[1]

            if len(sub_dirs) == 0:  # is the last dir
                files = tmp_tup[2]
                for f_nm in files:
                    files_list.append(root + '/' + f_nm)

        return files_list

    """
    :param
        f_path, file_dict
    :return
        file_dict = { brcd : ["BG_WT path", "BG_HDR path", "PE-treated_WT path", "PE-treated_HDR path"]
                    , 'AACACATTTTTTAGTGATCTCGATAGATACTATCAG': ['D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_BG\\CRISPResso_on_BG_AACACATTTTTTAGTGATCTCGATAGATACTATCAG/AACACATTTTTTAGTGATCTCGATAGATACTATCAG.WT.Alleles_frequency_table_around_sgRNA_AGTGGAAGCTGTGTTGCCAATGG.txt', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_BG\\CRISPResso_on_BG_AACACATTTTTTAGTGATCTCGATAGATACTATCAG/AACACATTTTTTAGTGATCTCGATAGATACTATCAG.HDR.Alleles_frequency_table_around_sgRNA_AGTGGAAGCTGTGTTGCCAATGG.txt', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_PE-treated\\CRISPResso_on_PE-treated_AACACATTTTTTAGTGATCTCGATAGATACTATCAG/AACACATTTTTTAGTGATCTCGATAGATACTATCAG.WT.Alleles_frequency_table_around_sgRNA_AGTGGAAGCTGTGTTGCCAATGG.txt', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_PE-treated\\CRISPResso_on_PE-treated_AACACATTTTTTAGTGATCTCGATAGATACTATCAG/AACACATTTTTTAGTGATCTCGATAGATACTATCAG.HDR.Alleles_frequency_table_around_sgRNA_AGTGGAAGCTGTGTTGCCAATGG.txt']
                    , 'AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT': ['D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_BG\\CRISPResso_on_BG_AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT/AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT.WT.Alleles_frequency_table_around_sgRNA_CTCCCCGTTCACGTTCTGCATGG.txt', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_BG\\CRISPResso_on_BG_AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT/AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT.HDR.Alleles_frequency_table_around_sgRNA_CTCCCCGTTCACGTTCTGCATGG.txt', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_PE-treated\\CRISPResso_on_PE-treated_AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT/AACGGGTTTTTTTACTCACATCAGCTCTGCGCAGCT.WT.Alleles_frequency_table_around_sgRNA_CTCCCCGTTCACGTTCTGCATGG.txt', '']
                    , 'AAGGTATTTTTTACATCTGCATATACTCATAACTGG': ['D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_BG\\CRISPResso_on_BG_AAGGTATTTTTTACATCTGCATATACTCATAACTGG/AAGGTATTTTTTACATCTGCATATACTCATAACTGG.WT.Alleles_frequency_table_around_sgRNA_GGAGTACCTTGTCAGGGGGTGGG.txt', '', 'D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/input/Output_HDRmode_PE-treated\\CRISPResso_on_PE-treated_AAGGTATTTTTTACATCTGCATATACTCATAACTGG/AAGGTATTTTTTACATCTGCATATACTCATAACTGG.WT.Alleles_frequency_table_around_sgRNA_GGAGTACCTTGTCAGGGGGTGGG.txt', '']
                    }
    """
    def get_file_path_dict(self, f_path, file_dict):
        if "Alleles_frequency_table_around" in f_path:
            barcd = f_path.split("/")[-1].split(".")[0]
            if barcd in file_dict:
                if "CRISPResso_on_BG" in f_path:
                    if "WT" in f_path:
                        if len(file_dict[barcd][0]) == 0:
                            file_dict[barcd][0] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_BG_WT\n", f_path)
                    elif "HDR" in f_path:
                        if len(file_dict[barcd][1]) == 0:
                            file_dict[barcd][1] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_BG_HDR\n", f_path)
                    else:
                        print("[ERROR] CRISPResso_on_BG\n", f_path)

                elif "CRISPResso_on_PE-treated" in f_path:
                    if "WT" in f_path:
                        if len(file_dict[barcd][2]) == 0:
                            file_dict[barcd][2] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_PE_WT\n", f_path)
                    elif "HDR" in f_path:
                        if len(file_dict[barcd][3]) == 0:
                            file_dict[barcd][3] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_PE_HDR\n", f_path)
                    else:
                        print("[ERROR] CRISPResso_on_PE\n", f_path)

                else:
                    print("[ERROR]", f_path)

            else:
                file_dict.update({barcd: ["", "", "",
                                          ""]})  # ["BG_WT path", "BG_HDR path", "PE-treated_WT path", "PE-treated_HDR path"]
                if "CRISPResso_on_BG" in f_path:
                    if "WT" in f_path:
                        if len(file_dict[barcd][0]) == 0:
                            file_dict[barcd][0] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_BG_WT\n", f_path)
                    elif "HDR" in f_path:
                        if len(file_dict[barcd][1]) == 0:
                            file_dict[barcd][1] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_BG_HDR\n", f_path)
                    else:
                        print("[ERROR] CRISPResso_on_BG\n", f_path)

                elif "CRISPResso_on_PE-treated" in f_path:
                    if "WT" in f_path:
                        if len(file_dict[barcd][2]) == 0:
                            file_dict[barcd][2] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_PE_WT\n", f_path)
                    elif "HDR" in f_path:
                        if len(file_dict[barcd][3]) == 0:
                            file_dict[barcd][3] += f_path
                        else:
                            print("[ERROR] CRISPResso_on_PE_HDR\n", f_path)
                    else:
                        print("[ERROR] CRISPResso_on_PE\n", f_path)

                else:
                    print("[ERROR]", f_path)
