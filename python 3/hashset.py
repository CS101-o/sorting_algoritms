from enum import Enum
import config
import time


class hashset:
    def __init__(self, size=10):

        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = size
        self.hash_table = [None] * self.hash_table_size  # Initialize the hash table
        self.total_collisions = 0
        self.total_rehashes = 0 # rehasing count
        self.count = 0
        self.load_factor_threshold = 0.7  # Threshold for rehashing
        self.total_insert_attempts = 0t

    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True

    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n

    def hash_function(self, value):
        # Simple hash function based on ASCII values
        return sum(ord(char) for char in value) % self.hash_table_size

    def rehash(self):
        old_hash_table = self.hash_table
        new_size = self.nextPrime(self.hash_table_size * 2)  # Resize to the next prime number
        self.hash_table = [None] * new_size
        self.hash_table_size = new_size
        self.total_rehashes += 1
        old_count = self.count
        self.count = 0  # Reset the count, it will be updated in self._reinsert

        for item in old_hash_table:
            if item is not None:
                self._reinsert(item)  # Reinsert items into the new hash table

        assert self.count == old_count, "Rehashing error: item count mismatch"

    def _reinsert(self, value):
        index = self.hash_function(value)
        while self.hash_table[index] is not None:
            index = (index + 1) % self.hash_table_size
        self.hash_table[index] = value
        self.count += 1

    def insert(self, value):
        self.total_insert_attempts += 1

        # Check load factor before calculating the hash
        if self.count / self.hash_table_size > self.load_factor_threshold:
            self.rehash()

        # Recalculate the hash index after rehashing
        index = self.hash_function(value)
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index] == value:
                # The value is already in the set, do not insert
                return
            self.total_collisions += 1
            index = (index + 1) % self.hash_table_size

        self.hash_table[index] = value
        self.count += 1  # Increment count after successful insertio


    def find(self, value):
        index = self.hash_function(value)
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index] == value:
                return True
            index = (index + 1) % self.hash_table_size
            if index == original_index:
                # We've looped back around to the original index
                return False

        return False

    def print_set(self):
        for index, value in enumerate(self.hash_table):
            if value is not None:
                print(f"Index {index}: {value}")
            else:
                print(f"Index {index}: Empty")

    def print_stats(self):

        # Calculate average collisions per access
        average_collisions = (self.total_collisions / self.total_insert_attempts
                              if self.total_insert_attempts > 0 else 0)

        start_time = time.perf_counter()
        # Perform the operation here
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Operation took {elapsed_time} seconds")

        print(f"Total collisions: {self.total_collisions}")
        print(f"Total rehashes: {self.total_rehashes}")
        print(f"Average collisions per access: {average_collisions:.2f}")
        print(f"Load factor: {self.count / self.hash_table_size:.2f}")


# Hashing Modes
class HashingModes(Enum):
    HASH_1_COLLISION_1 = 0
    HASH_1_COLLISION_2 = 1
    HASH_1_COLLISION_3 = 2
    HASH_2_COLLISION_1 = 3
    HASH_2_COLLISION_2 = 4
    HASH_2_COLLISION_3 = 5



