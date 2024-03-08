from utils import write_to_file, create_dir

from eth_account import Account

def create_eth_wallet():
    # Включение неаудитируемых функций HD Wallet
    Account.enable_unaudited_hdwallet_features()

    # Теперь вы можете использовать мнемоническую фразу для создания кошелька
    mnemonic = Account.create_with_mnemonic()

    # Создание кошелька из мнемонической фразы
    wallet = Account.from_mnemonic(mnemonic[1])

    # Получение адреса и приватного ключа
    address = wallet.address
    private_key = wallet.key

    # Возвращение информации о кошельке
    return mnemonic[1], private_key.hex(), address


def main():
    create_dir()
    wallet_count = int(input('Введите количество аккаунтов: '))

    for _ in range(wallet_count):
        seed, private_key, address = create_eth_wallet()
        write_to_file(private_key, 'wallets')
        write_to_file(address, 'address')
        write_to_file(seed,'seeds')
        write_to_file(f"{address}:{private_key}", "wallets_a:p")
        write_to_file(f"{address}:{seed}", "wallets_a:s")


if __name__ == '__main__':
    main()

