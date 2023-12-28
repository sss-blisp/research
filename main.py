import pandas as pd

from calc import Calc_dis

from extract import extration_per_100ms

from Feature_select import Feature_selection

import os

input_folder_path = '/Volumes/B2200190/実験/痛みなし/OpenFace/5秒/'
files = os.listdir(input_folder_path)
for index, file_name in enumerate(files, start=1):
    if index <10:
      index = f'{index:02}'
    input_csv_path = input_folder_path +str(index)+'.csv'

    output_csv_path = '../OpenFace/output/痛みなし/5秒/' +str(index)+'.csv'

    df = extration_per_100ms(input_csv_path)


    # ユークリッド距離の計算
    right_lmk = [
        'eye_lmk_X_0','eye_lmk_X_2','eye_lmk_X_4','eye_lmk_X_6','eye_lmk_X_8','eye_lmk_X_14',
        'eye_lmk_Y_0','eye_lmk_Y_2','eye_lmk_Y_4','eye_lmk_Y_6','eye_lmk_Y_8','eye_lmk_Y_14',
        'eye_lmk_Z_0','eye_lmk_Z_2','eye_lmk_Z_4','eye_lmk_Z_6','eye_lmk_Z_8','eye_lmk_Z_14'
    ]

    left_lmk = [
        'eye_lmk_X_28','eye_lmk_X_30','eye_lmk_X_32','eye_lmk_X_34','eye_lmk_X_42','eye_lmk_X_36',
        'eye_lmk_Y_28','eye_lmk_Y_30','eye_lmk_Y_32','eye_lmk_Y_34','eye_lmk_Y_42','eye_lmk_Y_36',
        'eye_lmk_Z_28','eye_lmk_Z_30','eye_lmk_Z_32','eye_lmk_Z_34','eye_lmk_Z_42','eye_lmk_Z_36'
    ]

    Calc_dis = Calc_dis(df)
    # outer_inner_center_of_the_eye(landark, 左右どちらの目かを判断)
    df = Calc_dis.outer_inner_center_of_the_eye(right_lmk, is_right = True)
    df1 = Calc_dis.outer_inner_center_of_the_eye(left_lmk, is_right = False)

    df['dis_left_outer'] = df1['dis_left_outer']
    df['dis_left_inner'] = df1['dis_left_inner']

    right_dis = [
        'dis_right_outer','dis_right_inner'
    ]

    left_dis = [
        'dis_left_outer','dis_left_inner'
    ]

    # 瞼間の距離の計算
    right_lmk_for_eyelids = ['eye_lmk_X_11','eye_lmk_X_17',
                            'eye_lmk_Y_11','eye_lmk_Y_17'
                            ]

    left_lmk_for_eyelids = ['eye_lmk_X_39','eye_lmk_X_45',
                            'eye_lmk_Y_39','eye_lmk_Y_45'
                            ]

    # 3Dでの瞼間の距離の計算
    right_upper_lmk_for_eyelids_3D = ['eye_lmk_X_10','eye_lmk_X_11','eye_lmk_X_12',
                                    'eye_lmk_Y_10','eye_lmk_Y_11','eye_lmk_Y_12',
                                    'eye_lmk_Z_10','eye_lmk_Z_11','eye_lmk_Z_12'
                            ]
    right_down_lmk_for_eyelids_3D = ['eye_lmk_X_16','eye_lmk_X_17','eye_lmk_X_18',
                                    'eye_lmk_Y_16','eye_lmk_Y_17','eye_lmk_Y_18',
                                    'eye_lmk_Z_16','eye_lmk_Z_17','eye_lmk_Z_18'
                            ]

    left_upper_lmk_for_eyelids_3D = ['eye_lmk_X_38','eye_lmk_X_39','eye_lmk_X_40',
                                    'eye_lmk_Y_38','eye_lmk_Y_39','eye_lmk_Y_40',
                                    'eye_lmk_Z_38','eye_lmk_Z_39','eye_lmk_Z_40'
                            ]
    left_down_lmk_for_eyelids_3D = ['eye_lmk_X_44','eye_lmk_X_45','eye_lmk_X_46',
                                    'eye_lmk_Y_44','eye_lmk_Y_45','eye_lmk_Y_46',
                                    'eye_lmk_Z_44','eye_lmk_Z_45','eye_lmk_Z_46'
                            ]
    # 瞼周辺3点の平均座標を算出する
    # euclidean_average_coordinate(landmark)

    # 右目
    right_upper_eye_mean = Calc_dis.euclidean_average_coordinate(right_upper_lmk_for_eyelids_3D)
    right_down_eye_mean = Calc_dis.euclidean_average_coordinate(right_down_lmk_for_eyelids_3D)

    # 左目
    left_upper_eye_mean = Calc_dis.euclidean_average_coordinate(left_upper_lmk_for_eyelids_3D)
    left_down_eye_mean = Calc_dis.euclidean_average_coordinate(left_down_lmk_for_eyelids_3D)


    # 瞼周辺3点の平均座標から、上下瞼間の距離を算出する
    # dis_euclidean_3D(上瞼の3点の平均座標, 下瞼の3点の平均座標, 左右どちらの目かを判断)

    # 右目
    df_eyelids_right = Calc_dis.dis_euclidean_3D(right_upper_eye_mean,right_down_eye_mean, is_right =True)

    # 左目
    df_eyelids_left = Calc_dis.dis_euclidean_3D(left_upper_eye_mean,left_down_eye_mean, is_right =False)

    df['dis_eyelids_left'] = df_eyelids_left['dis_eyelids_left']
    df['dis_eyelids_right'] = df_eyelids_right['dis_eyelids_right']

    # 痛みのデータは1,なしには0のラベル付けをする
    if 'なし' in input_csv_path:
        df['pain'] = 0
    else:
        df['pain'] = 1

    f_s = Feature_selection(df)
    df = f_s.select_with_timestamp()

    df.to_csv(output_csv_path)






