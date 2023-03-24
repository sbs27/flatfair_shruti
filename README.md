
# Flatfair Coding Challenge

The following repository includes my submission for the flatfair coding assessment for junior software engineer role.


## Description

This repository involves a function that computes the membership fee for an organization unit, taking into account its rental amount and period. The fee is determined using the rental amount **(in pence)**, rental period **(either "month" or "week")**, and the configuration of the organization unit.

The code is properly commented, uses descriptive variable names, handles errors effectively, and is designed for ease of maintenance.

## Installation
The submission is quite straightforward and would require Python3 installed in the host machine. Although there is a virtual envirnoment folder observed in the repository, there are no additional dependencies required.

## Execution

Clone the repository using the following command:
```bash
git clone https://github.com/sbs27/flatfair-challenge.git
```

Navigate to the test folder inside the comand prompt/terminal using the following command:

```bash
cd test
```

Execute the following command to run the test cases:

```bash
python -m unittest test_calculate_membership_fee.py
```

The above command runs variety of test cases which further solidifies the robustness and quality of the submission.


## Shortcomings/Limitations

- The membership fee, as instructed in the coding challenge, is a rounded integer value and not a float. For example, if the calculated fee is 1240.8 pence, it will be returned as 1240 pence.
- Insertion of data is limited to the structure of the test array of organisation units.


## License
This code is released under the [MIT](https://choosealicense.com/licenses/mit/) license.

## Contributing
Contributions to this codebase are welcome! Please fork the repository and submit a pull request.

## Contact
If you have any questions or issues with this code, please contact the developer at shrabana27@gmail.com.

## Author

- [@sbs27](https://github.com/sbs27)
