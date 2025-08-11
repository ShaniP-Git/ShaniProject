from jb_60.function_example.utilitis import utilitis

utilitis_1=utilitis()

nums = [4,12,21,32,43,54,65]
utilitis_1.avg_calculator(nums)
num1 = [1,7,5,9]
avg1,size1 = utilitis_1.avg_calculator(num1)
nums2 = [56,87,90,43,65]
avg2,size2 = utilitis_1.avg_calculator(nums2)
utilitis_1.avg_calculator([33,33,22,11])
if (avg2>avg1):
    print("avg 1 was bigger")


