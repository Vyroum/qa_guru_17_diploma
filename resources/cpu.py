from dataclasses import dataclass


@dataclass
class CPU:
    model: str
    quantity: str


cpu = CPU(model="Intel Core i7", quantity="1")