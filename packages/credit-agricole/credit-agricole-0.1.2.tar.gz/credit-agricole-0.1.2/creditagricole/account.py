# coding: utf-8

from datetime import date
from dataclasses import dataclass, field

from typing import List

@dataclass(frozen=True)
class Transaction:
    id: str
    label: str
    type_label: str
    description: str
    date: date
    amount: float

@dataclass(frozen=True)
class Account:
    id: str
    index: int = field(repr=False)
    owner: str
    balance: float
    currency: str
    label: str
    operations: List[Transaction] = field(repr=False)
