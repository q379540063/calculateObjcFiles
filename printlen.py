import  getopt, string, os, glob, hashlib, gc, zlib, base64,time

# def fileList():
#     fl = glob.glob("*.*")
#     return fl

# list = fileList();
# index = 0;
# allCount = 0;
# print(list)
# while (index < len(list)):
#     filePath = list[index]
#     filea = open(filePath);
#     count = len(filea.readlines());

#     allCount += count;
#     index = index + 1;
# print allCount

def calculatelines(tmpath,listdir):
	alllines = 0;
	for tmp in listdir:
		path = os.path.join(tmpath,tmp)
		if os.path.isfile(path) and (os.path.splitext(tmp)[1]=='.h' or os.path.splitext(tmp)[1]=='.m'):
			filea = open(path);
			count = len(filea.readlines());
			alllines += count
		elif os.path.isdir(path):
			alllines += calculatelines(path,[x for x in os.listdir(path)])
	return alllines;

alllines = calculatelines(os.path.abspath('.'),[x for x in os.listdir('.')])
print(alllines)
