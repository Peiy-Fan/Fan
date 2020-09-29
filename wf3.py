#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys
import re
import collections
import operator
import glob
def file_read(str):  
    #str=str+ '.txt'                                                     #用于读取文件并返回分词之后的单词列表
    f = open(str,'r',-1,'utf-8','ignore',None,True,None)
    tet = f.read().lower()
    text = tet.replace('\n',' ').replace('.',' ').replace(',',' ').\
               replace('!',' ').replace('\\',' ').replace('#',' ').\
               replace('[',' ').replace(']',' ').replace(':',' ').\
               replace('?',' ').replace('-',' ').replace('\'',' ').\
               replace('\"',' ').replace('(',' ').replace(')',' ').\
               replace('—',' ').replace(';',' ').split()
    count_dict = {}
    for str in text:
        if str in count_dict.keys():
           count_dict[str] = count_dict[str] + 1
        else:
           count_dict[str] = 1
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    f.close()
    return count_list                                                          #返回的分词列表
#对分完词之后的列表进行计算total、词频、输出等操作
def get_words(argv,flag):
    if len(argv) == 2:                                                         #如果有两个命令行参数
        try:
            list = file_read(argv[-1])
            opts, args = getopt.getopt(argv,"sh",["ifile","ofile"])
        except getopt.GetoptError:
            print("test.py -i <inputfile> -o <outputfile>")
            sys.exit(2)
        for opt,arg in opts:
            if opt == "-s":                                                    #如果第一个参数是-s
                num = len(list)
                print('total',num)
                print('\n')
                for word in list:
                    print('{:20s}{:>5d}{}'.format(word[0],word[1],'\n'))
            elif opt == "-h":
                print("please input the parameter")
    elif len(argv) == 1:                                                       #如果有一个命令行参数
        pattern = re.compile('.+\.txt')
        folder_name = argv[-1]
        m = re.findall(pattern,folder_name)
        if len(m) != 0:                                                          #参数以.txt结尾，为文件名，直接执行词频操作
            list = file_read(argv[-1])
            if flag == 0:                                                        #标志位为0，把所有单词都列出来
                print('total',len(list))
                print('\n')
                for item in list:
                    print('{:20s}{:>5d}{}'.format(item[0],item[1],'\n'))
            else:                                                                #标志位不为0，只列出前十
                print('total',len(list), 'words')
                print('\n')
                if len(list) > 10:
                    for i in range(10):
                        print('{:20s}{:>5d}'.format(list[i][0],list[i][1]))
                else:                                                            #如果本身不超过10个单词量，则列出所有单词即可
                    for item in list:
                        print('{:20s}{:>5d}'.format(item[0],item[1]))
        else:
            os.chdir(folder_name)                                                #文件夹操作
            filename_list = os.listdir()
            for file_name in filename_list:
                print(file_name[:-4] + '\n')
                file_list = [file_name]
                get_words(file_list,1)                                           #得到文件名，进行递归操作，标志位置1，说明要取前10
                print('----\n')

def main(argv):
    get_words(argv,0)

if __name__ == "__main__":
    main(sys.argv[1:])