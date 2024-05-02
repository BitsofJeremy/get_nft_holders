import os
import requests
import openpyxl

# Replace with your Alchemy API key
ALCHEMY_API_KEY = os.getenv('ALCHEMY_API_KEY')

# Define the PAPP contract address
CONTRACT_ADDRESS = "0xF39bE779905D16fE23B2cC1297Dc3e759D2dAA11"

# Set the Opensea SLUG
GET_TOKEN_BALANCES = True

# Get the data from Alchemy
url = f"https://base-mainnet.g.alchemy.com/nft/v2/{ALCHEMY_API_KEY}/getOwnersForCollection?contractAddress={CONTRACT_ADDRESS}&withTokenBalances={GET_TOKEN_BALANCES}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
holder_data = response.json()


def convert_hex_int(hex_value):
    """ Helper function to convert Hex to Int """
    integer_value = int(hex_value, 16)
    return integer_value


# Loop through holder_data
all_holders = []

for holder in holder_data['ownerAddresses']:
    # Set some variables
    ownerAddress = holder['ownerAddress']
    tokenBalance = len(holder['tokenBalances'])
    tokenBalances = holder['tokenBalances']
    # Loop through tokens
    tokenIds = []
    for tokenId in tokenBalances:
        # print(tokenId)
        _id = convert_hex_int(hex_value=tokenId['tokenId'])
        tokenIds.append(_id)
    # Create a string of integers from the array tokenIds
    comma_delimited_tokenIds = ', '.join(map(str, tokenIds))
    # Make a fancy dictionary
    holder_data = {
        'ownerAddress': ownerAddress,
        'tokenBalance': tokenBalance,
        'tokenIds': comma_delimited_tokenIds
    }
    # Append the data to all_holders
    all_holders.append(holder_data)


def export_spreadsheet(data):
    """ Helper function to create the spreadsheet with data """
    if os.path.exists('nft_holders.xlsx'):
        os.remove('nft_holders.xlsx')
    else:
        print("nft_holders.xlsx does not exist")
    # Setup spreadsheet
    active_wb = openpyxl.Workbook()
    ws = active_wb.active
    ws.title = 'NFT Holders'
    ws.append(['ownerAddress', 'tokenBalance', 'tokenIds'])
    for i in data:
        ws.append([i['ownerAddress'], i['tokenBalance'], i['tokenIds']])
    # Write it out
    active_wb.save('nft_holders.xlsx')


# Create the spreadsheet with the data
export_spreadsheet(data=all_holders)
print('done')
