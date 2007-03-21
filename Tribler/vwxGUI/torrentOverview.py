# -*- coding: iso-8859-1 -*- 
# Don't modify comment 

import wx
from bgPanel import *
from torrentFilter import *
from torrentTabs import *
from torrentGrid import *
from standardPager import *
from standardOverview import *
#[inc]add your include files here

#[inc]end your include

class personsOverview(wx.Panel):
    def __init__(self,parent,id = -1,pos = wx.Point(0,0),size = wx.Size(625,430),style = wx.TAB_TRAVERSAL,name = 'panel'):
        pre=wx.PrePanel()
        self.OnPreCreate()
        pre.Create(parent,id,pos,size,style,name)
        self.PostCreate(pre)
        self.initBefore()
        self.VwXinit()
        self.initAfter()

    def __del__(self):
        self.Ddel()
        return


    def VwXinit(self):
        self.fileImgBuf=[None] * 1
        self.fileImgBuf[0] = wx.Bitmap("images/triblerpanel_topcenter.png",wx.BITMAP_TYPE_PNG)
        self.pn10cImg0=self.fileImgBuf[0];
        self.Show(True)
        self.pn10c = wx.Panel(self,-1,wx.Point(10,0),wx.Size(20,21))
        self.pn10c.SetForegroundColour(wx.Colour(255,255,255))
        self.pn10c.SetBackgroundColour(wx.Colour(255,51,0))
        self.pn10c.Bind(wx.EVT_ERASE_BACKGROUND,self.VwXpn10c_VwXEvOnEraseBackground)
        self.st64c = wx.StaticText(self.pn10c,-1,"",wx.Point(0,4),wx.Size(194,17),wx.ST_NO_AUTORESIZE)
        self.st64c.SetLabel("Content")
        self.st64c.SetForegroundColour(wx.Colour(255,255,255))
        self.orange_top_right = bgPanel(self, -1, wx.Point(613,0), wx.Size(10,21))
        self.orange_top_left = bgPanel(self, -1, wx.Point(0,0), wx.Size(10,21))
        self.personsFilter = torrentFilter(self,-1,wxDefaultPosition,wxDefaultSize)
        self.personsFilter.SetDimensions(0,21,448,20)
        self.personsTabs = torrentTabs(self,-1,wxDefaultPosition,wxDefaultSize)
        self.personsTabs.SetDimensions(0,41,20,20)
        self.personsGrid = torrentGrid(self,-1,wxDefaultPosition,wxDefaultSize)
        self.personsGrid.SetDimensions(0,61,617,235)
        self.orange_bottom_left = bgPanel(self, -1, wx.Point(0,400), wx.Size(10,28))
        self.orange_bottom_center = bgPanel(self, -1, wx.Point(10,400), wx.Size(20,20))
        self.standardPager = standardPager(self,-1,wx.Point(440,400),wx.Size(183,28))
        self.standardOverview203c = standardOverview(self,-1,wx.Point(0,0),wx.Size(20,20))
        self.sz3s = wx.BoxSizer(wx.VERTICAL)
        self.header = wx.BoxSizer(wx.HORIZONTAL)
        self.footer = wx.BoxSizer(wx.HORIZONTAL)
        self.sz65s = wx.BoxSizer(wx.HORIZONTAL)
        self.sz3s.Add(self.header,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.personsFilter,0,wx.EXPAND|wx.ALIGN_LEFT|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.personsTabs,0,wx.EXPAND|wx.ALIGN_LEFT|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.personsGrid,1,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.footer,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.header.Add(self.orange_top_left,0,wx.FIXED_MINSIZE,3)
        self.header.Add(self.pn10c,1,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.header.SetItemMinSize(self.pn10c,20,10)
        self.header.Add(self.orange_top_right,0,wx.FIXED_MINSIZE,3)
        self.footer.Add(self.orange_bottom_left,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.footer.Add(self.orange_bottom_center,1,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.footer.Add(self.standardPager,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz65s.Add(self.st64c,0,wx.TOP|wx.EXPAND|wx.FIXED_MINSIZE,4)
        self.SetSizer(self.sz3s);self.SetAutoLayout(1);self.Layout();
        self.pn10c.SetSizer(self.sz65s);self.pn10c.SetAutoLayout(1);self.pn10c.Layout();
        self.Refresh()
        return
    def VwXDrawBackImg(self,event,win,bitMap,opz):
        if (event.GetDC()):
            dc=event.GetDC()
        else: dc = wx.ClientDC(win)
        dc.SetBackground(wx.Brush(win.GetBackgroundColour(),wx.SOLID))
        dc.Clear()
        if (opz==0):
            dc.DrawBitmap(bitMap,0, 0, 0)
        if (opz==1):
            rec=wx.Rect()
            rec=win.GetClientRect()
            rec.SetLeft((rec.GetWidth()-bitMap.GetWidth())   / 2)
            rec.SetTop ((rec.GetHeight()-bitMap.GetHeight()) / 2)
            dc.DrawBitmap(bitMap,rec.GetLeft(),rec.GetTop(),0)
        if (opz==2):
            rec=wx.Rect()
            rec=win.GetClientRect()
            for y in range(0,rec.GetHeight(),bitMap.GetHeight()):
                for x in range(0,rec.GetWidth(),bitMap.GetWidth()):
                    dc.DrawBitmap(bitMap,x,y,0)

    def VwXDelComp(self):
        return
    def VwXpn10c_VwXEvOnEraseBackground(self,event):
        self.VwXDrawBackImg(event,self.pn10c,self.pn10cImg0,2)
        self.pn10c_VwXEvOnEraseBackground(event)
        event.Skip(False)

        return

#[win]add your code here

    def bla(self):
        pass
        



    def pn10c_VwXEvOnEraseBackground(self,event): #init function
        #[ c0]Code event VwX...Don't modify[ c0]#
        #add your code here
        event.Skip()

        return #end function

    def OnPreCreate(self):
        #add your code here

        return

    def initBefore(self):
        #add your code here

        return

    def initAfter(self):
        #add your code here

        return

    def Ddel(self): #init function
        #[ bf]Code VwX...Don't modify[ bf]#
        #add your code here

        return #end function

#[win]end your code
