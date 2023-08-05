# Nexo Pro API Wrapper built with Python

- ✨ Work in Progress
- 🎌 Built with Python
- 🐋 Docker Available
- 🍻 Actively Maintained

## Description 📰

This is an unofficial Python wrapper for the Nexo Pro exchange REST API v1. I am in no way affiliated with Nexo, use at your own risk.

If you came here looking for the Nexo exchange to purchase cryptocurrencies, then go here. If you want to automate interactions with Nexo, stick around.

Heavily influenced by (https://github.com/sammchardy/python-binance)[python-binance]

## Roadmap 🌱

See it on Issue https://github.com/guilyx/crypto-dca-bot/issues/8

## What it does 🔎

Set up your bot by putting regular orders in your configuration file:

```json
{
    "orders": 
    [
        {
            "pair": "BTCBUSD",
            "quantity": 10,
            "frequency": "* * * * *",
            "exchange": "binance"
        },
        {
            "pair": "ETHBUSD",
            "quantity": 5,
            "frequency": "* 2 * * SUN",
            "exchange": "binance"
        }
    ]
}
```

Here, the first order should open a spot order for 10 (quantity) BUSD of BTC (pair) on Binance (exchange), every minute (cron frequency). The second order should open a spot order for 5 BUSD of ETH on Binance, every sunday at 2:00 (time set up in your docker).

You are responsible for filling up your account with the money you want to use with these periodic orders.

## How to Run It 📑

### Set it up 💾

1. Clone the Project: `git clone -b dev https://github.com/guilyx/crypto-dca-bot.git`
2. Move to the Repository: `cd crypto-dca-bot`
3. Create a copy of `.env.example` and name it `.env`
4. Fill up your API Keys (to do: put helper links)
5. Create a json file for setting up your orders, specify the name of that json file in your `.env`. The json file must be in the root of the repository.

### Run it 💨

1. Build and Compose the Docker: `docker-compose -f docker/docker-compose.yml up`
2. Your bot should be running, if you set up a Twitter or Telegram API you should be receiving tweets/messages.

## Contribute 🆘

Open an issue to state clearly the contribution you want to make. Upon aproval send in a PR with the Issue referenced. (Implement Issue #No / Fix Issue #No).

## Maintainers Ⓜ️

- Erwin Lejeune

## Buy me a Coffee

*ERC-20 / EVM: **0x482A82761710aeAf04665BB28E32Fb256B4a7bC8***

*BTC: **bc1q0c45w3jvlwclvuv9axlwq4sfu2kqy4w9xx225j***

*DOT: **1Nt7G2igCuvYrfuD2Y3mCkFaU4iLS9AZytyVgZ5VBUKktjX***
