import os
from datetime import datetime
from operator import itemgetter

class Donor():

    def __init__(self, donor_name, donation_amt=[]):
        """
        Set donor name and adds donation amount
        :param donor_name: str
        :param donation_amt: float
        """

        self.name = donor_name
        if isinstance(donation_amt, list):
            self.donation = donation_amt
        else:
            raise TypeError("Invalid input, donations must be provided in a list")


    def add_donation(self, new_donation):
        """
        Adds a new donation
        :param new_donation: int or float
        """
        if isinstance(new_donation, int) or isinstance(new_donation, float):
            self.donation.append(new_donation)
        else:
            raise TypeError("Invalid input, donations must be a number")

class DonorCollection():

    def __init__(self):
        """
        Listing of donors
        """
        self.donorlst = []

    def new_donor(self, donor: Donor):
        """
        Adds a new donor object
        :param donor: Donor
        :return: null
        """
        self.donorlst.append(donor)

    def enchance_donations(self, name, donation):
        """
        Adds new donation for an existing donor or adds a new donor
        :param name: str
        :param donation: float or int
        :return: null
        """
        for donor in self.donorlst:
            if donor.name == name.title():
                donor.add_donation(donation)
                return
        new_donor = Donor(name.title(), [donation])
        self.new_donor(new_donor)

    def email_text(self, name):
        """
        Compose and return a email thank you text, writes to drive
        :param name: str
        :return: str
        """
        for donor in self.donorlst:
            if donor.name.lower() == name.lower():
                email_text = f'Dear {donor.name}:\n Thank you for your donation of ${sum(donor.donation):.2f}.'
                filename1 = r"C:/Users/ravigant/UW_Python/" + donor.name + "/"
                if not os.path.exists(filename1):
                    os.makedirs(filename1)
                    f = open(((filename1 + str(datetime.now().strftime("%Y%m%d")) + '.txt')), 'w')
                    f.write(email_text)
                    f.close()
                return email_text

    def email_donors(self):
        """
        Writes to all donors
        :return: null
        """
        for donor in self.donorlst:
            self.email_text(donor.name)

    def donors_listing(self):
        """
        generates a list of donors
        :return: listing of donors
        """
        donors = []
        for donor in self.donorlst:
            donors.append(donor.name)
        return " ".join(donors)

    def report_content(self):
        """
        Builds report metrics like avg donation, total number of donations
        :return: list
        """
        report_metrics = []
        for donor in self.donorlst:
            report_metrics.append((donor.name, sum(donor.donation), len(donor.donation), (sum(donor.donation)/len(donor.donation))))
        sorted_report = sorted(report_metrics, key = itemgetter(1), reverse=True)
        return sorted_report
