from System import *
from Deadline.Events import *
from Deadline.Scripting import *


# Function to get an instance of event listener
def GetDeadlineEventListener():
    return AutoChunker()


# Cleanup function to ensure no memory leak
def CleanupDeadlineEventListener(eventListener):
    eventListener.Cleanup()


class ShotgunPublisher(DeadlineEventListener):

    def __init__(self):
        self.OnJobFinishedCallback += self.OnJobFinished
        self.sg_script_name = self.GetConfigEntryWithDefault("ShotgunScriptName", "")
        self.sg_script_key = self.GetConfigEntryWithDefault("ShotgunScriptKey", "")
        self.sg_script_address = self.GetConfigEntryWithDefault("ShotgunURL", "")

    # Cleanup function to ensure no memory leak
    def Cleanup(self):
        del self.OnJobFinishedCallback
    
    # This is called when a job is submitted.
    def OnJobFinished(self, job):
        self.LogInfo('Event dziala')
        if job.JobName != "":
            self.LogInfo('++++++ %s' % job.JobName)
