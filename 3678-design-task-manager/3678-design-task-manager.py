import heapq

class TaskManager:
    def __init__(self, tasks):
        # max heap: store (-priority, -taskId)
        self.pq = []
        # taskId -> (userId, priority)
        self.taskMap = {}
        for userId, taskId, priority in tasks:
            self.taskMap[taskId] = (userId, priority)
            heapq.heappush(self.pq, (-priority, -taskId))
    
    def add(self, userId, taskId, priority):
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.pq, (-priority, -taskId))
    
    def edit(self, taskId, newPriority):
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            self.taskMap[taskId] = (userId, newPriority)
            heapq.heappush(self.pq, (-newPriority, -taskId))
    
    def rmv(self, taskId):
        if taskId in self.taskMap:
            del self.taskMap[taskId]
    
    def execTop(self):
        while self.pq:
            negPriority, negTaskId = heapq.heappop(self.pq)
            taskId = -negTaskId
            priority = -negPriority
            if taskId in self.taskMap:
                userId, curPriority = self.taskMap[taskId]
                if curPriority == priority:
                    # valid top task
                    del self.taskMap[taskId]
                    return userId
            # else stale entry, continue
        return -1
