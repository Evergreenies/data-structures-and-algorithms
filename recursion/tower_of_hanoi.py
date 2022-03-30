"""
Tower of Hanoi
"""


def message(plate: int, frm: str, to: str) -> None:
    """
    Printing proper message just to show moving plates

    :param plate:
    :type plate:
    :param frm:
    :type frm:
    :param to:
    :type to:
    :return:
    :rtype:
    """
    print(f"Moving plate: {plate:5}  ==>    From: {frm:15}   -->   {to:15}")


def tower_of_hanoi(source: str, destination: str, helper: str, size: int) -> None:
    """
    Tower of Hanoi

    :param source:
    :type source:
    :param destination:
    :type destination:
    :param helper:
    :type helper:
    :param size:
    :type size:
    :return:
    :rtype:
    """

    if size == 1:
        message(size, source, destination)
        return

    tower_of_hanoi(source, helper, destination, size - 1)
    message(size, source, destination)
    tower_of_hanoi(helper, destination, source, size - 1)


if __name__ == '__main__':
    print("With 3 Disks")
    tower_of_hanoi('SOURCE', "DESTINATION", "HELPER", 3)

    print("\n\nWith 5 Disks")
    tower_of_hanoi('SOURCE', "DESTINATION", "HELPER", 5)
