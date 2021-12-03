from michaelGreenPaging import get_next_michael_box
import math, random


def oracle(accuracy, current_opt_box, biggest_side_len):
    pool = [i for i in range(int(math.log2(biggest_side_len)) + 1)]
    rand = random.randint(1, 100)
    output = current_opt_box

    if rand > accuracy:
        # ml fail, make a random mistake
        rand_pick = pool[random.randint(0, len(pool) - 1)]
        while rand_pick == int(math.log2(current_opt_box)):
            rand_pick = pool[random.randint(0, len(pool) - 1)]
        output = 2 ** rand_pick

    return output


def mi_sharing_green_paging(opt, accuracy, biggest_side_len, d):
    total_oracle_mi = 0
    total_michael_mi = 0
    # the given box height and width, try to pack the opt box
    available_height = 0
    available_width = 0
    # total impact
    sum_memory_impact = 0

    # counter to trace michael sequent
    box_counters = [0 for i in range(int(math.log2(biggest_side_len)) + 1)]
    previous_michael_box = 1

    # 3.2
    oracle_box = oracle(accuracy, opt[0], biggest_side_len)
    michael_box = get_next_michael_box(previous_michael_box, box_counters,
                                       biggest_side_len)

    # pseudo code 3. run forever
    for opt_box in opt:
        wait_length = 0  # 3.1
        remainder_width = opt_box  # the width of opt box need to be packed

        # try to find a box big enough to put the opt box into
        while available_height < opt_box or available_width == 0:
            # 3.3 While (cost(Oracle Box) + OracleTotal >
            #                         cost(Michael Box) + MichaelTotal)
            if oracle_box ** 2 + total_oracle_mi > \
                    michael_box ** 2 + total_michael_mi:
                # 3.3.1 using/run michael box
                box_counters[int(math.log2(michael_box))] += 1
                sum_memory_impact += (michael_box ** 2)
                previous_michael_box = michael_box
                # 3.3.2
                total_michael_mi += (michael_box ** 2)
                available_height = michael_box  # try to use michael to pack
                available_width = michael_box
                # 3.3.3
                wait_length += (michael_box ** 2)
                # 3.3.4
                if michael_box >= oracle_box or wait_length >= d ** 2:
                    oracle_box = oracle(accuracy, opt_box, biggest_side_len)
                    wait_length = 0

                # 3.3.5
                michael_box = get_next_michael_box(previous_michael_box,
                                                   box_counters,
                                                   biggest_side_len)

            else:
                # 3.4 using/run oracle box
                sum_memory_impact += (oracle_box ** 2)
                total_oracle_mi += (oracle_box ** 2)
                available_width = oracle_box
                available_height = oracle_box
                oracle_box = oracle(accuracy, opt_box, biggest_side_len)

        # We get a high enough box
        # begin to pack the remainder of the opt box
        if available_width >= remainder_width:   # opt box finished, no remainder
            available_width = available_width - remainder_width
        else:
            # opt box is not finished, has remainder
            remainder_width = remainder_width - available_width
            available_width = 0
            # try to find a box big enough to put the remainder opt box into
            while available_height < opt_box or available_width == 0:
                # 3.3 While (cost(Oracle Box) + OracleTotal >
                #                         cost(Michael Box) + MichaelTotal)
                if oracle_box ** 2 + total_oracle_mi > \
                        michael_box ** 2 + total_michael_mi:
                    # 3.3.1 using/run michael box
                    box_counters[int(math.log2(michael_box))] += 1
                    sum_memory_impact += (michael_box ** 2)
                    previous_michael_box = michael_box
                    # 3.3.2
                    total_michael_mi += (michael_box ** 2)
                    available_height = michael_box  # try to use michael to pack
                    available_width = michael_box
                    # 3.3.3
                    wait_length += (michael_box ** 2)
                    # 3.3.4
                    if michael_box >= oracle_box or wait_length >= d ** 2:
                        oracle_box = oracle(accuracy, opt_box, biggest_side_len)
                        wait_length = 0

                    # 3.3.5
                    michael_box = get_next_michael_box(previous_michael_box,
                                                       box_counters,
                                                       biggest_side_len)

                else:
                    # 3.4 using/run oracle box
                    sum_memory_impact += (oracle_box ** 2)
                    total_oracle_mi += (oracle_box ** 2)
                    available_width = oracle_box
                    available_height = oracle_box
                    oracle_box = oracle(accuracy, opt_box, biggest_side_len)

            # pack the remainder of the opt box
            available_width = available_width - remainder_width

    print(str(total_michael_mi) + '  -MICHAEL-e')
    print(str(total_oracle_mi) + '  -ML-e')
    return sum_memory_impact
