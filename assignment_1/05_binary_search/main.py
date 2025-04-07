import time
import matplotlib.pyplot as plt
import random

def binary_search(arr, target):
    """
    Binary search algorithm implementation
    Returns index of target if found, else -1
    """
    low = 0
    high = len(arr) - 1
    steps = 0  # Track number of steps taken
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        
        # Visualize current search range
        visualize_search(arr, low, high, mid)
        
        if arr[mid] == target:
            print(f"\nFound {target} at index {mid} in {steps} steps")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"\n{target} not found in array after {steps} steps")
    return -1

def linear_search(arr, target):
    """Linear search for comparison"""
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            print(f"Linear search found {target} at index {i} in {steps} steps")
            return steps
    print(f"Linear search didn't find {target} after {steps} steps")
    return steps

def visualize_search(arr, low, high, mid):
    """Visualize the current search range"""
    print("\nCurrent search range:")
    for i in range(len(arr)):
        if i == mid:
            print(f"[{arr[i]}]", end=" ")  # Current middle element
        elif low <= i <= high:
            print(arr[i], end=" ")         # Current search range
        else:
            print("_", end=" ")            # Outside search range
    print()

def compare_searches(arr_size=100):
    """Compare binary vs linear search performance"""
    arr = sorted(random.sample(range(1, arr_size*10), arr_size))
    target = random.choice(arr)
    
    print("\n=== Performance Comparison ===")
    print(f"Searching for {target} in array of size {arr_size}")
    
    # Binary search
    start = time.time()
    binary_steps = binary_search(arr, target)
    binary_time = time.time() - start
    
    # Linear search
    start = time.time()
    linear_steps = linear_search(arr, target)
    linear_time = time.time() - start
    
    # Print results
    print("\nComparison Results:")
    print(f"Binary Search: {binary_steps} steps, {binary_time:.6f} seconds")
    print(f"Linear Search: {linear_steps} steps, {linear_time:.6f} seconds")
    
    # Plot comparison
    plt.bar(['Binary Search', 'Linear Search'], [binary_steps, linear_steps])
    plt.title('Steps Comparison')
    plt.ylabel('Number of Steps')
    plt.show()

def interactive_mode():
    """Interactive binary search demo"""
    print("\n=== Interactive Binary Search ===")
    
    # Get user input for array
    while True:
        try:
            input_str = input("Enter sorted numbers separated by spaces: ")
            arr = [int(x) for x in input_str.split()]
            if arr != sorted(arr):
                print("Error: Array must be sorted!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
    # Get target to search
    while True:
        try:
            target = int(input("Enter number to search: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Perform search
    binary_search(arr, target)

def main_menu():
    """Main program menu"""
    while True:
        print("\nBinary Search Project")
        print("1. Interactive Binary Search")
        print("2. Compare Binary vs Linear Search")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            interactive_mode()
        elif choice == "2":
            size = int(input("Enter array size for comparison (default 100): ") or 100)
            compare_searches(size)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()