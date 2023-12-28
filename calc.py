import numpy as np
import pandas as pd

class Calc_dis():
    def __init__(self,df):
        self.df = df

    #眼球と目尻と目頭間の距離の算出
    def outer_inner_center_of_the_eye(self, lmk, bool):

        for record_i in range(len(self.df.index)):
            # 眼球の中心の座標を算出 
        
            X = np.array([ self.df[lmk[0]][record_i], self.df[lmk[1]][record_i], self.df[lmk[2]][record_i], self.df[lmk[3]][record_i]])
            mean_X = np.mean(X)
            Y = np.array([ self.df[lmk[6]][record_i], self.df[lmk[7]][record_i], self.df[lmk[8]][record_i], self.df[lmk[9]][record_i]])
            mean_Y = np.mean(Y)
            Z = np.array([ self.df[lmk[12]][record_i], self.df[lmk[13]][record_i], self.df[lmk[14]][record_i], self.df[lmk[15]][record_i]])
            mean_Z = np.mean(Z)

            center = np.array([mean_X, mean_Y, mean_Z])

            # 目尻、目頭の座標抽出
            # 目尻 = outer, 目頭 = inner
            outer = np.array([ self.df[lmk[4]][record_i] , self.df[lmk[10]][record_i], self.df[lmk[16]][record_i] ])
            inner = np.array([self.df[lmk[5]][record_i], self.df[lmk[11]][record_i], self.df[lmk[17]][record_i]])
            
            #眼球と目尻、目頭との距離
            # 眼球と目尻 = dist_between_center_outer
            # 眼球と目頭 = dist_between_center_inner
            dist_between_center_outer = np.linalg.norm(center - outer)
            dist_between_center_inner = np.linalg.norm(center - inner)
            
            # 列に挿入
            #右目
            if bool == True:
                self.df.loc[record_i, 'dis_right_outer'] = np.round(dist_between_center_outer, decimals=2)
                self.df.loc[record_i, 'dis_right_inner'] = np.round(dist_between_center_inner, decimals=2)

            #左目
            else:
                self.df.loc[record_i, 'dis_left_outer'] = np.round(dist_between_center_outer, decimals=2)
                self.df.loc[record_i, 'dis_left_inner'] = np.round(dist_between_center_inner, decimals=2)
           
        return self.df 
    
    # 閉眼の処理3D(上部、下部ごとの平均座標)
    def euclidean_average_coordinate(self, lmk):
        eye_mean = []
        for record_i in range(len(self.df.index)):
            # 今回は３点の平均値を算出する
            p1 = np.array([self.df[lmk[0]][record_i], self.df[lmk[3]][record_i] , self.df[lmk[6]][record_i] ])
            p2 = np.array([self.df[lmk[1]][record_i], self.df[lmk[4]][record_i] , self.df[lmk[7]][record_i] ])
            p3 = np.array([self.df[lmk[2]][record_i], self.df[lmk[5]][record_i] , self.df[lmk[8]][record_i] ])
            coordinate = np.vstack((p1, p2, p3))
            eye_part_means = np.mean(coordinate , axis=0)
            eye_mean.append(eye_part_means)        
        return eye_mean

    # 閉眼の処理3D(瞼の上下間の距離)
    def dis_euclidean_3D(self, upper_eye_list,down_eye_list, is_right):
        
        for record_i in range(len(self.df.index)):
            upper = np.array([upper_eye_list[record_i][0], upper_eye_list[record_i][1] , upper_eye_list[record_i][2]])
            lower = np.array([down_eye_list[record_i][0], down_eye_list[record_i][1] , down_eye_list[record_i][2]])
            dist = np.linalg.norm(upper - lower)
            dist = np.round(dist, decimals=2)

            # 右目
            if is_right == True:
                self.df.loc[record_i, 'dis_eyelids_right'] = dist
            # 左目
            else:
                self.df.loc[record_i, 'dis_eyelids_left'] = dist

        return self.df



    
