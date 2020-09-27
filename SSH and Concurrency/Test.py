#Concurrency vs Parallelism - Chcek out the graph from Kirk. Concurrency means over a short time multiple things are getting executed. It may
#or may not imply that they are executed in parallel.

#Ways to achieve to concurrency - Threads/Processes/Asynchronous (Threads and Processes in this course)

# Threads
#In a single process there could be multiple threads which job scheduler can pick which will allow us achieve concurrency.
#Eg. Multiple SSH sessions to different device. There could be potential race condition, also we need locks to gain access to a resource
#which can also lead to deadlock condition. Eg. Thread 1 gains a lock on some resource, thread 5 is then waiting and can reach deadlock.
#Global interpreter lock  - GIL - IF we have a single process, 50 threads, we can only run 1 thread at a time. (This would have been big deal if we
#were CPU bound but in network automation we are always IO bound. We are always waiting for remote device to respond. Hence, GIL Doesn't cause problem.

# Processes
# (50 individual processes as 50 ssh connections and say if we have 10 cpu's then 10/50 process will run at same time : Parallelism)
# In both Process/Threads the way to exchange info between them is difficult.
