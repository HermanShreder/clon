import os,re,glob
root=r'c:\Users\User\Downloads\site'
files=glob.glob(root+'/**/*', recursive=True)
files=[f for f in files if os.path.isfile(f)]
for f in files:
    try:
        with open(f,'r',encoding='utf-8',errors='ignore') as fh:
            data=fh.read()
    except Exception:
        continue
    if len(data) > 220000:
        continue
    if re.search(r'(window\.location|location\.href|location\.replace|location\.assign|window\.open|document\.location|setTimeout\([^\n]*location|open\()', data):
        print('====',f,'====')
        for m in re.finditer(r'(window\.location|location\.href|location\.replace|location\.assign|window\.open|document\.location|setTimeout\([^\n]*location|open\()', data):
            start=max(0,m.start()-220)
            end=min(len(data),m.end()+600)
            snippet=data[start:end].replace('\n',' ')
            print(snippet)
            print('---')
            break
