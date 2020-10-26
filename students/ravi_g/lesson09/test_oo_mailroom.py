#!/usr/bin/env python


import pytest
from donor_models import *
import os

n_donor = Donor('Mary M', [500,100,200])
d = DonorCollection()

d.new_donor(n_donor)


def test_new_donors():
    """ Checks if new donor object is added appropriately """
    assert n_donor.name == "Mary M"
    assert n_donor.donation == [500,100,200]

    # checks if donation can be input as list only
    with pytest.raises(TypeError):
        Donor("Jess J", 1) # single entry

    with pytest.raises(TypeError):
        Donor("Jess J", '1') # string type entry for donation

    with pytest.raises(TypeError):
        Donor("Jess J", (1,2,3)) # tuple type entry for donation
    



def test_add_existing_donor():
    """ checks if new donation amount can be added for an existing donor """

    # add to Mary M donation
    n_donor.add_donation(50.0)
    assert n_donor.donation == [500,100,200, 50.0]

    with pytest.raises(TypeError):
        n_donor.add_donation('test') # string type entry

    with pytest.raises(TypeError):
        n_donor.add_donation([1,2,3]) # list type entry
    

    # checks if new donor, Mary M, is indeed added to donor list
    assert d.donorlst[0].name == 'Mary M'
    assert d.donorlst[0].donation == [500,100,200, 50.0]


def test_report():
    """ checks report content """

    # Mary M is correctly listed
    assert d.donors_listing() == "Mary M"

    # report consists of entry for Mary M
    report = d.report_content()
    assert report == [('Mary M', 850.0, 4, 212.5)]

    
def test_emails():
    """ checks email content """
    email_txt = d.email_text(n_donor.name)
    assert email_txt == 'Dear Mary M:\n Thank you for your donation of $850.00.'

    # checks file existance
    filename1 = r"C:/Users/ravigant/UW_Python/Mary M/20201025.txt"
    assert os.path.isfile(filename1)
