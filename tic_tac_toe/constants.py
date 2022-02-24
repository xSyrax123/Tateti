FIELDS_X_O = ("X", "O")
FIELD_EMPTY = " "
SPACER = "-" * 50
WAYS_TO_WIN = (
    # Rows.
    slice(0, 3),
    slice(3, 6),
    slice(6, 9),
    # Columns.
    slice(0, 7, 3),
    slice(1, 8, 3),
    slice(2, 9, 3),
    # Diagonals.
    slice(0, 9, 4),
    slice(2, 7, 2)
)