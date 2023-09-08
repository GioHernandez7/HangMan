print("Let's play Hang Man!")
correct_letters = ['r','o','n','a','l','d','o']
good_letters = ['_','_','_','_','_','_','_']
bad_letters = []
status = "lose"
while len(bad_letters) < 6:
  if good_letters == correct_letters:
    print("You Win!")
    status = "win"
    break
  #if len(bad_letters) = 6:
  print("Take a guess!: ")
  answer = input()
  if answer in correct_letters:
    position = correct_letters.index(answer)
    good_letters.pop(position)
    good_letters.insert(position, answer)
    print("good" + str(good_letters))
    print("bad" + str(bad_letters))
  else:
    bad_letters.append(answer)
    print("good" + str(good_letters))
    print("bad" + str(bad_letters))

if status == "lose":
  print("You Lost!")



