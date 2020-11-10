from Deadline.Events import *
from Deadline.Scripting import *


# Function to get an instance of event listener
def GetDeadlineEventListener():
    return AutoChunker()

# Cleanup function to ensure no memory leak
def CleanupDeadlineEventListener( eventListener ):
    eventListener.Cleanup()
	
	
class ShotgunAutoSubmitter(DeadlineEventListener):

    def __init__(self):
        self.OnJobFinishedCallback += self.OnJobFinished

    # Cleanup function to ensure no memory leak
    def Cleanup( self ):
        del self.OnJobFinishedCallback
    
    # This is called when a job is submitted.
    def OnJobFinished(self, job):
    