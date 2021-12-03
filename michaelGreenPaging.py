import math
import random


def get_next_michael_box(previous, counters, biggest_side_len):
    if previous == biggest_side_len:
        return 1
    if counters[int(math.log2(previous))] > 0 and \
            counters[int(math.log2(previous))] % 4 == 0:
        return previous * 2
    return 1


def michael_green_paging(opt, biggest_side_len):
    available_height = 0
    available_width = 0
    sum_memory_impact = 0
    box_counters = [0 for i in range(int(math.log2(biggest_side_len)) + 1)]
    previous_michael_box = 1
    c = 0
    for opt_box in opt:
        # print(c)
        c = c + 1
        remainder_width = opt_box
        while available_height < opt_box or available_width == 0:
            michaelbox = get_next_michael_box(previous_michael_box, box_counters, biggest_side_len)
            box_counters[int(math.log2(michaelbox))]+=1
            previous_michael_box = michaelbox
            sum_memory_impact = sum_memory_impact + michaelbox * michaelbox
            available_height = michaelbox
            available_width = michaelbox

        if available_width >= remainder_width:
            available_width = available_width - remainder_width
        else:
            remainder_width = remainder_width - available_width
            available_width = 0
            while available_height < opt_box or available_width == 0:
                michaelbox = get_next_michael_box(previous_michael_box, box_counters, biggest_side_len)
                box_counters[int(math.log2(michaelbox))] += 1
                previous_michael_box = michaelbox
                sum_memory_impact = sum_memory_impact + michaelbox * michaelbox
                available_height = michaelbox
                available_width = michaelbox
            available_width = available_width - remainder_width

    return sum_memory_impact
