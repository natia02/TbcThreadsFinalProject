import concurrent.futures
import random
import time

from Rectangle import Rectangle
from Square import Square
from Trapezoid import Trapezoid


def create_instances(size=1000000):
    trapezoid = [Trapezoid((random.randint(1, 100),
                            random.randint(1, 100),
                            random.randint(1, 100))) for i in range(size)]
    rectangle = [Rectangle((random.randint(1, 100),
                            random.randint(1, 100))) for i in range(size)]
    square = [Square((random.randint(1, 100),)) for i in range(size)]

    return trapezoid + rectangle + square


def calculate_with_loop(number_of_figures):
    figures = create_instances(number_of_figures)
    for figure in figures:
        figure.area()


def run_loop(number_of_figures):
    start = time.perf_counter()
    calculate_with_loop(number_of_figures)
    end = time.perf_counter()
    print("Time elapsed with regular loop: ", round(end - start, 2))


def calculate_with_threads(number_of_figures, number_of_threads):
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        for _ in range(number_of_threads):
            executor.submit(calculate_with_loop, number_of_figures // number_of_threads)


def run_threads(number_of_figures, number_of_threads):
    start = time.perf_counter()
    calculate_with_threads(number_of_figures, number_of_threads)
    end = time.perf_counter()

    print("Time elapsed with threads: ", round(end - start, 2))


def calculate_with_processes(number_of_figures, number_of_processes):
    with concurrent.futures.ProcessPoolExecutor(max_workers=number_of_processes) as executor:
        for _ in range(number_of_processes):
            executor.submit(calculate_with_loop, number_of_figures // number_of_processes)


def run_processes(number_of_figures, number_of_processes):
    start = time.perf_counter()
    calculate_with_threads(number_of_figures, number_of_processes)
    end = time.perf_counter()

    print("Time elapsed with processes: ", round(end - start, 2))


def calculate_with_mix(number_of_figures, number_of_processes, number_of_threads):
    with concurrent.futures.ProcessPoolExecutor(max_workers=number_of_processes) as executor:
        for _ in range(number_of_processes):
            with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as thread_executor:
                for _ in range(number_of_threads):
                    thread_executor.submit(calculate_with_loop,
                                           (number_of_figures // number_of_threads // number_of_processes))


def run_mix(number_of_figures, number_of_processes, number_of_threads):
    start = time.perf_counter()
    calculate_with_mix(number_of_figures, number_of_processes, number_of_threads)
    end = time.perf_counter()
    print("Time elapsed with mix: ", round(end - start, 2))


if __name__ == "__main__":
    # you can test for different numbers

    run_loop(1000000)
    run_threads(1000000, 20)
    run_processes(1000000, 20)
    run_mix(1000000, 5, 20)

