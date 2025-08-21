# ModeratorDesk UML Class Diagram

## ASCII Art Class Diagram

```
+--------------------------------+              +--------------------------------+
|      SessionAssignments        |              |       QuestionModerator        |
+--------------------------------+              +--------------------------------+
| + moderator_id: int            |              | + session_id: str              |
| + assigned_sessions: list      |              | + incoming_questions: list     |
| + upcoming_talks: list         |              | + approved_questions: list     |
| + confirmed_sessions: list     |              | + rejected_questions: list     |
| + pending_confirmations: list  |              | + forwarded_to_speaker: list   |
| + availability_status: dict    |              | + flagged_questions: list      |
+--------------------------------+              | + moderation_queue: list       |
| + get_assigned_sessions(): list|              +--------------------------------+
| + get_upcoming_talks(): list   |              | + get_incoming_questions(): list|
| + confirm_availability(): bool |              | + approve_question(): bool     |
| + decline_session(): bool      |              | + reject_question(): bool      |
| + get_session_details(): dict  |              | + forward_to_speaker(): bool   |
| + request_reassignment(): bool |              | + flag_question(): bool        |
| + update_availability(): None  |              | + edit_question(): bool        |
| + get_session_materials(): list|              | + merge_questions(): dict      |
| + join_session(): bool         |              | + prioritize_question(): bool  |
| + get_speaker_info(): dict     |              | + batch_approve(): dict        |
| + get_moderation_guidelines()  |              | + batch_reject(): dict         |
| + export_schedule(): bytes     |              | + filter_questions(): list     |
+--------------------------------+              | + search_questions(): list     |
         |                                      | + get_moderation_stats(): dict |
         | assigns moderator to                 | + export_qa_log(): bytes       |
         ↓                                      +--------------------------------+
    QuestionModerator                                        |
         |                                                   | references in notes
         | creates notes for                                ↓
         ↓                                      +--------------------------------+
+--------------------------------+              |          NoteManager           |
|       SessionReminder          |              +--------------------------------+
+--------------------------------+              | + session_id: str              |
| + moderator_id: int            |              | + notes_content: str           |
| + active_reminders: list       |              | + note_timestamps: list        |
| + reminder_settings: dict      |              | + key_points: list             |
| + notification_methods: list   |              | + action_items: list           |
| + preferred_method: str        |              | + saved_notes: list            |
+--------------------------------+              | + auto_save_enabled: bool      |
| + set_reminder(): bool         |              +--------------------------------+
| + cancel_reminder(): bool      |              | + create_note(): str           |
| + update_reminder_settings()   |              | + add_timestamp(): None        |
| + get_active_reminders(): list |              | + add_key_point(): None        |
| + snooze_reminder(): bool      |              | + add_action_item(): None      |
| + acknowledge_reminder(): None |              | + edit_note(): bool            |
| + set_notification_method(): bool|            | + delete_note(): bool          |
| + test_notification(): bool    |              | + save_notes(): bool           |
| + get_upcoming_reminders(): list|             | + auto_save(): None            |
| + bulk_set_reminders(): dict   |              | + export_notes(): bytes        |
| + disable_all_reminders(): None|              | + search_notes(): list         |
| + enable_all_reminders(): None |              | + get_session_notes(): dict    |
| + get_reminder_history(): list |              | + create_summary(): str        |
+--------------------------------+              | + share_notes(): bool          |
         ↑                                      | + import_template(): bool      |
         | reminds about                        +--------------------------------+
         |                                      
    SessionAssignments                          
         |                                      
         | completes with                       
         ↓                                      
+--------------------------------+
|      ModerationFeedback        |
+--------------------------------+
| + moderator_id: int            |
| + session_id: str              |
| + overall_experience_rating: int|
| + technical_issues_rating: int |
| + speaker_cooperation_rating: int|
| + audience_engagement_rating: int|
| + comments: str                |
| + improvement_suggestions: str |
| + would_moderate_again: bool   |
| + submission_timestamp: datetime|
+--------------------------------+
| + set_overall_rating(): None   |
| + set_technical_rating(): None |
| + set_speaker_rating(): None   |
| + set_audience_rating(): None  |
| + add_comments(): None         |
| + add_suggestions(): None      |
| + report_issue(): bool         |
| + set_future_availability()    |
| + submit_feedback(): bool      |
| + save_draft(): None           |
| + validate_feedback(): list    |
| + get_previous_feedback(): list|
| + attach_evidence(): bool      |
+--------------------------------+

Moderator Workflow:
===================
SessionAssignments → SessionReminder → Join Session → QuestionModerator + NoteManager → ModerationFeedback
```

## Mermaid Class Diagram

```mermaid
classDiagram
    class SessionAssignments {
        +moderator_id: int
        +assigned_sessions: list
        +upcoming_talks: list
        +confirmed_sessions: list
        +pending_confirmations: list
        +availability_status: dict
        +get_assigned_sessions() list
        +get_upcoming_talks() list
        +confirm_availability(session_id: str) bool
        +decline_session(session_id: str, reason: str) bool
        +get_session_details(session_id: str) dict
        +request_reassignment(session_id: str, reason: str) bool
        +update_availability(date: datetime, available: bool) None
        +get_session_materials(session_id: str) list
        +join_session(session_id: str) bool
        +get_speaker_info(session_id: str) dict
        +get_moderation_guidelines() dict
        +export_schedule(format: str) bytes
    }

    class QuestionModerator {
        +session_id: str
        +incoming_questions: list
        +approved_questions: list
        +rejected_questions: list
        +forwarded_to_speaker: list
        +flagged_questions: list
        +moderation_queue: list
        +get_incoming_questions() list
        +approve_question(question_id: str) bool
        +reject_question(question_id: str, reason: str) bool
        +forward_to_speaker(question_id: str) bool
        +flag_question(question_id: str, flag_type: str) bool
        +edit_question(question_id: str, edited_text: str) bool
        +merge_questions(question_ids: list) dict
        +prioritize_question(question_id: str) bool
        +batch_approve(question_ids: list) dict
        +batch_reject(question_ids: list) dict
        +filter_questions(filter_type: str) list
        +search_questions(query: str) list
        +get_moderation_stats() dict
        +export_qa_log() bytes
    }

    class NoteManager {
        +session_id: str
        +notes_content: str
        +note_timestamps: list
        +key_points: list
        +action_items: list
        +saved_notes: list
        +auto_save_enabled: bool
        +create_note(content: str) str
        +add_timestamp() None
        +add_key_point(point: str) None
        +add_action_item(item: str) None
        +edit_note(note_id: str, new_content: str) bool
        +delete_note(note_id: str) bool
        +save_notes() bool
        +auto_save() None
        +export_notes(format: str) bytes
        +search_notes(query: str) list
        +get_session_notes(session_id: str) dict
        +create_summary() str
        +share_notes(recipient_ids: list) bool
        +import_template(template_name: str) bool
    }

    class SessionReminder {
        +moderator_id: int
        +active_reminders: list
        +reminder_settings: dict
        +notification_methods: list
        +preferred_method: str
        +set_reminder(session_id: str, time_before: timedelta) bool
        +cancel_reminder(reminder_id: str) bool
        +update_reminder_settings(settings: dict) None
        +get_active_reminders() list
        +snooze_reminder(reminder_id: str, minutes: int) bool
        +acknowledge_reminder(reminder_id: str) None
        +set_notification_method(method: str) bool
        +test_notification() bool
        +get_upcoming_reminders(hours: int) list
        +bulk_set_reminders(session_ids: list) dict
        +disable_all_reminders() None
        +enable_all_reminders() None
        +get_reminder_history() list
    }

    class ModerationFeedback {
        +moderator_id: int
        +session_id: str
        +overall_experience_rating: int
        +technical_issues_rating: int
        +speaker_cooperation_rating: int
        +audience_engagement_rating: int
        +comments: str
        +improvement_suggestions: str
        +would_moderate_again: bool
        +submission_timestamp: datetime
        +set_overall_rating(rating: int) None
        +set_technical_rating(rating: int) None
        +set_speaker_rating(rating: int) None
        +set_audience_rating(rating: int) None
        +add_comments(comments: str) None
        +add_suggestions(suggestions: str) None
        +report_issue(issue_type: str, description: str) bool
        +set_future_availability(available: bool) None
        +submit_feedback() bool
        +save_draft() None
        +validate_feedback() list
        +get_previous_feedback() list
        +attach_evidence(file_data: bytes, file_type: str) bool
    }

    %% Core relationships
    SessionAssignments --> QuestionModerator : assigns moderator to
    SessionAssignments --> NoteManager : creates notes for
    SessionAssignments --> SessionReminder : triggers reminders
    QuestionModerator --> NoteManager : references in notes
    SessionReminder --> SessionAssignments : reminds about
    ModerationFeedback --> SessionAssignments : provides feedback on
    
    %% Workflow relationships
    SessionAssignments *-- SessionReminder : manages
    QuestionModerator *-- NoteManager : uses during moderation
    SessionAssignments --> ModerationFeedback : completes with
```

## Class Descriptions

### SessionAssignments
Manages moderator's session assignments:
- View assigned and upcoming sessions
- Confirm or decline assignments
- Update availability calendar
- Access session materials and speaker info
- Export moderation schedule

### QuestionModerator
Real-time question moderation during sessions:
- Review incoming audience questions
- Approve/reject/edit questions
- Forward questions to speakers
- Flag inappropriate content
- Batch operations for efficiency
- Export Q&A logs

### NoteManager
Private note-taking during moderation:
- Create timestamped notes
- Mark key points and action items
- Auto-save functionality
- Template support
- Note sharing capabilities
- Export in multiple formats

### SessionReminder
Reminder management for moderation duties:
- Set custom reminders
- Multiple notification methods (email, push, SMS)
- Snooze functionality
- Bulk reminder settings
- Test notifications

### ModerationFeedback
Post-session feedback collection:
- Rate multiple aspects (technical, speaker, audience)
- Provide detailed comments
- Report issues with evidence
- Future availability indication

## Moderator Workflow

```mermaid
sequenceDiagram
    participant Moderator
    participant SessionAssignments
    participant SessionReminder
    participant QuestionModerator
    participant NoteManager
    participant ModerationFeedback
    
    Moderator->>SessionAssignments: View assignments
    SessionAssignments->>Moderator: Show upcoming sessions
    Moderator->>SessionAssignments: Confirm availability
    
    SessionAssignments->>SessionReminder: Set reminders
    SessionReminder->>Moderator: Send notification
    
    Moderator->>SessionAssignments: Join session
    SessionAssignments->>QuestionModerator: Start moderation
    
    loop During Session
        QuestionModerator->>Moderator: Show incoming questions
        Moderator->>QuestionModerator: Approve/Reject
        Moderator->>NoteManager: Take notes
        NoteManager->>NoteManager: Auto-save
    end
    
    Moderator->>NoteManager: Export notes
    Moderator->>ModerationFeedback: Submit feedback
    ModerationFeedback->>ModerationFeedback: Save feedback
```

## Key Features

### Pre-Session
- **Assignment management** with accept/decline
- **Availability calendar** for scheduling
- **Session preparation** with materials access
- **Customizable reminders** with multiple channels

### During Session
- **Real-time Q&A moderation** with filtering
- **Question editing** for clarity
- **Batch operations** for efficiency
- **Note-taking** with timestamps
- **Auto-save** functionality

### Post-Session
- **Multi-dimensional feedback** system
- **Issue reporting** with evidence
- **Note export** in multiple formats
- **Q&A log generation**

### Productivity Features
- **Template support** for notes
- **Search functionality** across questions and notes
- **Bulk operations** for efficiency
- **Calendar export** for schedule management
- **Statistics tracking** for moderation activity