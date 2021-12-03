from mlGreenPaging import oracle
from michaelGreenPaging import get_next_michael_box
import math


def mi_slicing_green_paging(opt, accuracy, biggest_side_len):
    piece = 1 * biggest_side_len * biggest_side_len
    by_oracle = False

    oracle_mi = 0
    michael_mi = 0

    total_oracle_mi = 0
    total_michael_mi = 0

    available_height = 0
    available_width = 0
    sum_memory_impact = 0

    box_counters = [0 for i in range(int(math.log2(biggest_side_len)) + 1)]
    previous_michael_box = 1
    previous_oracle = math.inf

    for opt_box in opt:
        remainder_width = opt_box
        while available_height < opt_box or available_width == 0:
            if by_oracle:
                mlbox = oracle(accuracy, opt_box, previous_oracle, biggest_side_len)
                previous_oracle = mlbox
                sum_memory_impact = sum_memory_impact + mlbox * mlbox
                total_oracle_mi = total_oracle_mi + mlbox * mlbox
                oracle_mi = oracle_mi + mlbox * mlbox
                available_height = mlbox
                available_width = mlbox
                if oracle_mi > piece:
                    michael_mi = 0
                    by_oracle = False
            else:
                michaelbox = get_next_michael_box(previous_michael_box, box_counters, biggest_side_len)
                box_counters[int(math.log2(michaelbox))] += 1
                previous_michael_box = michaelbox
                sum_memory_impact = sum_memory_impact + michaelbox * michaelbox
                total_michael_mi = total_michael_mi + michaelbox * michaelbox
                michael_mi = michael_mi + michaelbox * michaelbox
                available_height = michaelbox
                available_width = michaelbox
                if michael_mi > piece:
                    oracle_mi = 0
                    by_oracle = True

        if available_width >= remainder_width:
            available_width = available_width - remainder_width
        else:
            remainder_width = remainder_width - available_width
            available_width = 0
            while available_height < opt_box or available_width == 0:
                if by_oracle:
                    mlbox = oracle(accuracy, opt_box, previous_oracle, biggest_side_len)
                    previous_oracle = mlbox
                    sum_memory_impact = sum_memory_impact + mlbox * mlbox
                    total_oracle_mi = total_oracle_mi + mlbox * mlbox
                    oracle_mi = oracle_mi + mlbox * mlbox
                    available_height = mlbox
                    available_width = mlbox
                    if oracle_mi > piece:
                        michael_mi = 0
                        by_oracle = False
                else:
                    michaelbox = get_next_michael_box(previous_michael_box, box_counters, biggest_side_len)
                    box_counters[int(math.log2(michaelbox))] += 1
                    previous_michael_box = michaelbox
                    sum_memory_impact = sum_memory_impact + michaelbox * michaelbox
                    total_michael_mi = total_michael_mi + michaelbox * michaelbox
                    michael_mi = michael_mi + michaelbox * michaelbox
                    available_height = michaelbox
                    available_width = michaelbox
                    if michael_mi > piece:
                        oracle_mi = 0
                        by_oracle = True

            available_width = available_width - remainder_width

    print(str(total_michael_mi) + '  -MICHAEL-s')
    print(str(total_oracle_mi) + '  -ML-s')
    return sum_memory_impact
