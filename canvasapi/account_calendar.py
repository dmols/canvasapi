from canvasapi import CanvasObject

class AccountCalendar(CanvasObject):
    def __str__(self):
        return self.calendar_event_url
