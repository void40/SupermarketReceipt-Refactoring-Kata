from receipt import Receipt


class ReceiptPrinter:
    @staticmethod
    def print_receipt(receipt: Receipt):
        for item in receipt.get_items():
            print(item)
        print(f"Total: ${receipt.get_total():.2f}")
