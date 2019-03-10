# -*- coding: utf-8 -*-
from pyautocad import Autocad, APoint
class p2cad:
    def __init__(self):
        self.lst=[]
        self.ls_ar=[] # 把@数据存入ls_ar中
        self.ls_inx=[] # 把@索引存入ls_inx中
        self.spx = 100  # area startx
        self.spy = 2000 #area starty
        self.rw = 300   #area width
        self.rh = 400   #area height
        self.lst_p4 = []  #point4 x,y value
        self.fh=3  # font height
        self.m=0   # how many guizi in lst
        self.acad = Autocad(create_if_not_exists=True)
        txtsytle=self.acad.ActiveDocument.TextStyles.Add('HIT_TxtStyle')
        self.acad.ActiveDocument.ActiveTextStyle=self.acad.ActiveDocument.TextStyles.Item('Standard')
        self.acad.ActiveDocument.ActiveTextStyle.SetFont('楷体',False,False,1,0 or 0)
        self.TestB_Lock()

        self.txtlst=[]

    def TestB_Lock(self):
        return True
    def loadData(self,lst):
        self.lst=lst
        # print(self.lst)

    def addTxt(self,txt, posx, posy):
        txtObj = self.acad.model.AddText(txt, APoint(posx, posy), 3)
        self.txtlst.append(txtObj)

    def drawRec(self,px, py):
        p1 = APoint(px, py)
        p2 = APoint(p1.x + self.rw, p1.y)
        p3 = APoint(p2.x, p2.y + self.rh)
        p4 = APoint(p3.x - self.rw, p3.y)
        self.lst_p4.append(p4)
        l1 = self.acad.model.AddLine(p1, p2)
        l2 = self.acad.model.AddLine(p2, p3)
        l3 = self.acad.model.AddLine(p3, p4)
        l4 = self.acad.model.AddLine(p4, p1)

    def delTXT(self):
        for i in range(len(self.lst)):
            try:
                for obj in self.acad.iter_objects('Text'):
                    obj.Delete()
            except:
                pass
        return 'del autocad TXT success'

    def pasreAndDrawToAutoCad(self):
        for f, value in enumerate(self.lst):
            if (value == '@'):
                self.ls_inx.append(f)  # 判断lst中有几面柜子
                self.ls_ar.append([])  #把每面柜子的数据存入ls_ar中
        self.m=len(self.ls_inx)   # total guizi
        # print('m',self.m)
        if(self.m>0):

            # 根据m面柜子的数量来判断画几行几列的框
            # ##############################################################

            if (self.m % 10 > 0):
                lie = int(self.m / 10) + 1
            else:
                lie = int(self.m / 10)

            for d in range(lie):
                for l in range(1, 11):
                    self.drawRec(self.spx + self.rw * l + 30 * (l - 1), self.spy - self.rh * d - 30 * d)
            # ##############################################################

            # 把每面柜子的元素切入到列表ls_ar中
            for i, v in enumerate(self.ls_inx):
                if (i == 0):
                    self.ls_ar[0].append(self.lst[0:self.ls_inx[0]])
                else:
                    self.ls_ar[i].append(self.lst[(self.ls_inx[i - 1] + 1):(self.ls_inx[i - 1 + 1])])

            # 把文字添加到方框中
            for m in range(self.m):
                px = self.lst_p4[m].x
                py = self.lst_p4[m].y

                for u in range(len(self.ls_ar[m][0])):
                    self.addTxt(str(self.ls_ar[m][0][u]), px + 10, py - 10 - 3 * u - 10 * u)

            # print(len(self.txtlst), 'txtlst')

            self.ls_ar.clear()
            self.ls_inx.clear()
            return 'success to draw dwg'


        else:
            return 'faild to draw dwg'


########################################################################################################

# if __name__ == '__main__':
#     lst = ['ggd1', 'list', 'lst2', 'lst3', '@', 'lst4', '@', 'lst6', '@', 'lst6', '@', 'ggd1', 'list', 'lst2', 'lst3',
#            '@', 'lst6', '@', 'lst6', '@', 'lst6', '@', 'lst6', '@', 'lst6', '@', 'lst6', '@', 'lst6', '@']
#
#     aa=p2cad()
#     aa.loadData(lst)
#     aa.pasreAndDrawToAutoCad()