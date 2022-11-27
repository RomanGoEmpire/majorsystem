import time
from random import shuffle

major = {0: ["s", "z"], 1: ["d", "t", "th"], 2: ["n"], 3: ["m"], 4: ["r"], 5: ["l"], 6: ["j", "ch", "sch"],
         7: ["k", "q", "c", "ck", "g"], 8: ["f", "v", "w", "ph"], 9: ["p", "b"]}

big_major = {"0": "See", "1": "Tee", "2": "Noah", "3": "Mix", "4": "Ree", "5": "Allee", "6": "Schuh", "7": "Kuh",
             "8": "Ufo", "9": "Boa",
             "00": "Zeus", "01": "Soda", "02": "Ozean", "03": "Saum", "04": "Zar", "05": "Esel", "06": "Seuche",
             "07": "Zug", "08": "Sofa", "09": "Suppe",
             "10": "Dose", "11": "Dodu", "12": "Donau", "13": "Dom", "14": "Tor", "15": "Hotel", "16": "Tasche",
             "17": "Teig", "18": "TV", "19": "Typ",
             "20": "NASA", "21": "Not", "22": "Nonne", "23": "Nemo", "24": "Nero", "25": "Nil", "26": "Nische",
             "27": "Honig", "28": "Info", "29": "Neubau",
             "30": "Maus", "31": "Made", "32": "Mona", "33": "Mumie", "34": "Mixer", "35": "Mehl", "36": "Moschee",
             "37": "Mücke", "38": "Möwe", "39": "Mopp",
             "40": "Reis", "41": "Rad", "42": "Uran", "43": "Rom", "44": "Rohr", "45": "Real", "46": "Rauch",
             "47": "Reck", "48": "Rewe", "49": "Rabe",
             "50": "Lasso", "51": "Lady", "52": "Leine", "53": "Lama", "54": "Leier", "55": "Lolli", "56": "Leiche",
             "57": "Lego", "58": "Lava", "59": "Laub",
             "60": "Schuss", "61": "Jet", "62": "China", "63": "Schaum", "64": "Schere", "65": "Schal", "66": "Scheich",
             "67": "Jacke", "68": "Chef", "69": "Jeep",
             "70": "Käse", "71": "Gott", "72": "Kino", "73": "Kamm", "74": "Geier", "75": "Keule", "76": "Koch",
             "77": "Geige", "78": "Kaffee", "79": "Kappe",
             "80": "Fass", "81": "Foto", "82": "Wein", "83": "WM", "84": "Feuer", "85": "Falle", "86": "Wäsche",
             "87": "Waage", "88": "Waffe", "89": "Wabe",
             "90": "Bus", "91": "Bett", "92": "Biene", "93": "Baum", "94": "Bär", "95": "Pool", "96": "Bach",
             "97": "Bug", "98": "Pfau", "99": "Pappe",
             }

options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "00", "01", "02", "03", "04", "05", "06", "07",
           "08", "09"]


class Major:
    def __init__(self):
        self.big_major = big_major
        self.options = None
        self.wrong_answers = None
        self.stats = None

    def start(self):
        while True:
            print("Choose an option:\n"
                  "1. Words to number\n"
                  "2. Number to words\n"
                  "3. Exit")
            answer = input("Your choice: ")
            if answer == "1":
                self.training(self.question_words_to_number(), self.check_answer_words_to_number(), False)
                self.reset()
            elif answer == "2":
                self.training(self.question_number_to_words(), self.check_number_to_word(), True)
                self.reset()
            elif answer == "3":
                break
            else:
                print("Wrong input!")

    def reset(self):
        self.options = options
        shuffle(self.options)
        self.wrong_answers = []
        self.stats = {"correct": 0, "wrong": 0}

    def training(self, question, check_answer, is_number_to_words):
        self.reset()
        start_time = time.time()
        while self.options:
            number = self.options.pop()
            solved = False
            print(question(number))
            for i in range(3):
                answer = input()
                if check_answer(answer, number):
                    print("")
                    self.stats["correct"] += 1
                    solved = True
                    break
                else:
                    print(f"Try again! You have {2 - i} tries left.")
            if is_number_to_words:
                self.if_not_solved(number, solved, self.big_major[number])
            else:
                self.if_not_solved(number, solved, number)
        self.print_stats()
        print(f"Time elapsed: {int(time.time() - start_time)} seconds\n")

    @staticmethod
    def check_answer_words_to_number():
        return lambda answer, number: answer == number

    def question_words_to_number(self):
        return lambda number: self.big_major[number]

    @staticmethod
    def question_number_to_words():
        return lambda number: number

    def check_number_to_word(self):
        return lambda answer, number: answer.lower() == self.big_major[number].lower()

    def if_not_solved(self, number, solved, correct_answer):
        if not solved:
            self.stats["wrong"] += 1
            self.wrong_answers.append(number)
            self.options.append(number)
            print(f"Correct answer is {correct_answer}")

    def print_stats(self):
        print(f"You got {self.stats['correct']} correct and {self.stats['wrong']} wrong!")
        print(f"Your score is {self.stats['correct'] / (self.stats['correct'] + self.stats['wrong']) * 100}%")
        if self.wrong_answers:
            print("You got the following wrong:")
            for wrong_answer in self.wrong_answers:
                print(f"{wrong_answer}: {self.big_major[wrong_answer]}")
