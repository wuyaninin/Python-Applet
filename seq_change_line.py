#%%
# 这是一个用于处理DNA/aa序列格式的小程序
# 将长序列以每n个字符数换行
string = input('请输入你需要处理的 序列：')
string = "".join(string.split()) # 删除字符中的额外的空格
ch_per_line = int(input('请输入你需要的 每行的字符数目：'))

'''
测试用数据
string = '123456789'
ch_per_line = 4
'''

line_num = len(string)//ch_per_line
# print(line_num)

# 使用循环来分割string为长为ch_per_line的line_num+1个字符串
string_slice = []
for i in range(line_num):
    line_slice = string[i*ch_per_line:(i+1)*ch_per_line]
    # print(line_slice)
    string_slice.append(line_slice)

## 处理最后一个slice
last_line_slice = string[ch_per_line*(line_num):]
string_slice.append(last_line_slice)

string_sliced = ('\n').join(string_slice)
print(string_sliced)

#


# %%
