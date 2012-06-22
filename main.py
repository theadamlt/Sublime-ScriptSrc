import sublime, sublime_plugin
import commands


class scriptsrcCommand(sublime_plugin.WindowCommand, sublime.Window):

	def run(self):
		#script_list = ['jQuery', 'jQuery-UI', 'Chrome Frame', 'swfobject', 'mootools','YUI','ExtJS','prototype','scriptaculous','DOJO']
		script_list = ['jQuery',  'jQuery UI', 'Prototype', 'motools', 'dojo', 'swfobject', 'YIU', 'Ext core', 'Chrome Frame', 'scriptaculous']
		self.window.show_quick_panel(script_list, self.callback)

	def callback(self, index):
		if not self.window.views():
			self.window.new_file()

		global selected
		selected =  index
		type_list = ['Compressed', 'Uncompressed']
		self.window.show_quick_panel(type_list, self.callback2)

	def callback2(self, index):
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

		lib = libraries[selected]

		if index == 0:
			comp = 'compressed'
		else:
			comp = 'uncompressed'

		command = 'php -f scriptsrc.php '+lib+' '+comp
		output = commands.getoutput(command);
		if output == 'It seems like you dont have an internet connection':
			sublime.error_message('Couldn\'t fetch the latest script tag. Please check your internet connection');
		else:
			sublime.set_clipboard(output)
			sublime.status_message('Your script-tag has been added to the clipboard')

		# view = sublime.Window.active_view()
		# edit = view.begin_edit()
  		#view.insert(edit, 0, output)
  		#view.end_edit(edit)