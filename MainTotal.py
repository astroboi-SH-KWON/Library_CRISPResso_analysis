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
    WORK_DIR = "/extdata1/GS/PE_byproduct/PECV_CRISPResso/run_CRISPResso2_in_cmd/"
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

    resources = util.get_files_from_dir(WORK_DIR + OU + "*_result.txt")

    tot_res_list = []
    for f_path in resources:
        res_list = util.read_tsv_ignore_N_line(f_path)
        brcd = f_path.split("/")[-1].replace("_result.txt", "")
        wt_rtio = 0.0
        pure_pe = 0.0
        by_prdc = 0.0
        im_pure = 0.0

        for res_arr in res_list:
            prm_ed_flag = res_arr[2]
            mut_ed_flag = res_arr[7]
            corrct_read = float(res_arr[-1])
            if 'Not' in prm_ed_flag:
                if 'True' == mut_ed_flag:
                    wt_rtio += corrct_read
                else:
                    by_prdc += corrct_read
            else:
                if 'True' == mut_ed_flag:
                    pure_pe += corrct_read
                else:
                    im_pure += corrct_read

        tot_res_list.append([brcd, wt_rtio, pure_pe, by_prdc, im_pure])

    header = ["brcd", "WT%", "Pure_PE%", "By_product%", "Impure_PE%"]
    util.make_tsv(WORK_DIR + OU + "tot.txt", header, tot_res_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    main()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))