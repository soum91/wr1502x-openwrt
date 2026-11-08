import struct,sys
src,dst,sig,start,burn=sys.argv[1],sys.argv[2],sys.argv[3].encode(),int(sys.argv[4],16),int(sys.argv[5],16)
d=open(src,'rb').read()
d+=b'\0'*((-len(d))%4096)            # match original 4K padding
s=sum(struct.unpack('>%dH'%(len(d)//2),d))&0xffff
d+=struct.pack('>H',(0x10000-s)&0xffff)
open(dst,'wb').write(struct.pack('>4sIII',sig,start,burn,len(d))+d)
chk=sum(struct.unpack('>%dH'%(len(d)//2),d))&0xffff
print(dst,'len',hex(len(d)),'checksum sum',hex(chk))
