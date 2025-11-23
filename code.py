# import tqdm, and time
from tqdm import tqdm
import time as t

# code
while True:
    v = input('>')
    if (v == 'Unix'):
        print('download -U-n-i-x-')
        t.sleep(0.5)
        # bar
        for i in tqdm(range(100)):
            t.sleep(0.02)
        print('\nUnix-booted, enjoy dear user !')
        break
    
    # Syntax | failed
    else:
        print('what >?, sorry restart pls')

# input console |
while True:
    input('#~')