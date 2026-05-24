"""
Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

q1 is our start state, we begin reading commands from here
q2 is our accept state, we return true if this is our last state
And the transitions:

q1 moves to q2 when given a 1, and stays at q1 when given a 0
q2 moves to q3 when given a 0, and stays at q2 when given a 1
q3 moves to q2 when given a 0 or 1
The automaton should return whether we end in our accepted state (q2), or not (true/false).

Your task
You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3 for the myAutomaton instance. The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

Here are some resources on DFAs (the automaton this Kata asks you to create):

http://en.wikipedia.org/wiki/Deterministic_finite_automaton
http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf
Example
a = Automaton()
a.read_commands(["1", "0", "0", "1", "0"])  ==> False
We make these transitions:

input: ["1", "0", "0", "1", "0"]

1: q1 -> q2
0: q2 -> q3
0: q3 -> q2
1: q2 -> q2
0: q2 -> q3
We end in q3 which is not our accept state, so we return false
"""

class State:
    def __init__(self, name, is_accept = False):
        self.name = name
        self.is_accept = is_accept
        self.transitions = {}

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def next_state(self, symbol):
        return self.transitions[symbol]

class Automation:
    def __init__(self):
        self.q1 = State("q1")
        self.q2 = State("q2", is_accept = True)
        self.q3 = State("q3")

        self.q1.add_transition("0", self.q1)
        self.q1.add_transition("1", self.a2)

        self.q2.add_transition("0", self.q3)
        self.q2.add_transition("1", self.q2)

        self.q3.add_transition("0", self.q2)
        self.q3.add_transition("1", self.q2)

def read_commands(self, commands):
    current = self.q1

    for symbol in commands:
        current = current.next_state(symbol)

    return current.is_accept

my_Automation = Automation()
