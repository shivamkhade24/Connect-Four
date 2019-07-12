import os
import pickle
from random import randint
from tkinter import *

import time

from Board import Board


class GUI:

    turn = 0
    winner = -1

    def __init__(self, player1, player2):
        self.board = 0
        self.player1 = player1
        self.player2 = player2
        self.root = Tk()
        self.root.wm_title("Connect4 - Jay Cross")

        self.player1_color = "blue"
        self.player2_color = "red"

        self.initialize_setup_frame()

    def initialization(self):
        self.game_play_frame = Frame(self.root)
        self.game_play_frame.pack(side=LEFT)

        self.menu_frame = Frame(self.root)
        self.menu_frame.pack(side=RIGHT)

        self.grid_frame = Frame(self.game_play_frame)
        self.grid_frame.pack(side=TOP)

        self.divider_frame = Frame(self.game_play_frame)
        self.divider_frame.pack(side=TOP)

        self.buttons_frame = Frame(self.game_play_frame)
        self.buttons_frame.pack(side=TOP)

        self.restart_button = Button(self.menu_frame, text='Restart', background="white", command=lambda: self.restart_game())
        self.restart_button.pack(side=TOP)

        self.save_exit_btton = Button(self.menu_frame, text='Save and Exit', background="white",
                                     command=lambda: self.save_exit())
        self.save_exit_btton.pack(side=TOP)

        # initialize the board buttons
        self.board_buttons_array = [[0 for x in range(self.board.get_rows() + 1)] for y in
                                       range(self.board.get_columns() + 1)]

        self.turn = 0

        for y in range(self.board.get_rows()):
            for x in range(self.board.get_columns()):
                b = Button(self.grid_frame, text=' ', background="white", width=4, height=2)
                b.grid(row=y, column=x)
                self.board_buttons_array[x][y] = b

        # initialize divider
        divider = Label(self.divider_frame, text='\n')
        divider.pack(side=TOP)

        # initialize columns button selection row
        self.columns_button_array = [0 for x in range(self.board.get_columns() + 1)]

        for i in range(self.board.get_columns()):
            b = Button(self.buttons_frame, text='Col ' + str(i), command=lambda col=i: self.place_disk_on_column(col), background="white", width=4, height=2)
            b.grid(row=0, column=i)
            self.columns_button_array[i] = b

        self.refresh_grid()



    def initialize_setup_frame(self):

        self.player1_color = "blue"
        self.player2_color = "red"

        self.winner = -1

        self.setup_frame = Frame(self.root)
        self.setup_frame.pack(side=LEFT)

        self.color_selection_frame = Frame(self.setup_frame)
        self.color_selection_frame.pack(side=TOP)

        self.grid_selection_frame = Frame(self.setup_frame)
        self.grid_selection_frame.pack(side=TOP)


        # player 1 selection frame
        self.player1_setup_frame = Frame(self.color_selection_frame)
        self.player1_setup_frame.pack(side=TOP)

        self.player1_color_label = Label(self.player1_setup_frame, text="Player 1 color:")
        self.player1_color_label.pack(side=TOP)

        divider1 = Label(self.player1_setup_frame, text=" Selection: ")
        divider1.pack(side=LEFT)

        self.b1_selection = Button(self.player1_setup_frame, text=' ', background="white", width=2, height=1)
        self.b1_selection.pack(side=LEFT)

        divider1 = Label(self.player1_setup_frame, text="    ")
        divider1.pack(side=LEFT)

        b10 = Button(self.player1_setup_frame, text=' ', background="red", command=lambda: self.setup_color_selection_player1("red"),width=2, height=1)
        b10.pack(side=LEFT)
        b11 = Button(self.player1_setup_frame, text=' ', background="black",command=lambda: self.setup_color_selection_player1("black"), width=2, height=1)
        b11.pack(side=LEFT)
        b12 = Button(self.player1_setup_frame, text=' ', background="purple", command=lambda: self.setup_color_selection_player1("purple"), width=2, height=1)
        b12.pack(side=LEFT)

        # select computer versus frame
        self.computer_versus_setup_frame = Frame(self.color_selection_frame)
        self.computer_versus_setup_frame.pack(side=TOP)

        self.play_vs_computer_player1 = BooleanVar()
        self.player_vs_comp_checkbox = Checkbutton(self.computer_versus_setup_frame, text="Player 1 is computer:",
                                                   onvalue=True, offvalue=False, variable=self.play_vs_computer_player1)
        self.player_vs_comp_checkbox.pack()

        # player 2 selection frame
        self.player2_setup_frame = Frame(self.color_selection_frame)
        self.player2_setup_frame.pack(side=TOP)

        self.player2_color_label = Label(self.player2_setup_frame, text="Player 2 color:")
        self.player2_color_label.pack(side=TOP)

        self.divider2 = Label(self.player2_setup_frame, text=" Selection: ")
        self.divider2.pack(side=LEFT)

        self.b2_selection = Button(self.player2_setup_frame, text=' ', background="white", width=2, height=1)
        self.b2_selection.pack(side=LEFT)

        divider1 = Label(self.player2_setup_frame, text="    ")
        divider1.pack(side=LEFT)

        b20 = Button(self.player2_setup_frame, text=' ', background="blue", command=lambda: self.setup_color_selection_player2("blue"), width=2, height=1)
        b20.pack(side=LEFT)
        b21 = Button(self.player2_setup_frame, text=' ', background="green", command=lambda: self.setup_color_selection_player2("green"), width=2, height=1)
        b21.pack(side=LEFT)
        b22 = Button(self.player2_setup_frame, text=' ', background="yellow", command=lambda: self.setup_color_selection_player2("yellow"), width=2, height=1)
        b22.pack(side=LEFT)

        # select computer versus frame
        self.computer_versus_setup_frame = Frame(self.color_selection_frame)
        self.computer_versus_setup_frame.pack(side=TOP)

        self.play_vs_computer_player2 = BooleanVar()
        self.player_vs_comp_checkbox = Checkbutton(self.computer_versus_setup_frame, text="Player 2 is computer:",
                                                   onvalue=True, offvalue=False,variable=self.play_vs_computer_player2)
        self.player_vs_comp_checkbox.pack()


        # grid frame
        self.grid_size_label = Label(self.grid_selection_frame, text="Grid Size")
        self.grid_size_label.pack(side=TOP)


        self.grid_size_label_rows = Label(self.grid_selection_frame, text="ROWS")
        self.grid_size_label_rows.pack(side=TOP)
        rows = IntVar()
        entry_rows = Entry(self.grid_selection_frame, textvariable=rows)
        entry_rows.pack(side=TOP)
        rows.set(7)

        self.grid_size_label_col = Label(self.grid_selection_frame, text="COLUMNS")
        self.grid_size_label_col.pack(side=TOP)
        cols = IntVar()
        entry_col = Entry(self.grid_selection_frame, textvariable=cols)
        entry_col.pack(side=TOP)
        cols.set(6)

        start_button = Button(self.grid_selection_frame, text='START', background="WHITE", command=lambda: self.start_game(entry_rows.get(), entry_col.get()))
        start_button.pack(side=TOP)

        load_start = Button(self.grid_selection_frame, text='LOAD AND START', background="WHITE",
                              command=lambda: self.loat_start_game())
        load_start.pack(side=TOP)

        self.root.mainloop()

    def setup_color_selection_player1(self, color):
        self.b1_selection['bg'] = color
        self.player1_color = color

    def setup_color_selection_player2(self, color):
        self.b2_selection['bg'] = color
        self.player2_color = color

    def place_disk_on_column(self, col):

        print("BUTTON PRESSED")
        if self.winner == -1 and not self.board.check_if_board_full():
            # player vs player case
            if not self.play_vs_computer_player1.get() and not self.play_vs_computer_player2.get():
                if self.turn % 2 == 0:
                    self.board.put_disk_on_column(col, self.player1.get_player_number())
                    self.winner = self.board.check_for_winner(self.player1)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Player 2 wins!")
                    self.turn += 1
                else:
                    self.board.put_disk_on_column(col, self.player2.get_player_number())
                    self.winner = self.board.check_for_winner(self.player2)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Player 2 wins!")
                    self.turn += 1

            # player vs computer
            if not self.play_vs_computer_player1.get() and self.play_vs_computer_player2.get():
                if self.turn % 2 == 0:
                    self.board.put_disk_on_column(col, self.player1.get_player_number())
                    self.winner = self.board.check_for_winner(self.player1)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Player 1 wins!")

                    time.sleep(0.5)  # delays for 0.2sec
                    # computer move
                    temp_col = randint(0, self.board.get_columns() - 1)
                    self.board.put_disk_on_column(temp_col, self.player2.get_player_number())
                    self.winner = self.board.check_for_winner(self.player2)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Computer 2 wins!")

            # computer vs player
            if self.play_vs_computer_player1.get() and not self.play_vs_computer_player2.get():
                if self.turn % 2 == 0:
                    time.sleep(0.5)  # delays for 0.2sec

                    temp_col = randint(0, self.board.get_columns()-1)
                    self.board.put_disk_on_column(temp_col, self.player1.get_player_number())
                    self.winner = self.board.check_for_winner(self.player1)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Computer 1 wins!")
                    self.turn += 1
                else:
                    self.board.put_disk_on_column(col, self.player2.get_player_number())
                    self.winner = self.board.check_for_winner(self.player2)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Player 2 wins!")

                    time.sleep(0.5)  # delays for 0.2sec

                    temp_col = randint(0, self.board.get_columns())
                    self.board.put_disk_on_column(temp_col, self.player1.get_player_number())
                    self.winner = self.board.check_for_winner(self.player1)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Computer 1 wins!")


            # compute vs computer
            if self.play_vs_computer_player1.get() and self.play_vs_computer_player2.get():
                if not self.board.check_if_board_full():
                    time.sleep(0.1)  # delays for 0.2sec

                    temp_col = randint(0, self.board.get_columns()-1)
                    self.board.put_disk_on_column(temp_col, self.player1.get_player_number())
                    self.winner = self.board.check_for_winner(self.player1)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Computer 1 wins!")
                        return

                    time.sleep(0.1)  # delays for 0.2sec

                    temp_col = randint(0, self.board.get_columns())
                    self.board.put_disk_on_column(temp_col, self.player2.get_player_number())
                    self.winner = self.board.check_for_winner(self.player2)
                    self.refresh_grid()
                    if self.winner != -1:
                        self.popup_message("Computer 2 wins!")
                    return


    def start_game(self, rows, col):

        self.destroy_setup_frame()

        self.board = Board(int(rows), int(col))
        self.board.print_grid()

        self.initialization()
        print(str(self.play_vs_computer_player1.get()) + ' ' + str(self.play_vs_computer_player2.get()))
        if self.play_vs_computer_player1.get():
            self.place_disk_on_column(0)

        if self.play_vs_computer_player1.get() and self.play_vs_computer_player2.get():
            while self.board.check_for_winner(self.player1) == -1 or self.board.check_for_winner(self.player2) == -1:
                self.place_disk_on_column(0)

    def loat_start_game(self):
        file_name = "last_session.txt"
        file_path = os.path.join(sys.path[0], file_name)

        file = open(os.path.join(sys.path[0], file_name), "r")

        with open(file_path, 'rb') as fp:
            itemlist = pickle.load(fp)

        print(itemlist)

        board = Board(len(itemlist[0]), len(itemlist))
        board.set_board(itemlist)
        self.board = board

        board.print_grid()

        self.destroy_setup_frame()

        self.initialization()
        print(str(self.play_vs_computer_player1.get()) + ' ' + str(self.play_vs_computer_player2.get()))
        if self.play_vs_computer_player1.get():
            self.place_disk_on_column(0)

        if self.play_vs_computer_player1.get() and self.play_vs_computer_player2.get():
            while self.board.check_for_winner(self.player1) == -1 or self.board.check_for_winner(self.player2) == -1:
                self.place_disk_on_column(0)

    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def save_exit(self):

        file_name = "last_session.txt"
        file_path = os.path.join(sys.path[0], file_name)

        #file = open(file_path, "w")
        #file.write(str(self.board.get_board()))

        with open(file_path, 'wb') as fp:
            pickle.dump(self.board.get_board(), fp)

        #file.close()

        self.root.destroy()

    def restart_game(self):
        self.game_play_frame.destroy()
        self.menu_frame.destroy()
        self.initialize_setup_frame()

    def destroy_setup_frame(self):
        self.setup_frame.destroy()
        self.player1_setup_frame.destroy()
        self.player2_setup_frame.destroy()
        self.grid_selection_frame.destroy()

    def refresh_grid(self):
        for y in range(self.board.get_rows()):
            for x in range(self.board.get_columns()):
                if self.board.get_board_info_at_pos(x, y) == 1:
                    self.board_buttons_array[x][y]['bg'] = self.player1_color
                if self.board.get_board_info_at_pos(x, y) == 2:
                    self.board_buttons_array[x][y]['bg'] = self.player2_color

        self.board.print_grid()

    def popup_message(self, msg):
        popup = Tk()
        label = Label(popup, text=msg,)
        label.pack(side="top")
        b1 = Button(popup, text="Okay!", command=popup.destroy)
        b1.pack()
        popup.mainloop()
