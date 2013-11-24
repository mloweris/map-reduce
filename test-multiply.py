import numpy as np

a = np.array([
	[63, 45, 93, 32, 49, 62, 41, 89, 11, 63, 83],
	[33, 41, 69, 26, 95, 21, 0, 80, 100, 57, 99],
	[25, 11, 52, 60, 89, 4, 38, 47, 67, 66, 13],
	[24, 79, 24, 47, 18, 6, 15, 0, 89, 59, 27],
	[7, 98, 96, 27, 0, 22, 22, 10, 34, 81, 87],
	[87, 30, 92, 4, 34, 93, 50, 54, 37, 81, 0],
	[21, 40, 95, 96, 15, 10, 81, 84, 46, 25, 90],
	[9, 71, 85, 0, 65, 3, 77, 70, 92, 45, 56],
	[62, 24, 69, 0, 45, 83, 66, 0, 20, 55, 15],
	[71, 80, 86, 98, 38, 2, 45, 31, 35, 37, 81],
	[12, 81, 38, 33, 17, 85, 12, 24, 12, 33, 56]])

# print a

b = np.array([
	[63, 18, 89, 28, 39, 44, 13, 58, 46, 15, 23],
	[59, 76, 34, 12, 6, 62, 76, 42, 0, 41, 20],
	[30, 52, 49, 3, 95, 67, 23, 70, 29, 47, 42],
	[77, 75, 85, 16, 13, 22, 67, 36, 80, 42, 79],
	[96, 46, 33, 69, 88, 21, 49, 27, 44, 4, 41],
	[0, 80, 29, 7, 38, 58, 96, 86, 35, 59, 52],
	[48, 65, 3, 40, 1, 5, 85, 35, 52, 75, 23],
	[27, 5, 25, 84, 88, 31, 86, 57, 26, 41, 13],
	[8, 21, 46, 34, 95, 39, 30, 98, 88, 94, 66],
	[38, 59, 74, 14, 53, 77, 92, 50, 64, 63, 73],
	[49, 73, 37, 32, 43, 38, 73, 69, 26, 100, 81]])



c = a.dot(b)



#This is the re-arranged output from multiply.py (map reduce matrix multiplier.)
d = np.array([
 	[27502, 32121, 28416, 19938, 34472, 28520, 40199, 36324, 24085, 32386, 28164],
 	[27667, 28388, 28147, 22827, 41402, 26933, 35896, 37814, 27616, 34301, 31338],
	[23722, 21859, 23036, 17203, 29341, 18523, 27425, 25231, 25170, 22915, 23354],
 	[17237, 20813, 20265,  9044, 18871, 18437, 22819, 23144, 19652, 23035, 20616],
 	[20121, 29675, 22685,  9040, 23334, 25975, 31221, 28831, 17878, 30126, 25270],
 	[20815, 27010, 26626, 15061, 31501, 27652, 33845, 34310, 24185, 27195, 23218],
 	[27249, 31744, 26468, 19084, 30070, 22924, 37984, 33860, 26795, 35520, 29098],
 	[24322, 27238, 21227, 20375, 34456, 23768, 34494, 33282, 24100, 33206, 24592],
 	[17865, 24288, 19350, 10487, 21757, 20513, 26755, 25842, 18840, 22029, 19033],
 	[31619, 32999, 31150, 16114, 27655, 25394, 34459, 32435, 26042, 31140, 29259],
 	[16166, 25592, 17217,  8876, 17140, 20050, 28958, 24193, 13889, 22447, 19541]])

print c==d

