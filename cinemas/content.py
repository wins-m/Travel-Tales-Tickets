"""
(created by swmao on 28th July)

"""
import pandas as pd
import os

force_update = False
src = './cinemas.xlsx'
tgt = './tickets/content/tickets/'


def trans_seat(s):
    s = s.replace('排', '-')
    s = s.replace('座', '')
    s = s.replace('列', '')
    s = s.replace('一', '1')
    s = s.replace('二', '2')
    s = s.replace('层', '楼')
    s = s.replace(' 1楼', '')
    s = s.replace(' 2楼', '  2nd')
    return s

def main():
    os.makedirs(tgt, exist_ok=True)
    df = pd.read_excel(src)
    # df['remark'] = df['remark'].fillna('')
    for irow in df.iterrows():
        s = irow[1]
        filepath = tgt + f"""{s['movie']}.md"""
        if (not force_update) and os.path.exists(filepath):
            continue
        content = ['---\n']
        content.append(f"""title: '{s['movie']}'\n""")
        content.append(f"""date: '{s['date'].strftime('%Y-%m-%d')}'\n""")
        content.append(f"""price: '{s['price']:.1f}'\n""")
        content.append(f"""theaters: ['{s['theaters'].replace('（', '·').replace('）','')}']\n""")
        content.append(f"""seat: ['{trans_seat(s['seat'])}']\n""")
        if isinstance(s['remark'], str):
            content.append(f"""remark: {s['remark'].split('；')}\n""")
        content.append('---')

        with open(filepath, 'w') as f:
            f.writelines(content)
        print(filepath)

if __name__ == '__main__':
    main()
    
