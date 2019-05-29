import sys
import math
import time
import Queue as Q
import resource
from heapq import heappush, heappop
import itertools
from collections import deque

#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])

    def move_down(self):
        """ 
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index < 6:
            newconf = self.config[:]
            newconf[self.blank_index] = newconf[self.blank_index+3]
            newconf[self.blank_index+3] = self.config[self.blank_index]
            return PuzzleState(newconf, self.n, self, 'Down', self.cost+1)
        else:
            return None
      
    def move_up(self):
        """
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index > 2:
            newconf = self.config[:]
            newconf[self.blank_index] = newconf[self.blank_index-3]
            newconf[self.blank_index-3] = self.config[self.blank_index]
            return PuzzleState(newconf, self.n, self, 'Up', self.cost+1)
        else:
            return None
      
    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index not in [2, 5, 8]:
            newconf = self.config[:]
            newconf[self.blank_index] = newconf[self.blank_index+1]
            newconf[self.blank_index+1] = self.config[self.blank_index]
            return PuzzleState(newconf, self.n, self, 'Right', self.cost+1)
        else:
            return None

    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index not in [0, 3, 6]:
            newconf = self.config[:]
            newconf[self.blank_index] = newconf[self.blank_index-1]
            newconf[self.blank_index-1] = self.config[self.blank_index]
            return PuzzleState(newconf, self.n, self, 'Left', self.cost+1)
        else:
            return None
      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children


# Define a priority queue for update
class PriorityQueue(object):
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()

    def add_task(self, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def get_priority(self, task):
        return self.entry_finder[task][0]

    def empty(self):
        return len(self.entry_finder) == 0

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(result):
    ### Student Code Goes here
    key = ['path_to_goal', 'cost_of_path', 'nodes_expanded', 'search_depth',
           'max_search_depth', 'running_time', 'max_ram_usage']
    text_file = open("output.txt", "w")
    for i in range(len(key)):
        if i < 5:
            text_file.write("{0}:{1}\n".format(key[i], result[i]))
            print "{0}:{1}".format(key[i], result[i])
        else:
            text_file.write("{0}:{1:.8f}\n".format(key[i], result[i]))
            print "{0}:{1:.8f}".format(key[i], result[i])
    text_file.close()

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    queue = deque()
    queue.append(initial_state)
    visit = set()
    visit.add(tuple(initial_state.config))
    maxdist = 0
    solution_state = None
    count_expand = 0
    while queue:
        curr_state = queue.popleft()
        if test_goal(curr_state):
            solution_state = curr_state
            break
        else:
            children = curr_state.expand()
            count_expand += 1
            for child in children:
                if tuple(child.config) not in visit:
                    queue.append(child)
                    visit.add(tuple(child.config))
                    if child.cost > maxdist : maxdist = child.cost
    path_to_goal = []
    state = solution_state
    while state != initial_state :
        path_to_goal.insert(0,state.action)
        state = state.parent
    result = [path_to_goal, solution_state.cost, count_expand, solution_state.cost, maxdist]
    return result
                    

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    queue = Q.LifoQueue()
    queue.put(initial_state)
    visit = set()
    visit.add(tuple(initial_state.config))
    maxdist = 0
    solution_state = None
    count_expand = 0
    while not queue.empty() :
        curr_state = queue.get()
        if test_goal(curr_state):
            solution_state = curr_state
            break
        else:
            children = curr_state.expand()
            count_expand += 1
            for i in range(len(children)-1, -1, -1):
                child = children[i]
                if tuple(child.config) not in visit:
                    queue.put(child)
                    visit.add(tuple(child.config))
                    if child.cost > maxdist: maxdist = child.cost
    path_to_goal = []
    state = solution_state
    while state != initial_state:
        path_to_goal.insert(0, state.action)
        state = state.parent
    result = [path_to_goal, solution_state.cost, count_expand, solution_state.cost, maxdist]
    return result


def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    queue = PriorityQueue()
    queue.add_task(initial_state, calculate_total_cost(initial_state))
    visit = {}
    visit[tuple(initial_state.config)] = initial_state
    maxdist = 0
    solution_state = None
    count_expand = 0
    while not queue.empty():
        curr_state = queue.pop_task()
        visit[tuple(curr_state.config)] = None
        if test_goal(curr_state):
            solution_state = curr_state
            break
        else:
            children = curr_state.expand()
            count_expand += 1
            for child in children:
                if tuple(child.config) not in visit:
                    queue.add_task(child, calculate_total_cost(child))
                    visit[tuple(child.config)] = child
                    if child.cost > maxdist: maxdist = child.cost
                elif tuple(child.config) in visit and visit[tuple(child.config)] != None:
                    if calculate_total_cost(child) < queue.get_priority(visit[tuple(child.config)]):
                        queue.add_task(child, calculate_total_cost(child))
                        visit[tuple(child.config)] = child
                        if child.cost > maxdist: maxdist = child.cost
    path_to_goal = []
    state = solution_state
    while state != initial_state:
        path_to_goal.insert(0, state.action)
        state = state.parent
    result = [path_to_goal, solution_state.cost, count_expand, solution_state.cost, maxdist]
    return result

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    manhattan = 0
    for index, value in enumerate(state.config):
        if value != 0:
            manhattan += calculate_manhattan_dist(index, value)
    return manhattan + state.cost

def calculate_manhattan_dist(idx, value):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    r = idx / 3
    c = idx % 3
    goal = {1:[0,1], 2:[0,2], 3:[1,0], 4:[1,1], 5:[1,2], 6:[2,0], 7:[2,1], 8:[2,2]}
    return abs(r-goal[value][0]) + abs(c-goal[value][1])

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    goal_state_conf = [0,1,2,3,4,5,6,7,8]
    return puzzle_state.config == goal_state_conf

# Main Function that reads in Input and Runs corresponding Algorithm

def get_ram():
    ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'linux2':
        ram /= 1024.0
    else:
        ram /= 1024.0 * 1024.0
    return ram

def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    start_ram = get_ram()
    result = None
    ram = None
    if   search_mode == "bfs": result = bfs_search(hard_state)
    elif search_mode == "dfs": result = dfs_search(hard_state)
    elif search_mode == "ast": result = A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    end_time = time.time()
    end_ram = get_ram()
    result.append(end_time-start_time)
    result.append(end_ram-start_ram)
    writeOutput(result)
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()