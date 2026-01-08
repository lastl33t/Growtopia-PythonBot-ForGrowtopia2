from dataclasses import dataclass, field
from core.utils import PacketReader

@dataclass(slots=True)
class InventoryItem:
    id: int
    amount: int
    flag: int

class Inventory:
    def __init__(self) -> None:
        self.size: int = 0
        self.item_count: int = 0
        self.items: dict[int, InventoryItem] = field(default_factory=dict)

    def __iter__(self):
        return iter(self.items.values())

    def parse(self, data: bytes) -> None:
        self.reset()
        reader = PacketReader(data)

        reader.skip(1)

        self.size = reader.u32()
        self.item_count = reader.u16()

        for _ in range(self.item_count):
            item_id = reader.u16()
            amount = reader.u8()
            flag = reader.u8()

            self.items[item_id] = InventoryItem(
                id=item_id,
                amount=amount,
                flag=flag
            )

    def reset(self) -> None:
        self.size = 0
        self.item_count = 0
        self.items.clear()