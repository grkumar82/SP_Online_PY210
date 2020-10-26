#!/usr/bin/env python

import os
from donor_models import Donor, DonorCollection
import sys


# initialize with a set of donors
donors_db = [
Donor('Adam A', [100, 200]),
Donor('Betty', [100, 200, 200]),
Donor('Carl C', [100]),
Donor('Ed E', [50, 100, 25]),
Donor('Frank F', [50])
]

donors_dict = DonorCollection()
for donor in donors_db:
    donors_dict.new_donor(donor)

def quit_function():
    """
    This function terminates the program.
    """
    exit()

def default():
    """
    This function prompts user of invalid entry and asks for re-entry. Returns control back to program.
    """
    print('************************************************************')
    print('Incorrect input. Select from given menu items and try again!')
    print('************************************************************')
    return

def report():
    """
    This function prints neatly formatted report. Returns control back to program.
    """
    print('Donor Name'.ljust(20, " "), 'Total Given'.ljust(15, " "), 'Num Gifts'.ljust(10, " "),
          "Average Gift".ljust(10, " "))
    report = donors_dict.report_content()
    for name, total_given, num_gifts, avg_gift in report:
        total_given = str('{:.2f}'.format(total_given))
        num_gifts = str(num_gifts)
        avg_gift = str('{:.2f}'.format(avg_gift))
        print(name.ljust(20, " "),total_given.ljust(15, " "), num_gifts.ljust(10, " "), avg_gift.ljust(10, " "))
    return


def thanks():
    """
    This function requests user to enter a donation amount and send a thank you note.
    """
    try:
        name_to_thank = input("Name of the donor who you would like to send thank you note ")
    except ValueError: # if user enters non-string value
        print("Invalid input, input donor name to thank. ")
    if name_to_thank.lower() == 'quit':
        return
    if name_to_thank.lower() == 'list': # listing of donors
        print("Here are current list of donors: ")
        print(donors_dict.donors_listing())
        name_to_thank = input("Name of the donor who you would like to send thank you note ")
        if name_to_thank.lower() == 'quit':
            return
    while 1:
        try:
            donating_amt = float(input("Enter amount to donate: "))
        except ValueError:
            if donating_amt.lower() == 'quit':
                return
            donating_amt = float(input('Invalid input, enter amount to donate: '))
        else:
            break

    donors_dict.enchance_donations(name_to_thank, donating_amt)
    donors_dict.email_text(name_to_thank)

def letters():
    """
    This function writes to local drive a thank you note to donors.
    Returns control back to program.
    """
    donors_dict.email_donors()

if __name__ == '__main__':

    print(
        '''Welcome to donor program! You can add new donors or add donations to existing donors or 
print report about donations till date or send thank you letters to donors.''')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
    # menu items for user to select
    options = {'Thanks': thanks, 'Report': report, 'Letters': letters, 'Quit': quit_function}
    while 1:
        request = input(
            'Choose from following four items only. If you enter anything invalid, system will prompt for re-entry: \n'
            'input \'Thanks\' to send a thank you \n'
            'input \'Letters\' to send letters \n'
            'input \'Report\' to create a report \n'
            'input \'Quit\' to quit'
            '\n')

        try:  # any entry other than noted ones will result error
            options[request]()
        except KeyError:
            default()
