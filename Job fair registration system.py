from collections import deque

# Stack for registrations
undo_stack = []

current_register = []

# Queue for job fair requests
job_queue = deque()

#list of available job posts
available_jobs = []
 

current_register = ['Arthur']
undo_stack.append(current_register) 

# Undo last registration
if undo_stack:
    current_register = undo_stack.pop()
    print("Registration undone:", current_register)

# Queue
job_queue.append('Uwera')
job_queue.append('Jojo')
job_queue.append('Darren')
print("Job requests received:", list(job_queue))

# Dequeue
if job_queue:
    processed_participant = job_queue.popleft()
    print(f"{processed_participant} has been processed.")

#new job posts
available_jobs.append('Software Developer')
available_jobs.append('Data Analyst')
print("Available Jobs:", available_jobs)

# Remove a job post
if 'Data Analyst' in available_jobs:
    available_jobs.remove('Data Analyst')
print("Available Jobs after removal:", available_jobs)

print("Job Fair Requests in Queue:", list(job_queue))