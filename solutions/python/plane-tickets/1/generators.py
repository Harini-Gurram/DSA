"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    letters=['A','B','C','D']
    current_number=0
    while current_number<number:
        yield letters[current_number%4]
        current_number+=1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    letters=['A','B','C','D']
    seats_count=0
    current_number=0
    while seats_count<number:
        current_number+=1
        if current_number==13:
            continue
        for letter in letters:
            if seats_count<number:
                yield str(current_number)+letter
                seats_count+=1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_numbers=generate_seats(len(passengers))
    seats={}
    for passenger in passengers:
        seats[passenger]=seat_numbers.__next__()
    return seats
    


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield (seat+flight_id).ljust(12,'0')
