# Crypto Mining Cost Basis Script

Generic Python script used to calculate the cost-basis report of mined crypto-currency.


## Description

Using exported .csv file containing deposit transactions of mined crypto-currency, aggregate historical price info from yahoo finance to calculate fair market value.
Generate new .csv file with populated information which contains total taxable income for mining operation of said crypto-currency.


### Dependencies

```
pip install -r requirements.txt
```
* export csv from crypto wallet and filter for deposits only

### Installing
* Clone project
* Setup virutal environment
* Install requirements.txt


### Configuration

* Ensure .csv containing deposit transactions is in same directory as python script
* Edit file names/paths to corresponding input/output files
* Edit date range to pull historical price dates that correspond with deposit transactions


## Authors
Andrew Johnson 

## Version History
* 1.0
    * Initial Release


## License

This project is licensed under the MIT License

