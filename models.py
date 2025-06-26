class User:
    def __init__(self, id: str, name: str, email: str, is_active: bool = True):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active

class Speaker:
    def __init__(self, id: str, name: str, topic: str, is_active: bool = True):
        self.id = id
        self.name = name
        self.topic = topic
        self.is_active = is_active

class Event:
    def __init__(self, id: str, speaker_id: str, title: str, location: str, date: str, is_open: bool = True):
        self.id = id
        self.speaker_id = speaker_id
        self.title = title
        self.location = location
        self.date = date
        self.is_open = is_open

class Registration:
    def __init__(self, id: str, user_id: str, event_id: str, date: str, attended: bool = False):
        self.id = id
        self.user_id = user_id
        self.event_id = event_id
        self.date = date
        self.attended = attended

