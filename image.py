# -*- coding: UTF-8 -*-

import wx
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg') 

def graphshow(filepass):

	data = np.loadtxt(filepass,delimiter=",")
	print(data.shape)
	x = data[:,0]
	y = data[:,1]
	plt.plot(x, y)





class FileDropTarget(wx.FileDropTarget):
    """ Drag & Drop Class """
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, files):
        self.window.text_entry.SetLabel(files[0])
        print(files[0])
        graphshow(files[0])

        return 0


class App(wx.Frame):
    """ GUI """
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 200), style=wx.DEFAULT_FRAME_STYLE)

        # パネル
        p = wx.Panel(self, wx.ID_ANY)

        label = wx.StaticText(p, wx.ID_ANY, 'ここにファイルをドロップしてください', style=wx.SIMPLE_BORDER | wx.TE_CENTER)
        label.SetBackgroundColour("#e0ffff")

        # ドロップ対象の設定
        label.SetDropTarget(FileDropTarget(self))

        # テキスト入力ウィジット
        self.text_entry = wx.TextCtrl(p, wx.ID_ANY)

        # レイアウト
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(label, flag=wx.EXPAND | wx.ALL, border=10, proportion=1)
        layout.Add(self.text_entry, flag=wx.EXPAND | wx.ALL, border=10)
        p.SetSizer(layout)

        self.Show()

if __name__ == '__main__':

	app = wx.App()
	App(None, -1, 'タイトル')
	app.MainLoop()