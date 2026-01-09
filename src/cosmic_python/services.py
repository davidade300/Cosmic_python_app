from cosmic_python import model
from cosmic_python.model import Batch, OrderLine
from cosmic_python.orm import batches
from cosmic_python.repository import AbstractRepository


class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


# Typical service-layer functions have similar steps
# fetch objects from the repository -> make some checks/assertions about the
# request against the current state -> call a domain service -> if ok,
# save/update state


def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku(f'Invalid sku {line.sku}')

    batchref = model.allocate(line, batches)
    session.commit()

    return batchref
