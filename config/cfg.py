from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 浏览器访问系统
chromepath = r"D:/soft/chromedriver.exe"
url = 'http://10.1.1.120:9999'
username = 'admin'
password = 'ipharmacare'

# 审方数据库连接信息
host = '10.1.1.120'
port = '3306'
user_name = 'yyuser'
pwd = 'iPh@23ysq!'
db_auditcenter = 'ipharmacare_auditcenter_full'

# 常用元素定位
