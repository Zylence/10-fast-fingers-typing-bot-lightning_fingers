import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from tkinter import *

import random
import time
import math
import pytesseract
import threading

TYPO_DICT = {"a": ["s", "w"],
             "b": ["f", "g", "h", "v"],
             "c": ["s", "v", "d"],
             "d": ["e", "r", "s"],
             "e": ["f", "r", "s"],
             "f": ["r", "t", "g"],
             "g": ["h", "n", "r", "t"],
             "h": ["m", "n", "t"],
             "i": ["l", "o", "o", "u", "u", "o"],
             "j": ["m", "n", "h"],
             "k": ["l", "j"],
             "l": ["o", "p"],
             "m": ["n"],
             "n": ["m"],
             "o": ["p", "i"],
             "p": ["o", "ü"],
             "q": ["s", "w"],
             "r": ["t", "t", "t", "e"],
             "s": ["w", "a"],
             "t": ["r", "z"],
             "u": ["z"],
             "v": ["c", "b"],
             "w": ["e", "s"],
             "x": ["c", "c", "y"],
             "y": ["<", "x", "x", "x"],
             "z": ["u", "h", "u"],
             "'": ["*"]}


class XPATHS:
    normal_ip = "//*[@id='inputfield']"
    normal_resource = '//*[@id="row1"]/span['
    challenge_ip = '//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input'
    challenge_resource = '//*[@id="game"]/div[3]/div[2]/div[1]/div/span['
    anticheat_ip = '//*[@id="word-input"]'
    anticheat_resource = '//*[@id="word-img"]/img'
    rld_bttn = '//*[@id="reload-btn"]/span'


def micro_delay():
    """ calculates a micro delay
    and returns it"""

    factor1 = [0.003, 0.001, 0.002, 0.008, 0.0009, 0.005, 0.007, 0.004, 0.006]
    factor2 = random.randint(1, 4)
    delay = (random.choice(factor1)) * factor2
    return delay


def safety_delay():
    """returns a delay, chosen at random"""

    pause = (random.choice([3.5, 7, 9, 5]) + micro_delay())
    return pause


def spawn_as_thread(func, param_dict):
    """takes function 'func' and a dict 'param_dict'
    to create a thread based on the parameters"""

    t = threading.Thread(target=func, kwargs=param_dict, daemon=True)
    t.start()


class App:
    def __init__(self, tk):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.delete_all_cookies()
        self.driver.get("https://10fastfingers.com/login")

        self.root = tk
        self.root.title("Lightning Fingers")
        # self.root.iconbitmap("lightning_fingers.ico")

        self.mode_state = IntVar()
        self.output_text = StringVar()
        self.output_text.set("ᕦ( ͡° ͜ʖ ͡°)ᕤ")

        Seperator_Label = Label(self.root, text="______________________________________________________________")
        Seperator_Label.grid(row=4, column=1, columnspan=3, pady=5)

        Output_Label = Label(self.root, textvariable=self.output_text, font="Arial 10 bold", pady=15)
        Output_Label.grid(row=5, column=1, columnspan=3)

        frame0 = LabelFrame(self.root, text="Failure Rate (%)", padx=5, pady=5)
        frame0.grid(row=1, column=3, padx=20, pady=5, columnspan=1)

        frame = LabelFrame(self.root, text="Normal", padx=5, pady=5)
        frame.grid(row=2, column=2, padx=20, pady=5)

        frame2 = LabelFrame(self.root, text="Typing Speed (wpm)", padx=5, pady=5)
        frame2.grid(row=1, column=1, padx=20, pady=20, columnspan=2)

        frame3 = LabelFrame(self.root, text="Anti-Anticheat", padx=5, pady=5)
        frame3.grid(row=2, column=3, padx=20, pady=20)

        frame4 = LabelFrame(self.root, text="Multiplayer ;)", padx=5, pady=5)
        frame4.grid(row=2, column=1, padx=20, pady=20)

        frame5 = LabelFrame(self.root, text="Stat Creator", padx=5, pady=5)
        frame5.grid(row=3, column=2, padx=20, pady=20)

        frame7 = LabelFrame(self.root, text="Modes", padx=5, pady=5)
        frame7.grid(row=3, column=1, padx=20, pady=20)

        Entry_Words = Entry(frame2, width=40, borderwidth=5, fg="purple")
        Entry_Words.insert(0, 100)
        Entry_Words.grid(row=1, column=2, columnspan=3)

        Entry_FR = Entry(frame0, width=10, borderwidth=5, fg="purple")
        Entry_FR.insert(0, 5)
        Entry_FR.grid(row=1, column=2, columnspan=3)

        Entry_num_Games = Entry(frame5, width=10, borderwidth=5, fg="purple")
        Entry_num_Games.insert(0, 20)
        Entry_num_Games.grid(row=1, column=2)

        Start_Button = Button(frame, text="GO!", font="Arial 20 bold", fg="green",
                              command=lambda: spawn_as_thread(self.writer, {"wpm": Entry_Words.get(),
                                                                                "input": XPATHS.normal_ip,
                                                                                "resource": XPATHS.normal_resource,
                                                                                "failure_rate": int(Entry_FR.get()),
                                                                                "mode": int(self.mode_state.get())}))
        Start_Button.grid(row=2, column=2)

        Anti_Button = Button(frame3, text="GO!", font="Arial 10 bold", fg="red", padx=20,
                             command=lambda: spawn_as_thread(self.trick_anticheat, {"wpm": int(Entry_Words.get()),
                                                                                        "mode": int(
                                                                                            self.mode_state.get())}))
        Anti_Button.grid(row=3, column=2)

        Challenge_Button = Button(frame4, text="GO!", font="Arial 10 bold", fg="red", padx=20,
                                  command=lambda: spawn_as_thread(self.writer, {"wpm": Entry_Words.get(),
                                                                                    "input": XPATHS.challenge_ip,
                                                                                    "resource": XPATHS.challenge_resource,
                                                                                    "challenge_mode": True,
                                                                                    "failure_rate": int(Entry_FR.get()),
                                                                                    "mode": int(
                                                                                        self.mode_state.get())}))
        Challenge_Button.grid(row=2, column=1)

        Stat_Button = Button(frame5, text="GO!", font="Arial 10 bold", fg="red", padx=20,
                             command=lambda: spawn_as_thread(self.stat_creator, {"wpm": int(Entry_Words.get()),
                                                                                     "num_games": int(
                                                                                         Entry_num_Games.get()),
                                                                                     "fr_rate": int(Entry_FR.get())}))
        Stat_Button.grid(row=3, column=2)

        Stop_Button = Button(self.root, text="STOP", font="Arial 10 bold", fg="red", padx=20,
                             command=lambda: self.stop())
        Stop_Button.grid(row=5, column=3)

        Chk_Box = Checkbutton(frame7, text="Rage Mode", variable=self.mode_state, onvalue=3, offvalue=4)
        Chk_Box.grid(row=3, column=1)

        Chk_Box1 = Checkbutton(frame7, text="Dynamic Mode", variable=self.mode_state, onvalue=2, offvalue=5)
        Chk_Box1.select()
        Chk_Box1.grid(row=4, column=1)

        Chk_Box2 = Checkbutton(frame7, text="Standard Mode", variable=self.mode_state, onvalue=1, offvalue=6)
        Chk_Box2.grid(row=5, column=1)

    def stop(self):
        """kinda speaks for itself"""
        self.root.quit()
        self.driver.delete_all_cookies()
        self.driver.close()
        sys.exit(0)

    def update_output_label(self, message, pause):
        """refreshes the output layer using 'value',
         min delay between refreshes is defines with 'pause' """

        self.output_text.set(25 * " " + message + " " * 25)
        time.sleep(pause)
        root.update_idletasks()

    def trick_anticheat(self, wpm, mode):
        """utilizes tesseract to extract text from images
        gather -> process -> input """

        self.update_output_label("calling trick_anticheat..", 0.25)

        try:
            input_box = self.driver.find_element(By.XPATH, XPATHS.anticheat_ip)
            img = self.driver.find_element(By.XPATH, XPATHS.anticheat_resource)
        except NoSuchElementException:
            img = None
            input_box = None
            self.update_output_label("oops sth went wrong...", 1)
            print("encountered error, please retry")

        img.screenshot("pic.png")
        time.sleep(0.09 + micro_delay())
        input_box.send_keys(Keys.TAB, Keys.ENTER)
        time.sleep(0.09 + micro_delay())

        string = pytesseract.image_to_string('pic.png')
        word_lst = string.split()
        time_per_word = len(word_lst) / wpm

        if mode == 3:
            for word in word_lst:
                for letter in word:
                    input_box.send_keys(letter)
                input_box.send_keys(Keys.SPACE)

        else:
            for word in word_lst:
                self.update_output_label("word: " + str(word), 0)
                time_per_letter = time_per_word / len(word)
                for letter in word:
                    delay = micro_delay()
                    time.sleep((time_per_letter + delay))
                    input_box.send_keys(letter)
                input_box.send_keys(Keys.SPACE)
                time.sleep(micro_delay())

        time.sleep(0.246)
        input_box.send_keys(Keys.TAB, Keys.ENTER)

    def stat_creator(self, wpm, num_games, fr_rate):
        """Takes user Inputs: words, num_games and pause
        Calls writer funtion times num_games to create legit looking statistics"""

        self.update_output_label("calling stat_creator..", 0.15)

        start_wpm = wpm / 3
        delta_wpm = wpm - start_wpm
        gain_per_game = delta_wpm / num_games
        wpm = start_wpm
        percentage = [x for x in range(100)]

        for g in range(num_games):

            self.update_output_label("starting game:" + str(g), 0.25)
            pause = safety_delay()
            chance = random.choice(percentage)

            # 10 chance for temporary heavy decrease
            if chance <= 10:
                temp_wpm = wpm / random.choice([2, 2.5, 1.5, 3])
                self.writer(wpm=temp_wpm, failure_rate=fr_rate, input=XPATHS.normal_ip, resource=XPATHS.normal_resource,
                            mode=2)
                self.reload()
                time.sleep(pause + micro_delay())

            # 40% chance for temporary gain or loss
            elif 10 < chance <= 50:
                temp_wpm = wpm + random.choice([-25, 9, -22, 5, -10])
                self.writer(wpm=temp_wpm, failure_rate=fr_rate, input=XPATHS.normal_ip, resource=XPATHS.normal_resource,
                            mode=2)
                time.sleep(pause + micro_delay())
                self.reload()
                time.sleep(pause + micro_delay())

            # 50% chance for permanent increase
            else:
                wpm = wpm + gain_per_game * 2
                self.writer(wpm=wpm, failure_rate=fr_rate, input=XPATHS.normal_ip, resource=XPATHS.normal_resource,
                            mode=2)
                time.sleep(pause + micro_delay())
                self.reload()
                time.sleep(pause + micro_delay())

    def writer(self, wpm, failure_rate, input="", resource="", challenge_mode=False, mode=0):
        """the writer is the hearth of the programm.
        it has three modes: which can be set via var: 'optional' """

        try:

            alrdy_written = 0
            start_time = 0

            input_box = self.driver.find_element(By.XPATH, input)
            time_per_word = 60 / int(wpm)

            self.update_output_label("calling writer..", 0.15)

            # rage mode (no delays or mistakes)
            if mode == 3:
                self.update_output_label("typing...fast ;)", 0)
                for i in range(1, int(wpm)):

                    try:
                        data = self.driver.find_element(By.XPATH, resource + str(i) + ']')
                        word = data.text
                    except NoSuchElementException:
                        break

                    input_box.send_keys(word)
                    input_box.send_keys(Keys.SPACE)

            # legit mode (delays and mistakes)
            else:
                apprx_keystrokes = int(wpm) * 6
                wrong_apprx_keystrokes = math.ceil(((failure_rate / 2) / 100) * apprx_keystrokes)
                wrong_apprx_words = math.ceil((2 * (failure_rate / 2)) / 100 * wrong_apprx_keystrokes) * 4

                self.update_output_label("predicted keystrokes: " + str(apprx_keystrokes), 0.5)
                self.update_output_label("predicted false keystrokes: " + str(wrong_apprx_words), 0.5)
                self.update_output_label("predicted wrong words: " + str(wrong_apprx_words), 0.5)

                # starts timer at the beginning
                if alrdy_written == 0:
                    start_time = time.perf_counter()

                # loops over the number of words
                for i in range(1, int(wpm)):

                    # dynamic mode calculates tpl based on time left
                    if mode == 2:
                        time_left = 60 - (time.perf_counter() - start_time)
                        time_per_word = time_left / (int(wpm) - alrdy_written)
                    try:
                        data = self.driver.find_element(By.XPATH, resource + str(i) + ']')
                        word = data.text
                    except NoSuchElementException:
                        break

                    len_word = len(word)
                    # calculate tpl based on lenght of the word
                    try:
                        # speeds it up at first
                        time_per_letter = time_per_word / len_word
                        if alrdy_written < (int(wpm) / 2):
                            time_per_letter *= 0.8

                        # chooses tpl based on word lenght
                        if len_word <= 4:
                            time_per_letter *= 0.4
                        if len_word >= 5:
                            time_per_letter *= 1.13
                    except ZeroDivisionError as err:
                        print(err)
                        break
                    # rolls a dice for further decisions
                    for letter in word:
                        chance = random.choice(range(1, apprx_keystrokes))
                        # decide for mistakes
                        if chance <= wrong_apprx_keystrokes:
                            self.update_output_label("error...", 0.1)
                            # decide for double letter mistake
                            if random.choice(range(1, 5)) > 4:
                                time.sleep(time_per_letter)
                                input_box.send_keys(letter)
                                time.sleep(time_per_letter)
                                input_box.send_keys(letter)
                            else:
                                # picks wrong letter
                                try:
                                    wrong_letter = random.choice(TYPO_DICT[letter])
                                except KeyError as err:
                                    print(err)
                                    continue
                                time.sleep(time_per_letter)
                                input_box.send_keys(wrong_letter)
                            # enters correction mode (or not)
                            if challenge_mode is False:
                                # decides for correction
                                if chance > wrong_apprx_words:
                                    self.update_output_label("correcting...", 0.1)

                                    time.sleep(0.316)
                                    input_box.send_keys(Keys.BACKSPACE)
                                    time.sleep(time_per_letter / 2)
                                    input_box.send_keys(letter)
                            else:
                                self.update_output_label("correcting...", 0.1)
                                time.sleep(0.316)
                                input_box.send_keys(Keys.BACKSPACE)
                                input_box.send_keys(letter)
                        else:
                            self.update_output_label("typing...", 0)
                            time.sleep(time_per_letter)
                            input_box.send_keys(letter)
                    input_box.send_keys(Keys.SPACE)
                    alrdy_written += 1
        except UnexpectedAlertPresentException as err:
            print(err)
            pass

    def reload(self):
        """clicks the reload button in normal mode
        using resources defined in main"""

        time.sleep(safety_delay())
        self.driver.find_element(By.XPATH, XPATHS.rld_bttn).click()


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
