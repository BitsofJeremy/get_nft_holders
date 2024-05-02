# get_nft_holders

A simple script to get all the holders of a NFT collection and export to a spreadsheet

# Install

    git clone https://github.com/BitsofJeremy/get_nft_holders.git
    cd get_nft_holders
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

*[Note: See an example .env file below]*

    source .env

### Run it

    python get_nft_holders.py

This will create a spreadsheet called `nft_holders.xlsx` locally

### Example .env file

    export ALCHEMY_API_KEY=secret_key