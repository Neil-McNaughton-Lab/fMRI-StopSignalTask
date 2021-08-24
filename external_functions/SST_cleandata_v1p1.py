# -*- coding: utf-8 -*-
"""
Script to take psychopy output data and resave it in a format that
Neil's group's scripts can use.

Version's of PsychoPy installed on the pacific radiology clinic:
    PsychoPy2 1.85.6
    PsychoPy3 3.1.2 win64

@author: hobrh17p
"""
#Need panadas: 0.23.3
import pandas as pd

def resave(file_path, output_text=None):
    '''
    '''
    
    if file_path[-4:] != '.csv':
        file_path = file_path + '.csv'
    
    if output_text == None:
        output_text = 'Output from SSI program using GoRT to generate fast and slow SSDs'
    elif not isinstance(output_text ,str):
        raise TypeError('The variable \'output_text\' must be a str.')
    
    def check_data(data):
        # Check if the save function was called too early and exit if so:
        try:
            print(len(data['Trial']))
        except KeyError:
            print('No exeriment data stored in ' + file_path)
            raise NameError('No exeriment data stored in ' + file_path)
    
    # Load into panadas dataframe and isolate trial-by-trial data:
    data = pd.read_csv(file_path)
    check_data(data)
    new_data = data[data['Trial'].notna()].copy()
    
    # Check the last line of ned_data for NaN vlaues (cause from an aborted exp):
    index2drop = len(new_data)-1
    if str(new_data.iloc[index2drop]['frameRate']) == 'nan':
        new_data = new_data.drop(new_data.index[index2drop])
    
    # Correct the columns that often have mismatched rows:
    mmcol = ['SSD1',
             'SSD2',
             'SSD3']#,
             # 'blank_ISI_stim.started',
             # 'blank_ISI_stim.stopped',
             # 'text.started',
             # 'text.stopped',
             # 'focus_circle.started',
             # 'focus_circle.stopped',
             # 'green_go_circle.started',
             # 'green_go_circle.stopped',
             # 'arrow_stim_go.started',
             # 'arrow_stim_go.stopped',
             # 'feedback_img.started',
             # 'feedback_img.stopped',
             # 'polygon.started',
             # 'polygon.stopped']
    N_elements = len(new_data)
    for col in mmcol:
        mmcol_data = [i for i in data[data[col].notna()][col]]
        new_data[col] = mmcol_data + (N_elements-len(mmcol_data))*[None]
    
    # Look for columns take may not exist if the run was performed incorrectly
    # and create some artifical ones:
    try:
        len(new_data['gokey_resp.rt'])
    except:
        new_data['gokey_resp.rt'] = 0.0
    
        
    # %% Append and orgonise data (NOTE: order matters!):
    # Additional note: I loop over new_data['TrialType'] in a few places. 
    # This is done to improve readablity. However, it does mean there are a few 
    # more loops than there need to be. Processing time can be reduced by 
    # collapsing all these loops into one.
        
    ## Tone (Hz):
    new_data['Tone (Hz)'] = data[data['Tone (Hz)'].notna()]['Tone (Hz)'][0].copy()
    
    ## StopInhibit:
    new_data['StopInhibit'] = new_data['TrialType'].astype(bool).astype(int).copy()
    
    ## RXTime:
    try:
        new_data['RXTime'] = new_data['gokey_resp.rt'].combine_first(new_data['stopkey_resp.rt'])
    except:
        new_data['RXTime'] = new_data['gokey_resp.rt']
    new_data['RXTime'] = new_data['RXTime'].fillna(0.0)
    
    ## Choice:
    try:
        new_data['Choice'] = new_data['gokey_resp.keys'].combine_first(new_data['stopkey_resp.keys']).astype(str)
    except:
        new_data['Choice'] = new_data['gokey_resp.keys'].astype(str)
    new_data['Choice'] = new_data['Choice'].replace(['None','nan'], 'N')
    
    if new_data['handedness'].iloc[0] == 'Right':
        new_data['Choice'] = new_data['Choice'].replace(['1','1.0'], 'L')
        new_data['Choice'] = new_data['Choice'].replace(['2','2.0'], 'R')
    else:
        new_data['Choice'] = new_data['Choice'].replace(['8','8.0'], 'L')
        new_data['Choice'] = new_data['Choice'].replace(['7','7.0'], 'R')
    
    ## BlockSSD_Trial_N:
    block = [i for i in new_data['Block']]
    unique = set(block)
    new_block = []
    for item in unique:
        if item != 0:
            new_block = new_block + list(range(1,block.count(item)+1))
        else:
            new_block = new_block + [0]*block.count(item)
    new_data['BlockSSD_Trial_N'] = new_block  
    
    
    # Using TrialType and block to dertermine no-stop blocks used for training:
    # First, count the blocks and how many go trials they have:
    no_stop_blockN = []
    FBcount = [0, 0]
    for i, blockN in enumerate(new_data['Block']):
        diff = new_data['Block'].iloc[i] - new_data['Block'].iloc[i-1]
        if diff != 0.0:
            no_stop_blockN.append(FBcount)
            FBcount = [0, 0]
            
        # Check if the trail was a GO trial
        if new_data['TrialType'].iloc[i] == 0.0:
            FBcount[0] += 1
        
        # Count the lines in the block:
        FBcount[1] += 1
    no_stop_blockN.append(FBcount)
    if len(no_stop_blockN) > 1:
        no_stop_blockN.pop(0) #Remove the loops inital append from the first iteration
    
    # Second, determine which blocks are all go trials:
    no_stop = []
    for item in no_stop_blockN:
        if item[0] == item[1]:
            no_stop = no_stop + [1]*item[1]
        else:
            no_stop = no_stop + [0]*item[1]
    new_data['No_Stop_Block'] = no_stop
    
    
    ## StairIndex:
    # 1) Get the first stairindex called during stop-go trials:
    StairIndex = []
    for i in new_data['TrialType']:
        if i != 0.0:
            ct = int(i)
            break
    # 2) Construct the stairindex list:
    for i, item in enumerate(new_data['TrialType']):
        if new_data['No_Stop_Block'].iloc[i] == 1:
            StairIndex.append(1)
        elif item != 0.0:
            ct = int(item)
            StairIndex.append(ct)
        else:
            StairIndex.append(ct)
    new_data['StairIndex'] = StairIndex
    
    
    
    ## SSD:
    fullSSDs = [[new_data['SSD1'].iloc[i], new_data['SSD2'].iloc[i], new_data['SSD3'].iloc[i]] for i, a in enumerate(new_data['SSD1'])]
    SSD = []
    for i, blocktype in enumerate(new_data['No_Stop_Block']):
        if blocktype == 1:
            SSD.append(0)
        else:
            SSD.append(fullSSDs[i][new_data['StairIndex'].iloc[i]-1])
    new_data['SSD'] = SSD
    
    
    ## GoCor & GoNoRespons:
    gocor = []
    gonorespons = []
    for i, trial in enumerate(new_data['TrialType']):
        if trial == 0.0:
            if (new_data['Direction'].iloc[i] == '=>') and (new_data['Choice'].iloc[i] == 'R'):
                gocor.append(1)
                gonorespons.append(0)
            elif (new_data['Direction'].iloc[i] == '<=') and (new_data['Choice'].iloc[i] == 'L'):
                gocor.append(1)
                gonorespons.append(0)
            elif new_data['Choice'].iloc[i] == 'N':
                gocor.append(0)
                gonorespons.append(1)
            else:
                gocor.append(0)
                gonorespons.append(0)
        else:
            gocor.append(0)
            gonorespons.append(0)
    new_data['GoCor'] = gocor
    new_data['GoNoResponse'] = gonorespons
    
    
    ## NullTime:
    ''' Is this ISI + ITI or just ISI? '''
    new_data['NullTime'] = new_data['ISI'].copy()
        
        
    ## StairCounter(0)
    new_data['StairCounter(0)'] = 0
    ## StairCounter(1)
    new_data['StairCounter(1)'] = 0
    ## StairCounter(2)
    new_data['StairCounter(2)'] = -1*(new_data['No_Stop_Block']-1)
    ## StairCounter(3)
    new_data['StairCounter(3)'] = 0
    
    
    ## Prog.Trial:
    progtrial = []
    for trial in new_data['TrialType']:
        if trial == 0.0:
            progtrial.append('Go')
        else:
            progtrial.append('Stop')
    new_data['Prog.Trial'] = progtrial
    
    
    
    # %% create new data frame to save as a csv:## New dataframe:
    DATA = new_data[['Trial',
                     'Block',
                     'BlockSSD_Trial_N',
                     'TrialType',
                     'StopInhibit',
                     'SSD',
                     'RXTime',
                     'StairIndex',
                     'GoCor',
                     'Choice',
                     'GoNoResponse',
                     'NullTime',
                     'StairCounter(0)',
                     'StairCounter(1)',	
                     'StairCounter(2)',
                     'StairCounter(3)',
                     'Prog.Trial',
                     'Tone (Hz)']].copy()

    
    
    ## Creating File Name:
    # Get file name from file_path:
    def month2int(monthstr):
        monthstr = monthstr.lower()
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                  'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        monthstr = [i for i, month in enumerate(months) if month == monthstr][0] + 1
        return str(monthstr).zfill(2)
    
    # Correct the folder slashes and seperate all folders:
    new_path = file_path.replace('/','\\')
    folders = new_path.split('\\')
    
    # Break up the filename and adjust it (makes it disinguishable from psychopy's):
    name = folders[-1].split('_')
    name[-3] = month2int(name[-3])
    folders[-1] = '_'.join(''.join(name[-4:-1]))

    #Rejoin the file path:
    new_path = '\\'.join(folders)
    
    
    
    ## Preparing additional information to be written to the csv:
    #Create a list to locate the position of the break 
    #between go trials and stop-go trials.
    check = no_stop + [0]
    gap_line_position = []
    for i in range(len(check)-1):
        gap_line_position.append(check[i] - check[i+1])
    
    
    # Setting general info:
    general_info = ['']*11
    general_info[0] = ''.join([output_text, '\t', name[-2], '/', name[-3], '/', 
                               name[-4], '\t', name[-1][:-6], ':', name[-1][2:-4]])
    general_info[3] = 'Participant Number: ' + str(data['participant'].iloc[0])
    general_info[4] = 'Age: '
    general_info[5] = 'Weight: '
    general_info[6] = 'Gender: '
    general_info[7] = 'Handedness: '
    general_info[8] = 'Ethnicity: '
    
    
    ## CSV writing function:
    def write_csv(filename, df, units = 1):
        '''
        Units corresponds to the time units' order of magnitude.
            e.g.    1 = 1 s
                 1000 = 1 ms
                 1/60 = 1 minute
        '''
        import csv
        gap_bar = ''.join(['_-']*84)
        
        df['SSD'] = df['SSD']*units
        df['RXTime'] = df['RXTime']*units
        df['NullTime'] = df['NullTime']*units
        
        print('Saving: ' + filename)
        with open(filename, 'w', newline='') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',')#,
                                    # quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in general_info:
                datawriter.writerow([i])
                
            datawriter.writerow(df.columns.tolist())
                                   
            for i in range(len(df)):
                datawriter.writerow(list(df.iloc[i]))
                if gap_line_position[i] == 1:
                    datawriter.writerow([gap_bar])
    
    
    ## Write the csv:
    write_csv(new_path, DATA, units = 1000)
    return



# %% PFFFFFFFFFFFFFFFFF

# # Get all the data columns: 
# col_names = data.columns.tolist()
# for name in col_names:
#     print(name)
