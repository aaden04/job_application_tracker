class Progress:
    def __init__(self, id, status, interview_date, decision, applications_id):
        self.id = id
        self.status = status
        self.interview_date = interview_date 
        self.decision = decision  
        self.applications_id = applications_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__        

    def __repr__(self):
        return f"Application Number:{self.applications_id}, Status:{self.status}, Interview Date:{self.interview_date}, Decision:{self.decision})"
