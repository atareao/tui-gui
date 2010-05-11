#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
#
__author__='atareao'
__date__ ='$24-abr-2010 12:34:44$'
#
# <one line to give the program's name and a brief idea of what it does.>
#
# Copyright (C) 2009 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
import os
import sys
import gtk
import bitly


class MainWindow:
    def __init__(self):
	self.builder = gtk.Builder()
	self.builder.add_from_file('/usr/share/tui/tui.glade')
	self.window = self.builder.get_object('window')
        self.entry1 = self.builder.get_object('entry1')
        self.entry2 = self.builder.get_object('entry2')
	self.button1 = self.builder.get_object('button1')
        self.window.show_all()
        self.center_on_screen()
        # Magia :P
        self.builder.connect_signals(self)
    def center_on_screen(self):
	width=gtk.gdk.screen_width()
        height=gtk.gdk.screen_height()
        window_width=self.window.get_size()[0]
        window_height=self.window.get_size()[1]
        self.window.move((width-window_width)/2,(height-window_height)/2)
    def on_button1_clicked(self,widget):
	api = bitly.Api(login='atareao', apikey='R_7b09c8e1c8e474fce6e7c93a8a380a75')
	short=api.shorten(self.entry1.get_text())
	self.entry2.set_text(short)
    def on_button2_clicked(self,widget):
	clipboard = gtk.clipboard_get()
	porta=clipboard.wait_for_text()
	if porta!=None:
	    self.entry1.set_text(porta)
    def on_button3_clicked(self,widget):
	clipboard = gtk.clipboard_get()
	clipboard.set_text(self.entry2.get_text())
    def on_window_destroy(self,widget):
	exit()

if __name__ == '__main__':
    v = MainWindow()
    gtk.main()
