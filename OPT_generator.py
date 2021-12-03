import math
import random


def generate_opt_boxes(pattern, total_impact, biggest_side_len):
    boxes = []
    summary = 0
    if pattern == 'cliffs':
        boxes.append(1)
        summary = 1
        while summary < total_impact:
            current_box = boxes[-1]
            if current_box == biggest_side_len:
                boxes.append(1)
                summary = summary + 1
            else:
                boxes.append(current_box * 2)
                summary = summary + (current_box * 2) ** 2
        print(summary)

    if pattern == '1-constant':
        for i in range(total_impact):
            boxes.append(1)
        summary = total_impact

    if pattern == 'big-constant':
        while summary < total_impact:
            boxes.append(biggest_side_len)
            summary = summary + biggest_side_len * biggest_side_len

    if pattern == '64-constant':
        while summary < total_impact:
            side = 64
            boxes.append(side)
            summary = summary + side * side

    if pattern == '2-constant':
        while summary < total_impact:
            side = 2
            boxes.append(side)
            summary = summary + side * side

    if pattern == '4-constant':
        while summary < total_impact:
            side = 4
            boxes.append(side)
            summary = summary + side * side

    if pattern == '8-constant':
        while summary < total_impact:
            side = 8
            boxes.append(side)
            summary = summary + side * side

    if pattern == '16-constant':
        while summary < total_impact:
            side = 16
            boxes.append(side)
            summary = summary + side * side

    if pattern == '32-constant':
        while summary < total_impact:
            side = 32
            boxes.append(side)
            summary = summary + side * side

    if pattern == 'random':
        exp = random.randint(0, int(math.log2(biggest_side_len)))
        boxes.append(int(2 ** exp))
        summary = int((2 ** exp) * (2 ** exp))
        while summary < total_impact:
            exp = random.randint(0, min(1 + int(math.log2(boxes[-1])), \
                                        int(math.log2(biggest_side_len))))
            boxes.append(int(2 ** exp))
            summary = summary + int((2 ** exp) * (2 ** exp))

    if pattern == 'peaks':
        boxes.append(1)
        summary = 1
        up = True
        while summary < total_impact:
            if up:
                boxes.append(boxes[-1] * 2)
                if boxes[-1] == biggest_side_len:
                    up = False
            else:
                boxes.append(int(boxes[-1] / 2))
                if boxes[-1] == 1:
                    up = True
            summary = summary + (boxes[-1] ** 2)

    return boxes, summary
