import pandas as pd
import numpy as np
import datetime

df = pd.read_excel('transport_record.xlsx', skipfooter=4, dtype=object, parse_dates=True)


def cal_duration(x):

    def format_timedelta_to_hours_minutes(td):
        # 计算总小时数
        total_hours = td.days * 24 + td.seconds // 3600
        
        # 提取分钟
        minutes = (td.seconds % 3600) // 60
        
        # 构建格式化字符串
        if total_hours == 0:
            formatted_time = f"{minutes:}分"
        else:
            formatted_time = f"{total_hours}时{minutes:}分"
        return formatted_time
        
    if not isinstance(x, str):
        return ''

    if '(' in x:
        x, a = x.split('(')
        a = datetime.timedelta(int(a.replace('+','').replace(')', '')))
    else:
        a = datetime.timedelta(0)

    x0, x1 = (pd.to_datetime(_) for _ in x.split('-'))
    dur = x1 - x0 + a

    return format_timedelta_to_hours_minutes(dur)

sr = df['时间'].apply(cal_duration)
sr.to_csv('tmp.csv', encoding='GBK')

