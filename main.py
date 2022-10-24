import datetime
import time
from tkinter import *
from seckill.seckill_taobao import ChromeDriver


def main():
	hint = "淘宝定时秒杀系统 by LTEnjoy\n" \
		   "使用前提：请先安装好谷歌chrome浏览器，以及下载好对应的chromedriver（二者的版本要对应）\n" \
		   "使用步骤：\n" \
		   "		1. 输入下载好的chromedriver路径（请确保和chrome浏览器对应，路径最好不包含中文），例如：\n" \
		   "				C:\Program Files\Google\Chrome\Application\\chromedriver.exe\n" \
		   "		2. 设定好需要定时抢购的时间，格式为”年-月-日 时:分:秒“（例：2022-10-24 00:00:00）\n" \
		   "		3. 输入支付密码（可以跳过）\n" \
		   "		4. 通过手机扫码的方式在打开的网站上登录淘宝\n" \
		   "		5. 等待抢购时间到达随后进行抢购\n" \
		   # "		6. 如果抢购成功，即可通过手机支付宝扫码的方式扫码支付（输入密码会被检测到有风险，暂时还没考虑反爬措施）\n"

	print(hint)

	# 获取chromedriver的路径
	driver_path = input("请输入下载好的chromedriver的路径：").strip()

	# 设置抢购时间
	kill_time = input("请输入定时抢购的时间，格式参照上文（注意标点符号的正确）：").strip()

	# 输入支付密码
	password = input("请输入支付密码（如果跳过则直接回车）：").strip()

	# 开始抢购
	print("即将打开网址，请使用手机扫码登录")
	ChromeDriver(chrome_path=driver_path, seckill_time=kill_time, password=password).sec_kill()


if __name__ == '__main__':
	main()
