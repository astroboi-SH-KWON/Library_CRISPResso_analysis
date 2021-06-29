import time
import os
import multiprocessing as mp
import platform

import Util
import Logic
import LogicPrep
#################### st env ####################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/YuGooSang/20210527_CRISPResso2/WORK_DIR/"

IN = 'input/'
OU = 'output/'

os.makedirs(WORK_DIR + IN, exist_ok=True)
os.makedirs(WORK_DIR + OU, exist_ok=True)

TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)
#################### en env ####################

def main():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()
    logic = Logic.Logics()

    file_dict = {}
    for f_path in util.get_files_recursively(WORK_DIR + IN):
        util.get_file_path_dict(f_path, file_dict)

    for brcd, path_arr in file_dict.items():

        # # 1) CRISPResso result file 불러오기
        # # 2) Mut_type 결정 (예시 파일의 D열)
        bg_list, pe_list = logic_prep.get_bg_pe_list(path_arr)
        bg_dict = logic_prep.make_list_to_dict_by_ele(bg_list, 2)

        # # 3) PE-treated %Reads에서 BG % Reads 보정해주기 (예시 파일의 L, M, N 열)
        pe_list = logic.get_correct_reads(bg_dict, pe_list)

        # # 4) Mut_position / WT_seq / Mut_seq 정리 (예시 파일의 E, F, G열)
        pe_list = logic.get_mut_pos_seqs(pe_list)

        # # 5) prepare result_pe_list for result file
        pe_list = [[pe_arr[2], pe_arr[3], pe_arr[1], pe_arr[0].replace("_", " "),
                    str(pe_arr[-3]).replace("[", "").replace("]", ""),
                    str(pe_arr[-2]).replace("[", "").replace("]", ""),
                    str(pe_arr[-1]).replace("[", "").replace("]", "")] + pe_arr[4: 8] + pe_arr[9: 12] for pe_arr in
                   pe_list if pe_arr[11] != 0.0]  # Corrected.%reads == 0 인 row 삭제

        header = ["Aligned_Sequence", "Reference_Sequence", "Prime-editing", "Mut_type (Major)", "Mut_Position (Major)",
                  "WT_seq", "Mut_seq", "Mutated", "n_deleted", "n_inserted", "n_mutated", "PE-treated.%Reads",
                  "BG.%Reads", "Corrected.%Reads"]
        util.make_tsv(WORK_DIR + OU + brcd + "_result.txt", header, pe_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    main()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))