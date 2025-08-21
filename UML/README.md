# BookMeIn2 System - UML Class Documentation

## Overview
BookMeIn2 is a presentation booking system that allows presenters to create and manage presentations while attendees can discover and book presentations. The system is built using object-oriented design principles with clear class hierarchies and relationships.

## Class Diagram Structure

### Base Class: User
The `User` class serves as the base class for all user types in the system.

**Attributes:**
- `user_id` (int): Unique identifier for each user
- `first_name` (str): User's first name
- `last_name` (str): User's last name
- `email` (str): User's email address for authentication and communication
- `is_logged_in` (bool): Current login status of the user
- `registration_date` (datetime): When the user registered in the system

**Methods:**
- `login(password: str) -> bool`: Authenticates user and sets login status
- `logout() -> None`: Logs out the user from the system
- `get_full_name() -> str`: Returns the user's full name

### Derived Class: Presenter (inherits from User)
Represents users who can create and manage presentations.

**Additional Attributes:**
- `bio` (str): Presenter's biography or professional description
- `presentations` (list): List of presentations created by this presenter
- `specialization` (str): Area of expertise or specialization
- `rating` (float): Average rating from attendee feedback
- `total_presentations_given` (int): Count of completed presentations

**Methods:**
- `create_presentation(title, description, time, capacity) -> Presentation`: Creates a new presentation
- `view_my_presentations() -> List[Presentation]`: Returns all presentations by this presenter

### Derived Class: Attendee (inherits from User)
Represents users who can book and attend presentations.

**Additional Attributes:**
- `bookings` (list): List of current and past bookings
- `interests` (list): Topics or areas of interest for the attendee
- `attended_presentations` (list): History of presentations attended
- `feedback_given` (list): List of feedback provided for attended presentations

**Methods:**
- `book_presentation(presentation) -> Optional[Booking]`: Books a presentation if available
- `view_my_bookings() -> List[Presentation]`: Returns all booked presentations

### Class: Presentation
Represents a presentation event in the system.

**Attributes:**
- `presentation_id` (int): Unique identifier for the presentation
- `title` (str): Title of the presentation
- `description` (str): Detailed description of the presentation content
- `time` (datetime): Scheduled date and time of the presentation
- `capacity` (int): Maximum number of attendees allowed
- `presenter` (Presenter): Reference to the presenter giving this presentation
- `bookings` (list): List of all bookings for this presentation
- `location` (str): Venue or location details (physical or virtual)
- `duration_minutes` (int): Duration of the presentation in minutes
- `status` (str): Current status (scheduled/ongoing/completed/cancelled)
- `materials_url` (str): Link to presentation materials or resources
- `tags` (list): Categories or tags for easy discovery

**Methods:**
- `add_booking(booking) -> None`: Adds a new booking to the presentation
- `get_attendee_count() -> int`: Returns current number of bookings
- `get_available_slots() -> int`: Returns remaining available spots
- `is_full() -> bool`: Checks if presentation has reached capacity
- `cancel_presentation() -> None`: Cancels the presentation and notifies attendees

### Class: Booking
Represents a booking linking an attendee to a presentation.

**Attributes:**
- `booking_id` (int): Unique identifier for the booking
- `attendee` (Attendee): Reference to the attendee who made the booking
- `presentation` (Presentation): Reference to the booked presentation
- `booking_date` (datetime): When the booking was made
- `status` (str): Booking status (confirmed/cancelled/attended/no-show)
- `feedback_rating` (int): Rating given by attendee after attending
- `feedback_comment` (str): Text feedback from the attendee
- `confirmation_sent` (bool): Whether confirmation email was sent

**Methods:**
- `cancel_booking() -> None`: Cancels the booking and updates availability

## Class Relationships

### Inheritance Relationships
- `Presenter` → inherits from → `User`
- `Attendee` → inherits from → `User`

### Association Relationships
- `Presenter` (1) → creates → (*) `Presentation`
- `Attendee` (*) → books → (*) `Presentation` (through `Booking`)
- `Booking` → references → (1) `Attendee`
- `Booking` → references → (1) `Presentation`

## Key Design Patterns

### 1. Inheritance Pattern
The system uses inheritance to create specialized user types (Presenter and Attendee) from a base User class, promoting code reuse and maintaining a clear hierarchy.

### 2. Association Pattern
The Booking class acts as an association class, managing the many-to-many relationship between Attendees and Presentations while storing additional booking-specific information.

### 3. Aggregation Pattern
Presentations aggregate Bookings, and Presenters aggregate their created Presentations, establishing clear ownership and lifecycle management.

## System Flow

1. **User Registration**: Users register as either Presenters or Attendees
2. **Presentation Creation**: Presenters create presentations with details like title, description, time, and capacity
3. **Discovery**: Attendees browse available presentations based on interests and tags
4. **Booking**: Attendees book presentations that have available slots
5. **Attendance**: System tracks attendance status for each booking
6. **Feedback**: After attending, attendees can provide ratings and feedback
7. **Analytics**: Presenters can view attendance and feedback for their presentations

## Future Enhancements

Potential areas for system expansion:
- Payment processing for paid presentations
- Waitlist management for full presentations
- Automated reminder notifications
- Certificate generation for attendance
- Advanced search and recommendation system
- Multi-language support
- Integration with calendar applications
- Live streaming capabilities for virtual presentations

## File Structure

```
UML/
└── BookMeIn2/
    ├── __init__.py        # Package initialization
    ├── user.py            # Base User class
    ├── presenter.py       # Presenter class (inherits from User)
    ├── attendee.py        # Attendee class (inherits from User)
    ├── presentation.py    # Presentation class
    └── booking.py         # Booking association class
```

## Usage Example

```python
from BookMeIn2 import Presenter, Attendee, Presentation, Booking

# Create a presenter
presenter = Presenter(1, "John", "Doe", "john@example.com", "Expert in Python")

# Create a presentation
presentation = presenter.create_presentation(
    title="Introduction to Python",
    description="Learn Python basics",
    time="2024-01-15 14:00",
    capacity=50
)

# Create an attendee
attendee = Attendee(2, "Jane", "Smith", "jane@example.com")

# Book the presentation
booking = attendee.book_presentation(presentation)
```

## Notes

- All method implementations are currently stubs (`pass` statements) as this is a UML design documentation
- The actual implementation would include database persistence, validation, error handling, and business logic
- The system is designed to be extensible and maintainable following SOLID principles