import sublime
import sublime_plugin
import os
from subprocess import call
from threading import Timer

class SublimeGoimports(sublime_plugin.EventListener):
    def on_post_save(self, view):
        file = view.file_name()
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.go':
            result = call(["goimports", "-w", file], shell=True)
            if result == 0:
                self.view = view
                t = Timer(0.5, self.update_gutter_marks)
                t.start()

    def update_gutter_marks(self):
        self.view.run_command('git_gutter_compare_head')
        self.view.run_command('sublimelinter_lint')
