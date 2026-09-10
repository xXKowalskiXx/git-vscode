import sys
import os.path
import pytest
import random
from assignment import main
from mock_input_tests import *

def check_if_file_exists():
    try:
        exists = os.path.exists("assignment.py")
        assert exists == True
    except:
        sys.exit()

def test_hat():
    check_if_file_exists()
    
    # Testing > 20 C
    set_keyboard_input([random.randint(68, 100)])
    main()
    output = get_display_output()

    assert output == [
        "What is the temperature outside: ",
        "\nWear a hat",
        ]

def test_light_jacket():
    check_if_file_exists()
    
    # Testing > 20 C
    set_keyboard_input([random.randint(50, 67)])
    main()
    output = get_display_output()

    assert output == [
        "What is the temperature outside: ",
        "\nWear a light jacket",
        ]

def test_heavy_jacket():
    check_if_file_exists()
    
    # Testing > 20 C
    # Random number from 32 to 49
    set_keyboard_input([random.randint(32, 49)])
    main()
    output = get_display_output()

    assert output == [
        "What is the temperature outside: ",
        "\nWear a heavy jacket",
        ]
    
    