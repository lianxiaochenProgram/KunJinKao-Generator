import sys
if len(sys.argv)==1:
    filename=input("""请输入你要锟斤拷化的文件，
处理好后将放置于当前目录的output.txt文件中（请用GBK编码查看），
临时文件在当前目录的kjktemp.tmp。
（命令行帮助可输入nul\\help查看）
输入：""")
else:
    filename=sys.argv[1]

if filename.lower()==r"nul\help":
    print("""　　　　帮  助
命令行：
　　格式：python 自动锟斤拷生成器.py 文件名 [编码]
　　注：带方括号为可选参数。
　　参数说明：
　　文件名：指定要锟斤拷化的文件名。
　　编码：可选。指定原文件文字编码（如gbk、utf-8）。
""")
    exit()

if len(sys.argv)==3:
    encode=sys.argv[2]
else:
    encode=input("输入原文件文字编码(如gbk、utf-8)：")
if encode=="":
    encode=None

f=open(filename,encoding=encode,errors='replace')
#print(f.read())
"""
'replace' 使用适当的替换标记进行替换；Python 内置编解码器将在解码时使用官方
U+FFFD(�)替换字符，而在编码时使用 '?' 。
"""
tmp1=open('kjktemp.tmp','w',encoding='gbk',errors='replace')
tmp1.write(f.read())
tmp1.flush()
tmp1.close()
tmp2=open('kjktemp.tmp','r',encoding='utf-8',errors='replace')
out=open('output.txt','w',encoding='utf-8',errors='replace')
out.write(tmp2.read())
f.close()
tmp2.close()
print("已保存到",out.name,", 请用GBK编码打开此文件。")
out.close()
