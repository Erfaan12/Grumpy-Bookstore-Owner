class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        # Step 1: Calculate initially satisfied customers (when grumpy[i] == 0)
        total_satisfied = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                total_satisfied += customers[i]
        
        # Step 2: Calculate additional satisfied customers using the sliding window technique
        max_additional_satisfied = 0
        additional_satisfied = 0
        
        # Calculate the initial window of 'minutes' length
        for i in range(minutes):
            if grumpy[i]:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied
        
        # Slide the window across the array
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                additional_satisfied += customers[i]
            if grumpy[i - minutes]:
                additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        # The result is the sum of always satisfied customers and the maximum additional satisfied customers
        return total_satisfied + max_additional_satisfied

# Example usage
solution = Solution()
print(solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))  # Output: 16
print(solution.maxSatisfied([1], [0], 1))  # Output: 1
