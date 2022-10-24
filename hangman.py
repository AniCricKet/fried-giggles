import uuid

sessionIDs = {}


def newSession():
    localID = uuid.uuid4()
    sessionIDs.append(localID)