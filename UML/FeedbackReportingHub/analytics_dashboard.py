from typing import Dict, List, Optional
from datetime import datetime

class AnalyticsDashboard:
    """
    Main analytics dashboard displaying KPIs and event metrics.
    """
    
    def __init__(self):
        self.event_id = None
        self.overall_event_rating = 0.0
        self.total_feedback_submissions = 0
        self.delegate_engagement_score = 0.0
        self.most_successful_talk = ""
        self.keynote_address_score = 0.0
        self.attendance_metrics = {}
        self.engagement_trends = []
        self.real_time_data = {}
        
    def load_dashboard_data(self, event_id: str) -> Dict:
        """Load all dashboard data for an event."""
        pass
        
    def calculate_overall_rating(self) -> float:
        """Calculate overall event rating from all feedback."""
        pass
        
    def get_feedback_count(self) -> int:
        """Get total number of feedback submissions."""
        pass
        
    def calculate_engagement_score(self) -> float:
        """Calculate delegate engagement score."""
        pass
        
    def identify_top_sessions(self, limit: int = 5) -> List[Dict]:
        """Identify most successful sessions."""
        pass
        
    def get_attendance_metrics(self) -> Dict:
        """Get detailed attendance statistics."""
        pass
        
    def get_engagement_trends(self, period: str = "daily") -> List[Dict]:
        """Get engagement trends over time."""
        pass
        
    def get_real_time_metrics(self) -> Dict:
        """Get real-time event metrics."""
        pass
        
    def compare_to_previous_event(self, previous_event_id: str) -> Dict:
        """Compare metrics to previous event."""
        pass
        
    def get_demographic_breakdown(self) -> Dict:
        """Get attendee demographic information."""
        pass
        
    def get_session_performance(self) -> List[Dict]:
        """Get performance metrics for all sessions."""
        pass
        
    def export_dashboard(self, format: str = "pdf") -> bytes:
        """Export dashboard as PDF or image."""
        pass
        
    def set_refresh_interval(self, seconds: int) -> None:
        """Set auto-refresh interval for dashboard."""
        pass