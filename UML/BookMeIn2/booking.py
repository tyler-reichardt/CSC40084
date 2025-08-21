from datetime import datetime

class Booking:
    """
    Represents a booking, linking an Attendee to a Presentation.
    """
    def __init__(self, attendee: 'Attendee', presentation: 'Presentation'):
        self.booking_id = None
        self.attendee = attendee
        self.presentation = presentation
        self.booking_date = datetime.now()
        self.status = "confirmed"  # confirmed, cancelled, attended, no-show
        self.feedback_rating = None
        self.feedback_comment = None
        self.confirmation_sent = False

    def cancel_booking(self) -> None:
        pass