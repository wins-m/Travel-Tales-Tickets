"""
(created by swmao on 28th July)

"""
import pandas as pd
import os
PATH = '/mnt/d/Codes_代码/mygitrep/Travel-Tales-Tickets/cinemas/'

def main():
    force_update = False
    src = PATH + 'cinemas.xlsx'
    tgt = PATH + 'content/'
    os.makedirs(tgt, exist_ok=True)
    df = pd.read_excel(src)
    df['remark'] = df['remark'].fillna('')
    for irow in df.iterrows():
        s = irow[1]
        filepath = tgt + f"""{s['movie']}.md"""
        if (not force_update) and os.path.exists(filepath):
            continue
        content = ['---\n']
        content.append(f"""title: \"{s['movie']}\"\n""")
        content.append(f"""date: \"{s['date'].strftime('%Y-%m-%d')}\"\n""")
        content.append(f"""price: \"{s['price']:.2f}\"\n""")
        content.append(f"""theaters: [\"{s['theaters']}\"]\n""")
        content.append(f"""remark: {s['remark'].split('；')}\n""")
        content.append('---')

        with open(filepath, 'w') as f:
            f.writelines(content)
        print(filepath)

if __name__ == '__main__':
    main()
    
