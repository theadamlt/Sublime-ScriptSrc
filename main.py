import sublime, sublime_plugin
import commands
import os

path = sublime.packages_path();


class scriptsrcCommand(sublime_plugin.WindowCommand, sublime.Window):
	selected = ''

	def run(self):
		#script_list = ['jQuery', 'jQuery-UI', 'Chrome Frame', 'swfobject', 'mootools','YUI','ExtJS','prototype','scriptaculous','DOJO']
		script_list = ['jQuery',  'jQuery UI', 'Prototype', 'motools', 'dojo', 'swfobject', 'YIU', 'Ext core', 'Chrome Frame', 'scriptaculous']
		self.window.show_quick_panel(script_list, self.callback)

	def callback(self, index):
		if (index > -1):
			# if not self.window.views():
			# 	self.window.new_file()

			self.selected =  index
			type_list = ['Compressed', 'Uncompressed']
			self.window.show_quick_panel(type_list, self.callback2)

	def callback2(self, index):
		if (index > -1):

			if not self.window.views():
				self.window.new_file()

			libraries = {
				0: 'jquery',
				1: 'jqueryui',
				2: 'prototype',
				3: 'mootools',
				4: 'dojo',
				5: 'swfobject',
				6: 'yui',
				7: 'ext-core',
				8: 'chrome-frame',
				9: 'scriptaculous'
				}

			lib = libraries[self.selected]

			if index == 0:
				comp = 'compressed'
			else:
				comp = 'uncompressed'

			if os.path.exists(sublime.packages_path()+'/ScriptSrc'):
				if sublime.platform() == 'windows':
					path = sublime.packages_path()+'\ScriptSrc'
				else:
					path = sublime.packages_path()+'/ScriptSrc'
			else:
				if sublime.platform() == 'windows':
					path = sublime.packages_path()+'\Sublime-ScriptSRC'
				else:
					path = sublime.packages_path()+'/Sublime-ScriptSRC'


			if sublime.platform() != 'windows':
				command = 'php -f '+path+'/scriptsrc.php '+lib+' '+comp
				output = commands.getoutput(command)
			else:
				command = 'C:\PHP\php.exe -f "'+path+'\scriptsrc.php" -- '+lib+' '+comp
				output = os.popen(command).read()

			if output == 'It seems like you dont have an internet connection':
			 	sublime.error_message('Couldn\'t fetch the latest script tag. Please check your internet connection');
			else:
			 	sublime.set_clipboard(output)
			 	sublime.status_message('Your script-tag has been added to the clipboard')

			# view = sublime.Window.active_view()
			# edit = view.begin_edit()
	  		# view.insert(edit, 0, output)
	  		# view.end_edit(edit)