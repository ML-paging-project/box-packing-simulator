from OPT_generator import generate_opt_boxes
from memoryImpactSlicing import mi_slicing_green_paging
from miSharing211129 import mi_sharing_green_paging
from michaelGreenPaging import michael_green_paging
from mlGreenPaging import ml_green_paging

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    OPT_PATTERN = 'peaks'
    OPT_MI_BOUND = 10 ** 6
    MAX_SIDE = 128
    REPEAT = 20
    ACC = [5, 65, 95]
    # Pfail = [(100 - i * 10 - 5) / 100 for i in range(10)]
    # ACC = [95, 96, 97, 98, 99, 100]
    Pfail = [(100 - ACC[i]) / 100 for i in range(len(ACC))]
    green_boxes, OPT_MI = generate_opt_boxes(OPT_PATTERN, OPT_MI_BOUND, MAX_SIDE)

    MLratio = []
    MICHAELratio = []
    SLICINGratio = []
    MISHARINGd1ratio = []
    MISHARINGd2ratio = []
    MISHARINGd4ratio = []
    MISHARINGd8ratio = []
    MISHARINGd16ratio = []
    MISHARINGd32ratio = []
    MISHARINGd64ratio = []
    MISHARINGd128ratio = []

    for accuracy in ACC:
        mlmi = 0
        d1 = 0
        d2 = 0
        d4 = 0
        d8 = 0
        d16 = 0
        d32 = 0
        d64 = 0
        d128 = 0
        michmi = michael_green_paging(green_boxes, MAX_SIDE)
        slicingmi = 0
        for tick in range(REPEAT):
            print(str(accuracy) + '---' + str(tick))
            mlmi = mlmi + ml_green_paging(green_boxes, accuracy, MAX_SIDE) / REPEAT
            slicingmi = slicingmi + mi_slicing_green_paging(green_boxes, accuracy, MAX_SIDE) / REPEAT

            d1 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 1) / REPEAT
            d2 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 2) / REPEAT
            d4 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 4) / REPEAT
            d8 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 8) / REPEAT
            d16 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 16) / REPEAT
            d32 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 32) / REPEAT
            d64 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 64) / REPEAT
            d128 += mi_sharing_green_paging(green_boxes, accuracy, MAX_SIDE, 128) / REPEAT
        MLratio.append(mlmi / OPT_MI)
        MICHAELratio.append(michmi / OPT_MI)
        SLICINGratio.append(slicingmi / OPT_MI)
        MISHARINGd1ratio.append(d1 / OPT_MI)
        MISHARINGd2ratio.append(d2 / OPT_MI)
        MISHARINGd4ratio.append(d4 / OPT_MI)
        MISHARINGd8ratio.append(d8 / OPT_MI)
        MISHARINGd16ratio.append(d16 / OPT_MI)
        MISHARINGd32ratio.append(d32 / OPT_MI)
        MISHARINGd64ratio.append(d64 / OPT_MI)
        MISHARINGd128ratio.append(d128 / OPT_MI)

    print('\n\n\n')
    print('OPT MI: ' + str(OPT_MI) + ', OPT pattern: ' + OPT_PATTERN)
    print('Failure Pr, ' + str(Pfail).replace('[', '').replace(']', ''))
    print('Blind Oracle, ' + str(MLratio).replace('[', '').replace(']', ''))
    print('Michael, ' + str(MICHAELratio).replace('[', '').replace(']', ''))
    print('Slicing, ' + str(SLICINGratio).replace('[', '').replace(']', ''))
    print('d=1, ' + str(MISHARINGd1ratio).replace('[', '').replace(']', ''))
    print('d=2, ' + str(MISHARINGd2ratio).replace('[', '').replace(']', ''))
    print('d=4, ' + str(MISHARINGd4ratio).replace('[', '').replace(']', ''))
    print('d=8, ' + str(MISHARINGd8ratio).replace('[', '').replace(']', ''))
    print('d=16, ' + str(MISHARINGd16ratio).replace('[', '').replace(']', ''))
    print('d=32, ' + str(MISHARINGd32ratio).replace('[', '').replace(']', ''))
    print('d=64, ' + str(MISHARINGd64ratio).replace('[', '').replace(']', ''))
    print('d=128, ' + str(MISHARINGd128ratio).replace('[', '').replace(']', ''))
