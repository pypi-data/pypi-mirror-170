# blns Paper backup recovery

Minimalistic python tool to recover blns paper backup.

Paper backup consists of two parts:
- part 1 is sent together with the card, starts with `blns1` keyword
- part 2 is produced after signup flow on the phone, starts with `blns2` keyword

Recovery tool returns root seed and its [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) mnemonic representation. 

For more information on Bitcoin keys generation please refer to [Bitcoin book](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05.asciidoc#creating-an-hd-wallet-from-the-seed) 
or [learnmeabitcoin.com on extended keys](https://learnmeabitcoin.com/technical/extended-keys).

For a web browser-based recovery tool, visit the [recovery tool](https://blns-ltd.github.io/blns-recovery/recovery), sources on 
https://github.com/blns-ltd/blns-recovery. 

## Pip installation

BoolTest is available via `pip`:

```
pip3 install blns-recovery
```

If the package is uploaded on Pypi. If it is not the case, use local pip installation below.

## Local installation

From the local dir:

```
pip3 install --upgrade --find-links=. .
```

## Usage

Enter part1 and part2 as command line arguments.
The tool computes your master seed and outputs it as a hex-coded string. 
Use it to recover your funds to a newly created wallet. After the recovery, do not use recovered seed anymore.

```
$> blns-recovery --part1 'blns1 road there connect clap divert nothing hunt angle slush lesson glide lunar vocal scrub bubble clean unique hammer charge wreck satoshi glare surge urge memory gather' \
  --part2 'blns2 quit exchange miracle winter cupboard solve wing zero this leader auction result firm manage they total mimic stadium host borrow spray list canyon brick refuse april'

Recovered master seed: c166420301445f404a92acf30b39370aa0ed39991a5b27b7116ef7546bcc9936
BIP-39 mnemonic: scrap craft liar action echo parent clean few vessel flush evidence best attract orphan good enter chicken review forum upgrade effort town gospel shell
```

Usage:
```
usage: blns-recovery [-h] [--part1 PART1] [--part2 PART2]
                     [--part1-hex PART1_HEX] [--part2-hex PART2_HEX]
                     [--bip-language BIP_LANGUAGE] [--show-btc-secret]

BLNS paper backup recovery

optional arguments:
  -h, --help            show this help message and exit
  --part1 PART1         Part 1 of the paper backup
  --part2 PART2         Part 2 of the paper backup
  --part1-hex PART1_HEX
                        Part 1 of the paper backup in the hexadecimal form
  --part2-hex PART2_HEX
                        Part 2 of the paper backup in the hexadecimal form
  --bip-language BIP_LANGUAGE
                        BIP39 mnemonic language to use
  --show-btc-secret     Show BTC master private keys
```

## Key derivation scheme

Inputs: 
- paper backup `part1`
- paper backup `part2`

```
seed = HMAC-SHA512(key=0xFE42EF, msg=part1 || part2)
```

The `seed` is a root seed that can be used to recover your wallets.
