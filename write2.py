import xlwt
from datetime import datetime
from ctypes import *
import time
import win32file
import os
from os.path import join, getsize


style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

time1 = datetime.today()

ws.write(0, 1, datetime.now(), style1)
ws.write(1, 0,'服务器连接状态vms')
ws.write(2, 0, '软件运行状态组件-1')
ws.write(3, 0, '软件运行状态组件-2')
ws.write(4, 0, 'VMS-1（页面）')
ws.write(5, 0, 'VMS-2（页面）')
ws.write(6, 0, 'X盘')
ws.write(7, 0,'J盘' )
ws.write(8, 0, 'K盘')
ws.write(9, 0, 'L盘')
ws.write(10, 0,'W盘' )
ws.write(11, 0,'M盘' )
ws.write(12, 0,'R盘' )
ws.write(13, 0,'收录机器状态')
ws.write(14, 0,'配音机器状态' )
ws.write(15, 0,'收录文件(GB)' )
ws.write(16, 0,'收录机器状态')
ws.write(17, 0,'昨天入库条数')
ws.write(18, 0,'机器及软件状态196')
ws.write(19, 0,'机器及软件状态197')

def freespace(disk):
    sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters = \
            win32file.GetDiskFreeSpace(disk)
    mbytes = (numFreeClusters * sectorsPerCluster * bytesPerSector) /(1024 * 1024)#get free space
    return str(int(mbytes)) + 'MBytes'

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return str(int(size/1024/1024)) + 'MBytes'


ws.write(0, time1.day, datetime.now(),style1)
ws.write(1,time1.day,'asdfasf')
ws.write(2,time1.day,'asdfasf')
ws.write(3,time1.day,'asdfasf')
ws.write(4,time1.day,'asdfasf')
ws.write(5,time1.day,'asdfasf')
ws.write(6,time1.day,freespace('c:'))
ws.write(7,time1.day,freespace('c:'))
ws.write(9,time1.day,freespace('c:'))
ws.write(10,time1.day,freespace('c:'))
ws.write(11,time1.day,freespace('c:'))
ws.write(12,time1.day,freespace('c:'))
ws.write(15,time1.day, getdirsize(r'g:\\BaiduYunDownload'))




#ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save(str(time1.month)+'月'+str(time1.day)+'检测'+'.xls')