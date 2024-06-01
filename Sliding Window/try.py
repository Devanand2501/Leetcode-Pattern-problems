def maximum_sum_of_k_size_subarray(arr, k):
    # Placeholder for the actual function implementation
    # Add your sliding window logic here
    print(f"Array: {arr}, Window Size: {k}")

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for i in range(t):
        k = int(input("Enter the window size: "))
        arr = list(map(int, input("Enter the array elements separated by space: ").strip().split()))
        maximum_sum_of_k_size_subarray(arr, k)
