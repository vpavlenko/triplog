import datetime

import sublime, sublime_plugin


GREETING = 'Triplog: starting new trip at '
START_TIME_FORMAT = '%d.%m.%Y %H:%M'
TRIP_START_TIME = {}
MODIFIED_NOW = set()


def formatted_trip_time(trip_id):
    td = datetime.datetime.now() - TRIP_START_TIME[trip_id]
    days, hours, minutes = td.days, td.seconds // 3600, td.seconds // 60 % 60
    return "{0:02d}:{1:02d}".format(hours, minutes)


class IntoTripCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        first_line = self.view.substr(self.view.line(0))
        if first_line.startswith(GREETING):
            self.resume_trip(first_line)
        else:
            self.start_trip(edit)

    def resume_trip(self, first_line):
        time_str = first_line[len(GREETING):]
        TRIP_START_TIME[self.view.buffer_id()] = datetime.datetime.strptime(time_str, START_TIME_FORMAT)

    def start_trip(self, edit):
        TRIP_START_TIME[self.view.buffer_id()] = datetime.datetime.now()
        self.view.insert(edit, 0, '{0}{1}\n\n'.format(
            GREETING,
            TRIP_START_TIME[self.view.buffer_id()].strftime(START_TIME_FORMAT)))


class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        point = self.view.size()
        last_line = self.view.substr(self.view.line(point))
        nearly_last_line = self.view.substr(self.view.line(point - 1))
        if not last_line and not nearly_last_line:
            self.view.insert(edit, point, "{0}\n".format(formatted_trip_time(self.view.buffer_id())))
 

class TripEnterListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        if not view.buffer_id() in TRIP_START_TIME or view.buffer_id() in MODIFIED_NOW:
            return

        self.add_time_stamp(view)    

    def add_time_stamp(self, view):
        MODIFIED_NOW.add(view.buffer_id())
        edit = view.begin_edit(666, "random")  # TODO: avoid random params
        view.run_command('add_time_stamp')
        view.end_edit(edit)
        MODIFIED_NOW.remove(view.buffer_id())
