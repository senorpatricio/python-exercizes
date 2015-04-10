__author__ = 'patrickh'
# coding bat practice
# list-1
# def first_last6(nums):
#     if nums[0] == 6:
#         print True
#         if nums(len(nums)-1) == 6:
#             print True
#
#
#
# array1 = raw_input("Please ")

# Dave's code
def first_last6(nums):
      return 6 in [nums[0], nums[len(nums) -1]]

# Jared's code
def first_last6(nums):
  return 6 is nums[0] or 6 is nums[-1]

# Felicia's code
def first_last6(nums):
  if nums[(len(nums) - 1)] == 6 or nums[0] == 6:
      return True
  else:
      return False