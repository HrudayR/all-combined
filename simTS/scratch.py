import pandas as pd

df = pd.read_csv('/home/hruday/PycharmProjects/simTS/SimTS_Representation_Learning/mendeley_orig.csv')
df = pd.concat([df]*3)
print(df)
df.to_csv("/home/hruday/PycharmProjects/simTS/SimTS_Representation_Learning/datasets/mendeley.csv", index=False)



# import sys
# import scipy.io
# import pandas as pd
# from datetime import datetime
#
#
# mat = scipy.io.loadmat('/home/hruday/Downloads/07-19-17_10.33 10degC_trise_Cycle_1to4_w_pauses_Pan18650PF.mat')
#
# headers = ['TimeStamp', 'Voltage', 'Current', 'Ah', 'Wh', 'Power', 'Battery_Temp_degC', 'Time', 'Chamber_Temp_degC']
# time = mat['meas'][0][0][0]
# time = ['0' + time[x].tolist()[0][0] for x in range(len(time))][:400000]
# for i in range(len(time)):
#     try:
#         time[i] = datetime.strptime(time[i], "%m/%d/%Y %I:%M:%S %p")
#     except:
#         time[i] = datetime.strptime(time[i-1], "%m/%d/%Y %I:%M:%S %p")
#
# voltage = mat['meas'][0][0][1].tolist()
# voltage = [x[0] for x in voltage][:400000]
#
# current = mat['meas'][0][0][2].tolist()
# current = [x[0] for x in current][:400000]
#
# ah = mat['meas'][0][0][3].tolist()
# ah = [x[0] for x in ah][:400000]
#
# data = []
#
# for i in range(len(voltage)):
#     data.append([time[i], voltage[i], current[i], ah[i]])
#
# df = pd.DataFrame(data=data, columns=[['Time', 'Voltage', 'Current', 'Ah']])
# # df['Time'] = pd.to_datetime(df['Time'])
# print(df)
# df.to_csv("/home/hruday/PycharmProjects/simTS/SimTS_Representation_Learning/datasets/mendeley.csv", index=False)