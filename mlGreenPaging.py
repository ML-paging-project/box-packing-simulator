import math
import random


def oracle(accuracy, current_opt_box, previous_oracle, biggest_side_len):
    pool = [i for i in range(int(math.log2(biggest_side_len)) + 1)]
    rand = random.randint(1, 100)
    output = current_opt_box

    if rand > accuracy:
        # ml fail, make a random mistake
        rand_pick = pool[random.randint(0, len(pool) - 1)]
        while rand_pick == int(math.log2(current_opt_box)):
            rand_pick = pool[random.randint(0, len(pool) - 1)]
        output = 2 ** rand_pick

    output = min(output, 2 * previous_oracle)

    return output


def ml_green_paging(opt, accuracy, biggest_side_len):
    available_height = 0  # the height of box given by the ml
    available_width = 0  # the remaining width of box given by the ml
    sum_memory_impact = 0
    c = 0
    previous_oracle = math.inf
    for opt_box in opt:
        remainder_width = opt_box  # the remaining width of current opt box
        # print(c)
        c = c + 1
        while available_height < opt_box or available_width == 0:  # oracle box is too small or finished
            mlbox = oracle(accuracy, opt_box, previous_oracle, biggest_side_len)
            previous_oracle = mlbox
            sum_memory_impact = sum_memory_impact + mlbox * mlbox
            available_height = mlbox
            available_width = mlbox

        if available_width >= remainder_width:
            available_width = available_width - remainder_width
        else:
            remainder_width = remainder_width - available_width
            available_width = 0
            while available_height < opt_box or available_width == 0:
                mlbox = oracle(accuracy, opt_box, previous_oracle, biggest_side_len)
                previous_oracle = mlbox
                sum_memory_impact = sum_memory_impact + mlbox * mlbox
                available_height = mlbox
                available_width = mlbox
            available_width = available_width - remainder_width

    return sum_memory_impact
