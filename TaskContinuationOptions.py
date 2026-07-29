class TaskContinuationOptions:
    None_ = 0
    PreferFairness = 1
    LongRunning = 2
    AttachedToParent = 3
    DenyChildAttach = 4
    HideScheduler = 5
    LazyCancellation = 6
    RunContinuationsAsynchronously = 7
    NotOnRanToCompletion = 8
    NotOnFaulted = 9
    NotOnCanceled = 10
    OnlyOnRanToCompletion = 11
    OnlyOnFaulted = 12
    OnlyOnCanceled = 13
    ExecuteSynchronously = 14
