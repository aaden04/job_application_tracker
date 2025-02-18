
from lib.progress import Progress

def test_progress_constructs():
    progress = Progress(1, "Applied", "2023-01-01", "Accepted", 1)
    assert progress.id == 1
    assert progress.status == "Applied"
    assert progress.interview_date == "2023-01-01"
    assert progress.decision == "Accepted"
    assert progress.applications_id == 1

def test_progress_equality():
    progress1 = Progress(1, "Applied", "2023-01-01", "Accepted", 1)
    progress2 = Progress(1, "Applied", "2023-01-01", "Accepted", 1)
    assert progress1 == progress2

def test_progress_format_string():
    progress = Progress(1, "Applied", "2023-01-01", "Accepted", 1)
    expected = "Application Number:1, Status:Applied, Interview Date:2023-01-01, Decision:Accepted)"
    assert str(progress) == expected