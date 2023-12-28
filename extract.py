import pandas as pd
import numpy as np

def extration_per_100ms(input_csv_path):
    # 読み込む列名を指定する
    columns_to_extract = ['frame','face_id','timestamp',

                          'eye_lmk_X_0','eye_lmk_X_2','eye_lmk_X_4','eye_lmk_X_6',
                          'eye_lmk_Y_0','eye_lmk_Y_2','eye_lmk_Y_4','eye_lmk_Y_6',
                          'eye_lmk_Z_0','eye_lmk_Z_2', 'eye_lmk_Z_4', 'eye_lmk_Z_6',

                          'eye_lmk_X_28','eye_lmk_X_30','eye_lmk_X_32','eye_lmk_X_34',
                          'eye_lmk_Y_28','eye_lmk_Y_30','eye_lmk_Y_32','eye_lmk_Y_34',
                          'eye_lmk_Z_28', 'eye_lmk_Z_30', 'eye_lmk_Z_32', 'eye_lmk_Z_34',

                          'eye_lmk_X_8','eye_lmk_X_10','eye_lmk_X_11','eye_lmk_X_12','eye_lmk_X_14','eye_lmk_X_16','eye_lmk_X_17','eye_lmk_X_18',
                          'eye_lmk_Y_8', 'eye_lmk_Y_10', 'eye_lmk_Y_11', 'eye_lmk_Y_12', 'eye_lmk_Y_14', 'eye_lmk_Y_16','eye_lmk_Y_17', 'eye_lmk_Y_18',
                          'eye_lmk_Z_8', 'eye_lmk_Z_10', 'eye_lmk_Z_11', 'eye_lmk_Z_12', 'eye_lmk_Z_14', 'eye_lmk_Z_16','eye_lmk_Z_17', 'eye_lmk_Z_18',

                          'eye_lmk_X_36', 'eye_lmk_X_38', 'eye_lmk_X_39', 'eye_lmk_X_40', 'eye_lmk_X_42', 'eye_lmk_X_44','eye_lmk_X_45', 'eye_lmk_X_46',
                          'eye_lmk_Y_36', 'eye_lmk_Y_38', 'eye_lmk_Y_39', 'eye_lmk_Y_40', 'eye_lmk_Y_42', 'eye_lmk_Y_44','eye_lmk_Y_45', 'eye_lmk_Y_46',
                          'eye_lmk_Z_36', 'eye_lmk_Z_38', 'eye_lmk_Z_39', 'eye_lmk_Z_40', 'eye_lmk_Z_42', 'eye_lmk_Z_44','eye_lmk_Z_45', 'eye_lmk_Z_46',


                          'AU01_r', 'AU02_r','AU04_r','AU05_r','AU06_r','AU07_r','AU09_r','AU10_r','AU12_r','AU14_r','AU15_r',
                          'AU17_r','AU20_r','AU23_r','AU25_r','AU26_r','AU45_r',

                          'pose_Rx', 'pose_Ry', 'pose_Rz'
                          ]  

    # CSVファイルを読み込み
    df = pd.read_csv(input_csv_path)

    # 特定の列を抽出
    selected_columns = df[columns_to_extract]
    
    # 回転角に関する列を小数第２位で四捨五入
    selected_columns['pose_Rx'] = np.round(selected_columns['pose_Rx'], decimals=2)
    selected_columns['pose_Ry'] = np.round(selected_columns['pose_Ry'], decimals=2)
    selected_columns['pose_Rz'] = np.round(selected_columns['pose_Rz'], decimals=2)

    a = pd.DataFrame(columns=selected_columns.columns)

    # 0.1秒ごと
    for row in selected_columns.itertuples(index=False):
        row_dict = row._asdict()
        if sum(c.isdigit() for c in str(row.timestamp)) <=2:
   
            a = a.append(row_dict, ignore_index=True) 
    return a
  