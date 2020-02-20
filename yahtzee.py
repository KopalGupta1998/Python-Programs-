"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import poc_simpletest
import random
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def gen_all_permutations(outcomes,length):
    """
    Iterative function that finds all the permutations
    for the of a specific length
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = []
        for seq in ans:
            for item in outcomes:
                if item not in seq or seq.count(item)<outcomes.count(item):
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.append(tuple(new_seq))
        ans = temp
    return ans
    
    
def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    # computing the values associated with each side of the dice
    possible_scores= [hand.count(value)*value for value in hand]
    # returning the maximum value in possible_scores
    return max(possible_scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # finding all rolls possible
    all_rolls = gen_all_sequences((range(1,(num_die_sides+1))),num_free_dice)
    # finding all hands possible
    all_possible_hands = [hand + held_dice for hand in all_rolls]
    number_of_outcomes = float(len(all_rolls))
    expected = 0
    # computing the expected value using a for loop
    for hand in all_possible_hands:
        expected += (1/number_of_outcomes)*score(hand)
    return expected
    


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds=set([()])
    # Iterating over and generating all possible sets for each length
    for length in range(len(hand)+1):
        # sets generated for a partcular length
        all_permutations=gen_all_permutations(hand,length)
        # sorting each tuple generated
        all_combinations=[tuple(sorted(sequence)) for sequence in all_permutations]
        # adding the sorted sequences to all_holds
        all_holds.update(all_combinations)
    # returning all_holds
    return all_holds



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    dummy_all_hold=gen_all_holds(hand)
    all_holds=list(dummy_all_hold)
    largest=0
    value=0
    expected_value_list=[]
    for hold in all_holds:
        expected_value_number=expected_value(hold,num_die_sides,len(hand)-len(hold))
        expected_value_list.append(expected_value_number)
        if expected_value_number>largest:
            largest=expected_value_number
    hold_choice=[]
    for value in range(len(expected_value_list)):
        if largest==expected_value_list[value]:
            hold_choice.append(all_holds[value])
                     
        
    return (largest, random.choice(hold_choice))


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

    
#def run_suite(score):
    #suite=poc_simpletest.TestSuite()
    #suite.run_test(score((1,1,1,5,6)),6,"Test 1:")
    #suite.run_test(score((0,0,0,0,4)),4,"Test 2:")
    #suite.run_test(score((6,6,6,5,4)),18,"Test 3:")
    #suite.run_test(score((5,6,4,0,4)),8,"Test 4:")
    #suite.run_test(score((0,2,2,2,4)),6,"Test 5:")
    #suite.report_results()
#run_suite(score)
run_example()
#gen_all_holds((1,1,1,5,6))
#expected_value((6,),6,4)
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



