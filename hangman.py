import random

class Hangman():

    def __init__(self):
        self.words = open('words.txt').read().splitlines()
        self.guessed_letters = []
        self.won = False
        self.guesses = 0
        self.answer = random.choice(self.words)
        self.found_ans = '_'*len(self.answer)
        print('_ ' * len(self.answer))


    def run(self):
        while self.guesses < 5:
            while True:
                guess = input('Enter a character: ')
                if len(guess) != 1:
                    print('Invalid character')
                else:
                    if guess in self.guessed_letters:
                        print('That character has already been guessed')
                    else:
                        self.guessed_letters.append(guess)
                        break

            found = False
            new_answer = ''
            for ch in self.answer:
                if guess == ch:
                    found = True
                    new_answer += ch
                else:
                    if self.found_ans[self.answer.index(ch)] == '_':
                        new_answer += '_'
                    else:
                        new_answer += self.found_ans[self.answer.index(ch)]

            self.found_ans = new_answer

            na = ''
            for c in new_answer:
                na += '%s '%c

            if '_' in new_answer:
                if found:
                    print('Character found\n{}'.format(na))
                else:
                    self.guesses += 1
                    print('Character was not found, you have {} guesses left\n{}'.format((5 - self.guesses), na))
            else:
                print('Congratulations, you have won the game!\nThe word was {}'.format(new_answer))
                self.won = True
                break

        if self.won:
            quit()
        else:
            print('You ran out of guesses, you lose!\nThe word was {}'.format(self.answer))


h = Hangman()
h.run()
