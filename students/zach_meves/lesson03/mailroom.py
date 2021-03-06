#!/usr/bin/env python3

"""
mailroom.py

Zach Meves
Python 210
Lesson 03 Assignment

Mailroom Project Part 1
"""

# Initialize donors
_donors = [("Hans Zimmer", [1200, 20, 340]),
           ("Bill Boeing", [30, 75]),
           ("Homer Simpson", [1]),
           ("Fred Flintstone", [100]),
           ("Will Smith", [50, 125])]
# List of tuples containing donor information. First element of each tuple is name, second is list
# of donation amounts

_quit_responses = ('q', 'quit')  # Responses to interpret as a "quit" command


def _get_input(prompt, options, allow_new=False, reprompt_options=None):
    """For internal use only.

    Get user input and match the lowercase version to a list of options. Optionally restrict that
    input must be one of a few possible responses.

    Parameters
    ----------
    prompt : str
        Prompt to display
    options : sequence
        Sequence of valid response options
    allow_new : bool, optional
        If ``True``, allow responses that are not in the list of options
        If ``False``, re-prompt if a non-option given
    reprompt_options : sequence, optional
        Subset of given ``options`` that will be displayed to prompt user to enter a valid response,
        if not all entries of ``options`` should be shown.

    Returns
    -------
    str
        Input, matched to case of provided option if applicable"""

    _lwr_opts = [x.lower() for x in options]
    if reprompt_options is None:
        reprompt_options = options

    while True:
        _resp = input(prompt).strip()

        # Check that input is one of the options
        try:
            i = _lwr_opts.index(_resp.lower())
            return options[i]
        except ValueError:
            if not allow_new:
                print(f'Response must be one of the following: {", ".join(reprompt_options)}')

        if allow_new and _resp:  # If have a non-empty string
            return _resp


def _request_donation():
    """Requests a donation amount.

    Returns
    -------
    float or None
        Donation amount, or None if 'quit' requested
    """

    amt = _get_input("Enter a donation amount:\n> ", _quit_responses, allow_new=True)
    if amt in _quit_responses:
        return
    else:
        return float(amt)


def _compose_thank_you(name):
    """Compose a thank you note to a donor with the given name.

    Parameters
    ----------
    name : str
        Full name of donor, must be one of the existing donors

    Returns
    -------
    str
        Thank you note
    """

    for donor in _donors:
        if donor[0] == name:
            return (f"Dear {name},\n" +
                    f"    Thank you very much for your recent donation of $ {donor[1][-1]:.2f}. We truly \n" +
                    f"appreciate your contribution.\n\n    Your total tax-deductible donation amount is now " +
                    f"$ {sum(donor[1]):.2f}.\n\n" +
                    f"Sincerely,\n" +
                    f"    Zach")

    else:
        raise NameError(f"No donor with name {name} is present in data")


def _print_donors():
    """Prints list of donors."""
    print('Current donors: ' + ', '.join(_get_donor_names()))


def _get_donor_names():
    """Returns tuple of donor names."""
    return tuple(x[0] for x in _donors)


def send_thank_you():
    """Send a thank you note to a donor."""

    # Prompt user for a name
    name = ''
    while True:
        name = _get_input("Enter a full name (or 'list' to list the donors):\n> ",
                          _get_donor_names() + ('list',) + _quit_responses, allow_new=True)
        if name == 'list':
            _print_donors()
        else:  # Won't prompt again unless 'list' is entered
            # If quit, return to calling function
            if name in _quit_responses:
                return
            break  # Break out of while loop if a name entered

    # Request a donation amount
    amt = _request_donation()
    if amt is None:  # Return to calling function if quit
        return

    # Find requested donor
    for donor in _donors:
        if donor[0] == name:
            donor[1].append(amt)
            break
    else:  # If did not find donor
        _donors.append((name, [amt]))

    # Print thank you note
    print('\n')
    print(_compose_thank_you(name))
    print('\n')


def create_report():
    """Create a report of donations. Prints report and returns the value.

    Returns
    -------
    str
        Report"""

    # Sort by total donation amount
    _donors.sort(key=lambda x: -sum(x[1]))

    # Generate the report
    _str_ = ["Donor Name                | Total Given | Num Gifts | Average Gift\n" +
             "------------------------------------------------------------------"]
    for donor in _donors:
        sm = sum(donor[1])
        l = len(donor[1])
        _str_.append(f"{donor[0]:<25}   $ {sm:>9.2f}   {l:>9d}   $ {sm / l:>10.2f}")

    report = '\n'.join(_str_)
    print(report)
    return report


if __name__ == '__main__':
    """Main Mailroom Executable."""

    _thankyou_responses = ('1', 'thank you', 'thankyou', 'send a thank you')
    _report_responses = ('2', 'report', 'create a report')

    # Print intro
    print("\nWelcome to the Mailroom Program!\n")
    print("To quit the program, or return to the previous menu at any time, enter 'q' or 'quit'.\n")
    while True:
        response = _get_input("Select from the following options:\n"
                              " 1 - Send a Thank You\n"
                              " 2 - Create a Report\n"
                              " q - Quit\n"
                              "> ",
                              _thankyou_responses + _report_responses + _quit_responses, allow_new=False,
                              reprompt_options=('1', '2', 'q'))

        if response in _thankyou_responses:
            send_thank_you()
        elif response in _report_responses:
            print('')
            create_report()
            print('')
        elif response in _quit_responses:
            exit()
        else:
            raise RuntimeError("Internal error occurred")



