from transports import *

from rich import box
from rich.table import Table
from rich.console import Console
from rich.panel import Panel


def main():
    console = Console()

    table = Table(box=box.DOUBLE, show_header=False)
    table.add_row("System", "Freight Calculator")
    table.add_row()
    table.add_row("Input", "Enter the distance so the system can calculate the freight cost")

    console.print(Panel(table,title="Freight System", box=box.DOUBLE, expand=False))

    while True:
        try:
            distance = float(input("Distance (Km): "))

            if distance <= 0:
                print("The distance must be greater than 0 km")
                continue
            break

        except ValueError:
            print("ERROR! The system only accepts numeric values.")


    trip = [Motorcycle(distance), Truck(distance), Drone(distance)]

    console = Console()

    table = Table(box=box.DOUBLE)
    table.add_column("Distance (Km)", justify="center")
    table.add_column("Transport", justify="center")
    table.add_column("Freight (R$)", justify="center")

    for item in trip:
        table.add_row(
            f"{distance:.2f}",
            type(item).__name__,
            f"{item.freight_calc()}")

    console.print(Panel(table, title="Freights", expand=False, box=box.DOUBLE))


if __name__ == '__main__':
    main()