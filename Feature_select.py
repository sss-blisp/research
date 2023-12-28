# 必要な説明変数のみ抽出する

class Feature_selection:
    def __init__(self,df):
        self.df = df
    
    def select_with_timestamp(self):
        select_colums = ['timestamp','AU01_r', 'AU02_r', 'AU04_r', 'AU05_r', 'AU06_r', 'AU07_r', 'AU09_r', 'AU10_r', 'AU12_r', 'AU14_r', 'AU15_r', 'AU17_r', 'AU20_r', 'AU23_r', 'AU25_r', 'AU26_r', 'AU45_r', 
                            'pose_Rx', 'pose_Ry', 'pose_Rz', 
                            'dis_right_outer', 'dis_right_inner', 'dis_left_outer', 'dis_left_inner',
                            'dis_eyelids_right', 'dis_eyelids_left', 
                            'pain']
        self.df = self.df[select_colums]  
        return self.df