import sys
import argparse

parser = argparse.ArgumentParser(description='Test FMS.')
parser.add_argument('--myLength', metavar='N', type=int, nargs=1,default=1,help='the length of the input for the FSM')

args = parser.parse_args()

try:
	if args.myLength == 1:
		longInput = 1
	else:
		longInput = abs(int(args.myLength[0]))
except ValueError as verr:
	print('Please enter an integer')
except Exception as ex:
	print('ERROR')
	
#Source: http://www.python-course.eu/finite_state_machine.php
#date: 2017.01.31
class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.badStates = []

    def add_state(self, name, handler, end_state=0, bad_state = 0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)
        if bad_state:
            self.badStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        retorno = 0
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise  InitializationError("at least one state must be an end_state")
    
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                if newState.upper() in self.badStates:
                 #print("reached ", newState)
                 retorno = 1
                break 
            else:
                handler = self.handlers[newState.upper()]

        return retorno


def e0_transitions(input):
 current = input[0]
 del input[0]
 if current == "0":
  newState = "e2"
 else:
  newState = "e1"
 return (newState, input)

def e1_transitions(input):
 if not input:
  return ("e1f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e5"
  else:
   newState = "e8"
  return (newState, input)

def e2_transitions(input):
 if not input:
  return ("e2f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e3"
  else:
   newState = "e1"
  return (newState, input)

def e3_transitions(input):
 if not input:
  return ("e3f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e4"
  else:
   newState = "e1"
  return (newState, input)

def e4_transitions(input):
 if not input:
  return ("e4f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e4"
  else:
   newState = "e1"
  return (newState, input)

def e5_transitions(input):
 if not input:
  return ("e5f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e6"
  else:
   newState = "e8"
  return (newState, input)

def e6_transitions(input):
 if not input:
  return ("e6f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e7"
  else:
   newState = "e8"
  return (newState, input)

def e7_transitions(input):
 if not input:
  return ("e7f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e4"
  else:
   newState = "e8"
  return (newState, input)

def e8_transitions(input):
 if not input:
  return ("e8f", input)
 else:
  current = input[0]
  del input[0]
  if current == "0":
   newState = "e8"
  else:
   newState = "e8"
  return (newState, input)

if __name__== "__main__":
 m = StateMachine()
 m.add_state("e0", e0_transitions)
 m.add_state("e1", e1_transitions)
 m.add_state("e2", e2_transitions)
 m.add_state("e3", e3_transitions)
 m.add_state("e4", e4_transitions)
 m.add_state("e5", e5_transitions)
 m.add_state("e6", e6_transitions)
 m.add_state("e7", e7_transitions)
 m.add_state("e8", e8_transitions)
 m.add_state("e1f", None, end_state=1)
 m.add_state("e2f", None, end_state=1)
 m.add_state("e3f", None, end_state=1)
 m.add_state("e4f", None, end_state=1)
 m.add_state("e5f", None, end_state=1)
 m.add_state("e6f", None, end_state=1)
 m.add_state("e7f", None, end_state=1)
 m.add_state("e8f", None, end_state=1, bad_state = 1)
 m.set_start("e0")
 total = pow(2,longInput)
 goods = 0
 for i in range(0, pow(2,longInput)):
  input = list("{0:b}".format(i).zfill(longInput))
  aux = "{0:b}".format(i).zfill(longInput) 
  #print("Evaluating: ",input)
  retorno = m.run(input)
  if retorno == 0:
   goods += 1
   print("Good input", aux)
 print("There were ",goods," of ",total)