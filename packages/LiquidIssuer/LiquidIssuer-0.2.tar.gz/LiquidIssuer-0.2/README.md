# LiquidIssuer
Issue token on Blockstream Liquid sidechain compatible with Blockstream asset registry from a Python/Qt app.

## Install
Install from pip

```
pip install liquidissuer
```

## Configuration
The configuration file is available in your home folder in the file `~/liquidissuer/main.conf` and has the following format.

```
[LIQUID]
host:
port: 7041
username:
password:
wallet: wallet.dat
passphrase:
```

You can configure the content of the file directly from the config tab in the app.

## Usage
You can easily start the app running the command `li`

## Modify the GUI
Using the designer for QT you can modify the dialog.ui that contain all the graphical structure of the app.
