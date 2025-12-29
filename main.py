from purchase import Purchase


def main():
    purchase = Purchase("purchases.json")

    purchase.print_info()


if __name__ == "__main__":
    main()
