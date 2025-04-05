import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

"""
1. savefig: 用于将点云数据绘制并保存到指定的路径
2. get_sketches: 用于遍历某一存放草图点云的文件夹并按照目录结构将点云绘制成草图
"""

def savefig(input_path, output_path):
	# 读取文件中的所有点
	points = np.loadtxt(input_path, skiprows=0, delimiter=",", dtype=float)

	# 创建一个图形
	fig, ax = plt.subplots()
	# 绘制散点图
	ax.scatter(points[:, 0], points[:, 1], s=1)
	# 关闭坐标轴
	ax.axis("off")

	# 保存图片
	plt.savefig(output_path)
	# 释放图形节省内存空间
	plt.close(fig)

def get_sketches(input_dir, output_dir):
	# 获取该文件夹下所有文件数量
	total_files = sum([len(files) for _, _, files in os.walk(input_dir)])
	# 遍历输入文件夹下的所有文件夹和文件并用tqdm来美化处理界面
	for root, dirs, files in tqdm(os.walk(input_dir), total=total_files, desc="Converting dataset to sketches"):
		# 遍历该文件夹下的所有文件
		for file in files:
			# 将文件夹路径 + 文件名拼接为输入路径
			input_path = os.path.join(root, file)
			# 用目标输出文件夹代替输入文件夹获取输出路径, 并保存为png格式
			output_root = root.replace(input_dir, output_dir)
			name, ext = os.path.splitext(file)
			filename = name + ".png"
			output_path = os.path.join(output_root, filename)
			# 如果目标文件夹不存在则创建文件夹
			if not os.path.exists(output_root):
				os.makedirs(output_root)
			# 保存图片
			savefig(input_path, output_path)

if __name__ == '__main__':
	get_sketches("../data/dataset/", "../data/sketches/")