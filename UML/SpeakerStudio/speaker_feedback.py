from typing import Dict, List
from datetime import datetime

class SpeakerFeedback:
    """
    Submit feedback about the speaking experience and platform.
    """
    
    def __init__(self):
        self.speaker_id = None
        self.event_id = None
        self.platform_rating = 0
        self.technical_support_rating = 0
        self.organization_rating = 0
        self.additional_comments = ""
        self.improvement_suggestions = ""
        self.would_speak_again = None
        self.submission_date = None
        
    def set_platform_experience(self, rating: int) -> None:
        """Rate the platform experience (1-5)."""
        pass
        
    def set_technical_support(self, rating: int) -> None:
        """Rate technical support quality."""
        pass
        
    def set_organization(self, rating: int) -> None:
        """Rate event organization."""
        pass
        
    def add_comments(self, comments: str) -> None:
        """Add additional feedback comments."""
        pass
        
    def add_suggestions(self, suggestions: str) -> None:
        """Add improvement suggestions."""
        pass
        
    def set_future_participation(self, would_participate: bool) -> None:
        """Indicate willingness to speak at future events."""
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
        
    def get_feedback_history(self) -> List[Dict]:
        """Get speaker's previous feedback submissions."""
        pass
        
    def export_feedback(self) -> str:
        """Export feedback for records."""
        pass