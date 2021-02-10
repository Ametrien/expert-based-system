import random

# knowledge base

alien1 = [0, 'blonde', 'blue', 'tall', 'atheist', 'loonie']
alien2 = [0, 'red', 'green', 'tall', 'atheist', 'saturnian']
alien3 = [0, 'grey', 'black', 'normal', 'shinto', 'plutonian']
alien4 = [0, 'grey', 'green', 'tall', 'luteran', 'martian']
alien5 = [0, 'red', 'green', 'tall', 'pastafarian', 'cererian']
alien6 = [0, 'blonde', 'blue', 'normal', 'shinto', 'dwarf']

attr = ['score', 'hair', 'eyes', 'height', 'religion']
ll = [alien1, alien2, alien3, alien4, alien5, alien6]

all_input = []


# inference engine


def ask_question(i):  # all aliens, one attribute
    print("What can you tell me about their " + attr[i] + "?")


def rec_input():
    global ll
    # get user input
    global user_input
    user_input = input()
    all_input.append(user_input)
    llcopy = ll.copy()
    newlist = []
    suspects = []

    # exclude impossible species
    find = user_input
    for i in range(len(ll)):
        for j in range(len(attr)):
            if find == llcopy[i][j]:
                newlist.append(ll[i])
                suspects.append(ll[i][-1])

    if len(suspects) > 1:
        # uncomment the line below to make debugging process easier
        # print(newlist)
        print("INTERMEDIATE RESULTS: I narrowed my data down to aliens from the " + user_input + " " + attr[rn] + " family:")
        print(suspects)
    # elif len(suspects) == 1:
    #     print("I think you encountered a " + suspects[0])
    # else:
    #     print("The experts do not have any data about this creature, it must be unique")

    # the global list gets updated so that next time we call this function ll will be smaller
    ll = newlist
    counter()


def counter():
    for j in range(len(ll)):
        for i in range(len(attr)):
            if ll[j][i] == user_input:
                ll[j][0] += 1


def max_score():
    # create a dictionary of scores and aliens
    all_scores = []
    all_aliens = []

    for i in range(len(ll)):
        all_scores.append(ll[i][0])

    for i in range(len(ll)):
        all_aliens.append(ll[i][-1])

    zip_iterator = zip(all_aliens, all_scores)
    score_dic = dict(zip_iterator)
    # find max score
    max_score = [key for key in score_dic if score_dic[key] == max(score_dic.values())]
    # find corresponding alien
    max_alien = max(score_dic, key=score_dic.get)

    if len(max_score) == 1:
        print("FINAL RESULT: I think you encountered a " + max_alien + ", because you entered:")
        print(all_input)
    elif len(max_score) == 2:
        print('It sounds like it could be either ' + max_score[0] + ' or ' + max_score[1])
    elif len(max_score) >= 3:
        print('I am confused. Your info is either not enough or not valid')


def qanda(i):
    ask_question(i)
    # print(all_input)
    rec_input()


def interrogation():
    for i in range(1, len(attr)):
        qanda(i)
    max_score()


# if all attributes that are left in ll are the same, it returns true
def same(i):
    lst = [item[i] for item in ll]
    # print(lst)
    return all(x == lst[0] for x in lst)


def experts_reply():
    qsts = [1, 2, 3, 4]
    # print(random.choice(qsts))
    global rn

    while len(ll) > 1:
        rn = random.choice(qsts)
        # narrow down the set of possible aliens every iteration by excluding fruitless questions
        if not same(rn):
            qanda(rn)

    max_score()


experts_reply()

