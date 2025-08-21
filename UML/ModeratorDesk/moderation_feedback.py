from typing import Dict, List
from datetime import datetime

class ModerationFeedback:
    """
    Submit feedback about moderation experience.
    """
    
    def __init__(self):
        self.moderator_id = None
        self.session_id = None
        self.overall_experience_rating = 0  # 1-5 stars
        self.technical_issues_rating = 0
        self.speaker_cooperation_rating = 0
        self.audience_engagement_rating = 0
        self.comments = ""
        self.improvement_suggestions = ""
        self.would_moderate_again = None
        self.submission_timestamp = None
        
    def set_overall_rating(self, rating: int) -> None:
        """Set overall moderation experience rating."""
        pass
        
    def set_technical_rating(self, rating: int) -> None:
        """Rate technical aspects of moderation."""
        pass
        
    def set_speaker_rating(self, rating: int) -> None:
        """Rate speaker cooperation."""
        pass
        
    def set_audience_rating(self, rating: int) -> None:
        """Rate audience engagement level."""
        pass
        
    def add_comments(self, comments: str) -> None:
        """Add detailed feedback comments."""
        pass
        
    def add_suggestions(self, suggestions: str) -> None:
        """Add improvement suggestions."""
        pass
        
    def report_issue(self, issue_type: str, description: str) -> bool:
        """Report specific issue encountered."""
        pass
        
    def set_future_availability(self, available: bool) -> None:
        """Indicate availability for future moderation."""
        pass
        
    def submit_feedback(self) -> bool:
        """Submit the feedback form."""
        pass
        
    def save_draft(self) -> None:
        """Save feedback as draft."""
        pass
        
    def validate_feedback(self) -> List[str]:
        """Validate feedback before submission."""
        pass
        
    def get_previous_feedback(self) -> List[Dict]:
        """Get moderator's previous feedback."""
        pass
        
    def attach_evidence(self, file_data: bytes, file_type: str) -> bool:
        """Attach screenshots or other evidence."""
        pass