import pandas as pd
def process(em, qm, cm):
    sol_1_cols = []
    sol_2_cols = []
    sol_3_cols = []
    for column in em: 
        if 'Solution 1' in column:
            sol_1_cols.append(column)
        if 'Solution 2' in column:
            sol_2_cols.append(column)
        if 'Solution 3' in column:
            sol_3_cols.append(column)
    hg = [em, qm, cm]
    for df in hg:
        df['Solution 1'] = df[sol_1_cols].mean(axis = 1)
        df['Solution 2'] = df[sol_2_cols].mean(axis = 1)
        df['Solution 3'] = df[sol_3_cols].mean(axis = 1)
        df['Solution 1 Norm'] = df['Solution 1']/df['Total Marks']
        df['Solution 2 Norm'] = df['Solution 2']/df['Total Marks']
        df['Solution 3 Norm'] = df['Solution 3']/df['Total Marks']
        df['Solution 1 Norm Std'] = df[sol_1_cols].std(axis = 1)/df['Total Marks']
        df['Solution 2 Norm Std'] = df[sol_2_cols].std(axis = 1)/df['Total Marks']
        df['Solution 3 Norm Std'] = df[sol_3_cols].std(axis = 1)/df['Total Marks']
        df.drop(df.columns[[2, 3, 4, 5, 6, 7]], axis=1, inplace=True)   
    sol_1_cols = []
    sol_2_cols = []
    sol_3_cols = []
    for column in em: 
        if 'Solution 1' in column:
            sol_1_cols.append(column)
        if 'Solution 2' in column:
            sol_2_cols.append(column)
        if 'Solution 3' in column:
            sol_3_cols.append(column)
    # Iterate through each DataFrame in the HG list
    for i in range(len(hg)):
        df = hg[i]
        df1 = df.copy()
        df2 = df.copy()
        df3 = df.copy()
        
        # Drop the columns not related to each solution
        df1.drop(sol_2_cols + sol_3_cols, axis=1, inplace=True)
        df2.drop(sol_1_cols + sol_3_cols, axis=1, inplace=True)
        df3.drop(sol_1_cols + sol_2_cols, axis=1, inplace=True)
        
        # Rename the columns
        df1.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        df2.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        df3.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        
        # Concatenate the DataFrames
        concatenated_df = pd.concat([df1, df2, df3], ignore_index=True, axis=0)
        
        # Assign the concatenated DataFrame back to the original list
        hg[i] = concatenated_df
    return hg
    
def que_process(NMS_EM, NMS_CM, NMS_QM, MS_EM, MS_CM, MS_QM):
    sol_1_cols = []
    sol_2_cols = []
    sol_3_cols = []

    #Seperating Solution1,2,3 columns
    for column in NMS_EM: 
        if 'Solution 1' in column:
            sol_1_cols.append(column)
        if 'Solution 2' in column:
            sol_2_cols.append(column)
        if 'Solution 3' in column:
            sol_3_cols.append(column)
    SG = [NMS_EM, NMS_CM, NMS_QM, MS_EM, MS_CM, MS_QM]
    for df in SG:
        for column in df:
            if 'Unnamed' in column:
                df.drop(column, axis = 1, inplace = True)
        df['Solution 1'] = df[sol_1_cols].mean(axis = 1)
        df['Solution 2'] = df[sol_2_cols].mean(axis = 1)
        df['Solution 3'] = df[sol_3_cols].mean(axis = 1)
        df['Solution 1 Norm'] = df['Solution 1']/df['Total Marks']
        df['Solution 2 Norm'] = df['Solution 2']/df['Total Marks']
        df['Solution 3 Norm'] = df['Solution 3']/df['Total Marks']
        df['Solution 1 Norm Std'] = df[sol_1_cols].std(axis = 1)/df['Total Marks']
        df['Solution 2 Norm Std'] = df[sol_2_cols].std(axis = 1)/df['Total Marks']
        df['Solution 3 Norm Std'] = df[sol_3_cols].std(axis = 1)/df['Total Marks']
        df.drop(df.columns[[2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
        15, 16]], axis=1, inplace=True)
    sol_1_cols = []
    sol_2_cols = []
    sol_3_cols = []
    for column in NMS_EM: 
        if 'Solution 1' in column:
            sol_1_cols.append(column)
        if 'Solution 2' in column:
            sol_2_cols.append(column)
        if 'Solution 3' in column:
            sol_3_cols.append(column)

    # Iterate through each DataFrame in the SG list
    for i in range(len(SG)):
        df = SG[i]
        df1 = df.copy()
        df2 = df.copy()
        df3 = df.copy()
        
        # Drop the columns not related to each solution
        df1.drop(sol_2_cols + sol_3_cols, axis=1, inplace=True)
        df2.drop(sol_1_cols + sol_3_cols, axis=1, inplace=True)
        df3.drop(sol_1_cols + sol_2_cols, axis=1, inplace=True)
        
        # Rename the columns
        df1.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        df2.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        df3.columns = ['Questions', 'Total Marks', 'Marks', 'Norm', 'Norm Std']
        
        # Concatenate the DataFrames
        concatenated_df = pd.concat([df1, df2, df3], ignore_index=True, axis=0)
        
        # Assign the concatenated DataFrame back to the original list
        SG[i] = concatenated_df
    return SG