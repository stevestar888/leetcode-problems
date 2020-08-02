"""
https://leetcode.com/problems/task-scheduler/solution/

Strat:
    In my opinion, there are 3 ways to solve this problem: simulation, 
    greedy, and math. The simulation strategy uses greedy for placement, 
    so I’ll start off with greedy first. Greedy is as simple as taking 
    the counts of all letters, and then finding the task that occurs the 
    most frequently, thus we should deal with it first. In the greedy 
    approach, we have to go from the greatest number of occurrences to 
    the least, all while staying aware of potential gaps (this is the 
    approach that I did). The simulation approach is actually creating an 
    additional DS and laying out tasks; the placement of the letters 
    themselves uses the greedy approach. The last method is math, which 
    requires a bit of thinking, but essentially, you need to find the 
    number of times the biggest count occurs. Then, you, fittingly, do 
    some math and return the answer. 

Stats:
    In terms of runtime, math and greedy are both linear time and constant
    space. (Greedy does require sorting, or using a heap; however, since 
    our input is limited to 26 letters, the upper bound to runtime is capped,
    so we can effectively ignore the time it takes to sort because it will be
    capped to a constant.) The simulation approach, depending on implementation,
    could be linear time (?) but the space isn’t ideal, so there’s no need to
    contemplate it further.
    
Other solutions:
    https://leetcode.com/problems/task-scheduler/discuss/476819/Python-O(-n-)-sol.-based-on-dictionary-95%2B-With-explanation (math)
    https://abhinandandubey.github.io/posts/2019/05/05/Task-Scheduler.html (detailed explaination)
    
"""
class Solution(object):
    """
    Runtime: 372 ms, faster than 85.89% of Python online submissions for Task Scheduler.
    Memory Usage: 14.9 MB, less than 7.14% of Python online submissions for Task Scheduler.
    """
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        
        def calculate_space_needed(occurence):
            """
            Given the number of times a task occurs (i.e., occurence) and
            the break needed between repeat tasks (i.e., n), returns the
            minimum total space required to complete all occurence of the task.
            """
            #alternatively, this is (occurence - 1) * n
            return occurence * (n + 1) - n
        
        #convert tasks to counter object
        tasks = Counter(tasks)
        
        #init capacity and used, using values from the num with most occurences,
        #then remove that elem from counter
        most_common = tasks.most_common(1)[0] #gives us a tuple
        most_common_task = most_common[0]
        most_common_task_count = most_common[1]
        del tasks[most_common_task]
        
        capacity = calculate_space_needed(most_common_task_count)
        used = most_common_task_count
        
        for task in tasks.values():
            if used + task > capacity: #exceeded capacity, need more space
                used += task
                capacity = used
            else:
                #edge case: check if task has same max_space as capacity
                #OR the task has the same length as the original most_common_task_count
                #if so, capacity needs to be increased by 1
                if calculate_space_needed(task) == capacity or task == most_common_task_count:
                    capacity += 1
                
                used += task
        
        return capacity
