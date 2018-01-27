# 添加app
SUPPORT_APP_TYPE = ["youku","uc","dabai"]
# 定义答题框范围
REGION_DICT = {
        'youku':(75, 350, 990, 1300),
        'uc' : (75, 400, 990, 1220),
        'dabai' : (75, 400, 990, 1220),
        'default' : (75, 350, 990, 1200)
        }
# choices起始位置，避免选项前缀干扰
POS_DICT = {
        'youku' : 2 ,
        'uc' : 2 ,
        'dabai' : 1 ,
        'default' : 0
        }

