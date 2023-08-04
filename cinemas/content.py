"""
(created by swmao on 28th July)

"""
import argparse
import pandas as pd
import os


def trans_seat(s):
    s = s.replace('排', '-')
    s = s.replace('座', '')
    s = s.replace('列', '')
    s = s.replace('号', '')
    s = s.replace('一', '1')
    s = s.replace('二', '2')
    s = s.replace('层', '楼')
    s = s.replace('1楼', ' 1F')
    s = s.replace('2楼', ' 2F')
    return s


def main(args):
    force_update = args.force
    src = f'{args.path}/cinemas.xlsx'
    tgt = f'{args.path}/tickets/content/tickets/'
    os.makedirs(tgt, exist_ok=True)
    df = pd.read_excel(src)
    
    changed = False 
    for irow in df.iterrows():
        s = irow[1]
        filepath = tgt + f"""{s['movie']}.md"""
        if (not force_update) and os.path.exists(filepath):
            continue
        changed = True
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

    if changed:
        tgt_readme = f'{args.path}/README.md'
        df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df['time'] = df['time'].apply(lambda x: x.strftime('%H:%M'))
        df = df.fillna('')
        with open(tgt_readme, 'w') as f:
            f.writelines(df.to_markdown(index=False))
        print(tgt_readme)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Description of your script")
    parser.add_argument("path", type=str, help="Specify the path argument")
    parser.add_argument("--force", action="store_true", help="Specify the force_update argument")

    args = parser.parse_args()
    main(args)
    