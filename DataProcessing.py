class TransactionError(Exception):
    pass

class InMemoryDatabase:
    def __init__(self):
        self.db = {}
        self.transaction_active = False
        self.transaction_changes = {}
    
    def begin_transaction(self):
        if self.transaction_active:
            raise TransactionError("Transaction already in progress.")
        self.transaction_active = True
        self.transaction_changes = {}

    def put(self, key, value):
        if not self.transaction_active:
            raise TransactionError("No active transaction. Cannot put key-value.")
        self.transaction_changes[key] = value

    def get(self, key):
        if self.transaction_active and key in self.transaction_changes:
            return None
        return self.db.get(key, None)

    def commit(self):
        if not self.transaction_active:
            raise TransactionError("No active transaction to commit.")
        self.db.update(self.transaction_changes)
        self.transaction_active = False
        self.transaction_changes = {}

    def rollback(self):
        if not self.transaction_active:
            raise TransactionError("No active transaction to rollback.")
        self.transaction_active = False
        self.transaction_changes = {}

if __name__ == "__main__":
    inmemoryDB = InMemoryDatabase()

    try:
        print(inmemoryDB.get("A"))  # Should print None

        try:
            inmemoryDB.put("A", 5)  # Should throw error
        except TransactionError as e:
            print(f"Transaction error: {e} (expected)")

        inmemoryDB.begin_transaction()
        inmemoryDB.put("A", 5)
        print(inmemoryDB.get("A"))  # Should print None (not committed yet)

        inmemoryDB.put("A", 6)
        inmemoryDB.commit()

        print(inmemoryDB.get("A"))  # Should print 6

        try:
            inmemoryDB.commit()  # Should throw error
        except TransactionError as e:
            print(f"Transaction error: {e} (expected)")

        try:
            inmemoryDB.rollback()  # Should throw error
        except TransactionError as e:
            print(f"Transaction error: {e} (expected)")

        print(inmemoryDB.get("B"))  # Should print None

        inmemoryDB.begin_transaction()
        inmemoryDB.put("B", 10)
        inmemoryDB.rollback()

        print(inmemoryDB.get("B"))  # Should print None

    except TransactionError as e:
        print(f"Transaction error: {e}")