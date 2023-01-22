### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#the class needs an __init__ function to initialise

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False

  # 1. the operator in the if statement is incorrect, should be == not = 
  # 2. there is a : missing after the else statement
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

  # 1. a typo has been made defing the it, should be def not dif
  # 2. no comma between the card1 and card2 variables
  # 3. the if statement and following code is not indented
  # 4. the return on the if statement should return card1 not card


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total

  # 1. The whole function needs to be indented
  # 2. the total variable needs to have a value assigned to it for the function to run
  # 3. the return statement is in the for loop so needs to have its indentation removed to move it outside the loop
  # 4. the total in the return function needs to be converted to a string to be added to the preceding string

  
  
```
