import sys
from PIL import Image, ImageFilter
import numpy as np
def comp(n, k=0.9):
    b=Image.open(f'seq/{n}.png').convert('RGBA'); a=Image.open(f'seq/{n}-ao.png').convert('L').filter(ImageFilter.GaussianBlur(0.8))
    B=np.asarray(b).astype(np.float32); A=np.clip(np.asarray(a).astype(np.float32)/255.,0,1)**1.15
    B[...,:3]*=(1-k*(1-A))[...,None]
    return Image.fromarray(np.clip(B,0,255).astype(np.uint8),'RGBA')
if __name__=='__main__':
    for n in sys.argv[1:]: comp(n).save(f'seq/{n}-f.png')
