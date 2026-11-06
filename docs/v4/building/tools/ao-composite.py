import sys
from PIL import Image, ImageChops, ImageFilter
import numpy as np
def comp(name, k=0.9):
    b=Image.open(f'out/{name}.png').convert('RGBA'); a=Image.open(f'out/{name}-ao.png').convert('L').filter(ImageFilter.GaussianBlur(0.8))
    B=np.asarray(b).astype(np.float32); A=np.asarray(a).astype(np.float32)/255.
    A=np.clip(A,0,1)**1.15; m=1-k*(1-A)
    B[...,:3]*=m[...,None]
    return Image.fromarray(np.clip(B,0,255).astype(np.uint8),'RGBA')
if __name__=='__main__':
    for n in sys.argv[1:]:
        comp(n).save(f'out/{n}-f.png')
